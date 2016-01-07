#!/usr/bin/python
import re
from classes.summary_stat import Summary_stat
from classes.statistic_obj import Statistic_obj
## READING INPUT
f = open("resources/stats_summary.txt", "r")
data = f.read()
f.close()
print "Loaded data from resources/stats_summary.txt" + "\n"

# \1 teamname
# \2 shots_pg 
# \3 discipline (IGNORED)
# \4 possiession
# \5 pass_success
# \6 aerials_won
# \7 rating
regex = r"([^0-9\t\n]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*\n"
regex = re.compile(regex)

summary_stats = []

for iter in regex.finditer(data):
    summary_stats.append(Summary_stat(iter.group(1), iter.group(2), iter.group(4), iter.group(5), iter.group(6), iter.group(7)))

shots_per_game, possession_per_game, pass_success, aerials_won = [], [], [], []

for stat in summary_stats:
   shots_per_game.append(stat.shots_pg)
   possession_per_game.append(stat.possession)
   pass_success.append(stat.pass_success)
   aerials_won.append(stat.aerials_won)

shots_per_game = Statistic_obj(shots_per_game)
possession_per_game = Statistic_obj(possession_per_game)
pass_success = Statistic_obj(pass_success)
aerials_won = Statistic_obj(aerials_won)

print "Stats for 'shots per game':"
print str(shots_per_game) + "\n"
print "Stats for 'possession per game':"
print str(possession_per_game) + "\n"
print "Stats for 'pass success':"
print str(pass_success) + "\n"
print "Stats for 'aerials won':"
print str(aerials_won) + "\n"

# GENERATING CSV file
import csv
import sys

try:
    f = open("csv_data/summary_stats.csv", "wt")
except IOError:
    print "Failed opening output file"
    sys.exit()

try:
    writer = csv.writer(f)
    writer.writerow(('Team name', 'Shots per game', 'Possession per game', 'Pass success per game', 'Rating'))
    for stat in summary_stats:
        writer.writerow((stat.team_name, stat.shots_pg, stat.possession, stat.pass_success, stat.aerials_won, stat.rating))
finally:
    f.close()
    print "Statistics exported at csv_data/summary_stats.csv"
