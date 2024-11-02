from scipy.stats import chi2_contingency
import seaborn as sns
import stemgraphic
import researchpy as rp
from scipy.stats import skew
from scipy.stats import kurtosis
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# setting a workiing directory
import os
print(os.getcwd())
os.chdir(os.getcwd()+"/data")
print(os.getcwd())
#
score = pd.read_csv("score.csv")
print(score.head())
print("score.shape = ", score.shape)
# 기술통계
score["total"] = score["midterm"] + score["final"]
print("score.head(3) =\n", score.head(3))
print("score['total'].mean() = ", score['total'].mean())
print("score['total'].std() = ", score['total'].std())
print("score['total'].median() = ", score['total'].median())
print("score['total'].quantile(0.75) = ", score['total'].quantile(0.75))
print("score['total'].quantile(0.25) = ", score['total'].quantile(0.25))
# 기술통계2
# import collections
print("collections.Counter(score['gender']) = ",
      collections.Counter(score['gender']))

cols = ["midterm", "final", "total"]
score2 = score[cols]
print("score2.head(3) =\n", score2.head(3))
# score3 = score[:, 2:]  ->2:5, 2:-1 모두 에러
# print("score3.head(3) =\n", score3.head(3))
print("score2.describe() =\n", score2.describe())
aaa = score2.describe()
print("aaa = \n", aaa)
print("type(aaa) = \n", type(aaa))
print("aaa.loc['count'] = \n", aaa.loc["count"])
# from scipy.stats import skew
# 왜도
print("skew(score2) =\n", skew(score2))
# from scipy.stats import kurtosis
# 첨도
print("kurtosis(score2) =\n", kurtosis(score2))
# 심화
a = [0, 3, 4, 1, 2, 3, 0, 2, 1, 3, 2, 0, 2, 2, 3, 2, 5, 2, 3, 999]
a = np.array(a)
print("skew(a) =\n", skew(a))
print("kurtosis(a) =\n", kurtosis(a))
# 247 그룹별 기술통계
gstat = score.groupby("gender")['total'].describe()
print("gstat = \n", gstat)
print("gstat['mean'] = ", gstat['mean'])
print("gstat['std'] = ", gstat['std'])
print("gstat['75%'] = ", gstat['75%'])
# aggregate
gstat_total = score.groupby("gender")['total']
# print("gstat_total.agg() =\n", gstat_total.agg())
print("gstat_total.agg(['size','mean','std','min','max']) =\n",
      gstat_total.agg(['size', 'mean', 'std', 'min', 'max']))
gresult = gstat_total.agg(['size', 'mean', 'std', 'min', 'max'])
print("gresult.loc['f'] = \n", gresult.loc["f"])
print("gresult.loc['m'] = \n", gresult.loc["m"])
# pip install researchpy
# import researchpy as rp
print("rp.summary_cont(score['total']) =\n", rp.summary_cont(score['total']))
print("rp.summary_cont(score.groupby('gender')['total']) =\n", rp.summary_cont(
    score.groupby('gender')['total']))
# 줄기-잎 그림
# pip install stemgraphic
# import stemgraphic
stemgraphic.stem_graphic(score.total, scale=10)
plt.show()
# 상자그림
# import seaborn as sns
sns.set_theme(style="whitegrid")
sns.boxplot(x="total", data=score)
plt.show()
sns.boxplot(y="total", data=score)
plt.show()
sns.boxplot(x="gender", y="total", data=score)
plt.show()
sns.boxenplot(x="gender", y="total", data=score)
plt.show()
# histogram
plt.hist(score.total)
plt.show()
# groupby histogram
ftotal = score.loc[score.gender == 'f', 'total']
mtotal = score.loc[score.gender == 'm', 'total']
args = dict(alpha=0.5, bins=10)
plt.hist(ftotal, **args, color='b', label='female')
plt.hist(mtotal, **args, color='r', label='male')
plt.gca().set(title='Frequency Histogram of Score.total', ylabel='Frequency')
plt.legend()
plt.show()
# 빈도표
enqete = pd.read_csv('enqete.csv')
print("enqete.head(3)=\n", enqete.head(3))
# enqete_table = pd.crosstab(
#    index=enqete.grade, columns="count")
# print("enqete_table=\n", enqete_table)
# enqete_table.index = ['1학년', '2학년', '3학년', '4학년']
# print("enqete_table=\n", enqete_table)
# q1에 대한 분할표
grade_q1 = pd.crosstab(index=enqete["grade"],   columns=enqete["q1"])
grade_q1.index = ['1학년', '2학년', '3학년', '4학년']
print("grade_q1=\n", grade_q1)
enqete["q1"] = enqete["q1"].replace(0, np.NaN)
grade_q1 = pd.crosstab(index=enqete['grade'], columns=enqete['q1'])
grade_q1.index = ['1학년', '2학년', '3학년', '4학년']
print("grade_q1=\n", grade_q1)
# 분할표 카이검정
# from scipy.stats import chi2_contingency
print("chi2_contingency(grade_q1) = \n", chi2_contingency(grade_q1))
