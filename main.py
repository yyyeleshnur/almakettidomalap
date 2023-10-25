# %%
# import psycopg2
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
sns.set(color_codes=True)


# %%
# conn = psycopg2.connect(
#     dbname="Analiz",
#     user="postgres",
#     password="123",
#     host="localhost"
# )


# %%
# query = "SELECT * FROM mtcars;"
# df = pd.read_sql_query(query, conn)

df = pd.read_csv('C:/Users/hello/Downloads/Analiz-master/Analiz-master/mtcars.csv', sep=',')

# 1. Вычисляем средние значения для числовых столбцов:
df = df.drop(['model'], axis=1)  
stolb = df.mean() 
print(stolb)



""" Визуализация данных:
mpg      20.090625
cyl       6.187500
disp    230.721875
hp      146.687500
drat      3.596563
wt        3.217250
qsec     17.848750
vs        0.437500
am        0.406250
gear      3.687500
carb      2.812500
dtype: float64 """

# 2.Гистограмма распределения миль на галлон:


plt.figure(figsize=(8, 6))
sns.histplot(df['mpg'], bins=10, kde=True)
plt.title("Распределение км в литр")
plt.xlabel("Мили Процент Литр (mpg)")
plt.show()



"""Фильтрация данных: Приложил к файлу Фильтрация.png

3. Найти машины с высоким расходом топлива (mpg) и высокой мощностью (hp)"""

zhor = df[(df['mpg'] > 20) & (df['hp'] > 100)]
print("Машины с высоким mpg и мощностью:")
print(zhor)


"""Выходные данные:

Машины с высоким mpg и мощностью:
       model          mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
0   Mazda RX4           21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1   Mazda RX4 Wag   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
3   Hornet 4 Drive      21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
27 Lotus Europa        30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
31 Volvo 142E            21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2
"""
