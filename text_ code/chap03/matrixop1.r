mx1 <- matrix(1:6, ncol=3, byrow = T)
mx2 <- cbind(rep(1,3), rep(2,3))
mx1 %*% mx2
# mx1 * mx2 # 요건 에러
dim(mx1)

