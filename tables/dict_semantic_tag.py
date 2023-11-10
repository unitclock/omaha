# coding=utf-8

from .base import Base
from sqlalchemy import Column,Integer,String,DateTime


class DictSemanticTag(Base):
    __tablename__ = "dict_semantic_tag"
    __table_args__ = {'extend_existing': True}
        
    semantic_tag = Column(name="semantic_tag",type_=String(200),primary_key=True)
    semantic_tag_name = Column(name="semantic_tag_name",type_=String(200))
    semantic_tag_desc = Column(name="semantic_tag_desc",type_=Integer)

    def __init__(self) ->None:
        super.__init__()
        return 
    
    def __repr__(self) ->str:
        return f"<DictSemanticTag()>"

