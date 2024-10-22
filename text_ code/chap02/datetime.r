Sys.Date()
Sys.time()


format(Sys.Date(), "%Y년 %m월 %d일")
format(Sys.time(), "%Y년 %m월 %d일 %A %H시 %M분 %S 초")

dobstr1 <- c("1999-10-01", "2000-01-31", "2001-02-13")
as.Date(dobstr1)
format(as.Date(dobstr1), "%Y")

dobstr2 <- c("10/01/1999", "01/31/2000", "02/13/2001")
as.Date(dobstr2, "%m/%d/%Y")

year <- c(1999, 2000, 2001)
month <- c(10, 01, 02)
day <- c(01, 31, 13)
dobstr3 <- paste(year, "-", month, "-", day, sep="")
as.Date(dobstr3)
