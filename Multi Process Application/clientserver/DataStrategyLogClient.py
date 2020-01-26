import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the StrategyLog Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataStrategyLogClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataStrategyLogClient class
	Input Variables:
		strategylog_data_list: This is an input to be populated by the incoming data from the server.
		strategylog_params:    This is the params dictionary to be sent to the server for obtaining the strategylog data.
	Member Variables:
		m_nPort:		  	   This is the port number (default: 55000) to bind to the appropriate port in case of 							   connection loss. In case this is to be changed, change below.
	'''
	def __init__(self, strategylog_data_list, strategylog_params):
		CDataBaseClient.__init__(self, strategylog_data_list, strategylog_params)
		self.m_nPort = 55000

'''
This function creates an object of CDataStrategyLogClient class and starts the client.
'''
def main():
	input_list         = []
	strategylog_params = {'StrategyLogDataFile': 'ntwap_auto.txt', 'scrip': 'NTPC16JUNFUT', 'date': '14032016'}
	data_strategylog_client_obj = CDataStrategyLogClient(input_list, strategylog_params)
	data_strategylog_client_obj.StartClient(multiprocessing.Event(), data_strategylog_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
