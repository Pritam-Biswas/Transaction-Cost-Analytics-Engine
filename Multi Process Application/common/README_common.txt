This is the README file for the Common folder.
This folder contains two modules- CommonFunctions.py, Mapping.py

Modules overview-
CommonFunctions.py - class definition for functions to manipulate and format the data fields.
Mapping.py - class definition for mapping to symbol to RIC and vice-versa.

Modules functionality-
CommonFunctions.py
->GetDateTime() - generic function to get datetime object 
->GetDateTimePortfolio() - function to get datetime object from portfolio data feed
->GetDateTimeStrategyLog() -function to get datetime object from strategy log data feed
->CompareTime() -  compare two timestamps
->GetDateTimeList() - get list of datetime objects from list of dates in string format
->GetWindowList() - get list of datetime objects equally spaced based on window size, example : windowsize = 15 
->ParseBuffer() - parse the socket buffer to give list of json objects
->FormatDateJSONn() - format 'DateTime' field in json from string type to datetime type.



Mapping.py
->FillDict() - fills a dictionary of symbol<->RIC mapping
->Sym_RIC_map() - map a symbol to its RIC
->RIC_SYm_map() - map a RIC to symbol

*To add some new function used by all analyses, put the function definition in CCommonFunction and call it using its object.
*To shift to an updated mapping dictionary, place the new mapping dictionary in common folder, pass the new dictionary's  filename as argument while creating Mapping object.

    