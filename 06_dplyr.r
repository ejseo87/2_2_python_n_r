getwd()
load("wd.RData")
nwd <- wd
nwd[nwd$x2 < 0.11, "x2"] <- 99
nwd[nwd == 99] <- NA
nwd[nwd > 0.9] <- 99
nwd[nwd == 99] <- NA
head(nwd, n = 5)
rowSums(is.na(nwd))
colSums(is.na(nwd))
mywd <- na.omit(nwd)
head(mywd)
rowSums(is.na(mywd))
colSums(is.na(mywd))
names(nwd)
names(nwd)[6] <- "ny"
colnames(nwd) <- c("a1", "a2", "a3", "a4", "a5", "newy")
names(nwd)
install.packages("reshape")
library(reshape)
