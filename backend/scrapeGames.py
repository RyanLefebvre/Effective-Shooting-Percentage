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
from selenium import webdriver
import selenium as se


class Game(object):
    date = ""
    home = ""
    away = ""
    league = ""
    season = ""
    homeOnePointGoals = 0
    homeTwoPointGoals = 0
    homeTotalShots = 0 
    homeEffectiveShootingPercentage =  0
    awayOnePointGoals = 0
    awayTwoPointGoals = 0
    awayTotalShots = 0
    awayEffectiveShootingPercentage = 0
    effectiveShootingDifference = 0
    gameURL = "" 
    
    def toString( self ): 
        return ( "\tDate: " + str(self.date) + "\n\tHome: " + str(self.home) + "\n\tAway: " +
                str(self.away) +"\n\tLeague: " + str(self.league) + "\n\tSeason: "  + str( self.season ) +
                "\n\tHomeOnePointGoals: " + str(self.homeOnePointGoals) +
                "\n\tHomeTwoPointGoals: " + str(self.homeTwoPointGoals) + 
                "\n\tHomeShots: " + str(self.homeTotalShots) + "\n\tHomeES%: " +
                str(self.homeEffectiveShootingPercentage) + 
                "\n\tAwayOnePointGoals: " + str(self.awayOnePointGoals) +
                "\n\tAwayTwoPointGoals: " + str(self.awayTwoPointGoals) + 
                "\n\tAwayEffectiveShootingPercentage: " + 
                str(self.awayEffectiveShootingPercentage) +
                "\n\tEfectiveShootingDifference: " +
                str(self.effectiveShootingDifference) + "\n\tgameURL: " +  str(self.gameURL) )
    
    def toRow(self): #placeholder 
        return [ str(self.date), self.home, self.away,
                self.effectiveShootingDifference, self.league, self.season,
                self.homeOnePointGoals, self.homeTwoPointGoals,
                self.homeTotalShots , self.homeEffectiveShootingPercentage, 
                self.awayOnePointGoals,
                self.awayTwoPointGoals,
                self.awayTotalShots, self.awayEffectiveShootingPercentage,
                self.gameURL]
    
def makeGame( date, home, away, league, homeOnePointGoals, 
             homeTwoPointGoals, homeTotalShots, homeEffectiveShootingPercentage,
             awayOnePointGoals, awayTwoPointGoals, awayTotalShots,
             awayEffectiveShootingPercentage, effectiveShootingDifference,
             gameURL , season ):
    newGame = Game()
    newGame.date = date
    newGame.home = home
    newGame.away = away
    newGame.league = league
    newGame.homeOnePointGoals = homeOnePointGoals
    newGame.homeTwoPointGoals = homeTwoPointGoals
    newGame.homeTotalShots = homeTotalShots
    newGame.homeEffectiveShootingPercentage = homeEffectiveShootingPercentage
    newGame.awayOnePointGoals = awayOnePointGoals
    newGame.awayTwoPointGoals = awayTwoPointGoals
    newGame.awayTotalShots = awayTotalShots
    newGame.awayEffectiveShootingPercentage = awayEffectiveShootingPercentage
    newGame.effectiveShootingDifference = effectiveShootingDifference
    newGame.gameURL = gameURL
    newGame.season = season
    return newGame

