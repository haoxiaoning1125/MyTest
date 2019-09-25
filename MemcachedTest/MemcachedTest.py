#coding=utf-8

"""
Python操作memcached
"""

import memcache
import time

if __name__ == '__main__':
    mc=memcache.Client(["127.0.0.1:11211"],debug=True)

    # set，设置，若key已存在，则覆盖
    print("SET")
    mc.set("username","haoxiaoning",time=60*5)
    mc.set("username", "hao", time=60 * 5)

    # get，获取
    print("GET")
    print("username:",mc.get("username"))
    print("a:",mc.get("a"))
    mc.set("a","aa",1)
    time.sleep(1)
    print("a:",mc.get("a"))

    # gets
    print("GETS")
    print("username:",mc.gets("username"))

    # add，添加，若已存在，响应：NOT_STORED
    print("ADD")
    mc.add("username","h",60)
    mc.add("uname","h",60)
    print("username:",mc.get("username"))
    print("uname:",mc.get("uname"))

    # replace，替换
    print("REPLACE")
    mc.replace("username","h",60)
    print("username:",mc.get("username"))

    # append，在value后追加
    print("APPEND")
    mc.append("username","aoxiaoning")
    print("username:",mc.get("username"))

    # prepend，在value前追加
    print("PREPEND")
    mc.prepend("username","name:")
    print("username:",mc.get("username"))

    # cas，仅在当前客户端最后一次取值后，该key 对应的值没有被其他客户端修改的情况下，才能够将值写入
    print("CAS")
    mc.cas("username","empty")
    print("username",mc.get("username"))

    # delete
    print("DELETE")
    mc.delete("username")
    print("username:",mc.get("username"))

    # incr，数字value自增，decr，数字value自减
    print("INCR,DECR")
    mc.add("num",10)
    print("num:",mc.get("num"))
    mc.incr("num",10)
    print("num:",mc.get("num"))
    mc.decr("num",20)
    print("num:",mc.get("num"))

    # stats
    print("STATS")
    # print(mc.get_stats())

    # add list
    mc.add("list",[1,2],10)
    print("list:",mc.get("list"))
    l=mc.gets("list")
    l.append(3)
    mc.cas("list",l)
    print("list:",mc.get("list"))

    # flush_all，清除缓存中所有key-values
    print("FLUSH_ALL")
    mc.flush_all()
    print("list:",mc.get("list"))