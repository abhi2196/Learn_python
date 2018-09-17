'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
       
    timeStamp = line.split(' ')[1]
    logDate = timeStamp.split('T')[0]
    logTime = timeStamp.split('T')[1]

    return datetime(int(logDate.split('-')[0]), int(logDate.split('-')[1]), int(logDate.split('-')[2]), int(logTime.split(':')[0]), int(logTime.split(':')[1]), int(logTime.split(':')[2]))


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    timeList = []
    for line in loglines:
        if line.find(SHUTDOWN_EVENT) != -1:
            timeList.append(convert_to_datetime(line)) 
    if  len(timeList) > 0: 
        return timeList[-1] - timeList[0]
    else:
        return None
