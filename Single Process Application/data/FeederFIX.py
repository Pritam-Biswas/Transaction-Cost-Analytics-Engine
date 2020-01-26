from FeederAbstract import CFeederAbstract

class CFeederFIX(CFeederAbstract):
    def __init__(self, input_dict):
        self.m_strDate     = input_dict['date']
        self.m_strSymbol   = input_dict['symbol']
        self.m_nWindowSize = input_dict['window_size']
        super(self.__class__, self).__init__()  # This is to initialize the common variables.
    
    def GetData(self, object_dict):
        self.GetRIC()
        self.GetDataSource()
        if self.m_hash_DataSourceDict['Market'] == 'FIX':
            self.GetDataMarket(object_dict['Market'])
        if self.m_hash_DataSourceDict['Portfolio'] == 'FIX':
            self.GetDataTwapPortfolio(object_dict['Portfolio'])
        if self.m_hash_DataSourceDict['Predicted'] == 'FIX':
            self.GetDataPredicted(object_dict['Predicted'])
        if self.m_hash_DataSourceDict['Cash'] == 'FIX':
            self.GetDataCash(object_dict['Cash'])
        if self.m_hash_DataSourceDict['Future'] == 'FIX':
            self.GetDataFuture(object_dict['Future'])
        if self.m_hash_DataSourceDict['StrategyLogs'] == 'FIX':
            self.GetDataFuture(object_dict['StrategyLogs'])
        return True
    
    #Method to obtain data from csv file
    def GetDataMarket(self, market_obj):
        return True
    
    def GetDataTwapPortfolio(self, portfolio_obj):
        return True
    
    def GetDataPredicted(self, predicted_obj): 
        return True
    
    def GetDataCash(self, cash_obj):
         return True
    
    def GetDataFuture(self, future_obj):
         return True
