# Generate some example data
set.seed(123) # Set a seed for reproducibility
data <- data.frame(
  group = rep(c("A", "B"), each = 10),
  variable = c(rnorm(10, mean = 5, sd = 1), rnorm(10, mean = 7, sd = 1.5))
)

# t-test to compare means between two groups
t.test(variable ~ group, data = data)

# ANOVA to compare means across multiple groups
anova <- aov(variable ~ group, data = data)
summary(anova)

# Chi-squared test for independence between two categorical variables
table <- matrix(c(20, 10, 15, 25), nrow = 2, byrow = TRUE)
chisq.test(table)

# Correlation test between two continuous variables
cor.test(data$variable, rnorm(20, mean = 6, sd = 2))

# Linear regression to model the relationship between two variables
model <- lm(variable ~ group, data = data)
summary(model)

# Wilcoxon rank-sum test to compare medians between two groups
wilcox.test(variable ~ group, data = data)

# Kruskal-Wallis test to compare medians across multiple groups
kruskal.test(variable ~ group, data = data)

# Fisher's exact test to compare proportions between two groups
table <- matrix(c(10, 5, 15, 20), nrow = 2, byrow = TRUE)
fisher.test(table)

# One-sample t-test to compare a sample mean to a known population mean
t.test(data$variable, mu = 6)

# Paired t-test to compare means before and after an intervention
before <- c(3, 5, 6, 7, 9)
after <- c(5, 6, 7, 8, 10)
t.test(before, after, paired = TRUE)

# Analysis of covariance (ANCOVA) to compare means between groups while controlling for a continuous covariate
covariate <- rnorm(20, mean = 4, sd = 1)
model <- lm(variable ~ group + covariate, data = data)
summary(model)

# Create a scatter plot
plot(x = mtcars$wt, y = mtcars$mpg, main = "MPG vs. Weight", xlab = "Weight (1000 lbs)", ylab = "Miles per Gallon")

# Create a histogram
hist(mtcars$mpg, main = "MPG Distribution", xlab = "Miles per Gallon", ylab = "Frequency", col = "lightblue")

# Create a box plot
boxplot(mpg ~ cyl, data = mtcars, main = "MPG by Number of Cylinders", xlab = "Number of Cylinders", ylab = "Miles per Gallon", col = "lightblue")

# Create a line plot
x <- seq(0, 10, length = 100)
y <- sin(x)
plot(x, y, type = "l", main = "Sine Wave", xlab = "X", ylab = "Y")

# Create a bar plot
counts <- table(mtcars$cyl)
barplot(counts, main = "Number of Cars by Number of Cylinders", xlab = "Number of Cylinders", ylab = "Number of Cars", col = "lightblue")

# Create a scatter plot with a trendline
plot(mtcars$wt, mtcars$mpg, main = "MPG vs. Weight with Trendline", xlab = "Weight (1000 lbs)", ylab = "Miles per Gallon")
abline(lm(mpg ~ wt, data = mtcars), col = "red")


