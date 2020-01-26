import multiprocessing
from DataBaseClient import CDataBaseClient
# from clientserver.DataBaseClient import CDataBaseClient

'''
This is a class acting as a client for sending the MarketTrade Data.
It inherits the CDataBaseClient class and since most of the functions are common for all of the client classes, they are defined in CDataBaseClient class.
It is spawned by the CAnalysisEngine process.
'''
class CDataMarketTradeClient(CDataBaseClient):
	
	'''
	Parameterised constructor for CDataMarketTradeClient class
	Input Variables:
		market_data_list: This is an input to be populated by the incoming data from the server.
		market_params:    This is the params dictionary to be sent to the server for obtaining the market data.
	Member Variables:
		m_nPort:		  This is the port number (default: 50000) to bind to the appropriate port in case of connection 				   loss. In case this is to be changed, change below.
	'''
	def __init__(self, market_data_list, market_params):
		CDataBaseClient.__init__(self, market_data_list, market_params)
		self.m_nPort 	  = 50000

'''
This function creates an object of CDataMarketTradeClient class and starts the client.
'''
def main():
	input_list    = []
	market_params = {'MarketDataFile': 'REDY.NS_20160314_trades.csv', 'scrip': 'REDY.NS'}
	data_market_trade_client_obj = CDataMarketTradeClient(input_list, market_params)
	data_market_trade_client_obj.StartClient(multiprocessing.Event(), data_market_trade_client_obj.m_nPort)

'''
This calls the main function.
'''
if __name__ == '__main__':
	main()
