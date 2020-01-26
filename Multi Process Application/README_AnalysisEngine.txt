This is the README file for the AnalysisEngine.

The Analytics Engine performs the following tasks in this sequence-
1. It creates Clients which receives data feeds from independently running servers via TCP/IP socket communication.Data is received in form of JSON objects. The JSON objects have a custom boolean field - 'eof'. It is set to True if that feed is the last feed.
Preently the following data clients are created- MarketData Client, Execution data client, Strategylog client, Predicted data client.

2. It creates three types of analysis processes-  SimpleAnalysis VolVwap, SimpleAnalysis NTWAP, SimpleAnalysis Spread.
SimpleAnalysis Volvwap waits till it has received market, execution and predicted data.
SimpleAnalysis NTWAP waits till it has received market, execution and strategylog data.
SimpleAnalysis Spread waits till it has received Cash and Futures data.
The three analyses are started as separate processes. These process has class definitions in the analysis folder.

3. Shared memory is used for communication between the data clients and analysis processes.
Multiprocessing library provides us 'Manager' class for creating shared memory data structures.
We have used Manager.list()  to store list of json objects received by clients.

4. Multiprocessing library's 'event' module is used create an event driven framework.
For example: m_DataMarketTradeEOF is an event that waits for end of feed of the market data.
To wait till the event has occured, we use m_DataMarketTradeEOF.wait()

5. The CAnalysisEngine can be extended to new data clients or new analyses.
To add a new client create a class definition of the client, put it in clientserver and call that client in StartClients() in CAnalysisEngine
To add a new analysis create a class definition of the analysis and call that analysis in StartAnalyses() in CAnalysisEngine.
