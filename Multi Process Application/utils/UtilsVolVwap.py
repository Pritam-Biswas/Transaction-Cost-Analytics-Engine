from common.CommonFunctions import CCommonFunctions

#Class containing methods for computing volume and VWAP 
class CUtilsVolVwap():
    #To get volume of trade in one time window
    def GetVolWindow(self, data_object, list_index, time_window_index): 
        common_functions_obj = CCommonFunctions()        
        temp_vol             = 0
        
        while common_functions_obj.CompareTime(data_object.m_DatetimeList[list_index], data_object.m_strTimeWindowList[time_window_index]) == -1:
            if not data_object.m_nSizeList[list_index] == "NULL":
                temp_vol = temp_vol + float(data_object.m_nSizeList[list_index])
            
            list_index += 1
            
            if  list_index >= len(data_object.m_nSizeList) :
                break
        
        data_object.m_nVolumeWindowList.append(temp_vol)
        
        return list_index
        
    #To get Vwap in a given time window
    def GetVwapWindow(self, data_object, list_index, time_window_index):
        common_functions_obj = CCommonFunctions()        
        temp_vol             = 0
        temp_vwap            = 0
        
        while common_functions_obj.CompareTime(data_object.m_DatetimeList[list_index], data_object.m_strTimeWindowList[time_window_index]) == -1:
            if not data_object.m_nSizeList[list_index] == "NULL":
                temp_vol  = temp_vol  + float(data_object.m_nSizeList[list_index])
                temp_vwap = temp_vwap + float(data_object.m_nSizeList[list_index]) * float(data_object.m_fPriceList[list_index])
            
            list_index += 1
            
            if  list_index >= len(data_object.m_nSizeList):
                break
        
        if not temp_vol == 0:    
            temp_vwap = temp_vwap / temp_vol
            data_object.m_fVwapWindowList.append(temp_vwap)
        
        return list_index
    
    #To get list of % of trade volume 
    def GetPercentVol(self, data_object):
        for i in range(0, len(data_object.m_nVolumeWindowList)):
            data_object.m_fPercentVolumeWindowList.append(data_object.m_nVolumeWindowList[i] / CCommonFunctions.total_daily_market_volume * 100)
        return True
    
    #To convert fraction of daily trade volume into %
    def GetPercentFraction(self, data_object):
        for i in range(0, len(data_object.m_nVolumeWindowList)):
            data_object.m_fPercentVolumeWindowList.append(data_object.m_nVolumeWindowList[i] * 100)
        return True
    
    #To get Volume traded for entire day for different time windows as a list    
    def GetVolTotal(self, data_object):
        list_index = 0
       
        for iter in range(0, len(data_object.m_strTimeWindowList)):
            if list_index >= len(data_object.m_nSizeList) : 
                break
            list_index = self.GetVolWindow(data_object, list_index, iter)
        return True
    
    #To get Vwap for entire day for different time windows as a list  
    def GetVwapTotal(self, data_object):
        list_index = 0
        
        for iter in range(0, len(data_object.m_strTimeWindowList)):
            if list_index >= len(data_object.m_nSizeList) : 
                break
            list_index = self.GetVwapWindow(data_object, list_index, iter)
        
        return True
    
    #To get time window liat from the point where the portfolio started trading
    def GetPartialTimeWindowList(self, data_object):
        data_object.m_strPartialTimeWindowList = data_object.m_strTimeWindowList[len(data_object.m_strTimeWindowList) - len(data_object.m_fVwapWindowList): ]
        return True
