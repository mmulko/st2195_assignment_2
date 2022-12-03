# Importing required libraries
library(rvest)

# Getting page as html
cars_html <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values")

# Extracting required chunk of text
cars_data <- html_nodes(cars_html, "pre")
cars_text <- html_text(cars_data[11])

# Separating long character into separate rows
cars_list <- unlist(strsplit(cars_text,"\n"))

# Creating CSV file
write.table(cars_list, file="r_csv/cars.csv", row.names=FALSE, col.names=FALSE, sep=",", quote=FALSE)

# Checking the result
read.csv("r_csv/cars.csv")