def isPLLPlayOffGame( gameURL ):
    return( gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190921_1.json" or 
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_ARC_ATL_20190921_1.json" or 
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ARC_20190914_1.json" or 
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_CHA_20190914_1.json" or
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_WHP_CHA_20190907_1.json" or 
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_CHR_ATL_20190907_1.json" or
            gameURL == "https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_ARC_20190906_1.json")

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
        season = ""
        if( isPLLPlayOffGame(game) ):
            season = "PLL Playoffs 2019"
        else:
            season = "PLL Regular Season 2019"
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
        homeEffectiveShootingPercentage =  calculator.getEffectiveShootingPercentage( homeOnePointGoals, homeTwoPointGoals, homeTotalShots)
       

        awayTwoPointGoals =  eval(gameJson['TeamStats']['AwayTeam']['TwoPointGoals'])
        awayTotalShots = eval(gameJson['TeamStats']['AwayTeam']['Shots'])
        awayOnePointGoals = ( eval(gameJson['BoxScoreOverview']['AwayTeamScores']['FinalScore']) - ( awayTwoPointGoals * 2))
        awayEffectiveShootingPercentage = calculator.getEffectiveShootingPercentage( awayOnePointGoals, awayTwoPointGoals, awayTotalShots)      
        effectiveShootingDifference = round( abs( homeEffectiveShootingPercentage - awayEffectiveShootingPercentage ) , 2 )
        gameURL = game
        newGame = makeGame( gameDate , homeTeam , awayTeam , "PLL" , homeOnePointGoals , homeTwoPointGoals , homeTotalShots , homeEffectiveShootingPercentage, 
                           awayOnePointGoals, awayTwoPointGoals, awayTotalShots , awayEffectiveShootingPercentage , effectiveShootingDifference , gameURL, season )
        print( "\n-------------------------\n" + newGame.toString() )
        gameList.append( newGame )
        
#helper method for scraping MLL games returns true if a team is 
#one of the teams whose city is two words in length, this is needed for the aray 
#called 'splitInfo' because it affects the offsets for the idx's to that array
def isTwoWordTeamName( teamName ):
    return ( teamName.upper() == 'YORK' or teamName.upper() == "JERSEY" or
                        teamName.upper() == "ANGELES" or
                        teamName.upper() ==  "FRANSICO" or 
                        teamName.upper() == "ISLAND" )

#returns the full MLL team name, assumes teamname will be in the form that gets 
# passed from splitInfo in scrape MLL games method 
def getTeamNameMLL( teamName ):
    if( teamName.upper() == "BOSTON" ):
        return "Boston Cannons"
    elif( teamName.upper() == "BALTIMORE"):
        return "Baltimore Bayhawks"
    elif( teamName.upper() == "ISLAND" ):
        return "Long Island Lizards"
    elif( teamName.upper() == "ROCHESTER" ):
        return "Rochester Rattlers"
    elif( teamName.upper() == "BRIDGEPORT"):
        return "Bridgeport Barrage"
    elif( teamName.upper() == "JERSEY" ):
        return "New Jersey Pride"
    elif( teamName.upper() == "PHILADELPHIA" ):
        return "Philadelphia Barrage"
    elif( teamName.upper() == "WASHINGTON" ):
        return "Washington Bayhawks"
    elif( teamName.upper() == "DENVER"):
        return "Denver Outlaws"    
    elif( teamName.upper() == "ANGELES"):
        return "Los Angeles Riptide"
    elif( teamName.upper() == "FRANSICO" ):
        return "San Fransico Dragons"
    elif( teamName.upper() == "CHICAGO"):
        return "Chicago Machine"
    elif( teamName.upper() == "TORONTO"):
        return "Toronto Nationals"
    elif( teamName.upper() == "CHESAPEAKE"):
        return "Chesapeake Bayhawks"
    elif( teamName.upper() == "HAMILTON"):
        return "Hamilton Nationals"
    elif( teamName.upper() == "CHAROLETTE"):
        return "Charolette Hounds" 
    elif( teamName.upper() == "OHIO"):
        return "Ohio Machine"
    elif( teamName.upper() == "FLORIDA"):
        return "FLORIDA LAUNCH"    
    elif( teamName.upper() == "YORK" ):
        return "New York Lizards" 
    elif( teamName.upper() == "ATLANTA"):
        return "Atlanta Blaze"
    elif( teamName.upper() == "DALLAS"):
        return "Dallas Rattlers"
    else:
        return teamName #failsafe
        
       
