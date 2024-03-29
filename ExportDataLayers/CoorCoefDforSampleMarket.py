import requests
import json
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
import itertools
import itertools
from urllib import parse
import functools
from itertools import groupby
from operator import itemgetter
from pprint import pprint
from datetime import datetime
from datetime import date, timedelta 
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
startTime = datetime.now()
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine, MetaData, Table, text
import time
from selenium import webdriver


#For creating temp tables, and TABLES for further processing in PostrgeSQL DB, please insert necessary credentials into the vaiable "engine" and remove the hashtag #.
#engine = create_engine('postgresql+psycopg2://USERNAME:PASSWORD@HOSTNAME:PORTNUMBER/DBNAME')



with engine.connect() as con:
    with open("durationBins.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("tempTabsForCorrCoef.sql") as file:
        query = text(file.read())
        con.execute(query)

    
        

        tab1_2 = pd.DataFrame(psql.read_sql("SELECT * from corr_coefs   ", con))
        tab1_2.to_excel('graphData//tab1_2.xlsx')
        print(tab1_2.info())

        
        


        

        





