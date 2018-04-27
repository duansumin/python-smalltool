import time
import datetime
from dateutil import tz

UTCFORMAT = '%Y-%m-%dT%H:%M:%S-%fZ'

def utc2localstamp(utc):
    utcst = datetime.datetime.strptime(utc, UTCFORMAT)
    utcst = utcst.replace(tzinfo=tz.tzutc())
    localst = utcst.astimezone(tz.tzlocal())
    localstamp = time.mktime(localst.timetuple())
    return localstamp

def utc2localstamp2(utc):
    utcst = datetime.datetime.strptime(utc, UTCFORMAT)
    nowstamp = time.time()
    localtime = datetime.datetime.fromtimestamp(nowstamp)
    utctime = datetime.datetime.utcfromtimestamp(nowstamp)
    offset = localtime - utctime
    localst = utcst + offset
    localstamp =time.mktime(localst.timetuple())
    return localstamp



if __name__ == '__main__':	
    utc = '2018-04-25T06:44:22-081Z'
    tmstamp = utc2localstamp(utc)
    tmstamp1 = utc2localstamp2(utc)
    print utc 
    print '1: %d'%tmstamp
    print '2: %d'%tmstamp1

