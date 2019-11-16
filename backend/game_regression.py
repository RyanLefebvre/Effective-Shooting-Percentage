# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:33:01 2019

@author: Ryan
"""
import csv
import numpy
import regression_functions 
import regression_functions as regFunc 
import matplotlib.pyplot as plt
import scrape_MLL
import scrape_PLL 



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
    
    def toString(self): 
        return ( "\tDate: "  + str(self.date) +
                "\n\tHome: " + str(self.home) +
                "\n\tAway: " + str(self.away) +
                "\n\tLeague: " + str(self.league) +
                "\n\tSeason: "  + str( self.season ) +
                "\n\tHomeGoals: " + str( self.homeGoals())+ 
                "\n\tHome1PG: " + str( self.homeOnePointGoals)+
                "\n\tHome2PG: " + str( self.homeTwoPointGoals)+
                "\n\tHomeShots: " + str( self.homeTotalShots)+
                "\n\tHomeSh%: " + str( self.homeShootingPercentage())+
                "\n\tHomeSh%D: " + str( self.homeShootingPercentageDifference())+
                "\n\tHomeES%: " + str( self.homeEffectiveShootingPercentage)+
                "\n\tHomeES%D: " + str( self.homeShootingPercentageDifference())+
                "\n\tAwayGoals: " + str( self.awayGoals())+ 
                "\n\tAway1PG: " + str( self.awayOnePointGoals)+
                "\n\tAway2PG: " + str( self.awayTwoPointGoals)+
                "\n\tAwayShots: " + str( self.awayTotalShots)+
                "\n\tAwaySh%: " + str( self.awayShootingPercentage())+
                "\n\tAwaySh%D: " + str( self.awayShootingPercentageDifference())+
                "\n\tAwayES%: " + str( self.awayEffectiveShootingPercentage)+
                "\n\tAwayES%D: " + str( self.awayShootingPercentageDifference())+
                "\n\tABS(ES%D): " + str( self.effectiveShootingDifference)+
                "\n\tURL: " + str( self.gameURL))
    
    def toRow(self): 
        return [ #general
                self.date , self.home, self.away, self.league, self.season,
                #home
                self.homeGoals(), self.homeOnePointGoals, self.homeTwoPointGoals,
                self.homeTotalShots, self.homeShootingPercentage(), self.homeShootingPercentageDifference(),
                self.homeEffectiveShootingPercentage, self.homeEffectiveDifference(),
                #away
                self.awayGoals(), self.awayOnePointGoals, self.awayTwoPointGoals,
                self.awayTotalShots, self.awayShootingPercentage(), self.awayShootingPercentageDifference(),
                self.awayEffectiveShootingPercentage, self.awayEffectiveDifference(),      
                #general
                self.effectiveShootingDifference , self.gameURL]
        
    #helper methods for getting true true ES%D
    def homeEffectiveDifference(self):
        return round( self.homeEffectiveShootingPercentage - self.awayEffectiveShootingPercentage, 2 ) 
    
    def awayEffectiveDifference(self):
        return round( self.awayEffectiveShootingPercentage - self.homeEffectiveShootingPercentage , 2 )
    
    #heper methods for shooting percentage and shooting percentage difference
    def homeShootingPercentage(self):
        return round( ( self.homeOnePointGoals + self.homeTwoPointGoals ) / self.homeTotalShots , 2 ) 
    
    def awayShootingPercentage(self):
        return round( ( self.awayOnePointGoals + self.awayTwoPointGoals ) / self.awayTotalShots , 2 ) 
    
    def homeShootingPercentageDifference(self):
        return round(  self.homeShootingPercentage() - self.awayShootingPercentage() , 2 ) 

    def awayShootingPercentageDifference(self):
        return round(  self.awayShootingPercentage() - self.homeShootingPercentage() , 2 ) 

    #helper methods for calculating game score
    def homeWon(self):
        return self.homeGoals() > self.awayGoals()
    
    def awayWon(self):
        return not( self.homeWon() )
    
    def homeGoals(self):
        return self.homeOnePointGoals + ( 2 * self.homeTwoPointGoals )
    
    def awayGoals(self):
        return self.awayOnePointGoals + ( 2 * self.awayTwoPointGoals )
    
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

#function for calculating ES% 
def getEffectiveShootingPercentage( onePointGoals ,
                                   twoPointGoals , totalShotAttempts ):
    if( totalShotAttempts == 0 ):
        return 0 
    return round( ( onePointGoals + ( 2 * twoPointGoals ) ) /
                 totalShotAttempts , 2 ) 


#creates a mapping from teams -> seasons -> ( AES%D, AES%, szn win pct, ASh%, ASh%D )
def getTeamRegressionData( gameList ):
    #initial mapping built will be of form: 
        # teams -> seasons -> ( ES%DTotal , ES%Total, numWins , numGames ,Sh%Total, Sh%DTotal )
        # then we can divide ESDTotal / numGames to get average ESD
        # and we can divide numWins by numGames to get winpct 
    # teams -> seasons 
    teamDict = {}
    for game in gameList:
        
        ##########HOME##############
        #first check if team is in team list 
        if( not( game.home in teamDict.keys() ) ):
            #if not add team 
            teamDict[game.home] = {}          
        numHomeWins = 0
        if( game.homeWon() ):
            numHomeWins += 1 
        #check if this season has information yet 
        if( not( game.season in teamDict[game.home]) ):
            #if not then add season to the teams dictionary with default 
            # values 
            teamDict[game.home][game.season] = ( 
                    game.homeEffectiveDifference(),
                    game.homeEffectiveShootingPercentage,
                    numHomeWins,
                    1,
                    game.homeShootingPercentage(),
                    game.homeShootingPercentageDifference())
        else: # season has info so it needs to be updated 
            previous = teamDict[game.home][game.season] 
            teamDict[game.home][game.season] = ( 
                    previous[0] + game.homeEffectiveDifference(),      #ES%D Total 
                    previous[1] + game.homeEffectiveShootingPercentage,#ES% Total
                    previous[2] + numHomeWins,                         #NumWIns
                    previous[3] + 1,                                   #NumGames
                    previous[4] + game.homeShootingPercentage(),        #Sh%DTotal
                    previous[5] +  game.homeShootingPercentageDifference() )#Sh%DTotal                                   
        
        ##########AWAY##############
        #first check if team is in team list 
        if( not( game.away in teamDict.keys() ) ):
            #if not add team 
            teamDict[game.away] = {}          
        numAwayWins = 0
        if( game.awayWon() ):
            numAwayWins += 1 
        #check if this season has information yet 
        if( not( game.season in teamDict[game.away]) ):
            #if not then add season to the teams dictionary with default 
            # values 
            teamDict[game.away][game.season] = ( 
                    game.awayEffectiveDifference(),
                    game.awayEffectiveShootingPercentage,
                    numAwayWins,
                    1,
                    game.awayShootingPercentage(),
                    game.awayShootingPercentageDifference())
        else: # season has info so it needs to be updated 
            previous = teamDict[game.away][game.season] 
            teamDict[game.away][game.season] = ( 
                    previous[0] + game.awayEffectiveDifference(),
                    previous[1] + game.awayEffectiveShootingPercentage,
                    previous[2] + numAwayWins,
                    previous[3] + 1,                                  
                    previous[4] + game.awayShootingPercentage(),         
                    previous[5] +  game.awayShootingPercentageDifference() ) 

    
    #############CREATE FINAL MAPPING ###################
    # convert from: teams -> seasons -> ( ES%DTotal , ES%Total, numWins , numGames , Sh%Total , Sh%DTotal )
    # to: teams -> seasons -> ( AES%D , AES%, szn win pct , ASh% , ASh%D )
    for team in teamDict:
        for season in teamDict[team]:
            previousValue = teamDict[team][season]
            teamDict[team][season] =  ( 
                    round( previousValue[0] / previousValue[3]  , 2),
                    round( previousValue[1] / previousValue[3] , 2),
                    round( previousValue[2] / previousValue[3] , 2),
                    round( previousValue[4] / previousValue[3] , 2 ),
                    round( previousValue[5] / previousValue[3] , 2 ) )
    return teamDict
            
            
#performs a regression analysis on the list of game objects
# looks for a relationship between teams xValues and YValues
# depends on regression_functions.py
def performRegressionAnalysis( xValues , yValues, title ):
    regressionResults = ""
    plt.figure()
    regressionResults += "------------ Regression Analysis " + title + "-------------" 
    mbTuple = regFunc.compute_m_and_b( xValues , yValues )
    m = mbTuple[0]
    regressionResults += "\nm:\t " + str( round( m , 2 ) ) 
    b = mbTuple[1]
    regressionResults += "\nb:\t " + str( round( b , 2 ) )  
    fxResidTuple = compute_fx_residual( xValues , yValues , m, b )
    fx = fxResidTuple[0]
    r = compute_pearson_coefficient( xValues , yValues )
    regressionResults += "\nr:\t " + str( round( r , 2 ) ) 
    regressionResults += "\n\n  \t Analysis:\t " + interpretPearson( r)   
    regressionResults += "\n\n\n"
    #matplotlib stuff
    plt.plot( xValues , yValues , 'bo' )
    plt.plot( xValues , fx , 'red' )    
    plt.title(title)
    return regressionResults

# interprets pearsons r , determines strength of innear relationship 
# between two variables
def interpretPearson( r ):  
    direction = "Postive"
    if( r < 0 ):
        direction = "Negative"           
    r = abs( r )  
    strength = "Unknown"      
    if( r >= 0.00 and r <= 0.19 ):
        strength = "Very Weak"
    elif( r >= 0.20 and r <= 0.39):
        strength = "Weak"
    elif( r >= 0.40 and r <= 0.59):
        strength = "Moderate"
    elif( r >= 0.60 and r <= 0.79):
        strength = "Strong"
    elif( r >= 0.80 and r <= 1.0 ):
        strength = "Very Strong"
    
    return direction + " " + strength + " Relationship"

#expects a dictionary of the form returned from getTeamRegressionData()
# this method looks for a relationship between x: AES%D and y: Win%
def avgEffectDiffRegression( mappingDict ):
    xVals = []
    yVals = []
    for team in mappingDict:
        for season in mappingDict[team]:
            xVals.append(  mappingDict[team][season][0]  ) 
            yVals.append(  mappingDict[team][season][2]  )
    return performRegressionAnalysis( xVals , yVals, "AES%D vs WIN%" )

#expects a dictionary of the form returned from getTeamRegressionData()
# this method looks for a relationship between x: AES% and y: Win%
def avgEffectShootPercRegression( mappingDict ):
    xVals = []
    yVals = []
    for team in mappingDict:
        for season in mappingDict[team]:
            xVals.append(  mappingDict[team][season][1]  ) 
            yVals.append(  mappingDict[team][season][2]  )
    return performRegressionAnalysis( xVals , yVals, "AES% vs WIN%")
    

#expects a dictionary of the form returned from getTeamRegressionData()
# this method looks for a relationship between x: ASh% and y: Win%
def avgShootingPercRegression( mappingDict ):
    xVals = []
    yVals = []
    for team in mappingDict:
        for season in mappingDict[team]:
            xVals.append(  mappingDict[team][season][3]  ) 
            yVals.append(  mappingDict[team][season][2]  )
    return performRegressionAnalysis( xVals , yVals, "ASh% vs WIN%")
    

#expects a dictionary of the form returned from getTeamRegressionData()
# this method looks for a relationship between x: ASh%D and y: Win%
def avgShootingDiffRegression( mappingDict ):
    xVals = []
    yVals = []
    for team in mappingDict:
        for season in mappingDict[team]:
            xVals.append(  mappingDict[team][season][4]  ) 
            yVals.append(  mappingDict[team][season][2]  )
    return performRegressionAnalysis( xVals , yVals, "ASh%D vs WIN%")

    
#exports the full list of 2019 professional lacrosse players to a csv file 
def exportGamesToCSV( gameList ):
    with open('games.csv' , 'w', newline='' ) as writeFile:
        writer = csv.writer( writeFile )
        rowList = []
        colHeaders = [ "DATE", "HOME","AWAY", "LEAGUE","SEASON","HOMEGOALS",
                "HOME1PG", "HOME2PG", "HOMESHOTS", "HOMESh%","HomeSh%D",
                "HOMEES%","HomeES%D", "AwayGoals", "AWAY1PG","AWAY2PG",
                "AWAYSHOTS","AWAYSh%","AwaySh%D", "AwayES%", "AwayES%D", 
                "ABS(ES%D)","URL: " ] 
        rowList.append( colHeaders )
         
        for game in gameList:
            rowList.append( game.toRow() )      
        
        for row in rowList:
            writer.writerow(row)
            
        writeFile.close()
        
#exports data for each team by season, same data used to perform regr analysis
def exportTeamsToCSV( mappingDict ):
    with open('teams.csv' , 'w', newline='' ) as writeFile:
        writer = csv.writer( writeFile )
        rowList = []
        colHeaders = [ "TEAM", "SEASON", "AES%D",
                      "AES%", "AS%D", "AS%", "WIN%"] 
        rowList.append( colHeaders )
        for team in mappingDict:
            for season in mappingDict[team]:
                ts = mappingDict[team][season]
                rowList.append([team,season,ts[0],ts[1],ts[4],ts[3],ts[2]])
                    
        for row in rowList:
            writer.writerow(row)
            
        writeFile.close()
    
#exports regression results to text file, this way after program runs we 
#dont have to rely on the terminam output and will have a permanent 
#record of the regr analysis.    
def exportRegrResults( results ):
    file1 = open("RESULTS.txt","w")
    file1.write( results )
    file1.close()


            
#  MAIN   ####################################################################
# this program scrapes game statisics from MLL and PLL websites to calculate
# ES% and ES%D for teams per game .
def main():
    try:
        #scrape/calculate data
        gameList = []
        getPLLData( gameList )
        #getMLLData(gameList) 
        mappingDict = getTeamRegressionData( gameList )
        
        #perform analysis
        regressionResults = ""
            #Regression analysis between AES%D and Win % 
        regressionResults+= avgEffectDiffRegression( mappingDict )
            #Regression analysis between AES% and Win % 
        regressionResults+= avgEffectShootPercRegression( mappingDict )
            #Regression analysis between AS% and Win% 
        regressionResults+= avgShootingPercRegression( mappingDict )
            #Regression analysis between AS%D and Win% 
        regressionResults+= avgShootingDiffRegression( mappingDict )
        
        #export data for future use
        exportGamesToCSV( gameList )
        exportTeamsToCSV( mappingDict )
        exportRegrResults( regressionResults )
        
    except Exception as e:
        print( "ERROR, PROGRAM TERMINATING\n" )
        print( e )
        
if __name__ == '__main__':
    main()