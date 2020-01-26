This is the README file for analysis folder.
Analysis folder contains all the analyses.
There is Analysis abstract class -CAnalysisAbstract, all types of analyses may inherit this abstract class.
Presently there are 3 types of analysis- SimpleAnalysisVolVwap, SimpleAnalysisNtwap, SimpleAnalysisSpread.
All the analyses have a basic framework-
-> StartSimpleAnalysis< analysis_name >()-starts the analysis process, gets th data from shared memory , analyses it and shows results
-> GetData() - receives the data from the shared memory, formats it as required for the analysis.
-> AnalyseData() - analyses the formatted data, to generate the results
-> VisualizeData() - chooses to either plot the dat or show it in tabular format.
-> PlotData() - plots the data using the plotly library.
-> TabulateData() - to display the data in tabular format.

** To add a new analysis-
1. create a class definition of analysis inheriting the CAnalysisAbstract class
2. place the class in the analysis folder.
3. call the data clients this analysis needs in StartClients() of AnalysisEngine.py
4. call this analysis in StartAnalyses() of AnalysisEngine.py
