from datetime import *

epoch = datetime.utcfromtimestamp(0)

# a date in the form of 2017-01-09T21:45:29.894Z
published_at = '2017-01-09T21:45:29.894Z'

#a function to convert the time to epoch
def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0
    
def int_to_date(as_int):
    t = timedelta(0,seconds=as_int/1000.0)
    return epoch + t

date_as_int =  int(unix_time_millis(datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S.%fZ")))

# will display 1483998329894
print(date_as_int)

print datetime.strftime(func2(date_as_int), "%Y-%m-%dT%H:%M:%S.%fZ")

