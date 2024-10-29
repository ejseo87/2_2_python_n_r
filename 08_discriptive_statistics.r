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
