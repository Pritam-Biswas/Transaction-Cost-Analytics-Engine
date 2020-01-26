This the README file for the data folder.
This folder contains the class definitions for storing the different types of data before they can be analysed.
Modules Overview:
FormatData      - contains methods to convert the stream of json objects into list of paramters.
DataAbstract    - conatins common paramters of all data feeds
DataMarketTrade -contains paramters specific to the market data feed.
...


*To add any new format of data :
- put the class definition the new format in data folder.
- add a method definition to the CFormatData class in FormatData.py as FormatData<FormatName>
- call this FormatData<FormatName> in the GetData() of your analysis

