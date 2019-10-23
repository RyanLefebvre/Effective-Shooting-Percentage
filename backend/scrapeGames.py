# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:33:01 2019

@author: Ryan
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import scrapePlayersAndTeams as calculator

class Game(object):
    date = ""
    home = ""
    away = ""
    league = ""
    homeOnePointGoals = 0
    homeTwoPointGoals = 0
    homeTotalShots = 0 
    homeEffectiveShootingPercentage =  0
    awayOnePointGoals = 0
    awayTwoPointGoals = 0
    awayTotalShots = 0
    awayEffectiveShootingPercentage = 0
    effectiveShootingDifference = 0
    gameJsonURL = "" 
    
    def toString( self ): 
        return ( "Date: " + str(self.date) + "\tHome: " + str(self.home) + "\tAway: " +
                str(self.away) +"\tLeague: " + str(self.league) +
                "\tHomeOnePointGoals: " + str(self.homeOnePointGoals) +
                "\tHomeTwoPointGoals: " + str(self.homeTwoPointGoals) + 
                "\tHomeShots: " + str(self.homeTotalShots) + "\tHomeES%: " +
                str(self.homeEffectiveShootingPercentage) + 
                "\tAwayOnePointGoals: " + str(self.awayOnePointGoals) +
                "\tAwayTwoPointGOals: " + str(self.awayTwoPointGoals) + 
                "\tAwayEffectiveShootingPercentage: " + 
                str(self.awayEffectiveShootingPercentage) +
                "\tEfectiveShootingDifference: " +
                str(self.effectiveShootingDifference) + "\tGameJsonURL: " +  str(self.gameJsonURL) )
    
    def toRow(self): #placeholder 
        return []
    
def makeGame( date, home, away, league, homeOnePointGoals, 
             homeTwoPointGoals, homeTotalShots, homeEffectiveShootingPercentage,
             awayOnePointGoals, awayTwoPointGoals, awayTotalShots,
             awayEffectiveShootingPercentage, effectiveShootingDifference,
             gameJsonURL):
    newGame = Game()
    newGame.date = date
    newGame.home = home
    newGame.homeOnePointGoals = homeOnePointGoals
    newGame.homeTwoPointGoals = homeTwoPointGoals
    newGame.homeTotalShots = homeTotalShots
    newGame.homeEffectiveShootingPercentage
    newGame.awayOnePointGoals = awayOnePointGoals
    newGame.awayTwoPointGoals = awayTwoPointGoals
    newGame.awayEffectiveShootingPercentage = awayEffectiveShootingPercentage
    newGame.effectiveShootingDifference = effectiveShootingDifference
    newGame.gameJsonURL = gameJsonURL
    return newGame

# helper method for storing list of json objects that contain 
# info about PLL games, excludes All-Star game. Data for 37 games 
# between post season and regular season 
def getListOfPLLGameJsons():
    return [
######### PLAY OFFS   ##########
#Week 13
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190921_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_ATL_20190921_1.json",
#Week 12
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ARC_20190914_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_CHA_20190914_1.json",
#Week 11 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_CHA_20190907_1.json", 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ATL_20190907_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_ARC_20190906_1.json",            
########REGULAR SEASON##########
#Week 10 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_ARC_20190825_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_CHR_20190825_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ATL_CHA_20190824_1.json",
#Week 9 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_RED_20190818_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ATL_20190817_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_ARC_20190817_1.json",
#Week 8 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_ATL_20190811_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_WHP_20190810_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_CHA_20190810_1.json",
#Week 7 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_CHR_20190728_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_WHP_20190727_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ATL_RED_20190727_1.json",
#Week 6 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_CHA_20190707_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ATL_WHP_20190706_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_RED_20190706_1.json",
#Week 5
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190629_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_CHR_20190629_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ATL_ARC_20190628_1.json",
#Week 4 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_CHA_20190623_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_ATL_20190622_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_RED_20190622_1.json",
#Week 3 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ATL_20190616_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_WHP_20190615_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_RED_20190615_1.json",
#Week 2 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_ATL_20190609_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_ARC_20190608_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_CHR_20190608_1.json",
#Week 1 
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_ATL_20190602_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHA_WHP_20190601_1.json",
"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ARC_20190601_1.json",
]

#gets data from PLL website for games and stores data in the game List 
def getPLLData( gameList ):
    gameJSONs = getListOfPLLGameJsons()
    for game in gameJSONs:
        gameResponse = requests.get(game)
        gameSoup = BeautifulSoup( gameResponse.text ,"lxml" )
        gameJson = json.loads( gameSoup.text )
       
        gameDate = gameJson['timestamp'].split(" ")[0] #removes excess timestamp info
        homeTeam = gameJson['BoxScoreOverview']['HomeTeam']
        awayTeam = gameJson['BoxScoreOverview']['AwayTeam']
        league = "PLL"
        homeTwoPointGoals = eval(gameJson['TeamStats']['HomeTeam']['TwoPointGoals'])
        homeTotalShots = eval(gameJson['TeamStats']['HomeTeam']['Shots'])
        #onepoint goals not listed but we can calc manually from final score
        # and # of two point goals
        homeOnePointGoals = ( eval(gameJson['BoxScoreOverview']['HomeTeamScores']['FinalScore']) - ( homeTwoPointGoals * 2))
        homeEffectiveShootingPercentage =  calculator.getEffectiveShootingPercentage( homeOnePointGoals, homeTwoPointGoals, homeTotalShots)
       

        awayTwoPointGoals =  eval(gameJson['TeamStats']['AwayTeam']['TwoPointGoals'])
        awayTotalShots = eval(gameJson['TeamStats']['AwayTeam']['Shots'])
        awayOnePointGoals = ( eval(gameJson['BoxScoreOverview']['AwayTeamScores']['FinalScore']) - ( awayTwoPointGoals * 2))
        awayEffectiveShootingPercentage = calculator.getEffectiveShootingPercentage( awayOnePointGoals, awayTwoPointGoals, awayTotalShots)      
        effectiveShootingDifference = abs( homeEffectiveShootingPercentage - awayEffectiveShootingPercentage )
        gameJsonURL = game
        
        newGame = makeGame( gameDate , homeTeam , awayTeam , league , homeOnePointGoals , homeTwoPointGoals , homeTotalShots , homeEffectiveShootingPercentage, 
                           awayOnePointGoals, awayTwoPointGoals, awayTotalShots , awayEffectiveShootingPercentage , effectiveShootingDifference , gameJsonURL )
        print( newGame.toString())
    
    
#  MAIN   ####################################################################
# this program scrapes game statisics from MLL and PLL websites to calculate
# ES% and ES%D for teams per game .
try:
    gameList = []
    getPLLData( gameList ) 
    
    #MLL DATA IS IN PDF FORMAT, need to figure out how to deal w/ this 
        
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )