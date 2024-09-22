2 + 3 / 2
2^10
2**10
a <- 10
a
print(a)
cat("\n a=", a, "\n")

a <- c(1, 10)
print(a)
a <- (1:10)
print(a)
print(a / 3)
print(a %/% 3) # 몱
print(a %% 3) # 나머지

#자료형
a <- 100
mode(a)
mode(FALSE)
is.numeric(10.5)
is.integer(10.5)
#자료의 값을 다른 형태로
as.integer("1")
as.numeric("1")
#문자열합치기
paste("a", as.character(10.1), "cc", sep = "+")
#패키지
library("ggplot2")
data(mtcars)
head(mtcars)
tail(mtcars)
#?mtcars
qplot(wt, mpg, data = mtcars)
dev.new()
plot(mtcars$wt, mtcars$mpg, pch = 19, col = "RED")
# 결측치
heigt <- c(45, 75, 60, 51, NA)
print(mean(height))
print(mean(height, na.rm = TRUE))
#무한대
x <- c(1, -1, 0, Inf, -Inf)
print(x / 0)
# 날짜 시간
print(Sys.Date())
print(Sys.time())
print(format(Sys.Date(), "%Y년%m월%d일"))

dob <- c("1999-10-01")
as.Date(dob)
format(as.Date(dob),"%Y/%m/%d/%a")
