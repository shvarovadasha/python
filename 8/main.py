import zipfile
import pandas as pd
import os
import matplotlib.pyplot as plt

zip_path = "Cancer Deaths by Country and Type Dataset.zip"
csv_filename = "Cancer Deaths by Country and Type Dataset.csv"

if not os.path.exists(csv_filename):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print("Архив распакован.")
else:
    print("CSV-файл уже существует.")
df = pd.read_csv(csv_filename)
df.columns = df.columns.str.strip()

print("\nСтолбцы в таблице:")
print(df.columns.tolist())

countries = df['Country'].unique()
cancer_types = df.columns[3:]

print("\nДоступные страны:")
for i, country in enumerate(countries):
    print(f"{i+1}. {country}")
country_index = int(input("Введите номер страны: ")) - 1
selected_country = countries[country_index]

print("\nДоступные виды рака:")
for i, cancer in enumerate(cancer_types):
    print(f"{i+1}. {cancer}")
cancer_index = int(input("Введите номер типа рака: ")) - 1
selected_cancer = cancer_types[cancer_index]

filtered_df = df[['Country', 'Year', selected_cancer]]
filtered_df = filtered_df[filtered_df['Country'] == selected_country]
filtered_df = filtered_df.groupby('Year')[selected_cancer].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Year'], filtered_df[selected_cancer], marker='o')
plt.title(f"Смертность от {selected_cancer} в {selected_country} по годам")
plt.xlabel("Год")
plt.ylabel("Количество смертей")
plt.grid(True)
plt.tight_layout()
plt.show()
