from DataAbstract import CDataAbstract

#Class to feed values from the Cash file
class CDataCash(CDataAbstract):
    def __init__(self):
        self.m_nVolumeWindowList         = []
        self.m_fPercentVolumeWindowList  = []
        self.m_strTimeWindowList         = []
        self.m_strTimeWindowPlotList     = []
        self.m_fLastPriceList            = []    
        self.m_strLastPriceTimestampList = []
        CDataAbstract.__init__(self)     
