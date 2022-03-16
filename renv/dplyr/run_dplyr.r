library(dplyr)

mtcars <- as_tibble(mtcars)

print(mtcars %>% arrange(desc(cyl), desc(disp)))
print(mtcars[order(mtcars$cyl, mtcars$disp), , drop = FALSE])

