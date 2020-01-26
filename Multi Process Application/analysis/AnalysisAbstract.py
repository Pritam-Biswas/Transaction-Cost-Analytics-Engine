from abc import ABCMeta, abstractmethod

#Abstract Base Class for analysing data
class CAnalysisAbstract:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.m_hash_MetadataDict = {}
    
    #Collect data from the Feeder class and store it in respective objects
    @abstractmethod     
    def GetData(self):
        raise NotImplementedError
    
    #Analyse the collected data
    @abstractmethod     
    def AnalyseData(self):
        raise NotImplementedError
    
    #Visualise the analysed data through plots or tables
    @abstractmethod     
    def VisualizeData(self):
        raise NotImplementedError
