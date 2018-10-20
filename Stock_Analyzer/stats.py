
import numpy as np
import pandas_datareader.data as web
from datetime import datetime

class stock:
    def __init__(self,ticker,start,end,rf='BIL',benchmark='SPY'):
        """
        Creates a stock object
        
        Parameters:
            ticker (string): the ticker symbol for the stock to be initiated
            start (datetime.datetime): the earliest date to begin pulling data
            end (datetime.datetime): the last date from which data is to be pulled
            benchmark (string optional): the ticker symbol for the index to be used for the benchmark. Defaults to spy (S&P 500)
        
        Attributes:
            ticker (string): the original ticker that the data refers to
            returns (ndarray): the daily return of the stock over the specified period
            r_bar (float): the arithmetic mean of returns over the specified period
            dev (float): the standard deviation of returns
            n (int): the number of observations in returns
            bench_mark_returns (ndarray): the daily return of the benchmark index
            bench_bar (float): the average arithmetic mean of benchmark returns
            cov (float): the covariance between the stock and the benchmark
            correlation (float): the correlation between the benchmark and the stock
            skew (float): the Skew of the stock returns (sample not population)
                    large positive indicates large outliers on the upside 
                    while large negative indicates large outliers to the downside
            kurtosis (float): the kurtosis of the stock returns (sample, not population)
                    always positive, normal distribution has kurtosis 3, 
                    greater than 3 indicates high peak and fat tails, 
                    less than 3 indicates gradual peak and thin tails
            rf_returns: The historical return of the risk free rate
            rf_bar: The average historical risk free rate
            beta (float):Systematic risk in relation to the benchmark
        """
        self.ticker=ticker.upper()
        for i in range(4):
            try:
                stock = web.DataReader(self.ticker, 'iex', start, end)
                break
            except ConnectionError:
                stock=None
            except KeyError:
                raise ValueError('Ticker is invalid')
        if stock is None:
            raise ConnectionError('Could not retrieve data')
        self.prices=np.array(list(stock['close']))
        returns=np.zeros(len(self.prices)-1)
        for i in range(len(self.prices)-1):#get stock returns
            returns[i]=(self.prices[i+1]-self.prices[i])/self.prices[i]
        self.returns=returns*100
        self.r_bar=np.mean(returns)
        self.dev=returns.std()
        self.n=self.returns.size
        bench=web.DataReader(benchmark, 'iex', start, end)
        benchmark=np.array(list(bench['close']))
        bench_mark_returns=np.zeros(len(bench)-1)
        for i in range(len(benchmark)-1):#get bench mark returns
            bench_mark_returns[i]=(benchmark[i+1]-benchmark[i])/benchmark[i]
        bench_mark_returns=bench_mark_returns*100
        self.bench_bar=bench_mark_returns.mean()
        self.bench_mark_returns= bench_mark_returns
        cov=0
        for i in range(len(self.bench_mark_returns)):#covariance between stock and bench mark
            cov+=(self.returns[i]-self.r_bar)*(self.bench_mark_returns[i]-self.bench_bar)
        cov/=(self.n-1)
        correlation=cov/(self.dev*self.bench_mark_returns.std())
        self.cov=cov
        self.correlation=correlation
        toske=0
        tokur=0
        for i in self.returns:#finds the skew and kurtosis of the stock
            toske+=(i-self.r_bar)**3
            tokur+=(i-self.r_bar)**4
        self.skew=toske*(self.n/((self.dev**3)*(self.n-2)*(self.n-1)))
        self.kurtosis=tokur*((self.n*(self.n+1))/((self.dev**4)*(self.n-1)*(self.n-2)*(self.n-3)))
        rf=web.DataReader(rf, 'iex', start, end)
        rf=np.array(list(rf['close']))
        rf_returns=np.zeros(len(bench)-1)
        for i in range(len(rf)-1):#get bench mark returns
            rf_returns[i]=(rf[i+1]-rf[i])/rf[i]
        rf_returns=rf_returns*100+0.01/31#add 0.01/31 for the coupon payment
        self.rf_bar=rf_returns.mean()
        self.rf_returns= rf_returns
        self.beta=np.sum(((self.returns-self.rf_returns)-(self.r_bar-self.rf_bar))*((self.bench_mark_returns-self.rf_returns)
                        -(self.bench_bar-self.rf_bar)))/np.sum(((self.bench_mark_returns-self.rf_returns)-(self.bench_bar-self.rf_bar))**2)
    
        
    def up_cap(self):
        """
        calculates the up capture ratio
        inputs:
            None: uses closing prices given in initialization of the object
        returns:
            up_capture ratio, also stores the ratio as an attribute
        The up capture indicator is designed to measure the extent 
        to which the portfolio manager “captures” benchmark returns in positive markets.
        Higher Values are Preferable
        """
        mask=self.bench_mark_returns>0
        return self.returns[mask].mean()/self.bench_mark_returns[mask].mean()
        
    def down_cap(self):
        """
        Calculates the down capture ratio
        Parameters:
            None:
        Returns: 
            down_cap: the Down Capture ratio, also stores the ratio as an attribute
        The down capture indicator is analogous to the up capture 
        indicator and measures the extent to which the manager “captures” benchmark returns in negative markets.
        Lower values are preferred.
        """
        mask=self.bench_mark_returns<0
        return self.returns[mask].mean()/self.bench_mark_returns[mask].mean()
        
    def hurst(self):
        """
        Calculates the Hurst ratio, a measure of persistence
        
        Parameters:
            None only uses historical data stored as an attribute:
            
        Returns:
            hurst (float [0,1]): The Hurst Ratio
            
        The Hurst Ratio is a measure of persistence ranging form 0 to 1 with 1 being totally persistent 
        and 0 being totally mean reverting and .5 being totally random.
        In other words, a value between 0 and .5 indicates that historically a stock tends to revert to its mean
        when experiencing a down or up trend while a value between .5 and 1 indicates that a stock has historically tended
        to keep going in the direction it is headed once a trend is established
        """
        cum_dev=np.zeros(len(self.returns)+1)
        for i in range(1,1+len(self.returns)):
            cum_dev[i]=cum_dev[i-1]+self.returns[i-1]-self.r_bar
        R_S=(np.max(cum_dev)-np.min(cum_dev))/self.dev
        hurst=np.log(R_S)/np.log(self.n)
        return hurst
        
    def bias_ratio(self, bound=None):
        """
        Calculates the Bias Ratio
        
        Parameters: 
            bound (float): defines the definition of 'Close to zero' defaults to the standard deviation
        Returns: 
            Bias Ratio (float): ratio of small positive to small negative as defined by bound
        
        The Bias ratio finds the ratio of positive returns that are close to zero divided by 
        the number of returns that are negative and close to zero.
        it can be used as an additional indicator of volatility since having constant positive returns is certainly desirable
        """
        if bound is None:
            bound=self.dev
        mask=abs(self.returns)>bound
        upmask=self.returns[mask]>0
        downmask=self.returns[mask]<0
        return len(self.returns[mask][upmask])/(1+len(self.returns[mask][downmask]))
        
    def sharpe(self, risk_free=None):
        """
        Calculates the ADJUSTED Sharpe ratio (as opposes to standard or revised)
        
        Parameters: 
            risk_free (float): the risk free rate (calculated for the same period as the stock, default is daily),
            normally a short term bond such as the 30-day treasury bill
        """
        if risk_free is None:
            risk_free = self.rf_bar
        sharpe=(self.r_bar-risk_free)/self.dev
        return sharpe*(1+self.skew/6*sharpe-((self.kurtosis-3)/24)*sharpe**2)
        
    def tracking_error(self):
        """
        Calculates the geometric tracking error, or deviation of excess returns over the specified period
        
        Parameters:
            None:
        
        Returns:
            t_error: the tracking error of the geometric excess returns
            
        The tracking error is nothing more than the standard deviation of the excess returns over the bench mark
        """
        geo_excess=(1+self.returns)/(1+self.bench_mark_returns)-1
        return np.sqrt(np.sum((geo_excess-np.mean(geo_excess))**2)/self.n)
        
    def information_ratio(self):
        """
        Calculates the information ratio using geometric excess return
        
        Parameters: None
        
        Returns: i_ratio: the Information ratio 
        
        The Information Ratio 
        
        """
        return (np.mean(self.geo_excess)/self.t_error)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        