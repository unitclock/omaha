# coding=utf-8
from contextlib import contextmanager
from database import NewEngine
from utils import single
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from tables.core_term import CoreTerm
from tables.core_concept import CoreConcept
from tables.dict_semantic_tag import DictSemanticTag

@single
class Omaha():
    def __init__(self) ->None:
        self.__engine = NewEngine()
        self.__session = sessionmaker(bind=self.__engine)
        return 
    
    @contextmanager
    def session_gen(self):
        s = self.__session()
        try:
            yield s
            s.commit()
        except Exception as e:
            s.rollback()
            raise e
        finally:
            s.close()

    def execute(self,sql:str):
        try:
            conn = self.__engine.connect()
            result = conn.execute(text(sql))
            conn.close()
        except Exception as e:
            raise e
        finally:
            return result
    
    def term_gen(self)->None:
        page_size = 1
        current_page = 1
        offset = (current_page - 1) * page_size
        try:
            while True:
                with self.session_gen() as s:
                    results = s.query(CoreTerm.term,CoreTerm.id,CoreTerm.concept_id).offset(offset=offset).limit(page_size).all()
                    for row in results:
                        yield row
                current_page +=1
                offset = (current_page - 1) * page_size
                continue
        except Exception as e:
            print("term generated error")
            raise e
        finally:
            return
    
    def term_classify_by_concept_id(self,concept_id:int) -> tuple:
        try:
            with self.session_gen() as s:
                (semantic_tag,) = s.query(CoreConcept.semantic_tag).filter(CoreConcept.id == concept_id).first()
                result = s.query(DictSemanticTag.semantic_tag_name,DictSemanticTag.semantic_tag_desc).filter(DictSemanticTag.semantic_tag==semantic_tag).first()
        except Exception as e:
            print("term classified error")
            raise e
        finally:
            return result

    def find_synonym_from_concept_id(self,concept_id:int) ->list:
        try:
            synonyms = []
            with self.__session() as s:
                results = s.query(CoreTerm.term).filter(CoreTerm.concept_id == concept_id).all()
                for (row,) in results:
                    synonyms.append(row)
        except Exception as e :
            print("find synonym error")
            raise e
        finally:
            return synonyms

