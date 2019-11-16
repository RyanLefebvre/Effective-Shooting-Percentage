# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:17:04 2019

@author: Ryan
"""

import game_regression 
import requests
from bs4 import BeautifulSoup
import json
import selenium as se
from selenium import webdriver

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
    

#helper method for correct season name, don't want separate seasons for 
#playoffs and regular season 
def getMLLSeason( seasonName ):
    trimmedSeason = seasonName.strip().upper()    
    if( trimmedSeason == "PLAYOFFS 2018" or
       trimmedSeason == "SUMMER 2018" ):
        return "MLL 2018"
    elif( trimmedSeason == "PLAYOFFS 2017" or
       trimmedSeason == "SUMMER 2017" ):
        return "MLL 2017"
    elif( trimmedSeason == "PLAYOFFS 2016" or
       trimmedSeason == "SUMMER 2016" ):
        return "MLL 2016"    
    elif( trimmedSeason == "PLAYOFFS 2015" or
       trimmedSeason == "SUMMER 2015" ):
        return "MLL 2015"    
    elif( trimmedSeason == "PLAYOFFS 2014" or
       trimmedSeason == "SUMMER 2014" ):
        return "MLL 2014"   
    elif( trimmedSeason == "PLAYOFFS 2013" or
       trimmedSeason == "SUMMER 2013" ):
        return "MLL 2013"    
    elif( trimmedSeason == "PLAYOFFS 2012" or
       trimmedSeason == "SUMMER 2012" ):
        return "MLL 2012"    
    elif( trimmedSeason == "PLAYOFFS 2011" or
       trimmedSeason == "SUMMER 2011" ):
        return "MLL 2011"       
    elif( trimmedSeason == "PLAYOFFS 2010" or
       trimmedSeason == "SUMMER 2010" ):
        return "MLL 2010"
    elif( trimmedSeason == "PLAYOFFS 2009" or
       trimmedSeason == "SUMMER 2009" ):
        return "MLL 2009"      
    elif( trimmedSeason == "PLAYOFFS 2008" or
       trimmedSeason == "SUMMER 2008" ):
        return "MLL 2008"         
    elif( trimmedSeason == "PLAYOFFS 2007" or
       trimmedSeason == "SUMMER 2007" ):
        return "MLL 2007"   
    elif( trimmedSeason == "PLAYOFFS 2006" or
       trimmedSeason == "SUMMER 2006" ):
        return "MLL 2006"
    elif( trimmedSeason == "PLAYOFFS 2005" or
       trimmedSeason == "SUMMER 2005" ):
        return "MLL 2005"  
    elif( trimmedSeason == "PLAYOFFS 2004" or
       trimmedSeason == "SUMMER 2004" ):
        return "MLL 2004"  
    elif( trimmedSeason == "PLAYOFFS 2003" or
       trimmedSeason == "SUMMER 2003" ):
        return "MLL 2003"  
    elif( trimmedSeason == "PLAYOFFS 2002" or
       trimmedSeason == "SUMMER 2002" ):
        return "MLL 2002"  
    elif( trimmedSeason == "PLAYOFFS 2001" or
       trimmedSeason == "SUMMER 2001" ):
        return "MLL 2001"  
    return trimmedSeason #failsafe

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
        regressionSeason = getMLLSeason( season ) 
        print("Season: " + str( season) + "\t->\t" + str(regressionSeason) )
        season = regressionSeason
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
                homeEffectiveShootingPercentage = getEffectiveShootingPercentage( homeOnePointGoals, homeTwoPointGoals, homeTotalShots) 
                awayRoster = allTables[11]
                awayRoster = awayRoster.find_all('tr')
                awayTwoPointGoals = eval(awayRoster[len(awayRoster)-1].find_all('td')[3].text)
                awayTotalShots = eval(awayRoster[len(awayRoster)-1].find_all('td')[6].text)
                awayOnePointGoals = awayTotalGoals - ( 2 * awayTwoPointGoals )
                awayEffectiveShootingPercentage = getEffectiveShootingPercentage( awayOnePointGoals, awayTwoPointGoals, awayTotalShots )
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


