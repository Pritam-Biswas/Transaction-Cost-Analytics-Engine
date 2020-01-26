from DataAbstract import CDataAbstract

#Class to hold Portfolio Data
class CDataTwapPortfolio(CDataAbstract):
    def __init__(self):
        self.m_nVolumeWindowList                = []
        self.m_fPercentVolumeWindowList         = []
        self.m_fVwapWindowList                  = []
        self.m_strTimeWindowList                = []
        self.m_strPartialTimeWindowList         = []
        self.m_strTimeWindowPlotList            = []
        self.m_ntotal_daily_volume              = 0
        self.m_strOrderIDList                   = []
        self.m_strStatusList                    = []
        self.m_nOrderQtyList                    = []
        self.m_fOrderPriceList                  = []
        self.m_strSideList                      = []
        self.m_nFilledSizeList                  = []
        self.m_fAvgPriceList                    = []
        self.m_FillDateTimeList                 = []
        self.m_fOrderCompleteAvgPriceList       = []
        self.m_OrderCompleteDatetimeList        = []
        self.m_fOrderExecutionFillPriceList     = []
        self.m_OrderExecutionDatetimeList       = []
        self.m_fOrderExecutionMovingAverageList = []
        super(self.__class__, self).__init__()  # This is to initialize the common variables.
         
    #Method to obtain data from csv file
    
    #Method to obtain data from TRTH URL
    #Method to parse data in FIX format and store it 
