
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

print(f"\nCricket Teams :{teams}\n")

# Find the total number of matches played by each team.

def count(n):

    cricket_dict = df.to_dict()[n]
    teams = list(cricket_dict.values()) 

    team_count = {}

    for i in teams:
        team_count[i] = team_count.get(i,0)+1

    return team_count

team_one = count("team1")
team_two = count("team2")

total_count = team_one.copy()
for key, value in team_two.items():
    total_count[key] = total_count.get(key,0)+ value

print(f"Total count of matches played each teams:\n{total_count}")


# Find and display all matches won by **India**.

total_winner =count("winner")
if "India" in total_winner:
    print(f"\nIndia won's {total_winner["India"]} matches.")


# Find the total number of wins for each team.

print(f"\nTotal number of wins for each team:\n{count("winner")}")


# Find the team with the highest number of wins.

def maximum(n):
    max_key = None
    max_value = 0
    
    for key in n:
        value = n[key]
        
        if value > max_value:
            max_value = value
            max_key = key

    return(f"\nMaximun winner {max_key} with count of {max_value}")


print(maximum(total_winner))

# Find the team with the lowest number of wins.


def minimum(n):
    min_key = None
    min_value = float("inf")
    
    for key in n:
        value = n[key]
        
        if value < min_value:
            min_value = value
            min_key = key

    return(f"\nMinimun winner {min_key} with count of {min_value}")


print(minimum(total_winner))








