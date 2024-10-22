# if.test.r
if.test <- function(x) { # if-else test
 if (x %% 2 == 0) {
    cat("x는 짝수입니다\n")
 } else if (x %% 2 == 1) {
          cat("x는 홀수입니다\n")
        } else { 
          cat("x는 자연수가 아닙니다\n")
 } # end if
} # end function


