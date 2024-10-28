
import scipy.stats as stats
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 한글설
from matplotlib import rc
rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

# 1
plt.ioff()
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
plt.plot(x, sinus)
plt.show()
# 2
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "-b", x, sinus, "ob",
         x, cosinus, "-r", x, cosinus, "or")
plt.xlabel("x축이다!")
plt.ylabel("y축이다!")
plt.title("내 그래프")
plt.show()
# 3
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, label="sinum", color="blue",
         linestyle="--", linewidth=2)
plt.plot(x, cosinus, label="cosinus", color="red",
         linestyle="-", linewidth=2)
plt.legend()
plt.title("내 그래프")
plt.show()

# 4
plt.ioff()
# url = "https://github.com/neurospin/pystatsml/blob/master/"\
#    + "datasets/salary_table.csv"
url = "data/salary_table.txt"
# print("***url = ", url)
salary = pd.read_csv(url)
# print("***salary = \n", salary)
df = salary
colors = colors_edu = {"Bachelor": "r", "Master": "g", "Ph.D": "blue"}
plt.scatter(df["experience"], df["salary"],
            c=df["education"].apply(lambda x: colors[x]), s=100)
plt.xlabel("experience")
plt.ylabel("salary")
plt.legend(colors, loc='lower right', ncol=3, fontsize=8)
plt.show()
# 5
symbols_manag = dict(Y="*", N=".")
for values, d in salary.groupby(["education", "management"]):
    edu, manager = values
    plt.scatter(d["experience"], d["salary"], marker=symbols_manag[manager],
                color=colors_edu[edu], s=150, label=manager + "/" + edu)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend(loc='lower right')
plt.show()
# read_csv(url) 에서 데이터에 문제있을 때 사용해볼 수 있는 방법 중 하나
file_path = "data/salary_table.txt"
f = open(file_path, 'rt')
reader = csv.reader(f)
csv_list = []
for line in reader:
    csv_list.append(line)
