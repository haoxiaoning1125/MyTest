#coding=utf-8

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

engine = create_engine("mysql+pymysql://root:1125buaa1997@127.0.0.1:3306/mytestdb")
DBSession = sessionmaker(bind=engine)
session = DBSession()