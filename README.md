# Flask on Heroku

Visualizing stock prices over a fixed 2 year period (2016/1/1-2018/1/1), depending on stock ticker input.

Milestone project submission as part of the 12 day overview, prior to the start of The Data Incubator.

This project is intended to help tie together some important concepts and technologies from the 12-day course, including Git, Flask, JSON, Pandas, Requests, Heroku, and Bokeh for visualization.

# Index.html
For inputting the stock ticker

# App.py
Ticker value is fed into api string, and request sent to Quandl, to get data corresponding to fixed period. This dataframe containing stock closing prices over a month are then plotted through bokeh.



# plot.html
Plot of stock closing price is shown in this page



 


