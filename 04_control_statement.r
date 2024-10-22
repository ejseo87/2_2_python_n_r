iftest <- function(x) {
  if (x %% 2 == 0) {
    cat("x는 짝수입니다\n")
  } else if (x %% 2 == 1) {
    cat("x는 홀수입니다\n")
  } else {
    cat("x는 자연수가 아닙니다\n")
  }
}
iftest(99)
iftest(100)
iftest(1.1)
even_odd_test <- function(x) {
  if (x %% 2 == 0) {
    cat(x, " is even number\n")
  } else if (x %% 2 == 1) {
    cat(x, " is oddd number\n")
  } else {
    cat(x, "is not integer\n")
  }
}
even_odd_test(4)
even_odd_test(5)
even_odd_test(1.1)
# for
sum <- 0
for (x in 1:10) {
  sum <- sum + x^2
}
sprintf("for] sum is %d", sum)
# while
x <- 1
sum <- 0
while (x <= 10) {
  sum <- sum + x^2
  x <- x + 1
}
sprintf("while] sum is %d", sum)
# next
x <- 1:5
for (j in x) {
  if (j == 3) next
  cat(j, " ")
}
# break
x <- 1:5
for (j in x) {
  if (j == 3) break
  cat(j, " ")
}
# function
my_sum <- function(a = 0, b = 10) {
  my_data <- a:b
  sum1 <- 0
  sum2 <- 0
  for (i in my_data) {
    sum1 <- sum1 + i
    sum2 <- sum2 + i^2
  }
  result <- list(sum1 = sum1, sum2 = sum2, n = length(my_data))
  return(result)
}
my_sum(1, 3)
a <- my_sum(1, 10)
print(a)
average <- a$sum1 / a$n
variation <- (a$sum2 - a$n * average^2) / (a$n - 1)
result <- sprintf("average is %f, variation is %f", average, variation)
print(result)
