# 사용자로부터 입력받기
birthday <- function() {
  age <- readline(prompt = "Enter age: ")
  curyear <- as.numeric(format(Sys.Date(), "%Y"))
  b.year <- curyear - as.numeric(age)
  list(born.year = b.year)
}
birthday()
# 텍스트파일 읽기
# Fisher의 붓꽃 데이터 150records (3 types)
myiris <- read.table("./data/iris.txt", header = TRUE)
colnames(myiris) <- c(
  "SepalLength", "SepalWidth", "PetalLength",
  "PetalWidth", "species"
)
head(myiris, 3)
tail(myiris, 3)
# 텍스트파일쓰기
head(mtcars, 3)
write.table(mtcars, "")
write.table(mtcars, "./output/mtcars.csv",
  row.names = TRUE, quote = FALSE, sep = ",", fileEncoding = "UTF-8"
)
# setting a workiing directory
cur_dir <- getwd()
print(cur_dir)
working_dir <- paste0(cur_dir, "/data")
print(working_dir)
setwd(working_dir)
# 문자열 합치기(paste), 분리하기(strsplit)
str <- "abc"
print(nchar(str))
splited_str <- strsplit(str, split = "")
print(splited_str)
print(strsplit("abcabab", "b"))
print(paste(str, "ABC", sep = ""))
print(rep(str, 5))
