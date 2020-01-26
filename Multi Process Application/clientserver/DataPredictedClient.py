import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the Predicted Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataPredictedClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataPredictedClient class
	Input Variables:
		predicted_data_list: This is an input to be populated by the incoming data from the server.
		predicted_params:    This is the params dictionary to be sent to the server for obtaining the predicted data.
	Member Variables:
		m_nPort:		     This is the port number (default: 52000) to bind to the appropriate port in case of 							 connection loss. In case this is to be changed, change below.
	'''
	def __init__(self, predicted_data_list, predicted_params):
		CDataBaseClient.__init__(self, predicted_data_list, predicted_params)
		self.m_nPort = 52000

'''
This function creates an object of CDataPredictedClient class and starts the client.
'''
def main():
	input_list       = []
	predicted_params = {'PredictedDataFile': 'REDY.NS.csv', 'scrip': 'REDY.NS', 'date': '14032016'}
	data_predicted_client_obj = CDataPredictedClient(input_list, predicted_params)
	data_predicted_client_obj.StartClient(multiprocessing.Event(), data_predicted_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
