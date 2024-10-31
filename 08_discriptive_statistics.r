library(dplyr)
score <- read.csv("score.csv", header = TRUE)
head(score, 3)
dim(score)
score$total <- score$midterm + score$final
head(score, 3)
sapply(score[, -c(1:2)], mean, na.rm = TRUE)
sapply(score[, -c(1:2)], sd, na.rm = TRUE)
summary(score[, -1])
class(score$gender)
class(score$midterm)
fivenum(score$total)
install.packages("psych")
# describe
library(psych)
describe(score[, -c(1:2)])
desc_score <- describe(score[, -c(1:2)])
names(desc_score)
desc_score$mean
desc_score$min
psych::describe(desc_score[, -c(1:2)])
# 그룹별 기술통계 tapply 243page
head(score, 3)
tapply(score$total, score$gender, mean)
tapply(score$total, score$gender, sd)
tapply(score$total, score$gender, length)
xbar <- tapply(score$total, score$gender, mean)
s <- tapply(score$total, score$gender, sd)
n <- tapply(score$total, score$gender, length)
cbind(mean = xbar, stdev = s, n = n)
# aggretate함수
aggregate(
  (score[c("midterm", "final", "total")]), list(gender = score$gender),
  mean
)
aggregate(
  (score[c("midterm", "final", "total")]), list(gender = score$gender),
  sd
)
aggregate(
  (score[c("midterm", "final", "total")]), list(gender = score$gender),
  length
)
# by함수 가장 많이 사용
by(score[, 3:5], score$gender, summary)
# 245p psych
library(psych)
describeBy(score[, c(3:5)], score$gender)
# 250page 줄기-잎 그림
stem(score$total)
stem(score$total, scale = 2)
# 줄기잎 그래프 - 그불비교
install.packages("aplpack")
library(aplpack)
male_score <- score$total[score$gender == "m"]
female_score <- score$total[score$gender == "f"]
stem.leaf.backback(male_score, female_score)
median(male_score)
median(female_score)
# 2 변수에 대한  상자그림
par(mfrow = c(1, 2))
boxplot(total ~ gender, data = score)
title("boxplot: total ~ gender")
boxplot(female_score, male_score)
title("boxplot: variables")
# 두 변수에 대한 히스토르갬
par(mfrow = c(2, 1))
hist(male_score, col = "pink")
hist(female_score, col = "grey")
# 빈도표 부할표 258page
enqete <- read.csv("enqete.csv", header = T)
head(enqete, 3)
dim(enqete)
table(enqete$grade)
grade_freq <- table(enqete$grade)
names(grade_freq) <- c("gr1", "gr2", "gr3", "gr4")
grade_freq
par(mfrow = c(1, 2))
barplot(grade_freq)
pie(grade_freq)
# 분할표 261페이지
table(enqete$grade, enqete$q1)
enqete[enqete == 0] <- NA
enqete <- na.omit(enqete)
table(enqete$grade, enqete$q1)
college <- table(enqete$grade, enqete$q1)
colnames(college) <- c("ans1", "ans2")
rownames(college) <- c("grade1", "grade2", "grade3", "grade4")
college
# xtabs 262page
xtabs(~ grade + q1, data = enqete)
par(mfrow = c(1, 2))
barplot(college, legend = c("grade1", "grade2", "grade3", "grade4"))
barplot(t(college), legend = c("ans1", "ans2"))
# 두 표본 독립성 검정
chisq.test(college)
