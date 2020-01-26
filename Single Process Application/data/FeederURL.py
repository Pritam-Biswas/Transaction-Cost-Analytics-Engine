from FeederAbstract import CFeederAbstract

class CFeederURL(CFeederAbstract):
    def __init__(self, input_dict):
        self.m_strDate     = input_dict['date']
        self.m_strSymbol   = input_dict['symbol']
        self.m_nWindowSize = input_dict['window_size']
        self.m_strURL      = input_dict['URL']
        self.m_strUsername = input_dict['username']
        self.m_strPassword = input_dict['password']
        super(self.__class__, self).__init__()  # This is to initialize the common variables.
    
    def GetData(self, object_dict):
        self.GetRIC()
        self.GetDataSource()
        if self.m_hash_DataSourceDict['Market'] == 'URL':
            self.GetDataMarket(object_dict['Market'], self.m_strURL, self.m_strDate, self.m_strRIC, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Portfolio'] == 'URL':
            self.GetDataTwapPortfolio(object_dict['Portfolio'], self.m_strPath, self.m_strDate, self.m_strFilename, self.m_strSymbol, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Predicted'] == 'URL':
            self.GetDataPredicted(object_dict['Predicted'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Cash'] == 'URL':
            self.GetDataCash(object_dict['Cash'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['Future'] == 'URL':
            self.GetDataFuture(object_dict['Future'], self.m_strPath, self.m_strDate, self.m_strRIC, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        if self.m_hash_DataSourceDict['StrategyLogs'] == 'URL':
            self.GetDataFuture(object_dict['StrategyLogs'], self.m_strPath, self.m_strDate, self.m_strStrategyLogsFilename, self.m_strUsername, self.m_strPassword, self.m_nWindowSize)
        return True
    
    #Method to obtain data from csv file
    def GetDataMarket(self, market_obj, URL, date, scrip, username, password, windowInterval):
        return True
    
    def GetDataTwapPortfolio(self, portfolio_twap_obj, URL, date, scrip, username, password, windowInterval):
        return True
    
    def GetDataPredicted(self, predicted_obj, URL, date, scrip, username, password, windowInterval): 
        return True
    
    def GetDataCash(self, cash_obj, URL, date, scrip, username, password, windowInterval):
         return True
    
    def GetDataFuture(self, future_obj, URL, date, scrip, username, password, windowInterval):
         return True
