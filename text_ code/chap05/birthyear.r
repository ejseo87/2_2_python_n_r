## birthyear.r
birthyear <- function() {
  age <- readline(prompt="Enter age: ")
  curyear <- as.numeric( format(Sys.Date(), "%Y") )
  b.year <- curyear-as.numeric(age)
  list(born.year=b.year)
}
