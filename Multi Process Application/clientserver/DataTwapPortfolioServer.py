import csv
from DataAbstractServer import CDataAbstractServer
from CommonFunctions import CCommonFunctions

'''
This is a class acting as a server for sending the TwapPortfolio Data.
It inherits the CDataAbstractServer class and since most of the functions are common for all of the server classes, they are defined in CDataAbstractServer class.
It is a separate process; Not spawned by any parent process.
'''
class CDataTwapPortfolioServer(CDataAbstractServer):
    
    '''
    Default constructor of CDataTwapPortfolioServer class
    Member Variables:
        m_strFilename: This stores the filename of the file to be read and the data to be sent.
        Other member variables are defined in CDataAbstractServer
    '''
    def __init__(self):
        CDataAbstractServer.__init__(self)
        self.m_strFilename = ''
    
    '''
    This function returns a dictionary of various column names as keys and the data as values.
    In short, it parses the row so as to convert it into a understandable format.
    Input Variables:
        row: This is an entire row of data as read from the relevant csv file provided by GetDataFromFile
    '''
    def ParseRow(self, row):
        common_functions_obj = CCommonFunctions()
        temp_datetime        = row[0].strip().split(' ')
        date                 = temp_datetime[0]
        time                 = temp_datetime[1]
        DateTime    = common_functions_obj.GetDateTimePortfolio(date, time)
        ScripName   = row[1].strip()
        OrderID     = row[2].strip()
        Status      = row[3].strip()
        OrderQty    = row[4].strip()
        OrderPrice  = row[5].strip()
        Side        = row[6].strip()
        FilledSize  = row[7].strip()
        AvgPrice    = row[8].strip()
        Price       = row[9].strip()
        Size        = row[10].strip()
        return {'ScripName':ScripName, 'DateTime':str(DateTime), 'Price':Price, 'Size':Size, 'OrderID':OrderID, 'Status':Status, 'OrderQty':OrderQty, 'OrderPrice':OrderPrice, 'Side':Side, 'FilledSize':FilledSize, 'AvgPrice':AvgPrice, 'eof':False}
    
    '''
    This function in short reads all the data in the file and sends the data across the socket as a list of json objects.
    Default port for listen: 51000. In order to change the port, change below.
    '''
    def GetDataFromFile(self):
        self.Listen(51000)
        self.ReceiveParams()
        self.m_strFilename = self.m_hashParams['TwapPortfolioDataFile']

        count = 0
        with open(self.m_strFilename) as file_object:
            reader = csv.reader(file_object)
            for row in reader:
                if row[1] == self.m_strScripName:
                    data_dict = self.ParseRow(row)
                    self.m_DataList.append(data_dict)
                    count += 1            
        self.m_DataList[len(self.m_DataList) - 1]['eof'] = True
        self.SendJson()
        self.CloseClient()
        return True

'''
This function creates an object of CDataTwapPortfolioServer class and starts the server.
'''
def main():
    data_twap_portfolio_server_obj = CDataTwapPortfolioServer()
    data_twap_portfolio_server_obj.GetDataFromFile()

'''
This calls the main function.
'''
if __name__ == '__main__':
    main()
