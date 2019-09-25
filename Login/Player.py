#coding=utf-8

from Based import *
from User import User

class Player(Base):
    __tablename__="players"

    id=Column(Integer,primary_key=True,autoincrement=True)
    userid=Column(Integer,ForeignKey("users.id"),nullable=False)
    username=Column(String(64),nullable=False)
    lev=Column(Integer)
    money=Column(Integer)

    def to_dict(self):
        return {
            "id":self.id,
            "userid":self.userid,
            "username":self.username,
            "lev":self.lev,
            "money":self.money
        }


if __name__ == '__main__':
     Base.metadata.create_all(engine)

     session.add(Player(userid=1,username="zhangsan",lev=10,money=100))
     session.add(Player(userid=2,username="lisi",lev=20,money=200))
     session.add(Player(userid=3,username="wangwu",lev=30,money=300))
     session.add(Player(userid=4,username="haoxiaoning",lev=1,money=0))
     session.commit()

     session.close()
