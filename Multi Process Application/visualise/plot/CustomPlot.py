from PlotFramework import CPlotFramework

#Class to plot analysed data

#Sequence to be followed to obtain any plot:-
#a) Create PlotFramework object
#b) Call GetBarChart method
#c) Call GetScatterPlot method
#d) Call GetLayout method
#e) Call GetFigure method

class CCustomPlot():
    def __init__(self):
        return
    
    #To pass required arguments to plotting methods    
    def StartPlot(self, object_dict):
        print "entered plotting of volvwap"
        if object_dict['Market'] != '' or object_dict['Portfolio'] != '' or object_dict['Predicted'] != '':
            self.Market_vs_portfolio_vwap(object_dict['Market'], object_dict['Portfolio'])
            self.Market_vs_portfolio_vol_vwap(object_dict['Market'], object_dict['Portfolio'])
            self.Market_vs_predicted_vol(object_dict['Market'], object_dict['Predicted'])
            self.Market_vs_predicted_vol_diff(object_dict['Market'], object_dict['Predicted'])
            self.Market_vs_orderCompletion_price(object_dict['Market'], object_dict['Portfolio'])
        elif object_dict['Cash'] != '' or object_dict['Future'] != '':
            self.CF_Spread(object_dict['Cash'], object_dict['Future'], object_dict['Spread'])
        print "finished all plottings of volvwap"
        return True
    
    #To plot Market vs Portfolio (VWAP)  
    def Market_vs_portfolio_vwap(self, market_obj, portfolio_twap_obj):
        plot_framework_obj      = CPlotFramework()
        print "displaying portfolio date and vwap"
        for iter in range(0, len(portfolio_twap_obj.m_strPartialTimeWindowList)):
            print str(portfolio_twap_obj.m_strPartialTimeWindowList[iter]) + "\t" + str(portfolio_twap_obj.m_fVwapWindowList)
        portfolio_vwap_plot     = plot_framework_obj.GetScatterPlot(portfolio_twap_obj.m_strPartialTimeWindowList, portfolio_twap_obj.m_fVwapWindowList, 'Portfolio VWAP',     'lines+markers')
        market_vwap_plot        = plot_framework_obj.GetScatterPlot(market_obj.m_strPartialTimeWindowList,         market_obj.m_fVwapWindowList,         'Actual Market VWAP', 'lines+markers')
        layout                  = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET VS PORTFOLIO VWAP', 'TIME', 'VWAP')
        fig                     = plot_framework_obj.GetFigure([market_vwap_plot, portfolio_vwap_plot], layout, 'MARKET_PORTFOLIO_VWAP.html')
        return True
    
    #To plot Market vs Portfolio (Volume and VWAP)
    def Market_vs_portfolio_vol_vwap(self, market_obj, portfolio_twap_obj):
        plot_framework_obj              = CPlotFramework()
        percent_portfolio_volume_plot   = plot_framework_obj.GetBarChart(portfolio_twap_obj.m_strTimeWindowList,            portfolio_twap_obj.m_fPercentVolumeWindowList, 'Portfolio Volume')
        percent_market_volume_plot      = plot_framework_obj.GetBarChart(market_obj.m_strTimeWindowList,                    market_obj.m_fPercentVolumeWindowList,         'Actual Market Volume')
        portfolio_vwap_plot             = plot_framework_obj.GetScatterPlot(portfolio_twap_obj.m_strPartialTimeWindowList,  portfolio_twap_obj.m_fVwapWindowList,          'Portfolio VWAP',     'lines+markers', 'y2')
        market_vwap_plot                = plot_framework_obj.GetScatterPlot(market_obj.m_strPartialTimeWindowList,          market_obj.m_fVwapWindowList,                  'Actual Market VWAP', 'lines+markers', 'y2')
        layout                          = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET VS PORTFOLIO', 'TIME', 'PERCENTAGE OF VOLUME', 'VWAP')
        fig                             = plot_framework_obj.GetFigure([percent_market_volume_plot, percent_portfolio_volume_plot, market_vwap_plot, portfolio_vwap_plot], layout, 'MARKET_VS_PORTFOLIO_EXECUTIONS.html')        
        return True
    
    #To plot Market vs Predicted (Volume)
    def Market_vs_predicted_vol(self, market_obj, predicted_obj):
        plot_framework_obj      = CPlotFramework()
        predicted_volume_plot   = plot_framework_obj.GetBarChart(market_obj.m_strPartialTimeWindowList, predicted_obj.m_fPercentVolumeWindowList, 'Predicted market volume')
        market_volume_plot      = plot_framework_obj.GetBarChart(predicted_obj.m_strTimeWindowList,     market_obj.m_fPercentVolumeWindowList,    'Actual market volume')
        layout                  = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET: ACTUAL VS PREDICTED', 'TIME', 'PERCENTAGE OF VOLUME')
        fig                     = plot_framework_obj.GetFigure([predicted_volume_plot, market_volume_plot], layout, 'ACTUAL_PREDICTED_VOLUME.html')
        return True
    
    #To plot Market vs Predicted (Volume Difference) 
    def Market_vs_predicted_vol_diff(self, market_obj, predicted_obj):
        plot_framework_obj = CPlotFramework()
        volume_diff        = []
        for iter in range(0, len(market_obj.m_fPercentVolumeWindowList)):
            volume_diff.append(predicted_obj.m_fPercentVolumeWindowList[iter] - market_obj.m_fPercentVolumeWindowList[iter])
        
        diff_volume_plot = plot_framework_obj.GetBarChart(predicted_obj.m_strTimeWindowList, volume_diff, 'Predicted market volume - Actual market volume')
        layout           = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET: PREDICTED - ACTUAL', 'TIME', 'PERCENTAGE OF VOLUME', showlegend = True, legend = dict(x = 0.9, y = 1))
        fig              = plot_framework_obj.GetFigure([diff_volume_plot], layout, 'VOLUME_DIFFERENCE.html')
        return True
    
    #To plot Market vs Order Completion Price
    def Market_vs_orderCompletion_price(self, market_obj, portfolio_twap_obj):
        plot_framework_obj             = CPlotFramework()
        market_price_plot              = plot_framework_obj.GetScatterPlot(market_obj.m_DatetimeList,                      market_obj.m_fPriceList,                         'Market Price movement', 'lines', '', 'hv')
        order_complete_fillprice_plot  = plot_framework_obj.GetScatterPlot(portfolio_twap_obj.m_OrderCompleteDatetimeList, portfolio_twap_obj.m_fOrderCompleteAvgPriceList, 'Order Execution Price', 'markers')
        layout                         = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET AND EXECUTION PRICE MOVEMENTS', 'TIME', 'PRICE')
        fig                            = plot_framework_obj.GetFigure([market_price_plot, order_complete_fillprice_plot], layout, 'MARKET_EXECUTION_PRICE.html')
        return True
    
    #To plot Cash and Future spread data along with the minimum of both
    def CF_Spread(self, cash_obj, future_obj, spread_obj):
        plot_framework_obj  = CPlotFramework()
        cash_price_plot     = plot_framework_obj.GetScatterPlot(cash_obj.m_DatetimeList,            cash_obj.m_fPriceList,      'Cash Value',    'lines', '', 'hv')
        future_price_plot   = plot_framework_obj.GetScatterPlot(future_obj.m_DatetimeList,          future_obj.m_fPriceList,    'Future Value',  'lines', '', 'hv')
        min_price_plot      = plot_framework_obj.GetScatterPlot(spread_obj.m_MinPriceTimestampList, spread_obj.m_fMinPriceList, 'Minimum Value', 'lines', '', 'hv')
        layout              = plot_framework_obj.GetLayout('<b>' + cash_obj.m_strScripName.upper() + '</b><br>Cash || Future || Min(Cash, Future)', 'TIME', 'PRICE')
        fig                 = plot_framework_obj.GetFigure([cash_price_plot, future_price_plot, min_price_plot], layout, 'SMARTSWITCH_EXECUTION.html')
        
        return
    
    #To plot NTWAP execution data along with market data
    def NTWAP_Execution(self, market_obj, portfolio_twap_obj, strategy_log_obj):
        print "entered ntwap execution plot"
        plot_framework_obj             = CPlotFramework()
        FG_priceList                   = []
        FG_timestampList               = []
        HIT_priceList                  = []
        HIT_timestampList              = []
        moving_averages_timestampList  = portfolio_twap_obj.m_OrderExecutionDatetimeList[2: ]
        
        for iter in range(0, len(strategy_log_obj.m_strStrategyExecutionList)):
            if strategy_log_obj.m_strStrategyExecutionList[iter] == 'F&G':
                FG_priceList.append(portfolio_twap_obj.m_fOrderExecutionFillPriceList[iter])
                FG_timestampList.append(portfolio_twap_obj.m_OrderExecutionDatetimeList[iter])
            elif strategy_log_obj.m_strStrategyExecutionList[iter] == 'HIT':
                HIT_priceList.append(portfolio_twap_obj.m_fOrderExecutionFillPriceList[iter])
                HIT_timestampList.append(portfolio_twap_obj.m_OrderExecutionDatetimeList[iter])
        # print "displaying price list"
        # for price in market_obj.m_fPriceList:
        #     print str(price)
        # print "dispalying datetime list"
        # for date_obj in market_obj.m_DatetimeList:
        #     print str(date_obj)

        # print "displaying Strategy execution list"
        # for iter in range(0, len(strategy_log_obj.m_strStrategyExecutionList)):
        #     print str(strategy_log_obj.m_strStrategyExecutionList[iter])

        print "displaying F&G list"
        for iter in range(0, len(FG_priceList)):
            print str(FG_priceList[iter]) + '\t' + str(FG_timestampList[iter])

        print "displaying HIT list"
        for iter in range(0, len(HIT_priceList)):
            print str(HIT_priceList[iter]) + '\t' + str(HIT_timestampList[iter])

        market_price_plot    = plot_framework_obj.GetScatterPlot(market_obj.m_DatetimeList,     market_obj.m_fPriceList,                               'Market Price movement', 'lines', '', 'hv')
        FG_execution_plot    = plot_framework_obj.GetScatterPlot(FG_timestampList,              FG_priceList,                                          'F&G Execution',         'markers')
        HIT_execution_plot   = plot_framework_obj.GetScatterPlot(HIT_timestampList,             HIT_priceList,                                         'HIT Execution',         'markers')
        moving_averages_plot = plot_framework_obj.GetScatterPlot(moving_averages_timestampList, portfolio_twap_obj.m_fOrderExecutionMovingAverageList, 'Moving averages',       'lines')
        layout               = plot_framework_obj.GetLayout('<b>' + market_obj.m_strScripName.upper() + '</b><br>MARKET AND NTWAP PRICE MOVEMENTS', 'TIME', 'PRICE')
        fig                  = plot_framework_obj.GetFigure([market_price_plot, FG_execution_plot, HIT_execution_plot, moving_averages_plot], layout, 'NTWAP_EXECUTION.html')
        print "finished ntwap execution plot"
        return True
