import pandas as pd
import numpy as np
from IPython.display import HTML
import plotly.express as px


def getAllEducationData(cursor):
    cursor.execute('SELECT * FROM Education')
    return pd.DataFrame(cursor.fetchall(), columns=[
        'Country', 'Datum', 'Value', 'CountryCode'])


def getLiteracyVsGdp(cursor, nrows=10):
    cursor.execute("""
        SELECT *
        FROM (
            SELECT ed.Country, AVG(ed.Value) as literacy, AVG(g.Value) as gdp, ed.CountryCode as cc
            FROM Education ed 
            JOIN gdp g
            ON ed.Country = g.Country AND g.Datum = ed.Datum
            GROUP BY 1,4 ) as temp 
            ORDER BY temp.gdp DESC
            LIMIT {} 
                """.format(nrows))
    data = pd.DataFrame(cursor.fetchall(), columns=[
                        'Country', 'literacy', 'gdp', 'cc'])
    fig = px.scatter_geo(data, locations="cc", color="literacy",
                         hover_name="Country", size="gdp",
                         projection="natural earth")
    return HTML(fig.to_html()).data


def literacyVsGrowth(cursor, nrows=10):
    cursor.execute("""
            SELECT *
            FROM (
                SELECT ed.Country, AVG(ed.Value) as literacy, AVG(pg.Value) as average_growth, ed.CountryCode as cc
                FROM Education ed 
                JOIN population_growth pg
                ON ed.Country = pg.Country AND pg.Datum = ed.Datum
                GROUP BY 1,4 ) as temp 
                ORDER BY temp.average_growth DESC
                LIMIT {} 
            """.format(nrows))
    data_growth = pd.DataFrame(cursor.fetchall(), columns=[
        'Country', 'literacy', 'average_growth', 'cc'])
    fig = px.bar(data_growth, x='Country', y='average_growth',
                 hover_data=['average_growth', 'literacy'], color='literacy',
                 labels={'average_growth': 'Average growth of population through the years'}, height=400)
    return HTML(fig.to_html()).data


def literacyVsEmissions(cursor, nrows=10):
    cursor.execute("""
        SELECT *
        FROM (
            SELECT ed.Country, AVG(ed.Value) as literacy, AVG(co2.Emission) as average_emissions, ed.CountryCode as cc
            FROM Education ed 
            JOIN Co2_emission co2
            ON ed.Country = co2.Country AND co2.Datum = ed.Datum
            GROUP BY 1,4 ) as temp 
            ORDER BY temp.average_emissions DESC
            LIMIT {} 
        """.format(nrows))
    data_emissions = pd.DataFrame(cursor.fetchall(), columns=[
                                  'Country', 'literacy', 'average_emissions', 'cc'])
    fig = px.bar(data_emissions, x='literacy', y='average_emissions',
                 hover_data=['average_emissions', 'literacy'], color='Country',
                 labels={'average_emissions': 'Average emissions through the years'}, height=400)
    return HTML(fig.to_html()).data
