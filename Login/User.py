#coding=utf-8

"""
用户，实体类
"""

from Based import *

LOGIN=False                     # 是否登录
LOCKED=False                    # 账户是否锁定

class User(Base):
    __tablename__ = "users"

    id=Column(Integer,primary_key=True,autoincrement=True)  #id
    username=Column(String(64),nullable=False)              #用户名
    password=Column(String(64),nullable=False)              #密码
    login=Column(Boolean)                                   #登录状态
    locked=Column(Boolean)                                  #账户是否锁定

    def to_dict(self):
        return {
            "id":self.id,
            "username":self.username,
            "password":self.password,
            "login":self.login,
            "locked":self.locked
        }

if __name__ == '__main__':
    # 建表
    Base.metadata.create_all(engine)

    # 插入数据
    session.add(User(username="zhangsan",password="zhangsanpassword",login=LOGIN,locked=LOCKED))
    session.add(User(username="lisi",password="lisipassword",login=LOGIN,locked=LOCKED))
    session.add(User(username="wangwu",password="wangwupassword",login=LOGIN,locked=LOCKED))
    session.add(User(username="haoxiaoning", password="1125", login=LOGIN, locked=LOCKED))
    session.commit()

    session.close()