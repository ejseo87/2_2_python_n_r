xm <- matrix(1:8, nrow=2, byrow=T)
xm
y1 <- c(9:12)
xm2 <- rbind(xm, y1)
xm2
rbind(y1, xm)

y2 <- c(10, 20, 30)
xm3 <- cbind(y2, xm2)
xm3

rbind(xm3[1,], 13:17, xm3[2:3,])

xm2[-2,]
xm2[, -c(1,3)]

