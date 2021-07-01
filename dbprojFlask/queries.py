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
