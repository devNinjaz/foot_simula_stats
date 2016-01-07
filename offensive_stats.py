#!/usr/bin/python
import re
from classes.offensive_stat import Offensive_stat
from classes.statistic_obj import Statistic_obj
## READING INPUT
f = open("resources/stats_offensive.txt", "r")
data = f.read()
f.close()

print "Loaded data from resources/stats_offensive.txt" + "\n"
real_num = r"[0-9]*[.]?[0-9]*"

# \1 teamname
regex = r"([^0-9\t\n]*)\s*"
# \2 shots_pg 
regex += r"(" + real_num + r")\s*"
# \3 shots_ot
regex += r"(" + real_num + r")\s*"
# \4 dribbles_pg
regex += r"(" + real_num + r")\s*"
# \5 fouled_pg
regex += r"(" + real_num + r")\s*"
# \6  rating
regex += r"(" + real_num + r")\s*\n"

regex = re.compile(regex)

offense_stats = []

for iter in regex.finditer(data):
    offense_stats.append(Offensive_stat(iter.group(1), iter.group(2), iter.group(3), iter.group(4), iter.group(5), iter.group(6)))

shots_per_game, shots_ongoal_per_game, dribbles_per_game, fouled_per_game = [], [], [], []

for stat in offense_stats:
	shots_per_game.append(stat.shots_pg)
	shots_ongoal_per_game.append(stat.shots_ot_pg)
	dribbles_per_game.append(stat.dribbles_pg)
	fouled_per_game.append(stat.fouled_pg)

shots_per_game = Statistic_obj(shots_per_game)
shots_ongoal_per_game = Statistic_obj(shots_ongoal_per_game)
dribbles_per_game = Statistic_obj(dribbles_per_game)
fouled_per_game = Statistic_obj(fouled_per_game)

print "Stats for 'shots per game':"
print str(shots_per_game) + "\n"
print "Stats for 'shots on goal per game':"
print str(shots_ongoal_per_game) + "\n"
print "Stats for 'dribbles per game':"
print str(dribbles_per_game) + "\n"
print "Stats for 'fouled per game':"
print str(fouled_per_game) + "\n"

# GENERATING CSV file
import csv
import sys

try:
    f = open("csv_data/offensive_stats.csv", "wt")
except IOError:
    print "Failed opening output file"
    sys.exit()

try:
    writer = csv.writer(f)
    writer.writerow(('Team name', 'Shots per game', 'Shots on target per game', 'Dribbles per game', 'Fouled per game', 'Rating'))
    for stat in offense_stats:
        writer.writerow((stat.team_name, stat.shots_pg, stat.shots_ot_pg, stat.dribbles_pg, stat.fouled_pg))
finally:
    f.close()
    print "Statistics exported at csv_data/offensive_stats.csv"


