This is the README file of plot folder.
this folder contains a Plot framework and a CustomPlot modules.
Modules overview :
Plot Framework - contains methods for generating bar charts and scatter plots with different parameters
CustomPlot     - contains methods generate plots depending on the type of analysis

*To add a new type of plot say Pie-chart/Histogram
- add the plotting function definition to CPlotFramework class ,refer to https://plot.ly/python/ for further details on function definition
- call this new function from CCustomPlot class passing plotting variables as arguments

*To plot new figure for a different type of analysis
- Create a new CustomPlot class, say CCustomPlot2
- call the required CPlotFramework's method to generate the new figure