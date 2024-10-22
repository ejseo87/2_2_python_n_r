xv <- c(1, 10, 20, 50, 100)
is.vector(xv)
xv[2]
xv[c(1,3)]
x <- c(1, 2, 'a', TRUE)
x
is.numeric(x[1])
xx <- c(1, 2, TRUE)
xx
length(xv)
xm <- matrix(1:9, nrow=3, byrow=T, 
             dimnames=list(c('r1', 'r2', 'r3'), c('col1', 'col2', 'col3')))
xm

# xm <- matrix(1:9, nrow=3, byrow=T)
# colnames(xm) <- c('col1', 'col2', 'col3')))
# rownames(xm) <- c('r1', 'r2', 'r3')
# xm

xm[1,2]
xm[1,]
xm[1, 2:3]
length(xm)
dim(xm)
xv[2] <- -5; xm[1,2] <- 10
xv
xm
