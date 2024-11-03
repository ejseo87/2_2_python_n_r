getwd()
health <- read.csv("health.csv", header = TRUE)
head(health, 3)
# 산점도
plot(health$weight, health$time, pch = 19)
pairs(health[, -1], pch = 19)
# 상관계수
cor(health[, -1])
x <- health[, c(2:5)]
head(x, 3)
cor(x, health$time)
cor.test(health$weight, health$time)
cor.test(health$pulse, health$time)
cor.test(health$muscle, health$time)
cor.test(health$quarter, health$time)
# 회귀분석
health <- health[, -1]
fit <- lm(time ~ ., data = health)
names(fit)
fit$resid
fit$coef
summary(fit)
# 분산분석표
anova(fit)
# 회구모형 적합 판정을 위한 산점도
temp <- cbind(fitted(fit), residuals(fit))
head(temp)
plot(temp[, 1], temp[, 2], pch = 19)
confint(fit, level = 0.95)
