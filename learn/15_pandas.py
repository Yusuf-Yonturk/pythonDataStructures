# Pandas Series, verileri etkili bir şekilde manipüle etmenize ve analiz etmenize yardımcı olmak için 
# çeşitli özellikler ve yöntemler sunar. İşte bazı temel olanlar:

# values: Series verilerini NumPy dizisi olarak döndürür.
# index: Series’in indeksini (etiketlerini) döndürür.
# shape: Series’in boyutlarını temsil eden bir demet döndürür.
# size: Series’deki eleman sayısını döndürür.
# mean(), sum(), min(), max(): Verilerin özet istatistiklerini hesaplar.
# unique(), nunique(): Benzersiz değerleri veya benzersiz değerlerin sayısını alır.
# sort_values(), sort_index(): Series’i değerler veya indeks etiketlerine göre sıralar.
# isnull(), notnull(): Eksik (NaN) veya eksik olmayan değerleri kontrol eder.
# apply(): Series’in her bir elemanına özel bir fonksiyon uygular.

import pandas as pd
csv_path='./src/philo.csv'
df=pd.read_csv(csv_path)
df.head()
print(df.head())
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label


# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)

print(df['Name'])  # Access the 'Name' column
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

unique_dates = df['Age'].unique()
print(unique_dates)

high_above = df[df['Age'] > 29]
print(high_above)

df.to_csv('trading_data.csv', index=False)

# DataFrame Özellikleri ve Yöntemleri
# DataFrame’ler, veri manipülasyonu ve analizi için birçok özellik ve yöntem sunar, bunlar arasında:

# shape: DataFrame’in boyutlarını (satır ve sütun sayısı) döndürür.
# info(): DataFrame hakkında veri türleri ve null olmayan sayılar dahil olmak üzere bir özet sağlar.
# describe(): Sayısal sütunlar için özet istatistikler oluşturur.
# head(), tail(): DataFrame’in ilk veya son n satırını gösterir.
# mean(), sum(), min(), max(): Sütunlar için özet istatistikler hesaplar.
# sort_values(): DataFrame’i bir veya daha fazla sütuna göre sıralar.
# groupby(): Toplama için belirli sütunlara dayalı olarak verileri gruplar.
# fillna(), drop(), rename(): Eksik değerleri işler, sütunları kaldırır veya sütunları yeniden adlandırır.
# apply(): DataFrame’in her bir elemanına, satırına veya sütununa bir fonksiyon uygular.
#write your code here

dicData = {
    "Student": ["Ava", "Liam", "Noah", "Mia"],
    "Age": [19, 26, 23, 21],
    "Country": ["UK", "Germany", "Japan", "Brazil"],
    "Course": ["Quantum Computing", "Data Ethics", "Cybersecurity", "Game Design"],
    "Marks": [92, 78, 85, 88]
}
df1 = pd.DataFrame(dicData)

print(df1.iloc[0, 0])
print(df1.iloc[0, 2])
print(df1['Student'])
print(df1.loc[0, 'Marks'])

df2 = df1.set_index("Student")
print(df2.head())

print(df2.loc['Mia', 'Country'])
print(df2.loc['Liam', 'Course'])
print(df1.iloc[3, 2])

print(df1.iloc[0:2, 0:3])
print(df1.loc[0:2, 'Student':'Country'])
print(df2.loc['Liam':'Mia', 'Age':'Marks'])