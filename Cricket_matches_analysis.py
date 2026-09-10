
import pandas as pd

df = pd.read_csv("D:\cricket\cricket_matches_100_rows.csv")

cricket_dict = df.to_dict()

print(cricket_dict)


# Read the cricket_matches.csv file using Python and display the total number of matches. 

def total(n):
    count = 0
    for i in range (len(n)):

        count = count + 1
    
    return f"\nTotal number of Matches:{count}"

print(total(cricket_dict["match_id"]))

#Find and display all the unique teams present in the dataset. 

teams = set(cricket_dict["team1"].values())

print(f"\nCricket Teams :{teams}")








