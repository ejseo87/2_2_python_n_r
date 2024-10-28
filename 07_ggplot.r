library(ggplot2)
head(trees)
trees[c(1:2, 30:31), ]
h_gr <- cut(trees$Height, 4)
print(h_gr)
ggplot(data = trees) +
  geom_point(aes(x = Girth, y = Volume, col = h_gr))
#
head(mpg)
hwy_plot <- ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class)) +
  geom_smooth(
    mapping = aes(x = displ, y = hwy, linestyle = drv),
    method = "loess"
  )
hwy_plot +
  facet_grid(drv ~ cyl)
