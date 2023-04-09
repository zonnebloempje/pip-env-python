import utils
import read_csv
import charts
import pandas as pd

#### World Population Percentage

def run():
  df = pd.read_csv('data.csv') # df = data frame
  df = df[df['Continent'] == 'Europe']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
#### Population By Country 1970-2022
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()

