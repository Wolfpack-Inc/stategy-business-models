# Hurdl model predict based on sentiment of first two weeks

#install.packages("AER") 
#install.packages("dplyr")
#install.packages("pscl")
library(pscl)
library(AER)            # load package for Hurdle model
library(dplyr)          # load package for filtering

# load the data 
getwd()
data <- read.csv("Documents/GitHub/strategy-business-models/datasets/final-df-cs-2weeks-8-reviews.csv")

OLS_model <- lm(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action + is_pc,
                 data = data)
summary(OLS_model)
