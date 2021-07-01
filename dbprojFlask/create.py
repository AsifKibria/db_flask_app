def create_tables(cursor):
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS population_total (
            Country Text,
            Datum Int,
            Count Int,
            PRIMARY KEY (Country, Datum)
      )""")

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Co2_emission (
            Country Text,
            Datum Int,
            Emission Real,
            Code Text,
            PRIMARY KEY (Country, Datum)

        )""")

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS gdp (
            Country Text,
            Datum Int,
            Value Real,
            PRIMARY KEY (Country, Datum)

        )""")

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS population_growth (
            Country Text,
            Datum Int,
            Value Real,
            PRIMARY KEY (Country, Datum)

        )""")

    cursor.execute("""
            CREATE TABLE  IF NOT EXISTS Education (
            Country Text,
            Datum Int,
            Value Real,
            CountryCode Text,
            PRIMARY KEY (Country, Datum)

        )""")
    cursor.commit()
