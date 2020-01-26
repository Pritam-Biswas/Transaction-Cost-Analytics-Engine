import os

#Class to map symbols to RIC symbols for a particular portfolio
class CMapping:
    def __init__(self):
        self.m_hash_RICSymbolDict = dict()
        self.m_hash_SymbolRICDict = dict()
    
    #create mapping dictionary 
    def FillDict(self, filename): 
        file_obj        = open(os.path.join(os.path.dirname(__file__) + '/' + filename))
        file_contents   = file_obj.read().split('\n')
        
        for iter in range(0, len(file_contents)):
            pos_of_colon                       = file_contents[iter].find(':')
            pos_of_equals                      = file_contents[iter].find('=')
            symbol                             = file_contents[iter][0:pos_of_colon]
            RIC                                = file_contents[iter][pos_of_equals + 1: ]
            self.m_hash_RICSymbolDict[symbol]  = RIC
            self.m_hash_SymbolRICDict[RIC]     = symbol
        return True
    
    #search and return RIC for the corresponding symbol if available, return -1 otherwise
    def Sym_RIC_map(self, symbol): 
        try:        
            RIC = self.m_hash_RICSymbolDict[symbol]
            return RIC
        except:
            return -1
    
    #search and return symbol for the corresponding RIC if available, return -1 otherwise
    def RIC_Sym_map(self, RIC): 
        try:        
            symbol = self.m_hash_SymbolRICDict[RIC]
            return symbol
        except:
            return -1
