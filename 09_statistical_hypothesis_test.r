getwd()
# 1 sample test
crab <- scan("crab.txt")
crab
t.test(crab, mu = 24.3)
# 277page 2 sample test
drug <- read.csv("drug.csv", header = TRUE)
drug[c(1, 7), ]
t.test(time ~ drug, data = drug)
# 분산 동일성 검정 후 2 sample test
var.test(time ~ drug, data = drug)
t.test(time ~ drug, var.equal = TRUE, data = drug)
# 짝지어진 표본에서의 평균검정
deer <- read.csv("deer.csv", header = TRUE)
head(deer, 3)
t.test(deer$hleg, deer$fleg, paired = TRUE)
