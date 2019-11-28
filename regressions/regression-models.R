# Install and load necessary packages
#install.packages("MASS")
library(MASS)
#install.packages("pscl")
library(pscl)
#install.packages("countreg")
library(countreg)
#install.packages("AER")
library(AER)
#install.packages("countreg", repos="http://R-Forge.R-project.org")
library(countreg)
#install.packages("blorr")
library(blorr)
#install.packages("rsq")
library(rsq)

# set options for scientific notation
options(scipen = 999)

# Read data for OLS model from file
data_OLS <- read.csv("Documents/GitHub/strategy-business-models/datasets/final-df-cs-10-reviews.csv")
OLS_model <- lm(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action + is_pc,
                data = data_OLS)
summary(OLS_model)

car::vif(OLS_model)

# Read data for count models from file
data_count <- read.csv("Documents/GitHub/strategy-business-models/datasets/final-df-count-models.csv")

# Poisson Regression
poisson <- glm(nr_reviews ~ user_sentiment_var*critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action + is_pc,
               data=data_count, family='poisson')

summary(poisson)

# Check VIF values (multicollinearity)
car::vif(poisson)

## Visualize fit
countreg::rootogram(poisson)

## Test for overdispersion (dispersion and alpha parameters)
dispersiontest(poisson)
dispersiontest(poisson, trafo=2)

# Negative Binomial Regression
negbin <- glm.nb(nr_reviews ~ user_sentiment_var*critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action + is_pc,
                 data=data_count)
summary(negbin)

# Check VIF values (multicollinearity)
car::vif(negbin)

## Visualize fit
countreg::rootogram(negbin)


# Hurdle Regression
mod_hurdle <- hurdle(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action + is_pc,
                     data = data_count,
                     dist = "negbin")
summary(mod_hurdle)

## Visualize fit
countreg::rootogram(mod_hurdle)

