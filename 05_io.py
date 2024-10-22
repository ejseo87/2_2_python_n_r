import os
from pandas import DataFrame
import pandas as pd
import datetime


def birthday():
    age = input("Enter age: ")
    now = datetime.datetime.now()
    curyear = now.year
    b_year = curyear - int(age)
    print("born.year = ", b_year)

# birthday()


# 텍스트파일 읽기
# Fisher의 붓꽃 데이터 150records (3 types)
df1 = pd.read_csv("./data/iris.txt", header=0, sep=" ", encoding='utf-8')
print(df1.head())
print(df1.head(3))
print(type(df1))
df2 = pd.read_csv("./data/score.csv", header=0, encoding='utf-8')
print(df2.head())
df3 = pd.read_csv("./data/score.csv", header=0, skiprows=10, encoding='utf-8')
print(df3.head())
df5 = pd.read_csv("./data/score.csv", header=0,
                  encoding="utf-8", usecols=['id', 'final'])
print(df5.head())
df7 = pd.read_csv("./data/score.csv", header=0,
                  encoding='utf-8', index_col='id')
print(df7.head())
print(df7.loc[13001])
print(df7.iloc[0, :])
# 텍스트파일쓰기
cars = {'make': ['Hyundai', 'Kia', 'Ford', 'Chevrolet'],
        'model': ['Sonata', 'K5', 'Taurus', 'Impala'],
        'price':  [3200, 3100, 3500, 3700]}
cars_df = DataFrame(cars)
print(cars_df.head())
write_txt = cars_df.to_csv(
    "./output/cars2.txt", sep=" ", index=True, header=True)
f = open("./output/cars2.csv", "w")
write_csv = cars_df.to_csv(f, sep=",", index=None, header=True)
f.close()
# setting a workiing directory
print(os.getcwd())
os.chdir(os.getcwd()+"/data")
print(os.getcwd())
# 문자열 분리하기
a = "abc"
print(len(a))
print(a[1])
x, y, z = a
print(x)
str = "a test string"
splited_str1 = str.split()
splited_str2 = str.split('i')
print(splited_str1, splited_str2)
str = str + "!"
print(str)
