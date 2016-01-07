#!/usr/share/python
class Defensive_stat:
    def __init__ (self, team_name, shots_pg, tackles_pg, interceptions_pg, fouls_pg, offsides_pg, rating):
        self.team_name = team_name
        self.shots_pg = float(shots_pg)
        self.tackles_pg = float(tackles_pg)
        self.interceptions_pg = float(interceptions_pg)
        self.fouls_pg = float(fouls_pg)
        self.offsides_pg = float(offsides_pg)
        self.rating = float(rating)

    def __str__ (self):
        return_string = self.team_name.ljust(30) + str(self.shots_pg).ljust(6) + str(self.tackles_pg).ljust(6) + str(self.interceptions_pg).ljust(6) 
        return_string += str(self.fouls_pg).ljust(6) + str(self.offsides_pg).ljust(6) + str(self.rating).ljust(6)
        return return_string 
