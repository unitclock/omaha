# coding=utf-8

from sqlalchemy import create_engine
from config import *

def NewEngine() :
    engine = create_engine(
        f'mysql+pymysql://{db_user}:{db_passwd}@{db_addr}:{db_port}/{db_name}?charset=utf8',
        echo=bool(sqlalchemy_echo),
        pool_size=int(sqlalchemy_pool_size),
        max_overflow=int(sqlalchemy_max_overflow),
        pool_recycle=int(sqlalchemy_pool_recycle)
        )
    return engine
