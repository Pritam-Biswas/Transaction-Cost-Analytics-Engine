from AnalysisAbstract import CAnalysisAbstract
from data.DataMarketTrade import CDataMarketTrade
from data.DataTwapPortfolio import CDataTwapPortfolio
from data.DataPredicted import CDataPredicted
from utils.UtilsVolVwap import CUtilsVolVwap
from visualize.plot.CustomPlot import CCustomPlot
from data.FormatData import CFormatData

# Class to analyse market, portfolio, predicted data wrt volume and VWAP
class CSimpleAnalysisVolVwap(CAnalysisAbstract):
    
    #Input parameters are taken in the form of a dictionary
    def __init__(self, input_dict):
#        print "Entered multiprocessing vol vwap"
        self.m_DataMarketTrade_obj   = CDataMarketTrade()
        self.m_DataTwapPortfolio_obj = CDataTwapPortfolio()
        self.m_DataPredicted_obj     = CDataPredicted()
        self.m_FormatData_obj        = CFormatData(input_dict)
    
    #Collect data and store it in the respective objects
    def GetData(self, market_data_list, portfolio_data_list, predicted_data_list):
        # self.GetRIC()
        self.m_FormatData_obj.FormatDataMarket(self.m_DataMarketTrade_obj, market_data_list)
        print "Market Data Formatted"
        self.m_FormatData_obj.FormatDataTwapPortfolio(self.m_DataTwapPortfolio_obj, portfolio_data_list)
        print "Portfolio Data Formatted"
        self.m_FormatData_obj.FormatDataPredicted(self.m_DataPredicted_obj, predicted_data_list)
        print "Predicted Data Formatted"
        return True
        
    #Analyse collected data
    def AnalyseData(self): 
        utils_obj = CUtilsVolVwap()
        
        utils_obj.GetVolTotal  (self.m_DataMarketTrade_obj)
        utils_obj.GetPercentVol(self.m_DataMarketTrade_obj)
        print "Market data processed.."
        utils_obj.GetVolTotal (self.m_DataTwapPortfolio_obj)
        utils_obj.GetPercentVol(self.m_DataTwapPortfolio_obj)
        print "Portfolio data processed.."
        utils_obj.GetVolTotal (self.m_DataPredicted_obj)
        utils_obj.GetPercentFraction(self.m_DataPredicted_obj)
        print "Portfolio data processed.."
        utils_obj.GetVwapTotal(self.m_DataMarketTrade_obj)
        utils_obj.GetVwapTotal(self.m_DataTwapPortfolio_obj)
        
        utils_obj.GetPartialTimeWindowList(self.m_DataMarketTrade_obj)
        utils_obj.GetPartialTimeWindowList(self.m_DataTwapPortfolio_obj)
        self.m_DataPredicted_obj.m_strPartialTimeWindowList = self.m_DataPredicted_obj.m_strTimeWindowList
        print "All data processed"
        return True
    
    #Plot the data
    def PlotData(self): 
        print "entered volvwap plotdata"
        customplot_obj = CCustomPlot()
        customplot_obj.StartPlot({'Market': self.m_DataMarketTrade_obj, 'Portfolio': self.m_DataTwapPortfolio_obj, 'Predicted': self.m_DataPredicted_obj, 'Cash': '', 'Future': '', 'StrategyLog': ''})
        return True
    
    #Tabulate the data
    def TabulateData(self): 
        return True
    
    #Prepare graphs or tables
    def VisualizeData(self, choice = 'plot'): 
        if choice.upper() == 'PLOT':        
            self.PlotData()
        elif choice.upper() == 'TABULATE':
            self.TabulateData()
        return True
    
    #Method to be called to analyse the data 
    def StartSimpleAnalysisVolVwap(self, market_data_list, portfolio_data_list, predicted_data_list, choice = 'plot'):
        print "Start of Simple analysis Vol Vwap"
        self.GetData(market_data_list, portfolio_data_list, predicted_data_list)
        print "Start of analysing data"
        self.AnalyseData()
        print "Start of Plotting Data"
        self.VisualizeData(choice)
        print "End of Simple analysis Vol Vwap"
        return True

# if __name__ == "__main__":
#     argument_dict       = {'date': '14032016', 'symbol': 'DRREDDY-EQ', 'window_size': 15, 'path': 'C:/Users/rashishs/Downloads', 'portfolio_filename': '%T_145527.csv', 'strategy_logs_filename': 'ntwap_auto.txt', 'URL': '', 'username': '', 'password': ''}
#     simple_analysis_obj = CSimpleAnalysisVolVwap(argument_dict)
#     simple_analysis_obj.StartSimpleAnalysisVolVwap()
