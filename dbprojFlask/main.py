
from flask import Flask, request, redirect, url_for
import sqlite3
from flask import g
from datasets import DataLoader
from create import create_tables
from insert import insert_Co2_emission, insert_education, insert_gdp, insert_population_growth, insert_population_total
from queries import getAllEducationData, getLiteracyVsGdp, literacyVsGrowth, literacyVsEmissions
from flask import render_template

DATABASE = 'data.db'
dataLoader = DataLoader()
app = Flask(__name__)


@app.route("/")
def hello_world():
    initDB()
    return "<p>Hello, World!</p>"


# @app.route("/literacy_vs_gdp/view", methods=['GET'])
# def lit_v_gdp_vew_get():
#     return render_template('gdpliteracy.html')

# routes for the views

@app.route("/literacy_vs_gdp/view", methods=['POST', 'GET'])
def lit_v_gdp_vew_post():
    if request.method == 'GET':
        return render_template('form.html', act='lit_v_gdp_vew_post', title='GDP')
    n = request.form['n']
    return redirect(url_for('lit_v_gdp', n=n))


@app.route("/literacy_vs_emissions/view", methods=['POST', 'GET'])
def lit_v_gdp_emissions_post():
    if request.method == 'GET':
        return render_template('form.html', act='lit_v_gdp_emissions_post', title='Emissions')
    n = request.form['n']
    return redirect(url_for('lit_v_emissions', n=n))


@app.route("/literacy_vs_population_growth/view", methods=['POST', 'GET'])
def lit_v_gdp_growth_post():
    if request.method == 'GET':
        return render_template('form.html', act='lit_v_gdp_growth_post', title='Population Growth')
    n = request.form['n']
    return redirect(url_for('lit_v_growth', n=n))


# routes for charts
@app.route("/literacy_vs_gdp/<n>")
def lit_v_gdp(n=None):
    db = get_db().cursor()
    return getLiteracyVsGdp(db, n)


@app.route("/emissions/<n>")
def lit_v_emissions(n=None):
    db = get_db().cursor()
    return literacyVsEmissions(db, n)


@app.route("/population_growth/<n>")
def lit_v_growth(n=None):
    db = get_db().cursor()
    return literacyVsGrowth(db, n)


@app.route("/test")
def getTestData():
    db = get_db().cursor()
    return render_template('test.html', data=getAllEducationData(db))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def initDB():
    db = get_db()
    create_tables(db)
    insert_population_total(db, dataLoader.population_total)
    insert_population_growth(db, dataLoader.population_growth)
    insert_Co2_emission(db, dataLoader.co2)
    insert_education(db, dataLoader.education)
    insert_gdp(db, dataLoader.gdp)

    db.commit()
