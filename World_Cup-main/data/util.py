import pandas as pd
import os

def get_data(filepath):
    df = pd.read_csv(filepath)
    df["Championships"]=1
    df.rename(columns={"CHAMPION":"Country"}, inplace=True)
    df["Country"]=df["Country"].str.replace("West Germany", "Germany")
    champs = df.groupby(["Country"])[["Championships"]].sum()
    champs.sort_values("Championships", ascending=False, inplace=True)
    champs.reset_index(inplace=True)   #groupby created index, had to reset index to create column name 
    champs["Wins"]=[76,68,45,47,39,25,32,31]
    champs["Draws"]=[19,21,21,17,14,13,22,17]
    champs["Losses"]=[19,23,17,24,20,21,20,19]
    champs["Games Played"]= champs["Wins"]+champs["Draws"]+champs["Losses"]
    champs["Win %"] = round((champs["Wins"]/champs["Games Played"]),3)*100
    champs["Draw %"] = round((champs["Draws"]/champs["Games Played"]),3)*100
    champs["Loss %"] = round((champs["Losses"]/champs["Games Played"]),3)*100
    champs["Goals Scored"]=[237,232,128,152,136,89,104,108]
    champs["Goals Against"]=[108,130,77,101,85,76,68,75]
    champs["Goal Difference"]=champs["Goals Scored"]-champs["Goals Against"]
    champs["Avg Goals Scored per Game"]=round((champs["Goals Scored"]/champs["Games Played"]),2)
    champs["Avg Goals Against per Game"]=round((champs["Goals Against"]/champs["Games Played"]),2)
    champs["Avg Goal Difference per Game"]=round((champs["Goal Difference"]/champs["Games Played"]),2)
    # print(champs)    
    return champs
