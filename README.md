# SQLAlchemy-Challenge
Unit 10 SQLAlchemy Challenge | Surfs Up Climate Analysis | UC Davis Spring 2021

For this challenge, I used ORM queries and a SQLite database to extract climate data from different weather stations in Honolulu Hawaii.
I first queried the data through SQLAlchmeny, Pandas, and Matplotlib to find insights on precipitation and temeperature. I then created a Flask API app to return JSON results when the user selects a specific date or date range to assess. 

Through my analysis, I concluded that the months with the most amount of precipitation occured in August 2016 and April 2017. Based on my t-test results I found that there is typically a significant difference of 3.9 degrees farenheit between warmer temperatures in June and slightly colder temperatures in December. 

**Resouces Folder**
- Contains all data used in each analysis, including my two CSV files and a SQLlite file.

**Analysis Folder**
- Climate_starter ipynb: 
  -  This file contains the initial climate analysis of the SQLite database. I queried the database using SQLAlchemy ORM queries, Pandas and Matplotlib to find data on precipitation and temperature at a variety of weather stations throughout Honolulu.

- Bonus_1_starter ipynb file:
  - This file contains an analysis on temperature data in Honolulu across all weather stations to compare multi-year temperature trends in June and December months. From my t-test results, I concluded that there is a significant different of almost 4 degrees farenheit between June and December.

- Bonus_2_starter ipynb file:
  - This file contains an analysis on daily raingfall averages and temperature highs, lows, and averages for a specific date range over all the years in the database. The daily rainfall and temperature normals are provided so the user has access to the most relevant data on their upcoming Hawaii trip.     

- app.py: 
  -  This file runs a Flask API app that returns JSON responses for different queries to assess preciptation and temperature values for different dates in the database. The user can also input their own start and/or end dates to find the minimum, maximum, and average temperature for a given range of dates.

**Images Folder**
- Honolulu Precipitation Bar Graph
- Honolulu Temp vs. Frequency Histogram
- Trip Average Temperatures Bar Chart
- Trip Daily Temperatures Area Plot