#helper method for scraping MLL data, process is a little different because 
# we have data for more than one season, first step is to get a list of 
# seasons we have data for, then for each game in a given season
#scrape the games data and add it to the game list 
def getMLLData( gameList ):
    print("\nScraping MLL Data")
    seasonList = getMLLSeasonList()
    seasonURL = "http://mll.stats.pointstreak.com/leagueschedule.html"    
    for season in seasonList: 
        options = se.webdriver.ChromeOptions()
        driver = se.webdriver.Chrome()
        driver.get( seasonURL + season )
        gameTable = driver.find_element_by_class_name('tablelines').get_attribute('innerHTML')
        fullPageSoup = BeautifulSoup( driver.page_source ,"lxml" )
        #need this to get the date 
        season = fullPageSoup.find('select' , {'name':'seasons'}).find('option',{'value':season}).text.strip()
        seasonSplit = season.split(" ")
        print("\n****************************************")
        print("Season: " + str( season) )
        print("****************************************")
        year = seasonSplit[len(seasonSplit)-1]
        gameTableSoup = BeautifulSoup( gameTable , "lxml" )
        gameURLs = []
        for gameRow in gameTableSoup.find_all('tr',{'class':'light'}):
            gameSheetParams = gameRow.find('td' , {'align':'center'} ).find('a') 
            dayMonthString = gameRow.find_all('td')[1].text
            dayMonthString = dayMonthString.split(" ")
            day = dayMonthString[2]
            month = getNumericMonth( dayMonthString[1] )
            date =  str(month) + "/" + str(day) + "/" + str(year)
            if( not( gameSheetParams == None ) ):
                gameURLs.append( gameSheetParams.get('href') )
        driver.close()
        for game in gameURLs:
            try:
                #get full html after js has been rendered inside beautiful soup object 
                gameSheetURL = "http://mll.stats.pointstreak.com/" + game
                driver = se.webdriver.Chrome()
                driver.get( gameSheetURL )
                gameSheetHTML = driver.page_source
                gameSheetSoup = BeautifulSoup( gameSheetHTML , "lxml" )
                driver.close()
                league = "MLL"
                gameURL = gameSheetURL
                gameInfo = gameSheetSoup.find('p',{'class':'gameinfo'})
                #scraping will be messy because of not many selectors    
                #spit info gets messed up with new york, need to refactor this to accomodate for
                #cities with names that are two words long 
                splitInfo = gameInfo.text.split( " " )    
                #filter out annoying empty strings 
                splitInfo = [ string for string in splitInfo if string != '' ]
                away = splitInfo[len(splitInfo)-2] 
                homeTeamIDX = len(splitInfo)-5
                homeGoalsIDX = len(splitInfo)-4
                awayGoalsIDX = len(splitInfo)-1
                if( isTwoWordTeamName(away) ): # new york messes up split info alg because it is two words long 
                    homeTeamIDX -= 1
                    homeGoalsIDX -= 1
                away = getTeamNameMLL( away )
                home = splitInfo[homeTeamIDX]     
                #remove time that may accidentally be appended to home team 
                home = home.replace("pm","")
                home = home.replace("am","")
                home = getTeamNameMLL(home)
                homeTotalGoals = eval(splitInfo[homeGoalsIDX])            
                awayTotalGoals = eval(splitInfo[awayGoalsIDX])
                allTables = gameSheetSoup.find_all('table')
                homeRoster = allTables[9]
                homeRoster = homeRoster.find_all('tr')
                homeTwoPointGoals = eval(homeRoster[len(homeRoster)-1].find_all('td')[3].text)
                homeTotalShots = eval(homeRoster[len(homeRoster)-1].find_all('td')[6].text)
                homeOnePointGoals = homeTotalGoals - ( 2 * homeTwoPointGoals )
                homeEffectiveShootingPercentage = calculator.getEffectiveShootingPercentage( homeOnePointGoals, homeTwoPointGoals, homeTotalShots) 
                awayRoster = allTables[11]
                awayRoster = awayRoster.find_all('tr')
                awayTwoPointGoals = eval(awayRoster[len(awayRoster)-1].find_all('td')[3].text)
                awayTotalShots = eval(awayRoster[len(awayRoster)-1].find_all('td')[6].text)
                awayOnePointGoals = awayTotalGoals - ( 2 * awayTwoPointGoals )
                awayEffectiveShootingPercentage = calculator.getEffectiveShootingPercentage( awayOnePointGoals, awayTwoPointGoals, awayTotalShots )
                effectiveShootingDifference = round( abs( homeEffectiveShootingPercentage - awayEffectiveShootingPercentage ) , 2 )
            
                newGame = makeGame( date, home, away, league , homeOnePointGoals,
                                   homeTwoPointGoals, homeTotalShots,
                                   homeEffectiveShootingPercentage,
                                   awayOnePointGoals, awayTwoPointGoals,
                                   awayTotalShots, awayEffectiveShootingPercentage,
                                   effectiveShootingDifference, gameURL, season)
                print( "\n-------------------------\n" + newGame.toString() )
            except Exception as e:
                print( "ERROR SCRAPING GAME: " + str(e) )
                print( "\n-------------------------\n")


