from plotly.offline import plot
import plotly.graph_objs as go

#Framework class for plotting

#Sequence to be followed to obtain any plot:-
#a) Create PlotFramework object
#b) Call GetBarChart method
#c) Call GetScatterPlot method
#d) Call GetLayout method
#e) Call GetFigure method

class CPlotFramework:
    def __init__(self):
        return
    
    def GetBarChart(self, x_axis, y_axis,plot_name, y_axis_type = ''): #Method to get bar chart
        if y_axis_type == '':
            return go.Bar(x = x_axis, y = y_axis, name = plot_name)
        else:
            return go.Bar(x = x_axis, y = y_axis, name = plot_name, yaxis = y_axis_type)
        
        
    def GetScatterPlot(self, x_axis, y_axis, plot_name, plot_type = 'lines+markers',  y_axis_type = '', shape = ''): #Method to get scatter plot
        if y_axis_type == '':
            return go.Scatter(x = x_axis, y = y_axis, mode = plot_type, name = plot_name, line = dict(shape = shape))
        else:
            return go.Scatter(x = x_axis, y = y_axis, mode = plot_type, name = plot_name, yaxis = y_axis_type, line = dict(shape = shape))
        
    def GetLayout(self, title,x_axis = '', y_axis   = '' , y_axis2 = '', showlegend = True, legend = dict(x = 1, y = 1)): #Method to get plot layout
        if y_axis2 == '':
            return go.Layout(title = title, xaxis = dict(title = x_axis), yaxis = dict(title = y_axis), showlegend = showlegend, legend = legend)
        else :
            return go.Layout(title = title, xaxis = dict(title = x_axis), yaxis = dict(title = y_axis),yaxis2 = dict(title = y_axis2, titlefont = dict(color = 'rgb(148, 103, 189)'), tickfont = dict(color = 'rgb(148, 103, 189)'), overlaying = 'y', side = 'right'), showlegend = showlegend, legend = legend)
    
    def GetFigure(self, trace, layout, filename = 'default.html'): #Method to get figure object
        figure =  go.Figure(data = trace, layout = layout)
        return self.GetPlot(figure, filename)
        
    def GetPlot(self, figure, filename = "default.html"): #Method to plot using figure object
        return plot(figure, filename = filename, auto_open = False)
