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
        return ( "Date: " + str(self.date) + "\tHome: " + str(self.home) + "\tAway: " +
                str(self.away) +"\tLeague: " + str(self.league) +
                "\tHomeOnePointGoals: " + str(self.homeOnePointGoals) +
                "\tHomeTwoPointGoals: " + str(self.homeTwoPointGoals) + 
                "\tHomeShots: " + str(self.homeTotalShots) + "\tHomeES%: " +
                str(self.homeEffectiveShootingPercentage) + 
                "\tAwayOnePointGoals: " + str(self.awayOnePointGoals) +
                "\tAwayTwoPointGoals: " + str(self.awayTwoPointGoals) + 
                "\tAwayEffectiveShootingPercentage: " + 
                str(self.awayEffectiveShootingPercentage) +
                "\tEfectiveShootingDifference: " +
                str(self.effectiveShootingDifference) + "\tgameURL: " +  str(self.gameURL) )
    
    def toRow(self): #placeholder 
        return [ str(self.date), self.home, self.away,
                self.effectiveShootingDifference, self.league,
                
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
             gameURL):
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
    print( "Scraping PLL Data" )
    gameJSONs = getListOfPLLGameJsons()
    for game in gameJSONs:
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
                           awayOnePointGoals, awayTwoPointGoals, awayTotalShots , awayEffectiveShootingPercentage , effectiveShootingDifference , gameURL )
        
        gameList.append( newGame )
        
       
#helper method for scraping MLL data, process is a little different because 
# we have data for more than one season, first step is to get a list of 
# seasons we have data for, then for each game in a given season
#scrape the games data and add it to the game list 
def getMLLData( gameList ):
    print("Scraping MLL Data")
    seasonList = getMLLSeasonList()
    seasonURL = "http://mll.stats.pointstreak.com/leagueschedule.html"    
    for season in seasonList: 
        options = se.webdriver.ChromeOptions()
        driver = se.webdriver.Chrome()
        driver.get( seasonURL + season )
        gameTable = driver.find_element_by_class_name('tablelines').get_attribute('innerHTML')
        fullPageSoup = BeautifulSoup( driver.page_source ,"lxml" )
        #need this to get the date 
        seasonSplit = fullPageSoup.find('select' , {'name':'seasons'}).find('option',{'value':season}).text.strip().split(" ")
    
        year = seasonSplit[len(seasonSplit)-1]
        print( "season Split " + str( seasonSplit) + "\n--------------------------\n" )
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
            #get full html after js has been rendered inside beautiful soup object 
            gameSheetURL = "http://mll.stats.pointstreak.com/" + game
            driver = se.webdriver.Chrome()
            driver.get( gameSheetURL )
            gameSheetHTML = driver.page_source
            gameSheetSoup = BeautifulSoup( gameSheetHTML , "lxml" )
            driver.close()
            #variables neeeded for a game that havent been taken care of     
            league = "MLL"
            gameURL = gameSheetURL
            gameInfo = gameSheetSoup.find('p',{'class':'gameinfo'})
            #scraping will be messy because of not many sleectors
            
            
            
            
            
            
            
            
            #spit info gets messed up with new york, need to refactor this to accomodate for
            #cities with names that are two words long 
            
            
            
            splitInfo = gameInfo.text.split( " " )    
            print( "SplitInfo is: " + str( splitInfo )  )
            home = splitInfo[len(splitInfo)-6]  
            #remove time informationthat may accidentally be appended to home team 
            home = home.replace("pm","")
            print( "Home is " + str(home) )
            homeTotalGoals = eval(splitInfo[len(splitInfo)-5])     
            away = splitInfo[len(splitInfo)-3] 
            awayTotalGoals = eval(splitInfo[len(splitInfo)-2])
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
                               effectiveShootingDifference, gameURL)
            print( "\n-------------------------\n" + newGame.toString() )
        
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
        colHeaders = [ "DATE", "HOME", "AWAY", "ES%D", "LEAGUE",
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
        #getPLLData( gameList ) 
        #exportGamesToCSV( gameList )
        getMLLData(gameList)    
    except Exception as e:
        print( "ERROR, PROGRAM TERMINATING\n" )
        print( e )
        
if __name__ == '__main__':
    main()