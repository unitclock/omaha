# coding=utf-8

from .base import Base
from sqlalchemy import Column,Integer,String,DateTime


class CoreConcept(Base):
    __tablename__ = "core_concept"
    __table_args__ = {'extend_existing': True}
        
    id = Column(name="id",type_=Integer,primary_key=True)
    release_date = Column(name="release_date",type_=DateTime)
    status = Column(name="status",type_=Integer)
    semantic_tag =Column(name="semantic_tag", type_=String(200))

    def __init__(self) ->None:
        super.__init__()
        return 
    
    def __repr__(self) ->str:
        return f"<CoreConcept()>"

