#coding=utf-8

"""
用户管理
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from Users import *
import time
import memcache

RETRY_TIMES=3                   # 登录重试次数
LOCKED_TIMES=60                 # 账户锁定时间

# 数据库连接
engine=create_engine("mysql+pymysql://root:1125buaa1997@127.0.0.1:3306/mytestdb")
DBSession=sessionmaker(bind=engine)
session=DBSession()

# memcache
mc=memcache.Client(["127.0.0.1:11211"],debug=True)

# 登录
def func_login():
    in_username = raw_input("用户名:")
    user_get = session.query(User).filter(User.username == in_username).first()
    if user_get:
        lockedtime = mc.get(str(user_get.id))
        if lockedtime:
            print("账户还有%d秒解锁." % (lockedtime - time.time()))
        else:
            if user_get.login:
                print("用户已登录!")
                return 0,in_username
            else:
                for i in range(RETRY_TIMES):
                    in_password = raw_input("密码:")
                    if user_get.password == in_password:
                        user_get.login = True
                        user_get.locked = False
                        session.commit()
                        print("登录成功!")
                        print(user_get.to_dict())
                        return 0, in_username
                    else:
                        print("密码错误.")
                print("连续输错密码，账户被锁定.")
                user_get.locked = True
                session.commit()
                mc.set(str(user_get.id), int(time.time() + LOCKED_TIMES), time=LOCKED_TIMES)
    else:
        print("用户不存在.")
    return -1,""

# 注册
def func_register():
    in_username=raw_input("输入用户名:")
    user=session.query(User).filter(User.username==in_username).first()
    if user:
        print("用户名 %s 已存在!"%in_username)
        return
    in_password_1=raw_input("输入密码:")
    in_password_2=raw_input("确认密码:")

    if in_password_1==in_password_2:
        session.add(User(username=in_username,password=in_password_1,login=LOGIN,locked=LOCKED))
        session.commit()
        print("注册成功!")
    else:
        print("两次输入的密码不一致.")
        return

# 注销
def func_logoff():
    in_username=raw_input("用户名:")
    user = session.query(User).filter(User.username == in_username).first()
    if user:
        if user.login==True:
            user.login = False
            session.commit()
            print("注销成功!")
        else:
            print("用户未登录，无需注销.")
    else:
        print("用户不存在!")

# 删除用户
def func_delete():
    returncode,username=func_login()
    if returncode==0:
        if raw_input("是否删除此用户?y/n")=="y":
            user = session.query(User).filter(User.username == username).first()
            session.delete(user)
            session.commit()
            print("删除用户%s成功" % username)
    else:
        print("无法删除用户!")


if __name__ == '__main__':
    functions="0:退出,1:登录,2:注册,3:注销,4:删除"

    while True:
        print(functions)
        func = raw_input("选择功能:")
        if func=="0":
            break
        elif func == "1":
            func_login()
        elif func == "2":
            func_register()
        elif func=="3":
            func_logoff()
        elif func=="4":
            func_delete()
        else:
            print("No such function!")

    session.close()