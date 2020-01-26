This is the README file for clientserver folder.
This folder conatins all the data clients and data servers.
Presently the data servers are for DataMarketTrade,DatatwapPortfolio, DataCash, DataFuture...
All theses servers inherit the DataAbstractServer.

Modules overview:
DataAbstractServer - contains common socket connection and data transfer method definitions
DataMarketTradeServer - class definition for sending market data feed
...

DataBaseClient - contains method definitions for connectinf to server and receiving stream of json objects
DataMarketTradeClient - class definitions for receiving market data feed and storing shared memory
...

*To subscribe to a new data feed
- Create a Data<NewDataType>Server to connect to a web API / read data from csv file and send json objects
- Create a Data<NewDatatype>Client to connect to its server via socket and receive data 
- Both Server and Client should be base class of DataAbstractServer and DataBaseClient


