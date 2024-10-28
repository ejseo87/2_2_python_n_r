
import seaborn as sns
import matplotlib.pyplot as plt
# 한글설
from matplotlib import rc
rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

sns.set_theme(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")
print(df.head())

ax = plt.subplots()
# Show the results of a linear regression within each dataset
ax = sns.lmplot(
    data=df, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
plt.show()
# 217page seaborn패키지이용하여 iris 자료 특징 살펴보기
sns.set_theme(style="darkgrid")
iris = sns.load_dataset("iris")
print("***iris.__class__ = ", iris.__class__)
print("***iris.columns = ", iris.columns)
iris.columns = ["sl", "sw", "pl", "pw", "sp"]
print("iris.head() =\n", iris.head())

g = sns.FacetGrid(iris, col="sp")
g = g.map(plt.hist, "sl")

sns.catplot(x="sp", y="sl", kind="boxen", data=iris)

sns.jointplot(x="sw", y="sl", data=iris, kind="kde", space=0, color="g")

g = sns.PairGrid(iris, hue="sp")
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=3, legend=False)

sns.lmplot(x="sw", y="sl", data=iris)

sns.lmplot(x="sw", y="sl", hue="sp", data=iris)

plt.show()
