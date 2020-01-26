import datetime

#Class containing methods used commonly during analysis
#Seperate methods defined to get datetime objects from portfolio data as date and time are in a different format in portfolio data  
class CCommonFunctions:
    total_daily_market_volume = 0   
    
    def __init__(self):
        return 
    
    #To get datetime object for strategy log data from date and time (strings) 
    def GetDateTimeStrategyLog(self, date, time):
        time = time.split(':')
        return datetime.datetime(int(date[4: ]), int(date[2:4]), int(date[0:2]), int(time[0]), int(time[1]), int(time[2]), 0)
        
    
    #To get datetime object for portfolio data from date and time (strings) 
    def GetDateTimePortfolio(self, date, time): 
        date = date.split('-')
        time = time.split(':')
        return datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]), 0)
    
    #To get list of datetime objects for portfolio data    
    def GetDateTimeListPortfolio(self, date, timeList): 
        tempDatetimeList = []
        for iter in range(0, len(timeList)):            
            tempDatetimeList.append(self.GetDateTimePortfolio(date, timeList[iter]))
        return tempDatetimeList
    
    #To get datetime object from date and time (strings)    
    def GetDateTime(self, date, time): 
        # date: dd/mm/yyyy
        date = date.replace('/', '')
        date = date.replace('-', '')
        
        time = time[0:8].replace(':','')
        
        return datetime.datetime(int(date[4: ]), int(date[2:4]), int(date[0:2]), int(time[0:len(time) - 4]), int(time[len(time) -4 :len(time) -2]), int(time[len(time) -2: ]), 0)
    
    #To get list of datetime objects
    def GetDateTimeList(self, date, timeList): 
        tempDatetimeList = []
        for iter in range(0, len(timeList)):   
            tempDatetimeList.append(self.GetDateTime(date, timeList[iter]))
        return tempDatetimeList
    
    #To compare time
    def CompareTime(self, datetime1, datetime2):   #datetime1 and datetime2 are datetime objects
        if datetime1 < datetime2:
            return -1
        if datetime1 == datetime2:
            return 1
        if datetime1 > datetime2:
            return 1
    
    #To obtain time in hh:mm:ss format        
    def FormatTime(self, time): 
         time = time[0:len(time) - 4] + ":" + time[len(time) - 4:len(time) - 2] + ":" + time[len(time) - 2:len(time)]
         return time
    
    #To obtain date in yyyymmdd format: input date in ddmmyyyy format
    def FormatDate(self, date): 
        date = date[4: ] + date[2:4] + date[0:2]
        return date
    
    #To get list of windows of required time interval and list of mid-points of the time windows 
    def GetWindowList(self, interval): 
        hour_timelist            = 9
        minute_timelist          = 0
        total_minutes_timelist   = 0
        times                    = []
        
        hour_midptlist           = 9
        minute_midptlist         = int(interval / 2) 
        if (interval % 2) != 0:
            second = '30'
        else:
            second = '00'
        total_minutes_midptlist = minute_midptlist
        times_midpt             = []
        
        times_midpt.append(str(int((9 + int(interval / 120)))).zfill(2) + ':' + str(minute_midptlist % 60).zfill(2) + ':' + second)
        while total_minutes_timelist <= 390 - interval:    
            minute_timelist        = minute_timelist + interval
            total_minutes_timelist = total_minutes_timelist + interval
            if total_minutes_midptlist <= 390 - int(interval):
                total_minutes_midptlist = total_minutes_midptlist + interval
                minute_midptlist        = minute_midptlist + interval
                if minute_midptlist >= 60:
                    hour_midptlist   = hour_midptlist + int(minute_midptlist/60)
                    minute_midptlist = minute_midptlist % 60
                times_midpt.append(str(hour_midptlist).zfill(2) + ":" + str(minute_midptlist).zfill(2) + ':' + second)
            if minute_timelist >= 60:
                hour_timelist   = hour_timelist + int(minute_timelist/60)
                minute_timelist = minute_timelist % 60
            times.append(str(hour_timelist).zfill(2) + ":" + str(minute_timelist).zfill(2) + ':' + '00')
        return [times, times_midpt]

    def FindOccurences(self, socket_buffer, char):
        return [i for i, letter in enumerate(socket_buffer) if letter == char]

    def ParseBuffer(self, socket_buffer):
        #print "inside parsebuffer"
        begin_string_list = self.FindOccurences(socket_buffer, '{')
        end_string_list   = self.FindOccurences(socket_buffer, '}')
        #print begin_string_list
        #print end_string_list
        json_list = []
        for iter in range(0,len(begin_string_list)):
            json_list.append(socket_buffer[begin_string_list[iter] : (end_string_list[iter] + 1)])
        return json_list
    
    def FormatDateJSON(self, buffer_json):
        temp_date, temp_time    = buffer_json['DateTime'].strip().split(' ')
        buffer_json['DateTime'] = self.GetDateTimePortfolio(temp_date, temp_time)
        return buffer_json
