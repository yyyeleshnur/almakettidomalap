import pandas as pd
import os


current_directory = os.getcwd()
file_name = 'issues.csv'
file_path = os.path.join(current_directory, file_name)
data = pd.read_csv(file_path)

# Просмотр первых строк данных
print(data.head())

# Проверка типов данных и наличие пропущенных значений
print(data.info())

# Исследование данных по темам (topic)
topic_counts = data['topic'].value_counts()
print("Распределение стихийных бедствий и проблем по темам:")
print(topic_counts)

# Анализ данных по странам (country)
country_counts = data['country'].value_counts()
print("Страны с наибольшим количеством стихийных бедствий и проблем:")
print(country_counts)

# Изучение тенденций по годам (year)
trends_by_year = data.groupby('year')['index_trends'].value_counts()
print("Тенденции стихийных бедствий и проблем по годам:")
print(trends_by_year)

# Визуализация данных (для примера)
import matplotlib.pyplot as plt

# График распределения стихийных бедствий по темам
plt.figure(figsize=(8, 6))
topic_counts.plot(kind='bar')
plt.title('Распределение стихийных бедствий по темам')
plt.xlabel('Тема')
plt.ylabel('Количество')
plt.show()



