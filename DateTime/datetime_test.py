# coding:utf-8

from datetime import datetime, timedelta
# from datetime import timezone
import time

if __name__ == '__main__':
    now = datetime.now()
    print(type(now), now)

    dt1 = datetime(2019, 11, 25, 9, 10, 20, 30000)
    print(dt1)

    # datetime转换为timestamp
    print(time.mktime(now.timetuple()))   # Python2, 兼容Python3, dt1.timestamp()
    print(time.mktime(now.utctimetuple()))

    # timestamp转换为datetime
    print(datetime.fromtimestamp(time.time()))

    # 字符串转 datetime (str point to time)
    dt2 = datetime.strptime('2019.10.1 11:59:59', '%Y.%m.%d %H:%M:%S')
    print (type(dt2), dt2)

    # datetime 转字符串 (str from time)
    print(now.strftime('%Y--%m--%d %H:%M:%S'))

    # datetime加减
    now = datetime.now()
    print(now)
    print(now + timedelta(hours=10))
    print(now - timedelta(days=1))
    print(now + timedelta(hours=10, days=1))

    # 本地时间转 utc 时间
    # tz_utc_8 = timezone(timedelta(hours=8))
    # now = datetime.now()
    # print(now)
    # print(now.replace(tzinfo=tz_utc_8))

    dt3 = datetime(2019, 11, 25)
    tp3 = time.mktime(dt3.timetuple())
    print(dt3.day, datetime.fromtimestamp(tp3).day)
