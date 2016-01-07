#!/usr/bin/python
import re

# *************************************************************************************************
# *************************************************************************************************
class defensive_stat:
    def __init__ (self, team_name, shots_pg, tackles_pg, interceptions_pg, fouls_pg, offsides_pg, rating):
        self.team_name = team_name
        self.shots_pg = shots_pg
        self.tackles_pg = tackles_pg
        self.interceptions_pg = interceptions_pg
        self.fouls_pg = fouls_pg
        self.offsides_pg = offsides_pg
        self.rating = rating

    def __str__ (self):
        return_string = self.team_name.ljust(30) + self.shots_pg.ljust(6) + self.tackles_pg.ljust(6) + self.interceptions_pg.ljust(6) 
        return_string += self.fouls_pg.ljust(6) + self.offsides_pg.ljust(6) + self.rating.ljust(6)
        return return_string 

# *************************************************************************************************
# *************************************************************************************************

## READING INPUT
f = open("stats_defensive.txt", "r")
data = f.read()
f.close()

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
regex += r"(" + real_num + r")\s*"

# leftover trash, just in case
regex += r"[^\n]*\n"

regex = re.compile(regex)

defense_stats = []

for iter in regex.finditer(data):
    defense_stats.append(defensive_stat(iter.group(1), iter.group(2), iter.group(3), iter.group(4), iter.group(5), iter.group(6), iter.group(7)))

for stat in defense_stats:
    print stat
