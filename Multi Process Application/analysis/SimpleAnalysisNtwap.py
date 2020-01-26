from AnalysisAbstract import CAnalysisAbstract
from data.DataMarketTrade import CDataMarketTrade
from data.DataStrategyLog import CDataStrategyLog
from data.DataTwapPortfolio import CDataTwapPortfolio
from utils.UtilsNtwap import CUtilsNtwap
from visualize.plot.CustomPlot import CCustomPlot
from data.FormatData import CFormatData

class CSimpleAnalysisNtwap(CAnalysisAbstract):
    
    #Input parameters are taken in the form of a dictionary    
    def __init__(self, input_dict):
        self.m_DataMarketTrade_obj   = CDataMarketTrade()
        self.m_DataTwapPortfolio_obj = CDataTwapPortfolio()
        self.m_DataStrategyLog_obj   = CDataStrategyLog()
        self.m_FormatData_obj        = CFormatData(input_dict)

    def GetData(self, market_data_list, strategylog_data_list, portfolio_data_list):
        # self.GetRIC()
        self.m_FormatData_obj.FormatDataMarket(self.m_DataMarketTrade_obj, market_data_list)
        print "In Ntwap analysis, market data formatted"
        self.m_FormatData_obj.FormatDataTwapPortfolio(self.m_DataTwapPortfolio_obj, portfolio_data_list)
        print "In ntwap analysis, portfolio data formatted"
        self.m_FormatData_obj.FormatDataStrategyLog(self.m_DataStrategyLog_obj, strategylog_data_list)
        print "In ntwap analysis, strategy data formatted"
        return True
    
    def AnalyseData(self):
        utils_ntwap_obj = CUtilsNtwap()
        utils_ntwap_obj.GetStrategyList(self.m_DataStrategyLog_obj, self.m_DataTwapPortfolio_obj)
        print "In ntwap analysis, getting strategies"
        utils_ntwap_obj.GetMovingAverages(self.m_DataTwapPortfolio_obj)
        print "In ntwap analysis, getting moving averages"
        return True
        
    #Method make plots from NTWAP data
    def PlotData(self):
        print "entered ntwap plot data"
        custom_plot_obj = CCustomPlot()
        custom_plot_obj.NTWAP_Execution(self.m_DataMarketTrade_obj, self.m_DataTwapPortfolio_obj, self.m_DataStrategyLog_obj)
        return True

    #Tabulate the data
    def TabulateData(self): 
        return True
    
    #Method to ditermine type of output    
    def VisualizeData(self, choice = 'PLOT'):
        if choice == 'PLOT':
            self.PlotData()
        elif choice.upper() == 'TABULATE':
            self.TabulateData()
        return True
    
    #Method to trigger the NTWAP analysis    
    def StartSimpleAnalysisNtwap(self, market_data_list, strategylog_data_list, portfolio_data_list, choice = 'PLOT'):
        print "Start of Ntwap Analysis"
        self.GetData(market_data_list, strategylog_data_list, portfolio_data_list)
        print "In ntwap analysis, all data formatted"
        self.AnalyseData()
        print "In ntwap analysis, all data analysed"
        self.VisualizeData(choice)
        print "In ntwap analysis, all data plotted "
        print "End of Ntwap analysis process"
        return True

# if __name__ == "__main__":
#     simple_analysis_ntwap_obj = CSimpleAnalysisNtwap() 
#     simple_analysis_ntwap_obj.StartSimpleAnalysisNtwap()
