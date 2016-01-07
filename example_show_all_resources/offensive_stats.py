#!/usr/bin/python
import re

# *************************************************************************************************
# *************************************************************************************************
class offensive_stat:
    def __init__ (self, team_name, shots_pg, shots_ot_pg, dribbles_pg, fouled_pg, rating):
        self.team_name = team_name
        self.shots_pg = shots_pg
        self.shots_ot_pg = shots_ot_pg
        self.dribbles_pg = dribbles_pg
        self.fouled_pg = fouled_pg
        self.rating = rating

    def __str__ (self):
        return_string = self.team_name.ljust(30) + self.shots_pg.ljust(6) + self.shots_ot_pg.ljust(6) + self.dribbles_pg.ljust(6) 
        return_string += self.fouled_pg.ljust(6) + self.rating.ljust(6)
        return return_string 

# *************************************************************************************************
# *************************************************************************************************

## READING INPUT
f = open("stats_offensive.txt", "r")
data = f.read()
f.close()

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
regex += r"(" + real_num + r")\s*"

# leftover trash, just in case
regex += r"[^\n]*\n"

regex = re.compile(regex)

offense_stats = []

for iter in regex.finditer(data):
    offense_stats.append(offensive_stat(iter.group(1), iter.group(2), iter.group(3), iter.group(4), iter.group(5), iter.group(6)))

for stat in offense_stats:
    print stat
