import os
import json
from analysis.SimpleAnalysisVolVwap import CSimpleAnalysisVolVwap
from analysis.SimpleAnalysisSpread import CSimpleAnalysisSpread
from analysis.SimpleAnalysisNtwap import CSimpleAnalysisNTWAP

class CAnalysisEngine:
    def __init__(self, input_dict):
        self.m_hash_MetadataDict   = input_dict
        self.m_hash_DataSourceDict = {}
    
    def GetTCAMetadata(self):
        with open(os.path.join(os.path.dirname(__file__) + '/data/TCA_Metadata.json')) as datafile:
            self.m_hash_DataSourceDict = json.load(datafile)
        return True
    
    def PopulateTCAMetadataJson(self, analysis_flag):
        with open(os.path.join(os.path.dirname(__file__) + '/data/TCA_Metadata.json'), 'w') as datafile:
            data = {}
            if analysis_flag == 0:
                data = {"Analysis_type": "Vol_Vwap", "Market": "File", "Portfolio": "File", "Predicted": "File", "Cash": "", "Future": "", "StrategyLogs": ""}
            elif analysis_flag == 1:
                data = {"Analysis_type": "Spread", "Market": "", "Portfolio": "", "Predicted": "", "Cash": "File", "Future": "File", "StrategyLogs": ""}
            elif analysis_flag == 2:
                data = {"Analysis_type": "Ntwap", "Market": "File", "Portfolio": "File", "Predicted": "", "Cash": "", "Future": "", "StrategyLogs": "File"}
            json.dump(data, datafile)
    
    def StartTCA(self, analysis_flag):
        self.PopulateTCAMetadataJson(analysis_flag)
        self.GetTCAMetadata()
        
        if self.m_hash_DataSourceDict['Analysis_type'].upper() == 'VOL_VWAP':
            simple_analysis_vol_vwap_obj = CSimpleAnalysisVolVwap(self.m_hash_MetadataDict)
            simple_analysis_vol_vwap_obj.StartSimpleAnalysisVolVwap()
        elif self.m_hash_DataSourceDict['Analysis_type'].upper() == 'SPREAD':
            simple_analysis_spread_obj = CSimpleAnalysisSpread(self.m_hash_MetadataDict)
            simple_analysis_spread_obj.StartSimpleAnalysisSpread()
        elif self.m_hash_DataSourceDict['Analysis_type'].upper() == 'NTWAP':
            simple_analysis_ntwap_obj = CSimpleAnalysisNTWAP(self.m_hash_MetadataDict)
            simple_analysis_ntwap_obj.StartSimpleAnalysisNTWAP()

if __name__ == "__main__":
    analysis_flag          = 0
    argument_dict_vol_vwap = {'date': '14032016', 'symbol': 'DRREDDY-EQ',   'window_size': 15, 'path': 'D:/Repo/Branches/RB_1.0.1/TCA/modular', 'portfolio_filename': '%T_145527.csv', 'strategy_logs_filename': '',               'URL': '', 'username': '', 'password': ''}
    argument_dict_spread   = {'date': '26052016', 'symbol': 'ITC16MAYFUT',  'window_size': 15, 'path': 'D:/Repo/Branches/RB_1.0.1/TCA/modular', 'portfolio_filename': '',              'strategy_logs_filename': '',               'URL': '', 'username': '', 'password': ''}
    argument_dict_ntwap    = {'date': '06062016', 'symbol': 'NTPC16JUNFUT', 'window_size': 15, 'path': 'D:/Repo/Branches/RB_1.0.1/TCA/modular', 'portfolio_filename': '%T_085848.csv', 'strategy_logs_filename': 'ntwap_auto.txt', 'URL': '', 'username': '', 'password': ''}
    
    def ChooseDict():
        if analysis_flag == 0:
            return argument_dict_vol_vwap
        elif analysis_flag == 1:
            return argument_dict_spread
        elif analysis_flag == 2:
            return argument_dict_ntwap
    
    analysis_engine_obj    = CAnalysisEngine(ChooseDict())
    analysis_engine_obj.StartTCA(analysis_flag)
