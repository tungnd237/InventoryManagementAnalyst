library(nnet)
library(caret)
library(glmnet)
library(detectseparation)

data <- read.csv("/Users/silmari/2023_statdm_project/sascha/data/superstore_noid.csv")

ROOT.DIR <- ".."

ID.VAR <- "Id"
TARGET.VAR <- "Sales"