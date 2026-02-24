## Assignment 4 SciPy NBA Data Analysis

### Purpose

The purpose of this project is to analyze NBA player performance trends using SciPy statistical and mathematical tools. The analysis focuses on identifying long term shooting trends in regular season play by applying regression, integration, interpolation, and hypothesis testing methods to real player performance data.

This project demonstrates how hidden performance trends can be extracted from structured sports datasets using scientific computing techniques.

---

### Dataset Filtering

The dataset was filtered to include only entries labeled Regular_Season in the Stage column. All subsequent calculations were performed using this filtered dataset to ensure playoff and exhibition statistics did not influence long term performance analysis.

---

### Analysis Pipeline

The program performs the following steps:

1. Identifies the player who participated in the greatest number of unique regular seasons

2. Calculates three point shooting accuracy for this player by season using

   Accuracy = 3PM / 3PA

3. Applies linear regression using scipy.stats.linregress to model accuracy across time

4. Integrates the regression function using scipy.integrate.quad to estimate the average accuracy across the player’s career

5. Uses scipy.interpolate.interp1d to estimate accuracy for seasons in which the player did not participate

6. Computes descriptive statistics for the Field Goals Made and Field Goals Attempted columns including
   mean
   variance
   skew
   kurtosis

7. Performs a paired relational t test between Field Goals Made and Field Goals Attempted

8. Performs individual one sample t tests on each column

---

### Key Variables

regular_df
Filtered dataframe containing only regular season data

season_stats
Grouped seasonal totals for 3PM and 3PA for the selected player

x
Numeric representation of season year used for regression

y
Three point accuracy values used as dependent variable in regression

fit_line
Linear regression model used for integration

---

### Functions Used

scipy.stats.linregress
Used to model shooting accuracy over time

scipy.integrate.quad
Used to integrate the regression model to estimate average performance

scipy.interpolate.interp1d
Used to estimate missing seasonal accuracy values

scipy.stats.tmean
scipy.stats.tvar
scipy.stats.skew
scipy.stats.kurtosis
Used to describe distributional properties of FGM and FGA

scipy.stats.ttest_rel
Used to compare FGM and FGA relationally

scipy.stats.ttest_1samp
Used to test individual columns against their means

---

### Output

Program output is organized into clearly labeled sections including:

Player with most regular seasons
Seasonal three point accuracy
Regression based average accuracy
Actual average accuracy
Interpolated seasonal values
FGM statistics
FGA statistics
Paired t test results
One sample t test results

This structure allows each required rubric item to be easily identified in terminal output.

---

### Interpretation of T Tests

The paired t test compares Field Goals Made and Field Goals Attempted on a relational basis across observations.

The one sample t tests compare each column to its own mean. Because each dataset is being tested against its true average, the expected outcome is a t statistic near zero and a p value near one, indicating no statistical difference from the population mean.

---

### Limitations

Linear regression assumes a consistent trend in shooting accuracy over time and may not reflect abrupt performance changes due to injury or team changes.

Interpolation assumes linear progression between seasons and may not accurately reflect actual performance in missing seasons.

Three point accuracy calculations assume valid non zero attempt values. Seasons with zero attempts may require masking or exclusion to prevent divide by zero conditions.

---

### How to Run

Ensure players_stats_by_season_full_details.csv is in the same directory as scipy_analysis.py

Run using:

python scipy_analysis.py

---

### Repository Contents

scipy_analysis.py
players_stats_by_season_full_details.csv
README.md
AI Chat Log

---

### Use of Generative AI

ChatGPT was used as an assistance tool for debugging, formatting output, and implementing SciPy functions based on lecture material.
