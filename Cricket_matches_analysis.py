
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

no_of_matches = total(cricket_dict["match_id"])
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

def maximum(n,a,b):
    max_key = None
    max_value = 0
    
    for key in n:
        value = n[key]
        
        if value > max_value:
            max_value = value
            max_key = key

    
    return(f"\nMaximum {a} {max_key} with {b} of {max_value}")
    


print(maximum(total_winner,"winner","count"))

# Find the team with the lowest number of wins.


def minimum(n,a,b):
    min_key = None
    min_value = float("inf")
    
    for key in n:
        value = n[key]
        
        if value < min_value:
            min_value = value
            min_key = key

    return(f"\nMinimum {a} {min_key} with {b} of {min_value}")
    
print(minimum(total_winner,"winner","count"))



tol_runs = cricket_dict["runs_team1"].copy()

for key, value in cricket_dict["runs_team2"].items():
    tol_runs[key] = tol_runs.get(key,0)+value


#Find the match with the highest total runs scored by both teams combined. 

print(maximum(tol_runs,"runner","team"))


#Find the match with the lowest total runs scored by both teams combined.

print(minimum(tol_runs,"runner","team"))

 #Find the highest score made by a single team in any match. 


High_run_team1 = maximum(cricket_dict["runs_team1"],"runner","singleteam")


High_run_team2  = maximum(cricket_dict["runs_team2"],"runner","singleteam")


high_runner = High_run_team1
if High_run_team2 > High_run_team1:
    high_runner = High_run_team2 
print(f"{high_runner}\n")

#Find the average runs scored by each team. 

Teams = {}

for i in range(100):
    team1 = cricket_dict["team1"][i], cricket_dict["runs_team1"][i]
    team2 = cricket_dict["team2"][i], cricket_dict["runs_team2"][i]


    if team1[0] not in Teams:
        Teams[team1[0]] = team1[1]

    else:
        Teams[team1[0]] = Teams[team1[0]] + team1[1]

    if team2[0] not in Teams:
            Teams[team2[0]] = team2[1]
    
    else:
        Teams[team2[0]] = Teams[team2[0]] + team2[1]

print("\nAverage runs of each team:")
for team in Teams:
    average = Teams[team]/ total_count[team]
    print(team,average)


#Find the average number of wickets taken by each team. 

Wickets = {}

for i in range(100):
    team1 = cricket_dict["team1"][i], cricket_dict["wickets_team1"][i]
    team2 = cricket_dict["team2"][i], cricket_dict["wickets_team1"][i]


    if team1[0] not in Wickets:
        Wickets[team1[0]] = team1[1]

    else:
        Wickets[team1[0]] = Wickets[team1[0]] + team1[1]

    if team2[0] not in Wickets:
            Wickets[team2[0]] = team2[1]
    
    else:
        Wickets[team2[0]] = Wickets[team2[0]] + team2[1]

print("\nAverage wickets of each team:")
for team in Wickets:
    average = Wickets[team]/ total_count[team]
    print(team,average)




