from DataAbstract import CDataAbstract

#Class to hold Expected Market Behaviour Data
class CDataPredicted(CDataAbstract): 
    def __init__(self):
        self.m_nVolumeWindowList         = []
        self.m_fPercentVolumeWindowList  = []
        self.m_fVwapWindowList           = []
        self.m_strTimeWindowList         = []
        self.m_strPartialTimeWindowList  = []
        self.m_strTimeWindowPlotList     = []
        self.m_ntotal_daily_volume       = 0
        super(self.__class__, self).__init__()
    
    #Method to obtain data from csv file
    #Method to obtain data from TRTH URL
    #Method to parse data in FIX format and store it
