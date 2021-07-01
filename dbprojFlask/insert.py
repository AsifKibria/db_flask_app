def insert_population_total(cursor, population_total):
    for i in range(population_total.shape[0]):
        q = """ 
          INSERT INTO
          population_total(Country,Datum,Count)
          VALUES('{}',{},{})
        """.format(population_total['Country Name'][i],
                   int(population_total['Year'][i]),
                   population_total['Count'][i])

        cursor.execute(q)


def insert_Co2_emission(cursor, c02):
    for i in range(c02.shape[0]):

        q = """ 
          INSERT INTO
          Co2_emission(Country,Datum,Emission,Code)
          VALUES('{}',{},{},'{}')
        """.format(c02['Entity'][i],
                   int(c02['Year'][i]),
                   c02['Annual CO₂ emissions (tonnes )'][i],
                   c02['Code'][i])

        cursor.execute(q)


def insert_gdp(cursor, gdp):
    for i in range(gdp.shape[0]):
        q = """ 
          INSERT INTO
          gdp(Country,Datum,Value)
          VALUES('{}',{},{})
        """.format(gdp['Country Name'][i],
                   int(gdp['Date'][i]),
                   gdp['Value'][i])

        cursor.execute(q)


def insert_population_growth(cursor, population_growth):
    for i in range(population_growth.shape[0]):
        q = """ 
          INSERT INTO
          population_growth(Country,Datum,Value)
          VALUES('{}',{},{})
        """.format(population_growth['Country Name'][i],
                   int(population_growth['Date'][i]),
                   population_growth['Value'][i])

        cursor.execute(q)


def insert_education(cursor, Data):
    for col in Data.columns[2:]:
        start = col.find('[')+1
        end = col.find(']')
        code = col[start:end]
        country = col[0:start-2]
        for i in range(Data.shape[0]):
            literacy = Data[col][i]
            if literacy == '..':
                literacy = 0
            else:
                literacy = float(literacy)
            q = """ 
            INSERT INTO
            Education(Country,Datum,Value,CountryCode)
            VALUES('{}',{},{},'{}')
          """.format(country,
                     int(Data['Time'][i]),
                     literacy, code)

            cursor.execute(q)
