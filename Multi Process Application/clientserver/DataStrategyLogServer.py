from DataAbstractServer import CDataAbstractServer
from UtilsNtwap import CUtilsNtwap
from CommonFunctions import CCommonFunctions

'''
This is a class acting as a server for sending the StrategyLog Data.
It inherits the CDataAbstractServer class and since most of the functions are common for all of the server classes, they are defined in CDataAbstractServer class.
It is a separate process; Not spawned by any parent process.
'''
class CDataStrategyLogServer(CDataAbstractServer):
    
    '''
    Default constructor of CDataStrategyLogServer class
    Member Variables:
        m_strFilename: This stores the filename of the file to be read and the data to be sent.
        m_strData:     This stores the date for which the data is to be read.
        Other member variables are defined in CDataAbstractServer
    '''
    def __init__(self):
        CDataAbstractServer.__init__(self)
        self.m_strFilename = ''
        self.m_strDate     = ''
    
    '''
    This function returns a dictionary of various column names as keys and the data as values.
    In short, it parses the row so as to convert it into a understandable format.
    Input Variables:
        row: This is an entire row of data as read from the relevant csv file provided by GetDataFromFile
    '''
    def ParseRow(self, row, date, scrip):
        common_functions_obj = CCommonFunctions()
        utils_ntwap_obj      = CUtilsNtwap()
        ScripName  = scrip
        
        row = utils_ntwap_obj.FormatRow(row)        
        if len(row) > 0: #and not utils_ntwap_obj.GetPrice(row) == 'nan': 
            DateTime  = common_functions_obj.GetDateTimeStrategyLog(date, utils_ntwap_obj.GetTimeStamp(row))
            Price     = utils_ntwap_obj.GetPrice(row)
            if not Price == 'nan':
                Price = float(Price)
            Strategy  = utils_ntwap_obj.GetStrategy(row)
        return {'ScripName':ScripName, 'DateTime':str(DateTime), 'Price':Price, 'Strategy':Strategy, 'eof':False}
    
    '''
    This function in short reads all the data in the file and sends the data across the socket as a list of json objects.
    Default port for listen: 55000. In order to change the port, change below.
    '''
    def GetDataFromFile(self):
        self.Listen(55000)
        self.ReceiveParams()
        self.m_strFilename = self.m_hashParams['StrategyLogDataFile']
        self.m_strDate     = self.m_hashParams['date']

        count = 0
        strategy_logs_file_obj      = open(self.m_strFilename)
        strategy_logs_file_contents = strategy_logs_file_obj.read().split('\n')
        
        for row in strategy_logs_file_contents:
            data_dict = self.ParseRow(row, self.m_strDate, self.m_strScripName)
            self.m_DataList.append(data_dict)
            count += 1
        
        self.m_DataList[len(self.m_DataList) - 1]['eof'] = True    
        self.SendJson()
        self.CloseClient()
        return True

'''
This function creates an object of CDataStrategyLogServer class and starts the server.
'''
def main():
    data_strategylog_server_obj = CDataStrategyLogServer()
    data_strategylog_server_obj.GetDataFromFile()

'''
This calls the main function.
'''
if __name__ == '__main__':
    main()
