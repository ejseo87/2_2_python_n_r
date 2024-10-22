# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:06:13 2019

@author: Sim
"""
# fileio0.py
import pandas as pd

df1 = pd.read_csv('e:/hwp/books/PR4DS/source/score.txt', sep=" ", header=0, encoding='utf-8')
df2 = pd.read_csv('e:/hwp/books/PR4DS/source/score.csv', header=0, encoding='cp949')
df3 = pd.read_csv('e:/hwp/books/PR4DS/source/score.csv', header=0, encoding='euc-kr')
print(df1.head(3))
print(df2.head(3))
print(df3.tail(3))
print(type(df1))
# 다음은 인코딩 오류에 의한 에러
# df1 = pd.read_csv('d:/hwp/books/PR4DS/source/score.txt', header=0, encoding='cp949')
# df3 = pd.read_csv('d:/hwp/books/PR4DS/source/score.csv', header=0, encoding='utf-8')

# 첫 번째 행을 읽지 않아 보기
df4 = pd.read_csv('e:/hwp/books/PR4DS/source/score.csv', skiprows=1, encoding='euc-kr')
# 아래 결과에서 첫 번째 자료값이 열이름이 됨.
print(df4)

# 열의 일부만 읽기
df5 = pd.read_csv('e:/hwp/books/PR4DS/source/score.csv', header=0, encoding='euc-kr',
                 usecols=['english', 'name', 'korean', 'math'])
print(df5.head(3))
# 열의 순서 바꾸기
df6 = pd.read_csv('e:/hwp/books/PR4DS/source/score.csv', header=0, encoding='euc-kr',
                  usecols=['english', 'name', 'korean', 'math'])[['english', 'korean',
                               'math', 'name']]
print(df6.head(3))

df7 = pd.read_csv('e:/hwp/books/PR4DS/source/score.txt', sep=" ", index_col='name')
print(df7)
print(df7.loc['강대성'])
