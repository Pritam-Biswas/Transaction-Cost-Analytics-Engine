from CommonFunctions import CCommonFunctions

#Class to separate details of Time, Price, Strategy from the data read       
class CUtilsNtwap:
    def GetTimeStamp(self, row):
        return row[0][0:row[0].index('.')]
    
    def GetPrice(self, row):
        return row[4].strip().split(' ')[1]
        
    def GetStrategy(self, row):
        return row[4].strip().split(' ')[4]
        
    def FormatRow(self, row):
        return row.strip().split('-')
    
    def GetStrategyList(self, strategy_log_obj, portfolio_twap_obj):
        index_strategy       = 0
        index_portfolio      = 0
        common_functions_obj = CCommonFunctions()
        
        while index_strategy < strategy_log_obj.m_nCountOfRows and index_portfolio < len(portfolio_twap_obj.m_fOrderExecutionFillPriceList):
            if common_functions_obj.CompareTime(strategy_log_obj.m_DatetimeList[index_strategy], portfolio_twap_obj.m_DatetimeList[index_portfolio]) == -1:
                index_strategy += 1
            
            elif common_functions_obj.CompareTime(strategy_log_obj.m_DatetimeList[index_strategy], portfolio_twap_obj.m_DatetimeList[index_portfolio]) == 0 or common_functions_obj.CompareTime(strategy_log_obj.m_DatetimeList[index_strategy], portfolio_twap_obj.m_DatetimeList[index_portfolio]) == 1:
                strategy_log_obj.m_strStrategyExecutionList.append(strategy_log_obj.m_strStrategyList[index_strategy - 1]) 
                index_portfolio += 1
        return True
    
    def GetMovingAverages(self, portfolio_twap_obj):
        temp_FillSizeList = filter(lambda a: a != 'None', portfolio_twap_obj.m_nSizeList)
        for index_portfolio in range(2, len(portfolio_twap_obj.m_fOrderExecutionFillPriceList)):
            temp_moving_average = (float(portfolio_twap_obj.m_fOrderExecutionFillPriceList[index_portfolio - 2]) * int(temp_FillSizeList[index_portfolio - 2]) + float(portfolio_twap_obj.m_fOrderExecutionFillPriceList[index_portfolio - 1]) * int(temp_FillSizeList[index_portfolio - 1])) / (int(temp_FillSizeList[index_portfolio - 2]) + int(temp_FillSizeList[index_portfolio - 1]))
            portfolio_twap_obj.m_fOrderExecutionMovingAverageList.append(temp_moving_average)
        return True
