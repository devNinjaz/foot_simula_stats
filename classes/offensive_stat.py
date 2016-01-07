#!/usr/share/python
class Offensive_stat:
    def __init__ (self, team_name, shots_pg, shots_ot_pg, dribbles_pg, fouled_pg, rating):
        self.team_name = team_name
        self.shots_pg = float(shots_pg)
        self.shots_ot_pg = float(shots_ot_pg)
        self.dribbles_pg = float(dribbles_pg)
        self.fouled_pg = float(fouled_pg)
        self.rating = float(rating)

    def __str__ (self):
        return_string = self.team_name.ljust(30) + str(self.shots_pg).ljust(6) + str(self.shots_ot_pg).ljust(6) + str(self.dribbles_pg).ljust(6) 
        return_string += str(self.fouled_pg).ljust(6) + str(self.rating).ljust(6)
        return return_string 
