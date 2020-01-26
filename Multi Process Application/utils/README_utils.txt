This is the README file for utils folder.
This folder contains class definitions for utilities required by the analyses.

Modules overview-
UtilsVolVwap -  contains methods to get paramters such as Volumes, vwap,percent volumes for market and execution data.
UtilsNtwap  - contains methods to extract strategy, price, list of strategies wrt timestamps.
UtilsSpread - contains mehods to get last traded price for a time window or for an entire day.

*To add any new utility to a analysis:
-add the method definition to the Utils<analysis_name> class
-call the utils function from AnalyseData() inside SimpleAnalysis<analysis_name> 