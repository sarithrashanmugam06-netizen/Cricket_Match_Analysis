
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

    
    return(f"\n{a} {max_key} {b}{max_value}")
    


print(maximum(total_winner,"Maximun scored Winner:","Count:"))

# Find the team with the lowest number of wins.


def minimum(n,a,b):
    min_key = None
    min_value = float("inf")
    
    for key in n:
        value = n[key]
        
        if value < min_value:
            min_value = value
            min_key = key

    return(f"\n{a} {min_key} {b} {min_value}")
    
print(minimum(total_winner,"Minimun scored Winner:","Count:"))



tol_runs = cricket_dict["runs_team1"].copy()

for key, value in cricket_dict["runs_team2"].items():
    tol_runs[key] = tol_runs.get(key,0)+value


#Find the match with the highest total runs scored by both teams combined. 

print(maximum(tol_runs,"highest total runs of team :","score:"))


#Find the match with the lowest total runs scored by both teams combined.

print(minimum(tol_runs,"lowest total runs of team:","score"))

 #Find the highest score made by a single team in any match. 


High_run_team1 = maximum(cricket_dict["runs_team1"],"runner score:","singleteam ")


High_run_team2  = maximum(cricket_dict["runs_team2"],"runner score","singleteam ")


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

average_runs = []
for team in Teams:
    average = Teams[team]/ total_count[team]
    average_runs.append((team,average))
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

#Find the player who received Player of the Match award the highest number of times. 

players = count("player_of_match")
print(maximum(players,"score","player of the match \n"))

# Display the number of Player of the Match awards received by each player. 
print(f"Player of the Match:\n{players}")

# Find the venue where the highest number of matches were played. 
venues = count("venue")
print(maximum(venues,"highest no fo matches played venue:","count:"))
# Display the number of matches played at each venue. 

print(f"\nMatches played at each venue :\n{venues}")
# Find the top 5 highest-scoring matches based on the combined runs of both teams. 

sorted_runs = sorted(tol_runs.items(), key=lambda x: x[1],reverse=True)
top_5 = dict(sorted_runs[0:5])

print(f"\nTop 5 highest-scoring of matches:\n{top_5}") 

# Find all matches where the winning team scored more than 300 runs. 
print("\nThe winning team scored more than 300 runs:")
for i in range(100):
    if cricket_dict["winner"][i] == cricket_dict["team1"][i]:
        if cricket_dict["runs_team1"][i] > 300:
            print(f"{cricket_dict["team1"][i]} : {cricket_dict["runs_team1"][i]}")

    if cricket_dict["winner"][i] == cricket_dict["team2"][i]:
            if cricket_dict["runs_team2"][i] > 300:
                print(f"{cricket_dict["team2"][i]}: {cricket_dict["runs_team2"][i]}")

 #Find all matches where the difference between the two teams' scores was less than 20 runs.

print("\nDifference between the two teams less than 20 runs:")
    
for i in range(100):

    runs = abs(cricket_dict["runs_team1"][i]-cricket_dict["runs_team2"][i])

    if  runs < 20:
        print(f"{cricket_dict["match_id"][i]} {cricket_dict["team1"][i]} and {cricket_dict["team2"][i]}:{runs}")



 #Find the team with the highest average score.

print("\nHighest Average score:")
print(maximum(dict(average_runs),"higest average scored team","runs "))


 #Find the team with the lowest average score. 

print("\nlowest Average score:")
print(minimum(dict(average_runs),"lowest average scored team","runs "))

#Calculate the win percentage for each team. 

Winner_counts = count("winner")

print("\nWin Percentage of each team:")
win_percentage = {}

for key, value in Winner_counts.items():
    percentage = round(value / total_count[key] * 100,2)
    win_percentage[key] = percentage

print(win_percentage)

 #Display the teams ranked based on their win percentage. 

print("\n Rank based win Percentage:")
sorted_win = sorted(win_percentage.items(),key = lambda x : x[1],reverse=True)
print(sorted_win)

 
# Find how many matches each team won while batting first. 

batting = {}

for i in range(100):

    if cricket_dict["runs_team1"][i] > cricket_dict["runs_team2"][i]:

        team = cricket_dict["team1"][i]

        if team not in batting:
            batting[team] = 0

        batting[team] += 1

    if cricket_dict["runs_team2"][i] > cricket_dict["runs_team1"][i]:
    
            team = cricket_dict["team2"][i]
    
            if team not in batting:
                batting[team] = 0
    
            batting[team] += 1


print(batting)

# Find how many matches each team won while chasing.


chasing = {}

for i in range(100):

    if cricket_dict["runs_team1"][i] < cricket_dict["runs_team2"][i]:

        team = cricket_dict["team2"][i]

        if team not in chasing:
            chasing[team] = 0

        chasing[team] += 1

print(chasing)



# #Identify the team with the highest number of successful chases. 

print(maximum(chasing,"Highest number of chasing:","count:"))

# Ask the user to enter a team anme and display that team's complete statistics

def statistics(team):
    statistics = []

    for i in range(100):

        if team == cricket_dict["team1"][i] or team == cricket_dict["team2"][i]:

            match_id = cricket_dict["match_id"][i]
            date = cricket_dict["date"][i]

            if team == cricket_dict["team1"][i]:
                opponent = cricket_dict["team2"][i]
                runs = cricket_dict["runs_team1"][i]
                wickets = cricket_dict["wickets_team1"][i]
            else:
                opponent = cricket_dict["team1"][i]
                runs = cricket_dict["runs_team2"][i]
                wickets = cricket_dict["wickets_team2"][i]

            if team == cricket_dict["winner"][i]:
                result = "Won"
            else:
                result = "Lost"

            venue = cricket_dict["venue"][i]
            player = cricket_dict["player_of_match"][i]

            statistics.append({
                "Match id": match_id,
                "Date": date,
                "Opponent": opponent,
                "Runs": runs,
                "Wickets": wickets,
                "Result": result,
                "Venue": venue,
                "Player of the match": player
            })

    return statistics

