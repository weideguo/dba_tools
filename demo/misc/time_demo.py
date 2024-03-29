time.time()    
1504881596.747973

time.gmtime()
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=6, tm_min=51, tm_sec=23, tm_wday=4, tm_yday=251, tm_isdst=0)

time.localtime()
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=14, tm_min=51, tm_sec=32, tm_wday=4, tm_yday=251, tm_isdst=0)

time.localtime(0)
#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


time.asctime(time.localtime())
#'Fri Sep  8 14:53:45 2017'

time.ctime()  
#'Fri Sep  8 15:01:15 2017'

time.ctime(0) 
#'Thu Jan  1 08:00:00 1970'


time.mktime(time.localtime())
#1504853831.0


time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#'2017-09-08 14:59:25'


time.strptime('2017-09-08 14:59:25','%Y-%m-%d %H:%M:%S')
#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=8, tm_hour=14, tm_min=59, tm_sec=25, tm_wday=4, tm_yday=251, tm_isdst=-1)

#python2时区显示不正确
time.strftime('%Y-%m-%d %H:%M:%S %z',time.localtime())  
#'2020-08-11 11:41:35 +0900'

#string转时间戳
time.mktime(time.strptime('1968-09-08 14:59:25','%Y-%m-%d %H:%M:%S'))

#当前时区
time.tzname

#UTC跟当前时区的差值 秒 
time.timezone



import time
import pytz
from datetime import datetime

#显示所有时区
#pytz.all_timezones

#设置时时区
tz=pytz.timezone("Asia/Shanghai")

#显示指定时间戳的时间
dt=datetime.fromtimestamp(0,tz)
dt=datetime.fromtimestamp(time.time(),tz)


#当前时间
dt=datetime.now(pytz.timezone("Asia/Shanghai"))

#格式化
dt.strftime('%Y-%m-%d %H:%M:%S')


#string转时间戳

#python3
#默认使用系统时区
datetime.strptime('2020-08-11 10:22:54','%Y-%m-%d %H:%M:%S').timestamp() 
#带时区
datetime.strptime('2020-08-11 10:38:54 +0800','%Y-%m-%d %H:%M:%S %z').timestamp()


#python2 python3
ds=datetime.now(pytz.timezone("Asia/Shanghai"))
time.mktime(ds.timetuple())


# 时区转换
utc_now=datetime.strptime('2020-08-11 10:22:54','%Y-%m-%d %H:%M:%S')
utc_now=utc_now.replace(tzinfo=pytz.timezone("UTC"))                       # 设置时区
local_datetime=utc_now.astimezone(tz)                                      # 转换到其他时区

