from DataAbstract import CDataAbstract

#Class to hold Market Data
class CDataMarketTrade(CDataAbstract):
    def __init__(self): 
        CDataAbstract.__init__(self)
        self.m_nVolumeWindowList          = []
        self.m_fPercentVolumeWindowList   = []
        self.m_fVwapWindowList            = []
        self.m_strTimeWindowList          = []
        self.m_strPartialTimeWindowList   = []
        self.m_strTimeWindowPlotList      = []
        self.m_ntotal_daily_volume        = 0
    
    #Method to obtain data from TRTH URL
    
    #Method to parse data in FIX format and store it 
