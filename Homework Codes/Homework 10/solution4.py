#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:25:20 2022

@author: emirtarikarici
"""

class Team:
    def __init__(self,team,matches,win,loss):
        self.team = team
        self.matches = matches
        self.win = win
        self.loss = loss
        self.draw = matches - (win + loss)
    
    def report(self):
        print("Team: ", self.team + ",",
              "Matches:", str(self.matches) + ",", 
              "Wins:", str(self.win) + ",",
              "Loses:", str(self.loss) + ",",
              "Draws:", str(self.draw))
        
if __name__ == "__main__":
    team_a = Team("Red Team", 6, 2, 2) 
    team_b = Team("Blue Team", 5, 3, 2)
    team_a.report()
    team_b.report()