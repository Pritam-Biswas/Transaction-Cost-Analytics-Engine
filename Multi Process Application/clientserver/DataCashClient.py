import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the Cash Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataCashClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataCashClient class
	Input Variables:
		cash_data_list: This is an input to be populated by the incoming data from the server.
		cash_params:    This is the params dictionary to be sent to the server for obtaining the cash data.
	Member Variables:
		m_nPort:		This is the port number (default: 53000) to bind to the appropriate port in case of connection 				    loss. In case this is to be changed, change below.
	'''
	def __init__(self, cash_data_list, cash_params):
		CDataBaseClient.__init__(self, cash_data_list, cash_params)
		self.m_nPort = 53000

'''
This function creates an object of CDataCashClient class and starts the client.
'''
def main():
	input_list  = []
	cash_params = {'CashDataFile': 'ITC.NS_20160526_trades.csv', 'scrip' : 'ITC.NS'}
	data_cash_client_obj = CDataCashClient(input_list, cash_params)
	data_cash_client_obj.StartClient(multiprocessing.Event(), data_cash_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
