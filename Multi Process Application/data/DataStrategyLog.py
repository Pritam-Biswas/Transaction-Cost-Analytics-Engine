from DataAbstract import CDataAbstract

#Class to feed values from the Strategy Logs
class CDataStrategyLog(CDataAbstract):
    def __init__(self):
        CDataAbstract.__init__(self)
        self.m_strStrategyList          = []
        self.m_strStrategyExecutionList = []
