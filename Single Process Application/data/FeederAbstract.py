import json
import os
from common.Mapping import CMapping
from abc import ABCMeta, abstractmethod

class CFeederAbstract:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.m_hash_DataSourceDict = {}
        self.m_strRIC              = ''
    
    @abstractmethod
    def GetData(self):
        raise NotImplementedError
    
    def GetTCAMetadata(self):  
        with open(os.path.join(os.path.dirname(__file__) + '/' + 'TCA_Metadata.json')) as datafile:
            self.m_hash_DataSourceDict = json.load(datafile)
        return True
    
    def GetRIC(self):
        Mapping_obj   = CMapping()
        Mapping_obj.FillDict('FlexSymRICMap.txt')
        self.m_strRIC = Mapping_obj.Sym_RIC_map(self.m_strSymbol)
        return True
