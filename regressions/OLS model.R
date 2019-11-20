# Hurdl model predict based on sentiment of first two weeks

#install.packages("AER") 
#install.packages("dplyr")
#install.packages("pscl")
library(pscl)
library(AER)            # load package for Hurdle model
library(dplyr)          # load package for filtering

# load the data 
getwd()
data <- read.csv("C:/Users/20190298/Documents/GitHub/strategy-business-models/final-df-count-models.csv")

OLS_model <- glm(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + factor(genre) + factor(console))
