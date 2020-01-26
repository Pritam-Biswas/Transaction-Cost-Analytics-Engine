import csv
from DataAbstractServer import CDataAbstractServer
from CommonFunctions import CCommonFunctions

'''
This is a class acting as a server for sending the Predicted Data.
It inherits the CDataAbstractServer class and since most of the functions are common for all of the server classes, they are defined in CDataAbstractServer class.
It is a separate process; Not spawned by any parent process.
'''
class CDataPredictedServer(CDataAbstractServer):

    '''
    Default constructor of CDataPredictedServer class
    Member Variables:
        m_strFilename: This stores the filename of the file to be read and the data to be sent.
        m_strData:     This stores the date for which the data is to be read.
        m_strScrip:    This stores the scrip for which the data is to be read.
        Other member variables are defined in CDataAbstractServer
    '''
    def __init__(self):
        CDataAbstractServer.__init__(self)
        self.m_strFilename = ''
        self.m_strDate     = ''
        self.m_strScrip    = ''

    '''
    This function returns a dictionary of various column names as keys and the data as values.
    In short, it parses the row so as to convert it into a understandable format.
    Input Variables:
        row: This is an entire row of data as read from the relevant csv file provided by GetDataFromFile
    '''
    def ParseRow(self, row, date, scrip):
        common_functions_obj = CCommonFunctions()
        DateTime   = common_functions_obj.GetDateTime(date, common_functions_obj.FormatTime(row[0].strip()))
        Size       = float(row[1].strip())
        ScripName  = scrip
        return {'ScripName':ScripName, 'DateTime':str(DateTime), 'Size':Size, 'eof':False}
    
    '''
    This function in short reads all the data in the file and sends the data across the socket as a list of json objects.
    Default port for listen: 52000. In order to change the port, change below.
    '''
    def GetDataFromFile(self):
        self.Listen(52000)
        self.ReceiveParams()
        self.m_strFilename = self.m_hashParams['PredictedDataFile']
        self.m_strDate     = self.m_hashParams['date']
        self.m_strScrip    = self.m_hashParams['scrip']
        
        count = 0
        with open(self.m_strFilename) as file_object:
            reader = csv.reader(file_object)
            for row in reader:
#                if row[0] == self.m_strScripName:
                data_dict = self.ParseRow(row, self.m_strDate, self.m_strScrip)
                self.m_DataList.append(data_dict)
                count += 1
            self.m_DataList[len(self.m_DataList) - 1]['eof'] = True
        self.SendJson()
        self.CloseClient()
        return True

'''
This function creates an object of CDataPredictedServer class and starts the server.
'''
def main():
    data_predicted_server_obj = CDataPredictedServer()
    data_predicted_server_obj.GetDataFromFile()

'''
This calls the main function.
'''
if __name__ == '__main__':
    main()
