from abc import ABCMeta

#Abstract Base Class for holding data
class CDataAbstract:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.m_DatetimeList              = []
        self.m_fPriceList                = []
        self.m_nSizeList                 = []
        self.m_strScripName              = ''
        self.m_nCountOfRows              = 0
