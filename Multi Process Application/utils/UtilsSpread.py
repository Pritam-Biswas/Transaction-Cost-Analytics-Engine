#Class to calculate the LastPriceWindow and LastPriceTotal    
class CUtilsSpread:
    
    def GetLastPriceWindow(self, data_object, list_index, time_window_index):
        while data_object.m_DatetimeList[list_index] <= data_object.m_strTimeWindowList[time_window_index]:
            list_index += 1
            if  list_index >= len(data_object.m_fPriceList) :
                break
        data_object.m_fLastPriceList.append(data_object.m_fPriceList[list_index - 1])
        data_object.m_strLastPriceTimestampList.append(data_object.m_strTimeWindowList[time_window_index])
        return list_index
        
    def GetLastPriceTotal(self, data_object):
        list_index = 0
        for iter in range(0, len(data_object.m_strTimeWindowList)):
            if list_index >= len(data_object.m_fPriceList):   
                break
            list_index = self.GetLastPriceWindow(data_object, list_index, iter)
        return True
