import pandas as pd
import altair as alt
import os as os

os.chdir("/Users/ashfi/Documents/Datasets")
df = pd.read_csv('output.csv')
############
df = df.drop(columns=['Lower Confidence Interval',
             'Upper Confidence Interval'])

os.chdir("/Users/ashfi/Documents/Datasets")
df = pd.read_csv('output.csv', decimal='.', converters={
                 'Country': lambda x: str(x)})
############
df["Explained by: Healthy life expectancy"] = df["Explained by: Healthy life expectancy"].str.replace(
    ',', '.')
df["Explained by: Social support"] = df["Explained by: Social support"].str.replace(
    ',', '.')
df["Explained by: Perceptions of corruption"] = df["Explained by: Perceptions of corruption"].str.replace(
    ',', '.')
df["Explained by: Generosity"] = df["Explained by: Generosity"].str.replace(
    ',', '.')
df["Explained by: Freedom to make life choices"] = df["Explained by: Freedom to make life choices"].str.replace(
    ',', '.')
df["Happiness score"] = df["Happiness score"].str.replace(
    ',', '.')
df["Explained by: GDP per capita"] = df["Explained by: GDP per capita"].str.replace(
    ',', '.')
df["Explained by: Social support"] = df["Explained by: Social support"].str.replace(
    ',', '.')

df[["Explained by: Healthy life expectancy", "Explained by: Social support", "Explained by: Perceptions of corruption",
    "Explained by: Generosity", "Explained by: Freedom to make life choices", "Happiness score", "Explained by: GDP per capita"]] = df[[
        "Explained by: Healthy life expectancy", "Explained by: Social support", "Explained by: Perceptions of corruption", "Explained by: Generosity",
        "Explained by: Freedom to make life choices", "Happiness score", "Explained by: GDP per capita"]].apply(pd.to_numeric)
df['Happiness Rank'] = df['Happiness Rank'].fillna(
    0) + df['Happiness.Rank'].fillna(0) + df['RANK'].fillna(0) + df['Overall rank'].fillna(0)    # add to Happiness Rank
df = df.rename(columns={"Economy (GDP per Capita)": "Economy", "Health (Life Expectancy)": "Health",
               "Trust (Government Corruption)": "Trust"}, errors="raise")
df['Happiness Score'] = df['Happiness Score'].fillna(
    0) + df['Happiness.Score'].fillna(0) + df['Score'].fillna(0) + df['Ladder score'].fillna(0) + df['Happiness score'].fillna(0)   # Add to economy
df['Economy'] = df['Economy'].fillna(0) + df['GDP per capita'].fillna(
    0) + df['Explained by: Log GDP per capita'].fillna(0) + df['Economy..GDP.per.Capita.'].fillna(0) + df['Explained by: GDP per capita'].fillna(0)
#  # Add to economy
df['Health'] = df['Health'].fillna(0) + df['Healthy life expectancy'].fillna(
    0) + df['Explained by: Healthy life expectancy'].fillna(0) + df['Health..Life.Expectancy.'].fillna(0)
df['Freedom'] = df['Freedom'].fillna(0) + df['Freedom to make life choices'].fillna(
    0) + df['Freedom to make life choices'].fillna(0) + df['Explained by: Freedom to make life choices'].fillna(0)
df['Generosity'] = df['Generosity'].fillna(
    0) + df['Social support'].fillna(0) + df['Explained by: Social support'].fillna(0)
df['Trust'] = df['Trust'].fillna(0) + df['Perceptions of corruption'].fillna(
    0) + df['Trust..Government.Corruption.'].fillna(0) + df['Explained by: Perceptions of corruption'].fillna(0)
df.columns
df.fillna('', inplace=True)
