from data.DataCash import CDataCash
from data.DataFuture import CDataFuture
from utils.Spread import CSpread
from utils.UtilsSpread import CUtilsSpread
from data.FeederFile import CFeederFile
from data.FeederURL import CFeederURL
from data.FeederFIX import CFeederFIX
from visualize.plot.CustomPlot import CCustomPlot
from AnalysisAbstract import CAnalysisAbstract

#Class to perform SimpleAnalysis of Cash Futures Spread       
class CSimpleAnalysisSpread(CAnalysisAbstract):
    
    #Input parameters are taken in the form of a dictionary    
    def __init__(self, input_dict):
        self.m_hash_MetadataDict = input_dict
    
    #Create object to contain cash data
    def CreateCash_obj(self):     
        return CDataCash()
    
    #Create object to contain market data
    def CreateFuture_obj(self):     
        return CDataFuture()
    
    def CreateSpread_obj(self):
        return CSpread()
    
    def GetData(self, cash_obj, future_obj):
        # EDIT THIS METHOD TO GET DATA USING FEEDER
        feeder_file_obj = CFeederFile(self.m_hash_MetadataDict)
        feeder_file_obj.GetData({'Market': '', 'Portfolio': '', 'Predicted': '', 'Cash': cash_obj, 'Future': future_obj, 'StrategyLogs': ''})
        return True
        
    def AnalyseData(self, cash_obj, future_obj, spread_obj):
        utils_spread_obj = CUtilsSpread()
        utils_spread_obj.GetLastPriceTotal(cash_obj)
        utils_spread_obj.GetLastPriceTotal(future_obj)
        
        spread_obj.GetMinList(cash_obj, future_obj)
        return True
    
    #Method to plot data    
    def PlotData(self, cash_obj, future_obj, spread_obj):
        customplot_obj = CCustomPlot()
        customplot_obj.StartPlot({'Market': '', 'Portfolio': '', 'Predicted': '', 'Cash': cash_obj, 'Future': future_obj, 'Spread': spread_obj})
        return True
    
    #Method to display data in forms of tables
    def TabulateData(self, cash_obj, future_obj):
        return True
    
    #Method to choose form of output    
    def VisualizeData(self, cash_obj, future_obj, spread_obj, choice = 'PLOT'):
        if choice.upper() == 'PLOT':
            self.PlotData(cash_obj,future_obj, spread_obj)
        if choice.upper() == 'TABULATE':
            self.TabulateData(cash_obj, future_obj, spread_obj)   
        return True          

    #Method to trigger analysis of Cash Future Spreads            
    def StartSimpleAnalysisSpread(self, choice = 'PLOT'):
         cash_obj   = self.CreateCash_obj()
         future_obj = self.CreateFuture_obj()
         spread_obj = self.CreateSpread_obj()
         self.GetData(cash_obj, future_obj)
         self.AnalyseData(cash_obj, future_obj, spread_obj)
         self.VisualizeData(cash_obj, future_obj, spread_obj)
         return True
                
#Class to initiate an object of type CSimpleAnalysisSpread
class CTest:
    if __name__ == "__main__":      
        simple_analysis_cf_obj = CSimpleAnalysisSpread({'date': '14032016', 'symbol': 'DRREDDY-EQ', 'window_size': 15, 'path': 'C:/Users/rashishs/Downloads', 'portfolio_filename': '%T_145527.csv', 'strategy_logs_filename': 'ntwap_auto.txt', 'URL': '', 'username': '', 'password': ''})
        simple_analysis_cf_obj.StartSimpleAnalysisSpread()
                 
                    