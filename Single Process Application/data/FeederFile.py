import csv
import random
from FeederAbstract import CFeederAbstract
from common.CommonFunctions import CCommonFunctions
from utils.UtilsNtwap import CUtilsNtwap

class CFeederFile(CFeederAbstract):
    def __init__(self, input_dict):
        self.m_strDate                 = input_dict['date']
        self.m_strSymbol               = input_dict['symbol']
        self.m_nWindowSize             = input_dict['window_size']
        self.m_strPath                 = input_dict['path']
        self.m_strPortfolioFilename    = input_dict['portfolio_filename']
        self.m_strStrategyLogsFilename = input_dict['strategy_logs_filename']
        super(self.__class__, self).__init__()  # This is to initialize the common variables.
    
    def GetData(self, object_dict):
        self.GetRIC()
        self.GetTCAMetadata()
        
        if self.m_hash_DataSourceDict['Market'] == 'File':
            self.GetDataMarket(object_dict['Market'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Portfolio'] == 'File':
            self.GetDataTwapPortfolio(object_dict['Portfolio'], self.m_strPath, self.m_strDate, self.m_strPortfolioFilename, self.m_strSymbol, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Predicted'] == 'File':
            self.GetDataPredicted(object_dict['Predicted'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Cash'] == 'File':
            RIC_Cash = self.m_strRIC.replace(self.m_strRIC[self.m_strRIC.index(':') - 2: self.m_strRIC.index(':') + 1], '.')
            self.GetDataCash(object_dict['Cash'], self.m_strPath, self.m_strDate, RIC_Cash, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Future'] == 'File':
            self.GetDataFuture(object_dict['Future'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['StrategyLogs'] == 'File':
            self.GetDataStrategyLogs(object_dict['StrategyLogs'], self.m_strPath, self.m_strDate, self.m_strStrategyLogsFilename)
        return True
    
    #Method to obtain data from csv file
    def GetDataMarket(self, market_obj, path, date, scrip, windowInterval):
        common_functions_obj = CCommonFunctions()
        filename = path + '/' + common_functions_obj.FormatDate(date) + '/' + scrip.replace(':', '') + '_' + common_functions_obj.FormatDate(date) + '_trades.csv'
        with open(filename, 'rb') as marketTrade_file_obj:
            marketTrade_file_contents = csv.reader(marketTrade_file_obj)
            market_obj.m_strScripName = scrip
            
            for row in marketTrade_file_contents:
                if row[0].strip() == scrip:
                    market_obj.m_nCountOfRows += 1
                    market_obj.m_DatetimeList.append(common_functions_obj.GetDateTime(row[2].strip(), row[3].strip()))
                    market_obj.m_fPriceList.append(float(row[4].strip()))
                    market_obj.m_nSizeList.append(int(row[5].strip()))
            market_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[0])
            market_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[1])
            CCommonFunctions.total_daily_market_volume = sum(market_obj.m_nSizeList)
        return True
    
    def GetDataTwapPortfolio(self, portfolio_twap_obj, path, input_date, filename, scrip, windowInterval):
        common_functions_obj = CCommonFunctions()
        filename = path + '/' + common_functions_obj.FormatDate(input_date) + '/' + filename
        with open(filename, 'rb') as portfolio_file_obj:
            portfolio_file_contents           = csv.reader(portfolio_file_obj)
            portfolio_twap_obj.m_strScripName = scrip
            
            for row in portfolio_file_contents:
                if row[1].strip() == scrip:
                    temp_datetime = row[0].strip().split(' ')
                    date = temp_datetime[0]
                    time = temp_datetime[1]
                    portfolio_twap_obj.m_nCountOfRows += 1
                    portfolio_twap_obj.m_DatetimeList.append(common_functions_obj.GetDateTimePortfolio(date, time))
                    portfolio_twap_obj.m_strOrderIDList.append(row[2].strip())
                    portfolio_twap_obj.m_strStatusList.append(row[3].strip())
                    portfolio_twap_obj.m_nOrderQtyList.append(int(row[4].strip()))
                    portfolio_twap_obj.m_fOrderPriceList.append(float(row[5].strip()))
                    portfolio_twap_obj.m_strSideList.append(row[6].strip())
                    portfolio_twap_obj.m_nFilledSizeList.append(row[7].strip())
                    portfolio_twap_obj.m_fAvgPriceList.append(row[8].strip())
                    portfolio_twap_obj.m_fPriceList.append(row[9].strip())
                    portfolio_twap_obj.m_nSizeList.append(row[10].strip())
                    portfolio_twap_obj.m_FillDateTimeList.append(common_functions_obj.GetDateTimePortfolio(date, time))
                    
                    if row[3].strip().upper() == 'COMPLETE':
                        portfolio_twap_obj.m_OrderCompleteDatetimeList.append(common_functions_obj.GetDateTimePortfolio(date, time))
                        portfolio_twap_obj.m_fOrderCompleteAvgPriceList.append(row[8].strip())
                    
                    if not row[9].strip().upper() == 'NONE':
                        portfolio_twap_obj.m_OrderExecutionDatetimeList.append(common_functions_obj.GetDateTimePortfolio(date, time))
                        portfolio_twap_obj.m_fOrderExecutionFillPriceList.append(row[9].strip())
            
            portfolio_twap_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(input_date, common_functions_obj.GetWindowList(windowInterval)[0])
            portfolio_twap_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(input_date, common_functions_obj.GetWindowList(windowInterval)[1])
        return True
    
    def GetDataPredicted(self, predicted_obj, path, date, scrip, windowInterval): 
        common_functions_obj = CCommonFunctions()
        filename = path + '/' + common_functions_obj.FormatDate(date) + '/' + scrip.replace(':', '') + '.csv'
        with open(filename, 'rb') as predicted_file_obj:
            predicted_file_contents = csv.reader(predicted_file_obj)
            predicted_obj.m_strScripName     = scrip
            
            for row in predicted_file_contents:
                predicted_obj.m_nCountOfRows += 1
                predicted_obj.m_DatetimeList.append(common_functions_obj.GetDateTime(date, common_functions_obj.FormatTime(row[0].strip())))
                predicted_obj.m_nSizeList.append(float(row[1].strip()))
            predicted_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[0])
            predicted_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[1])
        return True
    
    def GetDataCash(self, cash_obj, path, date, scrip, windowInterval):
         common_functions_obj = CCommonFunctions()
         filename = path + '/' + common_functions_obj.FormatDate(date) + '/' + scrip + '_' + common_functions_obj.FormatDate(date) + '_trades.csv'
         with open(filename, 'rb') as cash_file_obj:
            cash_file_contents      = csv.reader(cash_file_obj)
            cash_obj.m_strScripName = scrip
            for row in cash_file_contents:
                if row[0].strip() == scrip:
                    cash_obj.m_nCountOfRows += 1
                    cash_obj.m_DatetimeList.append(common_functions_obj.GetDateTime(row[2].strip(), row[3].strip()))
                    cash_obj.m_fPriceList.append(float(row[4].strip()))
            cash_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[0])
            cash_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[1])
         return True
    
    def GetDataFuture(self, future_obj, path, date, scrip, windowInterval):
         common_functions_obj = CCommonFunctions()
         filename = path + '/' + common_functions_obj.FormatDate(date) + '/' + scrip.replace(':', '') + '_' + common_functions_obj.FormatDate(date) + '_trades.csv'
         with open(filename, 'rb') as future_file_obj:
            future_file_contents  = csv.reader(future_file_obj)
            future_obj.m_strScripName = scrip
            for row in  future_file_contents:
                if row[0].strip() == scrip:
                    future_obj.m_nCountOfRows += 1
                    future_obj.m_DatetimeList.append(common_functions_obj.GetDateTime(row[2].strip(), row[3].strip()))
                    future_obj.m_fPriceList.append(float(row[4].strip()))
            future_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[0])
            future_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(date, common_functions_obj.GetWindowList(windowInterval)[1])
         return True
    
    def GetDataStrategyLogs(self, strategy_log_obj, path, date, filename):
        common_functions_obj = CCommonFunctions()
        filename                    = path + '/' + common_functions_obj.FormatDate(date) + '/' + filename
        strategy_logs_file_obj      = open(filename)
        strategy_logs_file_contents = strategy_logs_file_obj.read().split('\n')

        utils_ntwap_obj      = CUtilsNtwap()
        for row in strategy_logs_file_contents:
            row = utils_ntwap_obj.FormatRow(row)
        
            if len(row) > 0 and not utils_ntwap_obj.GetPrice(row) == 'nan': 
                temp_timestamp = utils_ntwap_obj.GetTimeStamp(row)
                temp_price     = utils_ntwap_obj.GetPrice(row)
                temp_strategy  = utils_ntwap_obj.GetStrategy(row)
                strategy_log_obj.m_nCountOfRows += 1
                strategy_log_obj.m_DatetimeList.append(common_functions_obj.GetDateTimeStrategyLog(date, temp_timestamp))
                strategy_log_obj.m_fPriceList.append(float(temp_price))
                strategy_log_obj.m_strStrategyList.append(temp_strategy)
        return True
