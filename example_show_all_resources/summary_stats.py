#!/usr/bin/python
import re

# *************************************************************************************************
# *************************************************************************************************
class summary_stat:
    def __init__ (self, team_name, shots_pg, possession, pass_success, aerials_won, rating):
        self.team_name = team_name
        self.shots_pg = shots_pg
        self.possession = possession
        self.pass_success = pass_success
        self.aerials_won = aerials_won
        self.rating = rating

    def __str__ (self):
        return self.team_name.ljust(30) + self.shots_pg.ljust(7) + self.possession.ljust(7) + self.pass_success.ljust(7) + self.aerials_won.ljust(7) + self.rating.ljust(7)

# *************************************************************************************************
# *************************************************************************************************

## READING INPUT
f = open("stats_summary.txt", "r")
data = f.read()
f.close()

# \1 teamname
# \2 shots_pg 
# \3 discipline (IGNORED)
# \4 possiession
# \5 pass_success
# \6 aerials_won
# \7 rating
regex = r"([^0-9\t\n]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*([0-9]*[.]?[0-9]*)\s*[^\n]*\n"
regex = re.compile(regex)

summary_stats = []

for iter in regex.finditer(data):
    summary_stats.append(summary_stat(iter.group(1), iter.group(2), iter.group(4), iter.group(5), iter.group(6), iter.group(7)))

for stat in summary_stats:
    print stat
