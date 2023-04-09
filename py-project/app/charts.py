import matplotlib.pyplot as plt

#country = input('Type the country => ')

def generate_bar_chart(name, labels, values):  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  ax.ticklabel_format(useOffset=False, style='plain', axis='y')
  plt.title(f'Population of {name} (1970 - 2022)')
  plt.savefig(f'./images/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.title('World Population Percentage in Latin America')
  plt.savefig('pie_chart.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 60, 40]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)