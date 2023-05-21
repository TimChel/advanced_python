import pandas as pd
import numpy as np

import matplotlib.pyplot as plt # some imports to set up plotting
import seaborn as sns # pip install seaborn

import warnings
warnings.filterwarnings('ignore')

# Для каждой задачи получить ответ на вопрос через pandas и визуализировать его любым подходящим способом (у всех
# графиков должна быть легенда, подписаны оси):
# 1. доля всех задержек ко всем вылетам
# 2. найти зависимость количества задержек от длины пути, который предстоит пролететь самолету
# 3. топ 5 направлений, для которых чаще всего происходят задержки
# 4. в какие времена года чаще всего происходят задержки рейсов
# 5. найти топ 10 самых хороших перевозчиков, которые реже всего задерживают свои рейсы
# 6. найти топ 10 самых безответственных аэропортов, в которых чаще всего происходят задержки
# 7. найти необычную зависимость количества задержек от имеющихся данных
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%"

path_to_file = 'flight_delays.csv'
data = pd.read_csv(path_to_file, sep=',')

size1 = data[data['dep_delayed_15min'] == 'N'].size
size2 = data[data['dep_delayed_15min'] == 'Y'].size
plt.pie([size1, size2], autopct=lambda pct: func(pct, [size1, size2]), textprops=dict(color="w"))
plt.legend(['Не было задержки', 'Была задержка'], bbox_to_anchor=(0.75, 0, 0.5, 1))
plt.title('Доля всех задержек ко всем вылетам')

plt.show()

sns.distplot(data[data['dep_delayed_15min'] == 'Y']['Distance'])
plt.legend(['Приближение'])
plt.title('зависимость количества задержек от длины пути, который предстоит пролететь самолету')
plt.xlabel('Длина пути')
plt.grid()

plt.show()

# print(data[data['dep_delayed_15min'] == 'Y']['Dest'].count())
data_2 = data[data['dep_delayed_15min'] == 'Y'].groupby('Dest').count()
# print(data_2)
data_3 = data_2.sort_values(by=['dep_delayed_15min'], ascending=False)
# print(data_3)
plt.pie(data_3['dep_delayed_15min'])
plt.legend(data_3.head(5).index.tolist())
plt.title('топ 5 направлений, для которых чаще всего происходят задержки')
print('Топ 5 направлений, для которых чаще всего происходят задержки:\n', data_3['dep_delayed_15min'].head(5))
plt.show()

data_2 = data[data['dep_delayed_15min'] == 'Y'].groupby('Month').count()
data_2_1 = pd.DataFrame({'Kol': pd.Series([data_2['dep_delayed_15min']['c-12']+data_2['dep_delayed_15min']['c-1']
                      +data_2['dep_delayed_15min']['c-2'], data_2['dep_delayed_15min']['c-3']
                      +data_2['dep_delayed_15min']['c-4']+data_2['dep_delayed_15min']['c-5'], data_2['dep_delayed_15min']['c-6']
                      +data_2['dep_delayed_15min']['c-7']+data_2['dep_delayed_15min']['c-8'], data_2['dep_delayed_15min']['c-9']
                      +data_2['dep_delayed_15min']['c-10']+data_2['dep_delayed_15min']['c-11']], index =['Зима', 'Весна', 'Лето', 'Осень'])})
# print(data_2_1)
data_3 = data_2_1.sort_values(by = ['Kol'])
# print(data_3)
plt.pie(data_3['Kol'], autopct=lambda pct: func(pct, data_3['Kol']), textprops=dict(color="w"))
plt.legend(data_3.head().index.tolist())
plt.title('в какие времена года чаще всего происходят задержки рейсов')
print('Чаще всего задержки рейсов происходят в эту пору года:\n', data_3.head().index.tolist()[-1])
plt.show()

# print(data[data['dep_delayed_15min'] == 'Y']['Dest'].count())
data_2 = data[data['dep_delayed_15min'] == 'N'].groupby('UniqueCarrier').count()
# print(data_2)
data_3 = data_2.sort_values(by=['dep_delayed_15min'], ascending=False)
# print(data_3)
plt.pie(data_3['dep_delayed_15min'], autopct=lambda pct: func(pct, data_3['dep_delayed_15min']), textprops=dict(color="w"))
plt.legend(data_3.head(10).index.tolist())
plt.title('Круговая диаграмм компаний и незадержанных полетов')
print('Топ 10 самых хороших перевозчиков, которые реже всего задерживают свои рейсы:\n', data_3['dep_delayed_15min'].head(10))
plt.show()

# print(data[data['dep_delayed_15min'] == 'Y']['Dest'].count())
data_2 = data[data['dep_delayed_15min'] == 'Y'].groupby('Origin').count()
# print(data_2)
data_3 = data_2.sort_values(by=['dep_delayed_15min'], ascending=False)
# print(data_3)
plt.pie(data_3['dep_delayed_15min'], autopct=lambda pct: func(pct, data_3['dep_delayed_15min']), textprops=dict(color="w"))
plt.legend(data_3.head(10).index.tolist())
plt.title('Аэропорты и их косяки')
print('Топ 10 самых безответственных аэропортов, в которых чаще всего происходят задержки:\n', data_3['dep_delayed_15min'].head(10))
plt.show()


sns.distplot(data[data['dep_delayed_15min'] == 'Y']['DepTime'])
plt.legend(['Приближение'])
plt.title('зависимость количества задержек от времени отправления')
plt.xlabel('Время отправления')
plt.grid()
plt.show()