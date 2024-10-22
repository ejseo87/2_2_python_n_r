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

# 자료형
a <- 100
mode(a)
mode(FALSE)
is.numeric(10.5)
is.integer(10.5)
# 자료의 값을 다른 형태로
as.integer("1")
as.numeric("1")
# 문자열합치기
paste("a", as.character(10.1), "cc", sep = "+")
# 패키지
library("ggplot2")
data(mtcars)
head(mtcars)
tail(mtcars)
# ?mtcars
qplot(wt, mpg, data = mtcars)
dev.new()
plot(mtcars$wt, mtcars$mpg, pch = 19, col = "RED")
# 결측치
heigt <- c(45, 75, 60, 51, NA)
print(mean(height))
print(mean(height, na.rm = TRUE))
# 무한대
x <- c(1, -1, 0, Inf, -Inf)
print(x / 0)
# 날짜 시간
print(Sys.Date())
print(Sys.time())
print(format(Sys.Date(), "%Y년%m월%d일"))

dob <- c("1999-10-01")
as.Date(dob)
format(as.Date(dob), "%Y/%m/%d/%a")
# matrix
xm <- matrix(1:9,
  nrow = 3, byrow = TRUE,
  dimnames = list(
    c("r1", "r2", "r3"),
    c("col1", "col2", "col3")
  )
)
xm
xm <- matrix(1:9,
  nrow = 3, byrow = TRUE
)
xm
colnames(xm) <- c("col1", "col2", "col3")
rownames(xm) <- c("r1", "r2", "r3")
xm
# indexing
xm[1, ]
xm[, 1]
xm[, 2:3]
xm[, c(1, 3)]
# dataframe
x <- seq(1, 10, by = 2)
y <- letters[1:length(x)]
df <- data.frame(id = x, name = y)
df
df[1, ]
df[, 2]
df$id
df$name
