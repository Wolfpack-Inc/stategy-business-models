# Hurdl model predict based on sentiment of first two weeks

install.packages("AER") # Install the AER package (Applied Econometrics with R)
install.packages("dplyr")
install.packages("pscl")
library(pscl)
library(AER)            # load package for Hurdle model
library(dplyr)          # load package for filtering

# load the data 
getwd()
data <- read.csv("C:/Users/20190298/Documents/GitHub/strategy-business-models/final-df-count-models.csv")

plot(table(data$nr_reviews))

testje<-factor(data$genre)
levels(testje)

#factor should be lowercase
data$genre <- tolower(data$genre)
data$console <- tolower(data$console)

test_data <- cbind(data,dummy_cols(data$genre),dummy_cols(data$console))
colnames(test_data) <- c("game","nr_reviews","user_avg_grade","user_sentiment_var","critic_avg_grade","critic_sentiment_var","critic_volume","genre","console", ".data", "is_action","is_miscellaneous" ,"is_general","is_sports" , "is_role_playing" , "is_strategy" ,"is_action_adventure" ,"is_simulation", "is_adventure" ,"is_arcade" ,"is_racing" ,"is_driving" ,"is_puzzle", ".data2","is_pc","is_playstation_3","is_xbox_360","is_nintendo_64","is_switch","is_playstation_4","is_3ds","is_xbox_one","is_playstation_vita","is_wii_u","is_ds","is_playstation_2","is_wii","is_gamecube","is_ios","is_xbox","is_psp","is_game_boy_advance","is_playstation")
# Hurdle model 1
mod_hurdle <- hurdle(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume | user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + factor(genre) + factor(console),
                     data = data)mod_hurdle <- hurdle(nr_reviews ~ user_sentiment_var * critic_sentiment_var + user_avg_grade + critic_avg_grade + critic_volume + is_action+is_miscellaneous +is_general+is_sports + is_role_playing + is_strategy + is_action_adventure + is_simulation + is_adventure + is_arcade + is_racing + is_driving, data = test_data)

results_hurdle_2 <- summary(mod_hurdle)
summary(mod_hurdle)

# Visualize hurdle
#install.packages("countreg", repos="http://R-Forge.R-project.org")
library(countreg)
rootogram(mod.hurdle, max=40) # fit up to count 40
rootogram(mod.hurdle, max=150) # fit up to count 150


# Solution to overdispersion: negative binomial
mod.hurdle.nb <- hurdle(nr_reviews ~ 
                          user_sentiment_var * critic_sentiment_var +
                          user_avg_grade       +
                          critic_avg_grade     +
                          critic_volume,
                        data = data, 
                        dist = "negbin")

rootogram(mod.hurdle.nb, max=40) # fit up to count 40
rootogram(mod.hurdle.nb, max=150) # fit up to count 150

summary(mod.hurdle.nb)

# Compare models with AIC
AIC(mod.hurdle)
AIC(mod.hurdle.nb)



