import pandas as pd
import numpy as np


class DataLoader:

    def __init__(self):
        self.gdp = self.getGDP()
        self.co2 = self.getCo2()
        self.population_growth = self.getPopulationGrowth()
        self.population_total = self.getPopulationTotal()
        self.education = self.getEducationData()

    def getEducationData(self):
        Data = pd.read_csv("./data/final_enriched_world.csv", na_values=['..'])
        Data.drop(Data.tail(5).index, inplace=True)
        cols = [x[:-125] for x in Data.columns]
        cols[0] = 'Time'
        Data.columns = cols
        for c in Data.columns[2:]:
            Data[c].fillna(np.mean(Data[c]), inplace=True)
        Data = Data.dropna(axis=1, how='all')
        return Data

    def getCo2(self):
        c02 = pd.read_csv("./data/co2_emission.csv")
        c02['Entity'] = c02['Entity'].str.replace(r"[\"\',]", '')
        return c02

    def getGDP(self):
        gdp = pd.read_csv('./data/gdp.csv')
        gdp = gdp.drop(['Country Code', 'Indicator Name',
                        'Indicator Code', "Unnamed: 65"], axis=1)
        gdp = gdp.melt(id_vars=["Country Name"],
                       var_name="Date",
                       value_name="Value")
        gdp['Country Name'] = gdp['Country Name'].str.replace(r"[\"\',]", '')
        gdp['Value'] = gdp['Value'].fillna(np.mean(gdp['Value']))

        return gdp

    def getPopulationGrowth(self):
        population_growth = pd.read_csv("./data/population_growth.csv")
        population_growth = population_growth.drop(
            ['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)

        population_growth = population_growth.melt(id_vars=["Country Name"],
                                                   var_name="Date",
                                                   value_name="Value")
        population_growth['Value'] = population_growth['Value'].fillna(
            np.mean(population_growth['Value']))
        population_growth['Country Name'] = population_growth['Country Name'].str.replace(
            r"[\"\',]", '')

        return population_growth

    def getPopulationTotal(self):
        population_total = pd.read_csv("./data/population_total.csv")
        population_total['Count'] = population_total['Count'].fillna(
            np.mean(population_total['Count']))
        population_total['Country Name'] = population_total['Country Name'].str.replace(
            r"[\"\',]", '')
        return population_total
