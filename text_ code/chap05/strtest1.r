a <- "abc"
nchar(a)
xx <- strsplit(a, split="")
xx
strsplit("abcabab", split="b")
paste(a, "ABC", sep="")
rep(a, 5)

a = "abcdefgabcab"
substr(a, 4, 7)
regexpr('a', a, fixed=T, useB=F)[1]
unlist(gregexpr('a', a, fixed=T, useB=F))

strvec <- c("Abc", "bcd", "cdef", "defg")
grep("b",strvec) 
grepl("b",strvec) 


sub('a', "AA", a)
gsub('a', "AA", a)
