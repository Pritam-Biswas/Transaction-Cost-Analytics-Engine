# Transaction Cost Analytics Engine
A Python based framework hosted on Django for analyzing financial data

Transaction Cost Analysis
Technical Documentation:

a)	Introduction 
This project aims to provide post trade transaction cost analysis whose output can be represented as graphs or as csv files. The entire user interface is in the form of a lucid, easy to use webpage. This is an effective way of gauging the efficiency of a trade. At present there is no system in place to carry out such analysis.

b)	Functional Requirements
•	Python 2.7.
•	Plotly library for graph plotting.
•	Django library for hosting the website.
•	Other libraries – multiprocessing, json, socket, csv

c)	Implementation
1.	User  Interface
i.	A neatly designed webpage serves as the User Interface.
ii.	The user needs to enter details – date, type of analysis (algorithm) performed, name of portfolio, the scrip (instrument).
iii.	The required graphs pertaining to the kind of analysis are then prepared. Click on the hyperlink to display any graph as one graph is displayed at a time on the webpage.
2.	Analysis
i.	 All execution starts from the CAnalysisEngine class.
ii.	An abstract analysis class (CAnalysisAbstract) is created detailing the methods that need to be present (defined) in for all classes carrying out analysis. This serves as a framework for all analysis classes.
iii.	CAnalysisAbstract has the following abstract methods:-
a)	GetData            -  Used to fetch the required data.
b)	AnalyseData    -   Used to run the analyses.
c)	VisualizeData  -   Used to visualize data in the form of charts, graphs or tables.
iv.	Currently the classes designed can carry out – Volume VWAP analysis, NTWAP Execution analysis and Cash Future Spread analysis. 
These are the classes carrying out the analyses:-
a)	CSimpleAnalysisVolVwap
b)	CSimpleAnalysisNtwap
c)	CSimpleAnalysisSpread
v.	The modular nature of the code means that any alternate analysis can be carried out just by adding another class detailing the analysis to be performed.
vi.	Further, more complex analysis can be carried out by inheriting these existing classes that perform basic analysis thus making it scalable to a large extent.
3.	Feeder
i.	This is the broad representation of the data being fed into the Analysis Engine.
ii.	The files are read in accordance with the analysis being performed.
iii.	Data is collected using different server and client classes for different data (e.g execution data, market trade data) which can run concurrently.
iv.	Abstract server and abstract client classes are created detailing the methods that need to be present (defined) . These serve as frameworks for all server and client classes.
The following server and client classes are defined:-
a.	CDataAbstractServer              -   CDataBaseClient
b.	CDataMarketTradeServer      -   CDataMarketTradeClient
c.	CDataTwapPortfolioServer   -    CDataTwapPortfolioClient
d.	CDataPredictedServer            -   CDataPredictedClient
e.	CDataCashServer                     -   CDataCashClient
f.	CDataFutureServer                  -   CDataFutureClient
g.	CDataStrategyLogServer         -   CDataStrategyLogClient
v.	CDataAbstractServer has the following methods defined:-
a.	Listen      -      This method binds the socket to the port, which is taken as an argument. Then it starts listening for client’s connection. Finally, it accepts the connection from the client and the connection is established.
b.	ReceiveParams    -   This method receives the json message containing the parameters from the client and parses it. It then stores the scrip name contained in the parsed json message in a member variable.
c.	SendJson   -   This method sends the row-wise data one by one in the form of json messages to the client.
vi.	CDataBaseClient has the following methods defined:-
a.	Connect  -   This method connects to the server taking the port as an argument.
b.	StoreData  -  
c.	SendParams  -
d.	ReceiveData  -
e.	Disconnect  -
f.	StartClient  -
vii.	The data retrieved is stored then stored using different classes defined for different data. A data abstract class is also created which would have member variables common to all the data classes.
A class (CFormatData) is also defined which is used to convert row-wise data stored in the form of a list into separate lists column wise and store it.
The following data classes are defined:-
a.	CDataAbstract
b.	CDataMarketTrade
c.	CDataTwapPortfolio
d.	CDataPredicted
e.	CDataCash
f.	CDataFuture
g.	CDataStrategyLog 
viii.	The modular nature of the code means that any the retrieval of data for any alternate analysis can be carried out just by adding another class   detailing the data that needs to be fed.
4.	Utilities and Common Functions
i.	Utils classes are defined which contain methods used to do all the required calculations.
The following Utils classes are defined:-
a.	CUtilsVolVwap
It has the following methods:-
•	GetVolWindow  -  Method to get volume of trade in one time window.
•	GetVwapWindow  -  Method to get Vwap in a given time window.
•	GetPercentVol  -  Method to get list of percentage of trade volume.
•	GetPercentFraction  -  Method to convert fraction of daily trade volume into percentage.
•	GetVolTotal  -  Method to get Volume traded for entire day for different time windows as a list.
•	GetVwapTotal  -  Method to get Vwap for entire day for different time windows as a list.
•	GetPartialTimeWindowList  -  Method to get time window liat from the point where the portfolio started trading
b.	CUtilsSpread
It has the following methods:-
•	GetLastPriceWindow  -  Method to get last traded price and populate the list of last traded prices.  
•	GetLastPriceTotal  -  Method to get the list of last traded prices. 
c.	CUtilsNtwap 
It has the following methods:-
•	GetTimeStamp  -  Method to extract timestamp (string) from a row of data when reading a strategy log file.
•	GetPrice  -  Method to extract price from a row of data when reading a strategy log file.
•	GetStrategy  -  Method to extract strategy name from a row of data when reading a strategy log file. 
•	FormatRow  -  Method to convert a row of data in strategy log files into a list.
•	GetStrategyList  -  Method to populate executed strategies list.
•	GetMovingAverages  -  Method to get list of moving averages when a portfolio data object is passed as an argument.
ii.	A CSpread class is created which is used to store the calculated data pertaining to cash-future spread.
iii.	A CCommonFunctions class is created which contains methods used frequently in various modules of the code.
It has the following methods:-
a.	GetDateTime  -  Returns datetime object when date and time are passed as arguments.
b.	 GetDateTimeStrategyLog   -  Returns datetime object in case of reading a log file. 
c.	GetDateTimePortfolio  -  Returns datetime object in case of reading a csv file containing portfolio execution data.
d.	GetDateTimeList  -  Used to populate the datetime list and return it.
e.	GetDateTimeListPortfolio  -  Used to populate the datetime list when reading data from a csv file containing portfolio execution data and return it.
f.	CompareTime  -  Used to compare two datetime objects. Returns -1 if datetime 1 < datetime 2 and 1 otherwise.
g.	FormatTime  -  Returns time in “hh:mm:ss” format (string). Converts “hhmmss” (string) into the above format.
h.	FormatDate  -  Returns date in “yyyymmdd” format (string). Converts “ddmmyyyy” (string) into the above format.
i.	GetWindowList  -  Returns two lists. One of them contains time windows (string) and the other contains mid points of the time windows (string).
j.	FindOccurences  -  
k.	ParseBuffer  -  
l.	FormatDateJSON  -    
iv.	A CMapping class is created which is used to map RIC to symbols and vice versa.
5.	Plotter
i.	A CPlotFrameWork class is created which contains all the methods pertaining to plot/tabulate data. They are created in such a way that one needs to just pass the lists corresponding to the axes as arguments to obtain the graph. The other parameters are set as default within these methods (for e.g auto_open is set as False within these methods).
It has the following methods:-
a.	GetBarChart  -  Method to get bar chart
b.	GetScatterPlot  -  Method to get scatter plot
c.	GetLayout  -  Method to get plot layout
d.	GetFigure  -  Method to get figure object
e.	GetPlot  -  Method to plot using figure object
ii.	A CCustomPlot class is created which uses the methods defined in CPlotFramework to prepare the graphs. It prepares these graphs according to the type of analysis.
It has the following methods:-
a.	StartPlot  -  Method to pass required arguments to plotting methods.
b.	Market_vs_portfolio_vwap  -  Method to plot Market vs Portfolio (VWAP).
c.	Market_vs_portfolio_vol_vwap  -  Method to plot Market vs Portfolio (Volume and VWAP).
d.	Market_vs_predicted_vol  -  Method to plot Market vs Predicted (Volume)
e.	Market_vs_predicted_vol_diff  -  Method to plot Market vs Predicted (Volume Difference).
f.	Market_vs_orderCompletion_price   -  Method to plot Market vs Order Completion Price.
g.	CF_Spread  -  Method to plot Cash and Future spread data along with the minimum of both.
h.	NTWAP_Execution  -  Method to plot NTWAP execution data along with market data.
  