print(statistics("India"))

# Ask the user to enter a venue and display all matches played at that venue. 
print("\n")
def place(venue):
    print(f"This matches are played at {venue}")

    matches = []

    for i in range(100):
        if venue == cricket_dict["venue"][i]:
            team1 = cricket_dict["team1"][i]
            team2 = cricket_dict["team2"][i]

            matches.append({
                "Team1":team1,
                "Team2":team2
                })

    if len(matches) == 0:
            return (f"No matches played on {venue}")
        
       
    return matches

print(place("Mumbai"))
            

 #Ask the user to enter a date and display all matches played on that date. If no match exists, display an appropriate message.

print("\n")
def date(date):
    print(f"This match is played on {date}")

    matches = []

    for i in range(100):
        if date == cricket_dict["date"][i]:
            team1 = cricket_dict["team1"][i]
            team2 = cricket_dict["team2"][i]

            matches.append({
                "Team1":team1,
                "Team2":team2
                })

    if len(matches) == 0:
            return (f"No matches played on {date}")
        
       
    return matches

print(date("2025-11-16"))

"""
----------------------------------------------------------------------------
                        Basic Data Handling
----------------------------------------------------------------------------
"""



#Find the total number of matches played at each venue.
print("\n Total number of matches played at each venue:")
print(count("venue"))

#Find the number of matches played between India and Australia. 
Count_india_and_australia = 0

for i in range(100):
    if (cricket_dict["team1"][i] == "India" and cricket_dict["team2"][i] == "Australia") or (cricket_dict["team1"][i] == "Australia" and cricket_dict["team2"][i] == "India"):
        Count_india_and_australia = Count_india_and_australia + 1

print(f"\nIndia and Australia between matches : {Count_india_and_australia}")


#Find all matches where India was either Team 1 or Team 2. 
India_match = 0

for i in range(100):
    if (cricket_dict["team1"][i] == "India" or cricket_dict["team2"][i] == "India"):
        India_match = India_match + 1

print(f"\nwhere India was either Team 1 or Team 2 : {India_match}")

#Find all matches where the winning team was Team 1. 

def winner_count(n):
    winner_team_count = 0
    for i in range(100):
        if cricket_dict[n][i] == cricket_dict["winner"][i]:
            winner_team_count = winner_team_count +1

    return winner_team_count

print("\nwinner team was team 1:",winner_count("team1"))

#Find all matches where the winning team was Team 2.

print("\nwinner team was team 2:",winner_count("team2"))

#Count how many times each team appeared as Team 1. 

print("\nEach team appeared as team1:\n",count("team1"))

 #Count how many times each team appeared as Team 2. 

print("\nEach team appeared as team2:\n",count("team2"))

#Find the team that appeared in the highest number of matches. 

print(maximum(total_count,"Highest number of matches played ","that's count is "))

 #Find the team that appeared in the lowest number of matches. 

print(minimum(total_count,"Lowest number of matches played","that's count is "))

 #Find all matches played at Chennai.

def venue(n):
    count = 0
    for i in range(100):
        if n == cricket_dict["venue"][i]:
            count = count + 1

    return count

print("\nMatches played at Chennai: ",venue("Chennai"))


"""
----------------------------------------------------------------------------
                        Filtering & Conditions
----------------------------------------------------------------------------
"""



#Find matches where Team 1 scored more than 300 runs.
def team_score(n,m):
    for i in range(100):
        if cricket_dict[n][i] > 300 :
            print(cricket_dict[m][i] ,":",cricket_dict[n][i])
    
print("\nTeam 1  scored more tah 300 runs:")
team_score("runs_team1","team1")
 #Find matches where Team 2 scored more than 300 runs. 

print("\nTeam 2  scored more tah 300 runs:")
team_score("runs_team2","team2")
 #Find matches where both teams scored more than 250 runs.
print("\nBoth teams scored more than 250 runs:")
for i in range (100):
    if cricket_dict["runs_team1"][i] > 250 and cricket_dict["runs_team2"][i] > 250:
        print(cricket_dict["team1"][i],":",cricket_dict["runs_team1"][i], "and" ,cricket_dict["team2"][i] ,":", cricket_dict["runs_team2"][i])

 #Find matches where the winning margin was more than 100 runs.\
print("\nwinning margin was more than 100 runs:")
for i in range(100):
    if cricket_dict["winner"][i] == cricket_dict["team1"][i] or cricket_dict["winner"][i] == cricket_dict["team2"][i]:
        margin = abs(cricket_dict["runs_team1"][i]-cricket_dict["runs_team2"][i])
        if margin > 100:
            print(cricket_dict["winner"][i],":",margin)

 #Find matches where the winning margin was less than 10 runs. 

print("\nwinning margin was less than 10 runs:")
for i in range(100):
    if cricket_dict["winner"][i] == cricket_dict["team1"][i] or cricket_dict["winner"][i] == cricket_dict["team2"][i]:
        margin = abs(cricket_dict["runs_team1"][i]-cricket_dict["runs_team2"][i])
        if margin < 10:
            print(cricket_dict["winner"][i],":",margin)