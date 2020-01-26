from data.DataMarketTrade import CDataMarketTrade
from data.DataStrategyLog import CDataStrategyLog
from data.DataTwapPortfolio import CDataTwapPortfolio
from data.FeederFile import CFeederFile
from data.FeederURL import CFeederURL
from data.FeederFIX import CFeederFIX
from utils.UtilsNtwap import CUtilsNtwap
from visualize.plot.CustomPlot import CCustomPlot

class CSimpleAnalysisNTWAP:
    
    #Input parameters are taken in the form of a dictionary    
    def __init__(self, input_dict):
        self.m_hash_MetadataDict = input_dict
    
    def CreateStrategyLog_obj(self):
        return CDataStrategyLog()
    
    def CreateMarket_obj(self):
        return CDataMarketTrade()
    
    def CreatePortfolioTwap_obj(self):
        return CDataTwapPortfolio()
    
    def GetData(self, market_obj, strategy_log_obj, portfolio_twap_obj):
        feeder_file_obj = CFeederFile(self.m_hash_MetadataDict)
        feeder_file_obj.GetData({'Market': market_obj, 'Portfolio': portfolio_twap_obj, 'Predicted': '', 'Cash': '', 'Future': '', 'StrategyLogs': strategy_log_obj})
        return True
    
    def AnalyseData(self, strategy_log_obj, portfolio_twap_obj):
        utils_ntwap_obj = CUtilsNtwap()
        utils_ntwap_obj.GetStrategyList(strategy_log_obj, portfolio_twap_obj)
        utils_ntwap_obj.GetMovingAverages(portfolio_twap_obj)
        return True
        
    #Method make plots from NTWAP data
    def PlotData(self, market_obj, portfolio_twap_obj, strategy_log_obj):
        custom_plot_obj = CCustomPlot()
        custom_plot_obj.NTWAP_Execution(market_obj, portfolio_twap_obj, strategy_log_obj)
        return True
    
    #Method to ditermine type of output    
    def VisualizeData(self, market_obj, portfolio_twap_obj, strategy_log_obj, choice = 'PLOT'):
        if choice == 'PLOT':
            self.PlotData(market_obj, portfolio_twap_obj, strategy_log_obj)
        return True
    
    #Method to trigger the NTWAP analysis    
    def StartSimpleAnalysisNTWAP(self):
        market_obj         = self.CreateMarket_obj()
        strategy_log_obj   = self.CreateStrategyLog_obj()
        portfolio_twap_obj = self.CreatePortfolioTwap_obj()
        self.GetData(market_obj, strategy_log_obj, portfolio_twap_obj)
        self.AnalyseData(strategy_log_obj, portfolio_twap_obj)
        self.VisualizeData(market_obj, portfolio_twap_obj, strategy_log_obj)
        return True

#Class to create instance of the SimpleAnalysisNTWAP
class CTest:
    if __name__ == "__main__":
        simple_analysis_ntwap_obj = CSimpleAnalysisNTWAP() 
        simple_analysis_ntwap_obj.StartSimpleAnalysisNTWAP()
