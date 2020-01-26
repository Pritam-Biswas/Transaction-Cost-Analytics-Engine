import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the Future Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataFutureClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataFutureClient class
	Input Variables:
		future_data_list: This is an input to be populated by the incoming data from the server.
		future_params:    This is the params dictionary to be sent to the server for obtaining the future data.
	Member Variables:
		m_nPort:		  This is the port number (default: 54000) to bind to the appropriate port in case of connection 				   loss. In case this is to be changed, change below.
	'''
	def __init__(self, future_data_list, future_params):
		CDataBaseClient.__init__(self, future_data_list, future_params)
		self.m_nPort = 54000

'''
This function creates an object of CDataFutureClient class and starts the client.
'''
def main():
	input_list    = []
	future_params = {'FutureDataFile': 'ITCK6NS_20160526_trades.csv', 'scrip': 'ITCK6:NS'}
	data_future_client_obj = CDataFutureClient(input_list, future_params)
	data_future_client_obj.StartClient(multiprocessing.Event(), data_future_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
