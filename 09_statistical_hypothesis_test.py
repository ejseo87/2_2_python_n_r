from scipy import stats
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# setting a workiing directory
import os
print(os.getcwd())
os.chdir(os.getcwd()+"/data")
print(os.getcwd())
#
f = open("crab.txt")
crab = f.read()
f.close()
print("crab =\n", crab)
print("type(crab) = ", type(crab))
crab = crab.split()
print("crab = crab.split() \n", crab)
print("type(crab) = ", type(crab))
fcrab = [float(x) for x in crab]
print("fcrab =\n", fcrab)
print("type(fcrab) = ", type(fcrab))
# from scipy import stats
crab_ttest = stats.ttest_1samp(fcrab, 24.3)
print("type(crab_ttest) = ", type(crab_ttest))
print("crab_ttest =\n", crab_ttest)
print("T-value = %.3f, p-value = %.3f" % crab_ttest)
print(f'T-value = {crab_ttest[0]}, p-value = {crab_ttest[1]}')
print("T-value = %.3f" % crab_ttest[0], "p-value = %.3f" % crab_ttest[1])
#
crab = pd.read_csv("crabpy.txt", header=None)
print("type(crab) = ", type(crab))
# print("crab = ", crab)
crab_ttest_tvalue,  crab_ttest_pvalue = stats.ttest_1samp(crab, 24.3)
print("type(crab_ttest_tvalue) = ", type(crab_ttest_tvalue))
print("type(crab_ttest_pvalue) = ", type(crab_ttest_pvalue))
np.set_printoptions(precision=3, suppress=True)
print(f"T-value = {crab_ttest_tvalue}, p-value = {crab_ttest_pvalue}")
# 279page 2 sample test
drug = pd.read_csv("drug.csv", header=0)
print("type(drug) = ", type(drug))
print("drug.columns = ", drug.columns)
drug_b = drug.loc[drug.drug == 'B'].time
drug_g = drug.loc[drug.drug == 'G'].time
print("drug_b = ", drug_b)
print("drug_g = ", drug_g)
drug_ttest = stats.ttest_ind(drug_b, drug_g, equal_var=False)
print("type(drug_ttest) = ", type(drug_ttest))
print("drug_ttest = ", drug_ttest)
# 분산 동일성 검종 후
drug_vartest1 = stats.bartlett(drug_b, drug_g)
print("type(drug_vartest1) = ", type(drug_vartest1))
print("drug_vartest1 = ", drug_vartest1)
drug_vartest2 = stats.levene(drug_b, drug_g)
print("type(drug_vartest2) = ", type(drug_vartest2))
print("drug_vartest2 = ", drug_vartest2)
drug_ttest2 = stats.ttest_ind(drug_b, drug_g, equal_var=True)
print("type(drug_ttest2) = ", type(drug_ttest2))
print("drug_ttest2 = ", drug_ttest2)
# 짝지어진 표본에서의 평균검정
deer = pd.read_csv("deer.csv")
print("type(deer) = ", type(deer))
print("deer.columns = ", deer.columns)
print("deer.head(3) =\n", deer.head(3))
deer_pttest = stats.ttest_rel(deer.hleg, deer.fleg)
print("type(deer_pttest) = ", type(deer_pttest))
print("deer_pttest = ", deer_pttest)
