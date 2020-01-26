from DataAbstract import CDataAbstract

#Class to feed values from the Futures file
class CDataFuture(CDataAbstract):
    def __init__(self):
        self.m_fLastPriceList            = []
        self.m_strLastPriceTimestampList = []
        CDataAbstract.__init__(self)
