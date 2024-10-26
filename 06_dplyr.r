working_dir <- getwd()
print(working_dir)
if (!is.null(working_dir)) setwd(working_dir)
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
# install.packages("reshape")
# library(reshape)
insurance <- read.table("insurance.txt", header = TRUE)
head(insurance, n = 3)
insurance$job <- factor(insurance$job,
  levels = c(1:3),
  labels = c("근로자", "사무직", "전문가")
)
head(insurance, n = 3)
insurance$edu2 <- ordered(insurance$edu,
  levels = c(1:5),
  labels = c("무학", "국졸", "중졸", "고졸", "대졸")
)
head(insurance, n = 3)
job_freq <- table(insurance$job)
barplot(job_freq)
title("막대그림 : job")
# R자체 기능으로 recode 하기
install.packages("openxlsx")
library(openxlsx)
drug <- read.xlsx("drug.xlsx")
head(drug)
drug$age_group <- drug$age
drug$age_group[drug$age >= 20 & drug$age <= 40] <- 1
drug$age_group[drug$age > 40 & drug$age <= 60] <- 2
drug$age_group[drug$age > 60] <- 3
drug[c(1, 20, 40, 95), ]
# car 패키지의 reciode() 활용  -> 패키지 설치 실패
# install.packages("car")
# library(car)
# drug$age_group2 <- drug$age
# drug$age_group2 <- recode(drug$age, "lo:40 = 1; 40:60 = 2; 60:hi = 3")
# dplyr 패키지
insurance <- read.table("insurance.txt", header = TRUE)
library(dplyr)
dim(insurance)
# tbl_df(insurance) -> 아래의 tibble 로 대체됨
tibble(insurance)
install.packages("nycflights13")
library(nycflights13)
dim(flights)
tibble(flights)
# dplyr 패키지 - 데이터 추출 filtering
man_3 <- filter(insurance, sex == "m", edu == 3)
man_3
man_or_3 <- filter(insurance, sex == "m" | edu == 3)
man_or_3
selected_cols <- select(insurance, sex, job, amount, salary)
head(selected_cols)
selected_cols_m_3 <- filter(insurance, sex == "m", edu == 3)
head(selected_cols_m_3)
selected_cols_m_or_3 <- filter(insurance, sex == "m" | edu == 3)
head(selected_cols_m_or_3)
insurance_added <- mutate(insurance, amopersal = amount / salary)
head(insurance_added)
# cbind : R 기본 함수
amopersal_col <- insurance$amount / insurance$salary
insurance_added2 <- cbind(insurance, amopersal_col)
head(insurance_added2)
# dplyr sorting
selected_cols_arrage <- arrange(selected_cols, sex, job)
head(selected_cols_arrage)
selected_cols_arrage_descending <- arrange(selected_cols, desc(sex), desc(job))
head(selected_cols_arrage_descending)
# dplyr 요약결과
ins_job <- arrange(insurance, job)
ins_job_g <- group_by(ins_job, job)
ins_job_gm <- summarise(ins_job_g, amMean = mean(amount), aSal = mean(salary))
ins_job_gm
ins_job_g
# dplyr chain 기능 %>% "then"\
b1 <- select(insurance, amount, salary)
b2 <- filter(b1, salary > 130)
b2
nb2 <- insurance %>%
  select(amount, salary) %>%
  filter(salary > 130)
nb2
head(mtcars)
mtcars %>%
  filter(am == 0) %>%
  group_by(carb) %>%
  summarise(mean(mpg))
mtcars %>%
  filter(gear != 5) %>%
  group_by(gear) %>%
  summarise(
    Abg_mpg = mean(mpg),
    Median_hp = as.numeric(median(hp)),
    Count = n()
  ) %>%
  arrange(desc(Count))
# 교재 183 페이지 부터
# 일자별로 출발이 가장 빠른 비행편과 가장 늦은 비행편
library(nycflights13)
ls("package:nycflights13")
flights %>% dim()
not_cancelled <- flights %>% filter(!is.na(dep_delay), !is.na(arr_delay))
not_cancelled %>% dim()
not_cancelled %>%
  head(3) %>%
  .[, 1:6]
not_cancelled %>%
  group_by(year, month, day) %>%
  mutate(r = min_rank(desc(dep_time))) %>%
  filter(r %in% range(r)) %>%
  .[, 1:6]
# 취항 항공사수가 많은 순서부터 도착지 공항 정렬하기
not_cancelled %>%
  group_by(dest) %>%
  summarise(carriers = n_distinct(carrier)) %>%
  arrange(desc(carriers))
## https://rpubs.com/justmarkham/dplyr-tutorial
# library(hflights)<- 패키자가 없다는 에러 발생
