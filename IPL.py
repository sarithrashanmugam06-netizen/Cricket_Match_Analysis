import csv
cricket = []

with open("cricket_matches_100_rows.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cricket.append(row)

print(cricket)

#unique teams in cricket
teams = set()

for row in cricket:
    teams.add(row["team1"])

print(f"\n{teams}")

#total number of matches played by each team.

count_1 = {}


for team in cricket:
    team_name =(team["team1"])

    if team_name not in count_1:
        count_1[team_name] = 0

    count_1[team_name] +=1


print(sorted(count_1.items()))


count_2 = {}

for team in cricket:
    team_name = (team["team2"])

    if team_name not in count_2:
        count_2[team_name] = 0

    count_2[team_name] +=1

print(sorted(count_2.items()))

total = {}
for key in count_1:
    total[key] = count_1[key] + count_2[key]

print(f"\n")
print(f"total:{total}")

#Find the total number of wins for each team.

print("\n")


winner_count= {}


for team in cricket:
    team_name =(team["winner"])

    if team_name not in winner_count:
        winner_count[team_name] = 0

    winner_count[team_name] += 1

print(f"\nWinner:{winner_count}")

#Find and display all matches won by **India**

#print("\n")
for name, won in winner_count.items():
    if name == "India":
        print(f"Name:{name},\nWon: {won}")
        
#Find the team with the highest number of wins.

high = max(winner_count)
print(f"\n{high} is hightest numbers of wins")

#Find the team with the lowest number of wins.

low = min(winner_count)
print(f"\n{low} is lowest number of wins")

#Find the match with the highest total runs scored by both teams combined

total_runs = []
for row in cricket:
    runs = int(row["runs_team1"]) + int(row["runs_team2"]) , row["match_id"]

    total_runs.append(runs)
    high_runs = max(total_runs)

    low_runs = min(total_runs)

print(f"\nhighest total runs :{high_runs}")

#Find the match with the lowest total runs scored by both teams combined.

print(f"\nlowest total runs :{low_runs}")

#Find the highest score made by a single team in any match.

run1 = []
run2 = []

for row in cricket:
    score1 = row["runs_team1"],row["team1"]
    run1.append(score1)

print(sorted(run1))

for row in cricket:
    score2 = row["runs_team2"],row["team2"]
    run2.append(score2)

Max_run1 = max(run1)
Max_run2 = max(run2)


highest_score = Max_run2

if Max_run1 > Max_run2:
    highest_score = Max_run1

print(f"\nhighest score made by a single team :{highest_score}")


#13. Find the player who received **Player of the Match** award the highest number of times.

player_of_match_count = {}

for row in cricket:
    players = (row["player_of_match"])

    if players not in player_of_match_count:
        player_of_match_count[players] = 0

    player_of_match_count[players] += 1


print(player_of_match_count)

highest_player = max(player_of_match_count,key = player_of_match_count.get)
player_score = max(player_of_match_count.values())

print(f"\nPlayer of the match :{highest_player}, player_score:{player_score}")

#14. Display the number of Player of the Match awards received by each player.

print(f"\nPlayer of the match :{player_of_match_count}")

#15. Find the venue where the highest number of matches were played.

venue_count = {}

for team in cricket:
    venue_name = (team["venue"])

    if venue_name not in venue_count:
        venue_count[venue_name] = 0

    venue_count[venue_name] += 1


max_venue_name= max(venue_count,key=venue_count.get)
max_venue_count = max(venue_count.values())


print(f"\nVenue : {max_venue_name}\nCount : {max_venue_count}")

#16. Display the number of matches played at each venue.

print("\n")
print(venue_count)

#17. Find the top 5 highest-scoring matches based on the combined runs of both teams.

run1 = []
run2 = []

for row in cricket:
    score1 = row["runs_team1"],row["team1"]
    run1.append(score1)


for row in cricket:
    score2 = row["runs_team2"],row["team2"]
    run2.append(score2)

concate = run1 + run2

high_score = sorted(concate,reverse = True)
print('\n')

print(high_score)

print('\n')
print(f"Top 5 :\n{high_score[0:5]}")

#18. Find all matches where the winning team scored more than **300 runs**.

winner_count= {}


for team in cricket:
    team_name =(team["winner"])

    if team_name not in winner_count:
        winner_count[team_name] = 0

    winner_count[team_name] += 1

print(f"\nWinner:{winner_count}")