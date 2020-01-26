#Class to calculate the Cash Futures Spread
class CSpread:
    def __init__(self):
        self.m_fPriceDiffList         = []
        self.m_PriceDiffTimestampList = []
        self.m_fMinPriceList          = []
        self.m_MinPriceTimestampList  = []
    
    def GetMinList(self, cash_obj, future_obj, delta = 0):
        index_cash        = 0
        index_future      = 0
        prev_cash_price   = max(cash_obj.m_fPriceList)   + 1000
        prev_future_price = max(future_obj.m_fPriceList) + 1000
        
        while index_cash < cash_obj.m_nCountOfRows and index_future < future_obj.m_nCountOfRows:
            if cash_obj.m_DatetimeList[index_cash] < future_obj.m_DatetimeList[index_future]:
                if cash_obj.m_fPriceList[index_cash] < (prev_future_price + delta):
                    self.m_fMinPriceList.append(cash_obj.m_fPriceList[index_cash])   
                else:
                    self.m_fMinPriceList.append(prev_future_price + delta)
                    
                self.m_MinPriceTimestampList.append(cash_obj.m_DatetimeList[index_cash])
                prev_cash_price = cash_obj.m_fPriceList[index_cash]
                index_cash     += 1
            
            elif cash_obj.m_DatetimeList[index_cash] > future_obj.m_DatetimeList[index_future]:
                if future_obj.m_fPriceList[index_future] + delta < prev_cash_price:
                    self.m_fMinPriceList.append(future_obj.m_fPriceList[index_future] + delta)
                else:
                    self.m_fMinPriceList.append(prev_cash_price)
                
                self.m_MinPriceTimestampList.append(future_obj.m_DatetimeList[index_future])
                prev_future_price = future_obj.m_fPriceList[index_future]
                index_future     += 1
                
            elif cash_obj.m_DatetimeList[index_cash] == future_obj.m_DatetimeList[index_future]:
                if future_obj.m_fPriceList[index_future] + delta < cash_obj.m_fPriceList[index_cash]:
                    self.m_fMinPriceList.append(future_obj.m_fPriceList[index_future] + delta)
                else:
                    self.m_fMinPriceList.append(cash_obj.m_fPriceList[index_cash]) 
                
                self.m_MinPriceTimestampList.append(future_obj.m_DatetimeList[index_future])
                prev_future_price  = future_obj.m_fPriceList[index_future]
                prev_cash_price    = cash_obj.m_fPriceList[index_cash]
                index_cash        += 1
                index_future      += 1
        return