#creates a mapping from seasons -> teams -> team win% for mll
                
                #ALSO A POSSIBILITY TO MANUALLY CALC FROM GAME LISTS!!!!
def getMLLWinPecentages():
    return   #http://mll.stats.pointstreak.com/playoffstandings.html?leagueid=323&seasonid=18576

#creates a mapping from seasons -> teams -> team win% for pll
def getPLLWInPercentages():
    return 

#performs a regression analysis on the list of game objects
# looks for a relationship between teams average ES%d and win%
def performRegressionAnalysis():
    return
                
        
#returns a list of query params that can be used to navigate to each season 
# the MLL has data for
def getMLLSeasonList():
    seasonList = []
    #start with an arbitrary season since they all contain the same select
    # element that has the list of seasons
    options = se.webdriver.ChromeOptions()
    driver = se.webdriver.Chrome()
    driver.get( "http://mll.stats.pointstreak.com/leagueschedule.html" )
    selectDiv = driver.find_element_by_class_name('proSeason')
    selectSoup = BeautifulSoup( selectDiv.get_attribute('innerHTML') ,"lxml" )
    for seasonOption in selectSoup.find_all('option'):
        value = seasonOption.get('value')
        #some options in list have values that are not query params, all 
        # query params we want start with a '?', this filters list 
        if( not( value == None ) and value[0] == '?' ):
            seasonList.append( value )
    driver.close()
    return seasonList
    
#exports the full list of 2019 professional lacrosse players to a csv file 
def exportGamesToCSV( gameList ):
    with open('games.csv' , 'w', newline='' ) as writeFile:
        writer = csv.writer( writeFile )
        rowList = []
        colHeaders = [ "DATE", "HOME", "AWAY", "ES%D", "LEAGUE", "SEASON",
                 "HOME 1PG", "HOME 2PG","HOME SHOTS", "HOME ES%",
                 "AWAY 1PG", "AWAY 2PG", "AWAY SHOTS","AWAY ES%",
                 "URL"] 
        rowList.append( colHeaders )
         
        for game in gameList:
            rowList.append( game.toRow() )      
        
        for row in rowList:
            writer.writerow(row)
            
        writeFile.close()
        
#helper method for construction of MLL dates, converts 3 letter month 
# abbreviation to numeric value so dates can be put in mm/dd/yyyy format 
def getNumericMonth( month ):
    month = month.lower()    
    if( month == "jan" ):
        return 1
    elif( month ==  "feb"):
        return 2
    elif( month ==  "mar"):
        return 3;
    elif( month ==  "apr"):
        return 4;
    elif( month ==  "may"):
        return 5;
    elif( month ==  "jun"):
        return 6;
    elif( month ==  "jul"):
        return 7
    elif( month ==  "aug"):
        return 8
    elif( month ==  "sep"):
        return 9
    elif( month ==  "oct"):
        return 10
    elif( month ==  "nov"):
        return 11
    elif( month == "dec" ):
        return 12
        
    
#  MAIN   ####################################################################
# this program scrapes game statisics from MLL and PLL websites to calculate
# ES% and ES%D for teams per game .
def main():
    try:
        gameList = []
        getPLLData( gameList )
        #getMLLData(gameList) 
        exportGamesToCSV( gameList )
    except Exception as e:
        print( "ERROR, PROGRAM TERMINATING\n" )
        print( e )
        
if __name__ == '__main__':
    main()