f.close()
df = pd.DataFrame(csv_list)
# 6 subplots
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax1.hist(np.random.randn(100), bins=20, color="k", alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
ax3.plot(np.random.randn(50).cumsum(), "k--")
plt.show()

# 교재 189페이지부터
plt.ioff()
x = np.random.randn(100)
y = np.random.randn(100)
plt.plot(y, "b:")
plt.title("Blue Dotted Line")
#

plt.figure()
plt.plot(y, "g-")
plt.title("Green Solid Lie")
# plt.show()

# plt.ion()
plt.figure()
h = plt.plot(y, "g-")
plt.getp(h)
plt.setp(h, "color", "red")


plt.figure()
plt.plot(y, alpha=0.5, ls="-.", marker="o",
         mec="red", mew=2, mfc="blue", ms=10)
plt.show()
# 다양한 선그르기
plt.ioff()
z = np.arange(40)/20
plt.figure()
plt.plot(z, z, "g-", z, z*z, "r:", z, z*z*z, "b--")
plt.show()
# 다양한 선그르기 2n 그리고 R 스타일로 그리기
# R ggplot 스타일 지정
plt.style.available
plt.style.use("ggplot")
x = np.linspace(0, 2, 100)
plt.figure()
plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")
plt.xlim(-0.25, 2.25)
plt.yticks([0, 1, 2, 4, 8])
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()
plt.grid(True)
plt.text(1.6, 7, r'$y=x^3$')
plt.text(1.9, 4.5, r'$y=x^2$')
plt.text(1.9, 1.4, r'$y=x$')
plt.title("Simple Polynomials")
plt.show()
# 캔버스와 부분그림의 활성화
plt.ioff()
plt.figure()
plt.subplot(211)
plt.plot([1, 2, 3])
plt.subplot(212)
plt.plot([4, 5, 6])
plt.figure(2)
plt.plot([4, 5, 6])
plt.figure(1)
plt.subplot(211)
plt.title("Test 1, 2, 3")
plt.show()
# subplot
plt.ioff()
x = np.linspace(0, 1, 200)
y = np.sqrt(x)
fig = plt.figure()
ax = fig.add_subplot(211)
plt.title("sqrt(x)")
ax.plot(x, y)
ax = fig.add_subplot(212)
ax.plot(x, y)
plt.show()
# subplot 2
plt.ioff()
fig, ax = plt.subplots()
ax.plot(x, y)
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, y)
ax2.plot(x, -y)
plt.show()
# subplot 3
plt.ioff()
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, -y)
axs[1, 0].plot(x, y)
axs[1, 1].plot(x, -y)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x, y)
ax2.plot(x, -y)
ax3.plot(x, y)
ax4.plot(x, -y)
plt.show()
# 부분그림에서 공동 축의 사용
plt.ioff()
plt.style.use("ggplot")
z = np.linspace(-1, 1, 100)
w = np.sqrt(1-z**2)
# print("***\n", z[::-1][1:100])
xo = np.concatenate([z, z[::-1][1:100]])
# print("***xo=\n", xo)
yo = np.concatenate([w, -1*w[::-1][1:100]])
fig, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                        gridspec_kw={"hspace": 0, "wspace": 0})
(ax1, ax2), (ax3, ax4) = axs
fig.suptitle("Sharing x per column, y per row")
ax1.plot(xo-1, yo, "blue")
ax2.plot(xo-1, yo-1, "orange")
ax3.plot(xo+1, yo+1, "green")
ax4.plot(xo+1, yo, "red")
plt.show()
# 표준정규분포 히스토그램과 밀도함수
plt.ioff()
plt.style.use("ggplot")
xh = np.random.randn(4000)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(xh, bins=30, color="skyblue", rwidth=0.9, label="Empirical")
xlim = ax.get_xlim()
ylim = ax.get_ylim()
print("xlim=", xlim)
print("ylim=", ylim)
xs = np.linspace(xlim[0], xlim[1], 200)
dx = stats.norm.pdf(xs)
dx = dx*(ylim[1]/dx.max())
plt.plot(xs, dx, "r-", label="PDF", color="orange")
ax.set_ylim((ylim[0], 1.2*ylim[1]))
plt.legend()
plt.text(1, 320, r'normal density : $\phi(x)$')
plt.title("Histogram and Density")
plt.show()
# Axes 객체 속성 변경하기
plt.ioff()
x = np.random.randn(1000)
fig = plt.figure()
plt.style.use("default")
ax1 = fig.add_subplot(121)
ax1.hist(x)
ax2 = fig.add_subplot(122)
ax2.hist(x)
ax2.set_facecolor("#E6E6E6")
ax2.set_axisbelow(True)
ax2.grid(color="w", linestyle="solid")
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.tick_params(colors="gray", direction="out")
for tick in ax2.get_xticklabels():
    tick.set_color("gray")
for tick in ax2.get_yticklabels():
    tick.set_color("gray")
ax2.hist(x, edgecolor="#E6E6E6", color="#EE6666")
plt.show()
# plt.rcParams 변경방법
plt.ioff()
plt.style.use("default")
fig = plt.figure()
plt.rc("axes", facecolor="gray")
ax = fig.add_subplot(121)
ax.hist(x)
plt.rcParams["axes.facecolor"] = "pink"
ax = fig.add_subplot(122)
ax.hist(x)
plt.show()
# 좌우 그림에서 각기 다른 스타일을 적용
plt.ioff()
r = np.arange(0, (2*np.pi), 0.01)
fig = plt.figure()
plt.style.use("default")
ax = fig.add_subplot(121)
ax.plot(r, 1+np.cos(4*r), "red")
plt.style.use("ggplot")
ax = fig.add_subplot(122, polar=True)
ax.plot(r, 1+np.cos(4*r), "green")
plt.show()
# colormap : 팔레트 선정 효과
plt.ioff()
x = np.linspace(0, 10, 1000)
i = np.sin(x) * np.cos(x[:, np.newaxis])


def notick():
    plt.xticks([])
    plt.yticks([])


cm1 = plt.get_cmap("Blues")
cm2 = plt.get_cmap("Blues", 5)
cm3 = plt.get_cmap("hsv", 7)
fig = plt.figure(figsize=(19, 6))
fig.add_subplot(131).imshow(i, cmap=cm1)
notick()
fig.add_subplot(132).imshow(i, cmap=cm2)
notick()
fig.add_subplot(133).imshow(i, cmap=cm3)
notick()
plt.show()
