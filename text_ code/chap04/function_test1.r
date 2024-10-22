# function_test1.r
my_sums <- function(a=0, b=10) {
  data <- a:b
  sum1 <- 0; sum2 <- 0
  for (i in data) { 
    sum1 = sum1 + i
    sum2 = sum2 + i^2
  } # end for-loop
  # sum1 <- sum(a:b); sum2 <- sum((a:b)^2)
  list(sum1=sum1, sum2 = sum2, n=length(data))
} # end of function


a <- my_sums(1,10)
mm <- a$sum1 /a$n
vv <- (a$sum2 -a$n* mm^2)/(a$n-1)
