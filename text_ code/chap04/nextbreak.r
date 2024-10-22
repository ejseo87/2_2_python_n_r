x <- 1:5
for (j in x) {
  if (j == 3) next
   cat(j, " ")
}

x <- 1:5
for (j in x) {
  if (j == 3) break
   cat(j, " ")
}
