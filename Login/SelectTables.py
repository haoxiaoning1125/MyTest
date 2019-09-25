#coding=utf-8

"""
查询
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from Users import User

# 数据库连接
engine=create_engine("mysql+pymysql://root:1125buaa1997@127.0.0.1:3306/mytestdb")
DBSession=sessionmaker(bind=engine)
session=DBSession()

def output(user):
    if user:
        print(len(user))
        for u in user:
            print(u.to_dict())

if __name__ == '__main__':
    output(session.query(User).filter(and_(User.username=="haoxiaoning",User.locked==False)).all())

    output(session.query(User).filter(User.username=="haoxiaoning",User.username=="lisi").all())

    output(session.query(User).filter(or_(User.username=="haoxiaoning",User.username=="lisi")).all())

    output(session.query(User).filter(User.username.in_(["haoxiaoning","lisi"])).all())

    print("count(User.locked==False):"+str(session.query(User).filter(User.locked==False).count()))

    output(session.query(User).from_statement(text("select * from users where locked =:locked")).\
           params(locked=False).all())




