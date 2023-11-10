# coding=utf-8

from .base import Base
from sqlalchemy import Column,Integer,String,DateTime


class CoreTerm(Base):
    __tablename__ = "core_term"
    __table_args__ = {'extend_existing': True}
    # set id as primary_key
    id = Column(name="id",type_=Integer,primary_key=True)
    release_date = Column(name="release_date",type_=DateTime)
    status = Column(name="status",type_=Integer)
    concept_id = Column(name="concept_id",type_=Integer)
    term =Column(name="term", type_=String(200))
    term_type = Column(name="term_type",type_=Integer)

    def __init__(self) ->None:
        super.__init__()
        return 
    
    def __repr__(self) ->str:
        return f"<CoreTerm()>"

