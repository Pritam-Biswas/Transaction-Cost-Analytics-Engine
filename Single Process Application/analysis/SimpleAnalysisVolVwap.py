from AnalysisAbstract import CAnalysisAbstract
from data.DataMarketTrade import CDataMarketTrade
from data.DataTwapPortfolio import CDataTwapPortfolio
from data.DataPredicted import CDataPredicted
from data.FeederFile import CFeederFile
from data.FeederURL import CFeederURL
from data.FeederFIX import CFeederFIX
from utils.UtilsVolVwap import CUtilsVolVwap
from visualize.plot.CustomPlot import CCustomPlot

# Class to analyse market, portfolio, predicted data wrt volume and VWAP
class CSimpleAnalysisVolVwap(CAnalysisAbstract):
    
    #Input parameters are taken in the form of a dictionary
    def __init__(self, InputDict):  
        self.m_hash_MetadataDict = InputDict
    
    #Create object to contain market data
    def CreateMarket_obj(self):     
        return CDataMarketTrade()
    
    #Create object to contain portfolio data
    def CreatePortfolioTwap_obj(self):  
        return CDataTwapPortfolio()
    
    #Create object to contain expected market behaviour data
    def CreatePredicted_obj(self):  
        return CDataPredicted()
    
    #Collect data and store it in the respective objects
    def GetData(self, market_obj, portfolio_twap_obj, predicted_obj): 
        feeder_file_obj = CFeederFile(self.m_hash_MetadataDict)
        feeder_file_obj.GetData({'Market': market_obj, 'Portfolio': portfolio_twap_obj, 'Predicted': predicted_obj, 'Cash': '', 'Future': '', 'StrategyLogs': ''})
        return True
    
    #Analyse collected data
    def AnalyseData(self, market_obj, portfolio_twap_obj, predicted_obj): 
        utils_obj = CUtilsVolVwap()
        
        utils_obj.GetVolTotal (market_obj)
        utils_obj.GetPercentVol(market_obj)
        
        utils_obj.GetVolTotal (portfolio_twap_obj)
        utils_obj.GetPercentVol(portfolio_twap_obj)
        
        utils_obj.GetVolTotal (predicted_obj)
        utils_obj.GetPercentFraction(predicted_obj)
        
        utils_obj.GetVwapTotal(market_obj)
        utils_obj.GetVwapTotal(portfolio_twap_obj)
        
        utils_obj.GetPartialTimeWindowList(market_obj)
        utils_obj.GetPartialTimeWindowList(portfolio_twap_obj)
        predicted_obj.m_strPartialTimeWindowList = predicted_obj.m_strTimeWindowList
        return True
    
    #Plot the data
    def PlotData(self, market_obj, portfolio_twap_obj, predicted_obj): 
        customplot_obj = CCustomPlot()
        customplot_obj.StartPlot({'Market': market_obj, 'Portfolio': portfolio_twap_obj, 'Predicted': predicted_obj, 'Cash': '', 'Future': ''})
        return True
    
    #Tabulate the data
    def TabulateData(self, market_obj, portfolio_twap_obj, predicted_obj): 
        return True
    
    #Prepare graphs or tables
    def VisualizeData(self, market_obj, portfolio_twap_obj, predicted_obj, choice = 'plot'): 
        if choice.upper() == 'PLOT':        
            self.PlotData(market_obj, portfolio_twap_obj, predicted_obj)
        elif choice.upper() == 'TABULATE':
            self.TabulateData(market_obj, portfolio_twap_obj, predicted_obj)
        return True
    
    #Method to be called to analyse the data 
    def StartSimpleAnalysisVolVwap(self, choice = 'plot'):
        market_obj         = self.CreateMarket_obj()
        portfolio_twap_obj = self.CreatePortfolioTwap_obj()
        predicted_obj      = self.CreatePredicted_obj()
        
        self.GetData(market_obj, portfolio_twap_obj, predicted_obj)
        self.AnalyseData(market_obj, portfolio_twap_obj, predicted_obj)
        self.VisualizeData(market_obj, portfolio_twap_obj, predicted_obj, choice)
        return True

if __name__ == "__main__":
    argument_dict       = {'date': '14032016', 'symbol': 'DRREDDY-EQ', 'window_size': 15, 'path': 'C:/Users/rashishs/Downloads', 'portfolio_filename': '%T_145527.csv', 'strategy_logs_filename': 'ntwap_auto.txt', 'URL': '', 'username': '', 'password': ''}
    simple_analysis_obj = CSimpleAnalysisVolVwap(argument_dict)
    simple_analysis_obj.StartSimpleAnalysisVolVwap()
