from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine=create_engine("mysql+mysqldb://root@localhost:3306/mytestdb")
Base=declarative_base()

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    username=Column(String(64),nullable=False)
    password=Column(String(64),nullable=False)
    email=Column(String(64),nullable=False)

    def __repr__(self):
        return "%s(%r)"%(self.__class__.__name__,self.username)

if __name__ == '__main__':
    pass