from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
from pandas import DataFrame,Series
import datetime as dt
import bokeh
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.annotations import Title
from bokeh.io import output_file, show
import os


def fetch_quandl(ticker) :
	ticker=ticker.upper()

	now=dt.datetime.now().date()
	then=now-dt.timedelta(days=30)
	then = "&start_date=" + then.strftime("%Y-%m-%d")
	now  = "&end_date=" + now.strftime("%Y-%m-%d")

	reqUrl='https://www.quandl.com/api/v3/datasets/WIKI/' + ticker + \
					'.json?api_key=' + 'ozDdzwk5k595x9k9VgNS' + '&end_date=2018-02-01' + '&start_date=2016-02-01'

	r=requests.get(reqUrl)
	name=r.json()['dataset']['name']
	name=name.split('(')[0]

	dat= r.json()['dataset']
	df = DataFrame(dat['data'], columns=dat['column_names'])
	df = df.set_index(pd.DatetimeIndex(df['Date']))

	return(df, name) 

def make_figure(df, tickerText):

	p=figure(x_axis_type="datetime", width=400, height=300)
	p.line(df.index, df['Close'],line_width=5)
	t = Title()
	t.text = tickerText

	p.grid.grid_line_alpha=0.3
	p.xaxis.axis_label = 'Date'
	p.yaxis.axis_label = 'Price'
	p.title = t
	bokeh.io.output_file('templates/plot.html')
	bokeh.io.save(p)
	script, div=components(p)
	return(script, div)

app = Flask(__name__)
app.vars = {}
keyFile = 'API_KEYS'
keyName = 'quandl'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/plotpage', methods=['POST'])
def plotpage():
	tickStr=request.form['tickerText']
	app.vars['ticker']=tickStr.upper()
	df,name=fetch_quandl(app.vars['ticker'])
	script,div=make_figure(df, app.vars['ticker'])
	return render_template('plot.html', script=script, div=div, ticker=name)

 	#return render_template('plot.html', script=script, div=div, ticker=name)
if __name__ == '__main__':
 	app.run(port=33507)
