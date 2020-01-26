from data.DataCash import CDataCash
from data.DataFuture import CDataFuture
from utils.Spread import CSpread
from utils.UtilsSpread import CUtilsSpread
from data.FormatData import CFormatData
from visualize.plot.CustomPlot import CCustomPlot
from AnalysisAbstract import CAnalysisAbstract

#Class to perform SimpleAnalysis of Cash Futures Spread       
class CSimpleAnalysisSpread(CAnalysisAbstract):
    
    #Input parameters are taken in the form of a dictionary    
    def __init__(self, input_dict):
        self.m_DataCash_obj    = CDataCash()
        self.m_DataFuture_obj  = CDataFuture()
        self.m_UtilsSpread_obj = CSpread()
        self.m_FormatData_obj  = CFormatData(input_dict)

    def GetData(self, cash_data_list, future_data_list):
        self.m_FormatData_obj.FormatDataCash(self.m_DataCash_obj, cash_data_list)
        self.m_FormatData_obj.FormatDataFuture(self.m_DataFuture_obj, future_data_list)
        return True
        
    def AnalyseData(self):
        utils_spread_obj = CUtilsSpread()
        utils_spread_obj.GetLastPriceTotal(self.m_DataCash_obj)
        utils_spread_obj.GetLastPriceTotal(self.m_DataFuture_obj)
        self.m_UtilsSpread_obj.GetMinList(self.m_DataCash_obj, self.m_DataFuture_obj)
        return True
    
    #Method to plot data    
    def PlotData(self):
        customplot_obj = CCustomPlot()
        customplot_obj.StartPlot({'Market': '', 'Portfolio': '', 'Predicted': '', 'Cash': self.m_DataCash_obj, 'Future': self.m_DataFuture_obj, 'Spread': self.m_UtilsSpread_obj})
        return True
    
    #Method to display data in forms of tables
    def TabulateData(self):
        return True
    
    #Method to choose form of output    
    def VisualizeData(self, choice = 'PLOT'):
        if choice.upper() == 'PLOT':
            self.PlotData()
        if choice.upper() == 'TABULATE':
            self.TabulateData()   
        return True          

    #Method to trigger analysis of Cash Future Spreads            
    def StartSimpleAnalysisSpread(self, cash_data_list , future_data_list, choice = 'PLOT'):
         self.GetData(cash_data_list, future_data_list)
         self.AnalyseData()
         self.VisualizeData(choice)
         return True
                
#Class to initiate an object of type CSimpleAnalysisSpread
class CTest:
    if __name__ == "__main__":      
        simple_analysis_cf_obj = CSimpleAnalysisSpread({'date': '14032016', 'symbol': 'DRREDDY-EQ', 'window_size': 15, 'path': 'C:/Users/rashishs/Downloads', 'portfolio_filename': '', 'strategy_logs_filename': '', 'URL': '', 'username': '', 'password': ''})
        simple_analysis_cf_obj.StartSimpleAnalysisSpread()
