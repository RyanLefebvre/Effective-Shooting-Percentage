# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:16:04 2019

@author: Ryan
"""


import requests
from bs4 import BeautifulSoup
import json
import game_regression

# helper method for storing list of json objects that contain 
# info about PLL games, excludes All-Star game. Data for 37 games 
# between post season and regular season. No way to scrape to obtain 
# this list so this function is necessary 
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
    print( "Scraping PLL Data" )
    gameJSONs = getListOfPLLGameJsons()
    for game in gameJSONs:
        season = "PLL 2019"
        gameResponse = requests.get(game)
        gameSoup = BeautifulSoup( gameResponse.text ,"lxml" )
        gameJson = json.loads( gameSoup.text )
       
        gameDate = gameJson['timestamp'].split(" ")[0] #removes excess timestamp info
        homeTeam = gameJson['BoxScoreOverview']['HomeTeam']
        awayTeam = gameJson['BoxScoreOverview']['AwayTeam']
        homeTwoPointGoals = eval(gameJson['TeamStats']['HomeTeam']['TwoPointGoals'])
        homeTotalShots = eval(gameJson['TeamStats']['HomeTeam']['Shots'])
        #onepoint goals not listed but we can calc manually from final score
        # and # of two point goals
        homeOnePointGoals = ( eval(gameJson['BoxScoreOverview']['HomeTeamScores']['FinalScore']) - ( homeTwoPointGoals * 2))
        homeEffectiveShootingPercentage =  getEffectiveShootingPercentage( homeOnePointGoals, homeTwoPointGoals, homeTotalShots)
       
        awayTwoPointGoals =  eval(gameJson['TeamStats']['AwayTeam']['TwoPointGoals'])
        awayTotalShots = eval(gameJson['TeamStats']['AwayTeam']['Shots'])
        awayOnePointGoals = ( eval(gameJson['BoxScoreOverview']['AwayTeamScores']['FinalScore']) - ( awayTwoPointGoals * 2))
        awayEffectiveShootingPercentage = getEffectiveShootingPercentage( awayOnePointGoals, awayTwoPointGoals, awayTotalShots)      
        effectiveShootingDifference = round( abs( homeEffectiveShootingPercentage - awayEffectiveShootingPercentage ) , 2 )
        gameURL = game
        newGame = makeGame( gameDate , homeTeam , awayTeam , "PLL" , homeOnePointGoals , homeTwoPointGoals , homeTotalShots , homeEffectiveShootingPercentage, 
                           awayOnePointGoals, awayTwoPointGoals, awayTotalShots , awayEffectiveShootingPercentage , effectiveShootingDifference , gameURL, season )
        print( "\n-------------------------\n" + newGame.toString() )
        gameList.append( newGame )
        