Functional Documentation:
a)	Introduction
Post trade TCA is used to evaluate the performance of a strategy or trader. This kind of evaluation helps in identifying flaws which can be improved upon. It can be used with real time data feed as well to know the performance of the strategy in so far in the day. At present, there is no in-house facility to address this need.
b)	Functional Requirement
There is a need to evaluate the performance of any strategy and benchmark it. A strategy which works fine now may start decaying any time in the future.  There is a need to whether the strategy has executed trades at the right time. These things make a post trade TCA engine a requirement any trading firm cannot compromise with.
This TCA engine helps in analyzing the performance of the strategies by displaying graphs and charts in a very dynamic UI. It can be improved further to do a lot of other things. For e.g. it can be extended to run various other kinds of analyses, a backtesting engine can also be added to backtest the strategies and further a portfolio manager can also be developed and plugged into this device. Because of the ‘plug and play’ architecture, one just has to develop these additional components separately and plug it into the existing architecture.
c)	User Manual
1)  Open the dedicated web-page.
2)  Select the date over which you want to run the analysis on.
3)  Select the type of analysis from the drop-down menu.
4)  Select the desired portfolio from the drop down menu containing the portfolios registered under the traders.
5)  Select the desired derivative from the drop down menu containing the derivatives under that portfolio.
6)  Click on “Generate Report” button and the graphs will be prepared.
7)  Click on the respective links to display the graphs.
              

