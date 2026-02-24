import pandas as pd
import numpy as np
from scipy.stats import linregress
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy import stats

#------------------------------------
#Load Datast
#------------------------------------

df = pd.read_csv("players_stats_by_season_full_details.csv")

#------------------------------------
#Filter for Regular Season Data only
#------------------------------------

regular_df = df[df["Stage"] == "Regular_Season"]

#--------------------------------------------------
#Determine Player with Most Regular Seasons
#--------------------------------------------------

season_counts = regular_df.groupby("Player")["Season"].nunique()
most_seasons_player = season_counts.idxmax()

print("\nPlayer with Most Regular Seasons")
print("Player:", most_seasons_player)

#--------------------------------------------------
#Calculate Seasonal 3PT Accuracy for this Player
#--------------------------------------------------
player_df = regular_df[regular_df["Player"] == most_seasons_player]
season_stats = player_df.groupby("Season")[["3PM", "3PA"]].sum()

#Use numpy.divide with a conditional mask to prevent divide by zero
season_stats["Accuracy"] = np.divide(
    season_stats["3PM"],
    season_stats["3PA"],
    out=np.zeros_like(season_stats["3PM"], dtype=float),
    where=season_stats["3PA"] != 0
)
season_stats["Year"] = season_stats.index.str[:4].astype(int)

print("\nSeasonal Three Point Accuary")
print(season_stats)

#--------------------------------------------------
#Linear Regression on Accuracy Across Years
#--------------------------------------------------
x = season_stats["Year"]
y = season_stats["Accuracy"]

slope, intercept, r, p, std_err = linregress(x,y)

def fit_line(x):
    return slope * x + intercept

#-------------------------------------------
#Integrate Line of Best Fit
#-------------------------------------------
earliest = x.min()
latest = x.max()

area, _ = quad(fit_line, earliest, latest)

avg_accuracy_fit = area / (latest - earliest)
actual_avg_accuracy = y.mean()

print("\nAverage 3PT Accuracy Comparison")
print("Average Accuracy from Regression:", avg_accuracy_fit)
print("Actual Average Accuracy:", actual_avg_accuracy)

#-------------------------------------------
#Interpolation for Missing Seasons
#-------------------------------------------

interp_function = interp1d(x, y, kind='linear', fill_value="extrapolate")

missing_2002 = interp_function(2002)
missing_2015 = interp_function(2015)

print("\nInterpolated Missing Seasons")
print("Estimated Accuracy for 2002-2003:", missing_2002)
print("Estimated Accuracy for 2015-2016:", missing_2015)

#-------------------------------------------
#Statistical Analysis for FGM and FGA
#-------------------------------------------
fgm = regular_df["FGM"]
fga = regular_df["FGA"]

print("\nFGM STATISTICS")
print("Mean:", stats.tmean(fgm))
print("Variance:", stats.tvar(fgm))
print("Skew:", stats.skew(fgm))
print("Kurtosis:", stats.kurtosis(fgm))

print("\nFGA STATISTICS")
print("Mean:", stats.tmean(fga))
print("Variance:", stats.tvar(fga))
print("Skew:", stats.skew(fga))
print("Kurtosis:", stats.kurtosis(fga))

#-----------------------------------------
#T - Tests
#-----------------------------------------

paired_test = stats.ttest_rel(fgm, fga)
fgm_test = stats.ttest_1samp(fgm, stats.tmean(fgm))
fga_test = stats.ttest_1samp(fga, stats.tmean(fga))

print("\nPaired T-Test (FGM vs FGA)")
print("T-Statistic:", round(paired_test.statistic, 4))
print("P-Value:", paired_test.pvalue)
print("Degrees of Freedom:", paired_test.df)

print("\nOne Sample T-Test (FGM)")
print("T-Statistic:", round(fgm_test.statistic, 4))
print("P-Value:", fgm_test.pvalue)
print("Degrees of Freedom:", fgm_test.df)

print("\nOne Sample T-Test (FGA)")
print("T-Statistic:", round(fga_test.statistic, 4))
print("P-Value:", fga_test.pvalue)
print("Degrees of Freedom:", fgm_test.df)