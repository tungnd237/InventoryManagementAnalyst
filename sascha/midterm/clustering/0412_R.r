library(nnet)
library(caret)
library(glmnet)
library(detectseparation)

data <- read.csv("../data/superstore.csv")

ROOT.DIR <- ".."

ID.VAR <- "Id"
TARGET.VAR <- "Sales"