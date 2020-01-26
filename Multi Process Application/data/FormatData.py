from common.CommonFunctions import CCommonFunctions

'''
This class takes in the various data lists (json objects (rows of data)) and splits them into individual variable lists.
'''
class CFormatData:

    '''
    Parameterised constructor of CFormatData class.
    Input Variables:
        input_dict:    This is also a sort of params variable.
    Member Variables:
        m_nWindowSize: This stores the window size as desired by the user; provided in the UI.
    '''
    def __init__(self, input_dict):
		self.m_nWindowSize = input_dict['window_size']

    '''
    This function splits the MarketTrade objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        market_obj:       This is given as an input so that this function can populate this object.
        market_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataMarket(self, market_obj, market_data_list):
        common_functions_obj = CCommonFunctions()
        market_obj.m_strScripName = market_data_list[0]['ScripName']
        temp_date = market_data_list[0]['DateTime'].date()
        temp_date = str(temp_date.day) + '-' + str(temp_date.month) + '-' + str(temp_date.year)
        for market_data in market_data_list:
            market_obj.m_nCountOfRows += 1
            market_obj.m_DatetimeList.append(market_data['DateTime'])
            market_obj.m_fPriceList.append(market_data['Price'])
            market_obj.m_nSizeList.append(market_data['Size'])
        market_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[0])
        market_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[1])
        CCommonFunctions.total_daily_market_volume = sum(market_obj.m_nSizeList)
        return True

    '''
    This function splits the TwapPortfolio objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        portfolio_obj:       This is given as an input so that this function can populate this object.
        portfolio_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataTwapPortfolio(self, portfolio_obj, portfolio_data_list):
        common_functions_obj = CCommonFunctions()
        portfolio_obj.m_strScripName = portfolio_data_list[0]['ScripName']
        temp_date = portfolio_data_list[0]['DateTime'].date()
        temp_date = str(temp_date.day) + '-' + str(temp_date.month) + '-' + str(temp_date.year)
        print "temp date :" + str(temp_date)
        for portfolio_data in portfolio_data_list:
            portfolio_obj.m_nCountOfRows += 1
            portfolio_obj.m_DatetimeList.append(portfolio_data['DateTime'])
            portfolio_obj.m_strOrderIDList.append(portfolio_data['OrderID'])
            portfolio_obj.m_strStatusList.append(portfolio_data['Status'])
            portfolio_obj.m_nOrderQtyList.append(portfolio_data['OrderQty'])
            portfolio_obj.m_fOrderPriceList.append(portfolio_data['OrderPrice'])
            portfolio_obj.m_strSideList.append(portfolio_data['Side'])
            portfolio_obj.m_nFilledSizeList.append(portfolio_data['FilledSize'])
            portfolio_obj.m_fAvgPriceList.append(portfolio_data['AvgPrice'])
            portfolio_obj.m_fPriceList.append(portfolio_data['Price'])
            portfolio_obj.m_nSizeList.append(portfolio_data['Size'])
            
            if portfolio_data['Status'].upper() == 'COMPLETE':
                portfolio_obj.m_OrderCompleteDatetimeList.append(portfolio_data['DateTime'])
                portfolio_obj.m_fOrderCompleteAvgPriceList.append(portfolio_data['AvgPrice'])
            
            if not (portfolio_data['Price'].upper() == 'NULL' or portfolio_data['Price'].upper() == 'NONE'):
                portfolio_obj.m_OrderExecutionDatetimeList.append(portfolio_data['DateTime'])
                portfolio_obj.m_fOrderExecutionFillPriceList.append(portfolio_data['Price'])
        
        portfolio_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[0])
        portfolio_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[1])
        print "displaying portfolio timw window list"
        for iter in range(0, len(portfolio_obj.m_strTimeWindowList)):
            print str(portfolio_obj.m_strTimeWindowList[iter])  +"\t" + str(portfolio_obj.m_strTimeWindowPlotList[iter])
        print "end of display"

        return True

    '''
    This function splits the PredictedTrade objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        predicted_obj:       This is given as an input so that this function can populate this object.
        predicted_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataPredicted(self, predicted_obj, predicted_data_list): 
        common_functions_obj = CCommonFunctions()
        temp_date = predicted_data_list[0]['DateTime'].date()
        temp_date = str(temp_date.day) + '-' + str(temp_date.month) + '-' + str(temp_date.year)
        
        for predicted_data in predicted_data_list:
            predicted_obj.m_nCountOfRows += 1
            predicted_obj.m_DatetimeList.append(predicted_data['DateTime'])
            predicted_obj.m_nSizeList.append(predicted_data['Size'])
        predicted_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[0])
        predicted_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[1])
        return True

    '''
    This function splits the CashTrade objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        cash_obj:       This is given as an input so that this function can populate this object.
        cash_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataCash(self, cash_obj, cash_data_list):
        common_functions_obj = CCommonFunctions()
        temp_date = cash_data_list[0]['DateTime'].date()
        temp_date = str(temp_date.day) + '-' + str(temp_date.month) + '-' + str(temp_date.year)
        cash_obj.m_strScripName = cash_data_list[0]['ScripName']

        for cash_data in cash_data_list:
            cash_obj.m_nCountOfRows += 1
            cash_obj.m_DatetimeList.append(cash_data['DateTime'])
            cash_obj.m_fPriceList.append(cash_data['Price'])
        cash_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[0])
        cash_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[1])
        return True
    
    '''
    This function splits the FutureTrade objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        future_obj:       This is given as an input so that this function can populate this object.
        future_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataFuture(self, future_obj, future_data_list):
        common_functions_obj = CCommonFunctions()
        temp_date = future_data_list[0]['DateTime'].date()
        temp_date = str(temp_date.day) + '-' + str(temp_date.month) + '-' + str(temp_date.year)
        future_obj.m_strScripName = future_data_list[0]['ScripName']
        
        for future_data in future_data_list:
            future_obj.m_nCountOfRows += 1
            future_obj.m_DatetimeList.append(future_data['DateTime'])
            future_obj.m_fPriceList.append(future_data['Price'])
        future_obj.m_strTimeWindowList     = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[0])
        future_obj.m_strTimeWindowPlotList = common_functions_obj.GetDateTimeList(temp_date, common_functions_obj.GetWindowList(self.m_nWindowSize)[1])
        return True

    '''
    This function splits the StrategyLogTrade objects into the individual lists.
    Rest of the statements in the function are self-explanatory.
    Input Variables:
        strategylog_obj:       This is given as an input so that this function can populate this object.
        strategylog_data_list: This is an input which is used by this function to parse the row objects.
    '''
    def FormatDataStrategyLog(self, strategylog_obj, strategylog_data_list):
        print "displaying strategylog list :"
        for strategylog_data in strategylog_data_list:
            strategylog_obj.m_nCountOfRows += 1
            strategylog_obj.m_DatetimeList.append(strategylog_data['DateTime'])
            strategylog_obj.m_fPriceList.append(strategylog_data['Price'])
            strategylog_obj.m_strStrategyList.append(strategylog_data['Strategy'])
        print "displaying strategy list"
        print strategylog_obj.m_strStrategyList
    	return True
