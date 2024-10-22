# install.packages('readxl')
library(readxl)
# 전체 읽기
read_excel(path="k:/hwp/books/PR4DS/bmi.xlsx", sheet=1, 
      col_names=c("height", "weight", "year", "religion", "gender", "marriage"))
# A1:C10 영역만 읽기
read_excel(path="k:/hwp/books/PR4DS/bmi.xlsx", sheet=1, 
          range=("A1:C10"), col_names=c("height", "weight", "year"))
# 몸무게와 성별만 읽기
read_excel(path="k:/hwp/books/PR4DS/bmi.xlsx", sheet=1, 
      col_names=c("height", "weight", "year", "religion", "gender", "marriage"),
      col_types=c("skip", "numeric", "skip", "skip", "text", "skip"))

####################
# install.packages("xlsx")
library(xlsx)
read.xlsx(file="k:/hwp/books/PR4DS/bmi.xlsx", sheetIndex=1)
 
name <- c("강대성", "한준호", "김종욱", "박상호", "김소현")
number <- c(87, 73, 53, 65, 69)
df <- data.frame(name, number)
 
write.xlsx(df, "k:/hwp/books/PR4DS/scorebyR.xlsx", 
    sheetName="data", row.names=FALSE)


