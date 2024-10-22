myiris <- read.table("K:\\HWP\\books\\PR4DS\\iris.txt", header=T)
myiris <- read.table("K:/HWP/books/PR4DS/iris.txt", header=T)
myiris <- read.table(file.choose(), header=T)
myiris <- read.table(url("http://jupiter.hallym.ac.kr/ftpdata/data/iris.txt"), 
           skip=9, 
           col.names=c("No", "SepalLength"," SepalWidth","PetalLength","PetalWidth","Species"))
head(myiris)
tail(myiris)

##############

write.table(mtcars, "")
write.table(mtcars, "", row.names=F, quote=F)
write.table(mtcars, "K:/hwp/books/PR4DS/mtars.csv", row.names=T, quote=F, sep=",",
         fileEncoding="UTF-8")

write.table(mtcars, file.choose(), quote=F, sep=",")

