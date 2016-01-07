#!/usr/bin/python
import re
from classes.defensive_stat import Defensive_stat
from classes.statistic_obj import Statistic_obj

## READING INPUT
f = open("resources/stats_defensive.txt", "r")
data = f.read()
f.close()
print "Loaded data from resources/stats_defensive.txt" + "\n"
real_num = r"[0-9]*[.]?[0-9]*"

# \1 teamname
regex = r"([^0-9\t\n]*)\s*"
# \2 shots_pg 
regex += r"(" + real_num + r")\s*"
# \3 tackles_pg
regex += r"(" + real_num + r")\s*"
# \4 interceptions_pg
regex += r"(" + real_num + r")\s*"
# \5 fouls_pg
regex += r"(" + real_num + r")\s*"
# \6 offsides_pg
regex += r"(" + real_num + r")\s*"
# \7 rating
regex += r"(" + real_num + r")\s*\n"

regex = re.compile(regex)

defense_stats = []

for iter in regex.finditer(data):
    defense_stats.append(Defensive_stat(iter.group(1), iter.group(2), iter.group(3), iter.group(4), iter.group(5), iter.group(6), iter.group(7)))

shots_conceded_per_game, tackles_per_game, interceptions_per_game, fouls_per_game, offsides_per_game = [], [], [], [], []

for stat in defense_stats:
    shots_conceded_per_game.append(stat.shots_pg)
    tackles_per_game.append(stat.tackles_pg)
    interceptions_per_game.append(stat.interceptions_pg)
    fouls_per_game.append(stat.fouls_pg)
    offsides_per_game.append(stat.offsides_pg)

shots_conceded_per_game = Statistic_obj(shots_conceded_per_game)
tackles_per_game = Statistic_obj(tackles_per_game)
interceptions_per_game = Statistic_obj(interceptions_per_game)
fouls_per_game = Statistic_obj(fouls_per_game)
offsides_per_game = Statistic_obj(offsides_per_game)


print "Stats for 'shots conceded per game':"
print str(shots_conceded_per_game) + "\n"
print "Stats for 'tackles per game':"
print str(tackles_per_game) + "\n"
print "Stats for 'interceptions per game':"
print str(interceptions_per_game) + "\n"
print "Stats for 'fouls per game':"
print str(fouls_per_game) + "\n"
print "Stats for 'offsides per game':"
print str(offsides_per_game) + "\n"

# GENERATING CSV file
import csv
import sys

try:
    f = open("csv_data/defensive_stats.csv", "wt")
except IOError:
    print "Failed opening output file"
    sys.exit()

try:
    writer = csv.writer(f)
    writer.writerow(('Team name', 'Shots per game', 'Tackles per game', 'Interceptions per game', 'Fouls per game', 'Offsides per game', 'Rating'))
    for stat in defense_stats:
        writer.writerow((stat.team_name, stat.shots_pg, stat.tackles_pg, stat.interceptions_pg, stat.fouls_pg, stat.offsides_pg, stat.rating))
finally:
    f.close() 
    print "Statistics exported at csv_data/defensive_stats.csv"
