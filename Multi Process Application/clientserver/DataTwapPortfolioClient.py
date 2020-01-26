import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the TwapPortfolio Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataTwapPortfolioClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataTwapPortfolioClient class
	Input Variables:
		portfolio_data_list: This is an input to be populated by the incoming data from the server.
		portfolio_params:    This is the params dictionary to be sent to the server for obtaining the portfolio data.
	Member Variables:
		m_nPort:		     This is the port number (default: 51000) to bind to the appropriate port in case of 							 connection loss. In case this is to be changed, change below.
	'''
	def __init__(self, portfolio_data_list, portfolio_params):
		CDataBaseClient.__init__(self, portfolio_data_list, portfolio_params)
		self.m_nPort = 51000

'''
This function creates an object of CDataTwapPortfolioClient class and starts the client.
'''
def main():
	input_list       = []
	portfolio_params = {'TwapPortfolioDataFile': '%T_145527.csv', 'scrip': 'DRREDDY-EQ'}
	data_twap_portfolio_client_obj = CDataTwapPortfolioClient(input_list, portfolio_params)
	data_twap_portfolio_client_obj.StartClient(multiprocessing.Event(), data_twap_portfolio_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
