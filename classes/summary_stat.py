#!/usr/share/python
class Summary_stat:
    def __init__ (self, team_name, shots_pg, possession, pass_success, aerials_won, rating):
        self.team_name = team_name
        self.shots_pg = float(shots_pg)
        self.possession = float(possession)
        self.pass_success = float(pass_success)
        self.aerials_won = float(aerials_won)
        self.rating = float(rating)

    def __str__ (self):
        return self.team_name.ljust(30) + str(self.shots_pg).ljust(7) + str(self.possession).ljust(7) + str(self.pass_success).ljust(7) + str(self.aerials_won).ljust(7) + str(self.rating).ljust(7)
