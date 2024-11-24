library(readr)

library(stargazer)
econ_data <- read_csv("C:/Users/ahmee/OneDrive/Desktop/Books for Fall 2024/Econometrics/Econometrics Project/econ.dat")


econ_data$inflation_rate <- as.numeric(econ_data$inflation_rate)
econ_data$gdp_growth <- as.numeric(econ_data$gdp_growth)
econ_data$region <- as.factor(econ_data$region)

data_cleaned <- econ_data[!econ_data$Name %in% c("qatar", "botswana", "venezuela", "zimbabwe"), ]
plot(data_cleaned$`inflation_rate`, data_cleaned$`Unemployment`)



levels(econ_data$region)
base_model <- lm(Unemployment ~ inflation_rate , data=econ_data)
model_all <- lm(Unemployment ~ inflation_rate + region + gdp_growth, data = econ_data)
model_all_no_outliers <- lm(Unemployment ~ inflation_rate + region + gdp_growth, data=data_cleaned)


stargazer(base_model,model_all,model_all_no_outliers,
          title = "Regression of Wage on Education",
          type="latex"
          , column.sep.width = "1pt", font.size = "small"
          #,out="regression_wage_MLR.doc"
)


