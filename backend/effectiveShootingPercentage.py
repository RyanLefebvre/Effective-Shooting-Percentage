# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:47:13 2019

@author: Ryan
"""
import requests
from bs4 import BeautifulSoup
import json
import csv

#class for holding important information about a player 
class Player(object):
    firstName = ""
    lastName = ""
    team = ""
    league = ""
    position = ""
    onePointGoals = 0
    twoPointGoals = 0
    totalShotAttempts = 0
    effectiveShootingPercentage = 0.0
    
    # used for printing player to the console
    def toString( self ):
        return ( "Name: " + self.firstName + " " + self.lastName +
                "\t League: " + self.league  + "\tTeam: " + self.team +
                "\t Position: " + self.position + "\t One Point Goals: " + 
                str(self.onePointGoals) + "\t Two Point Goals: " + str(self.twoPointGoals) + 
                "\t Shots: " + str(self.totalShotAttempts) + "\tES%: " + 
                str( self.effectiveShootingPercentage) )
        
    #used to export the list of players to a csv    
    def toRow( self ):
        return [ self.lastName  ,  self.firstName  , self.league 
               ,  self.team  ,  self.position  ,  self.onePointGoals 
               ,  self.twoPointGoals  ,  self.totalShotAttempts,
               self.effectiveShootingPercentage ] 
        
#class for holding information about a team 
class Team(object):
    name = ""
    league = ""
    onePointGoals = 0
    twoPointGoals = 0
    totalShotAttempts = 0
    effectiveShootingPercentage = 0.0 
    roster = []
    
    def getEffectiveShots( self ):
        return self.effectiveShootingPercentage * self.totalShotAttempts
    
    def toString( self ):
        return ( "Name: " + self.name + "\t League: " + self.league  + 
                "\t One Point Goals: " + str(self.onePointGoals) + 
                "\t Two Point Goals: " + str(self.twoPointGoals) + 
                "\t Shots: " + str(self.totalShotAttempts) + "\tES%: " + 
                str( self.effectiveShootingPercentage) )    
        
    def toRow( self ):
        return [ self.name, self.league, self.onePointGoals,
                self.twoPointGoals, self.totalShotAttempts,
                self.effectiveShootingPercentage ]
        

#function for calculating ES% of a player
def getEffectiveShootingPercentage( onePointGoals ,
                                   twoPointGoals , totalShotAttempts ):
    if( totalShotAttempts == 0 ):
        return 0 
    return round( ( onePointGoals + ( 1.5 * twoPointGoals ) ) /
                 totalShotAttempts , 2 ) 

# creates and returns a new player object based on the arguments passed in as 
# parameters, calculates ES% for a player in the process
def makePlayer( firstName , lastName , team ,  onePointGoals,
               twoPointGoals , totalShotAttempts , league , position  ):
    newPlayer = Player() 
    newPlayer.firstName = firstName 
    newPlayer.lastName = lastName 
    newPlayer.team = team 
    newPlayer.onePointGoals = onePointGoals 
    newPlayer.twoPointGoals = twoPointGoals 
    newPlayer.totalShotAttempts = totalShotAttempts
    newPlayer.league = league
    newPlayer.position = position
    newPlayer.effectiveShootingPercentage = getEffectiveShootingPercentage(
            newPlayer.onePointGoals , newPlayer.twoPointGoals ,
            newPlayer.totalShotAttempts)
    return newPlayer 

def makeTeam( teamName , league ):
    newTeam = Team()
    newTeam.name = teamName
    newTeam.league = league
    return newTeam

#adds a player to the team if their team exists, otherwise a new team is 
# created and the player is added to the team 
def addPlayerToTeam( player , teamName  , teams ):
    # first check if the team does not already exist 
    if( not( teamName in teams.keys() )  ):
        # if not then make a new team
        teams[teamName] =  makeTeam( teamName , player.league ) 
    #add player to teams roster and update stats
    teams[teamName].roster.append( player )
    teams[teamName].onePointGoals += player.onePointGoals
    teams[teamName].twoPointGoals += player.twoPointGoals 
    teams[teamName].totalShotAttempts += player.totalShotAttempts
    
#gets data for all current PLL players and updates teamlist/playerlist to 
# include new data 
def getPLLData( playerList , teamDict ):
    pll_response = requests.get("https://dn0a11v09sa0t.cloudfront.net/" + 
                                "SeasonTeamAndPlayersStats.json")
    pllSoup = BeautifulSoup( pll_response.text ,"lxml" ).find("p").text
    pllJson = json.loads( pllSoup )
    for team in pllJson['Teams']:
       for player in team['Players']:
           newPlayer = ( makePlayer( 
                   player['FirstName'] , player['LastName'],
                   getFullPLLTeamName(player['TeamId']), player['OnePointGoals'], 
                   player['TwoPointGoals'] , eval(player['Shots']),
                   "PLL" , getFullPosition( player["Position"] ) ) )
           playerList.append( newPlayer )
           #figure out error
           addPlayerToTeam( newPlayer, newPlayer.team , teamDict )
    return

#gets data for all current MLL players and updates teamlist/playerlist to 
# include new data 
def getMLLData( playerList , teamDict ):
    mll_response = requests.get("https://iframe.faststats.online/iframes/" + 
                                "offense-stats-table-iframe.php")
    mllSoup = BeautifulSoup( mll_response.text ,"lxml" ).find("div" ,
                           {"id":"regular-season"}).find("table" ,
                           {"id":"player-table"}).find("tbody").findAll("tr") 
    for player in mllSoup:
        playerColumns = player.findAll("td")
        #name in MLL data is one column of form last , first 
        # remove comma and separate tokens 
        fixedNameList = playerColumns[0].text.split(",")
        firstName  = fixedNameList[0].strip()
        lastName = fixedNameList[1].strip()
        newPlayer = makePlayer( firstName , lastName , playerColumns[1].text ,
                   eval(playerColumns[6].text), eval(playerColumns[7].text) , 
                   eval(playerColumns[10].text), "MLL", getFullPosition( 
                           playerColumns[2].text ) )
        playerList.append( newPlayer )
        #need to fix the team name for the player if it lists multiple teams 
        if( len( newPlayer.team) > 3 ):
            #just grab the first team 
            newPlayer.team = newPlayer.team[0:3]
        newPlayer.team = getFullMLLTeamName( newPlayer.team )
        addPlayerToTeam( newPlayer , newPlayer.team , teamDict )      
    return

# converts a 3 letter team abbreviation to the temas full name 
def getFullPLLTeamName( abreviation ):
    abreviation = abreviation.lower()
    fullName = abreviation #default in case we dont know the team 
    #PLL team names 
    if( abreviation == "arc" ):
        fullName = "Archers"
    elif( abreviation == "atl"):
        fullName = "Atlas"
    elif( abreviation == "cha" ):
        fullName = "Chaos"
    elif( abreviation == "chr" ):
        fullName = "Chrome"
    elif( abreviation == "red" ):
        fullName = "Redwoods"
    elif( abreviation == "whp" ):
        fullName = "Whipsnakes"
        
    return fullName

# converts a 3 letter team abbreviation to the temas full name 
def getFullMLLTeamName( abreviation ):
    abreviation = abreviation.lower()
    fullName = abreviation #default in case we dont know the team     
    #MLL
    if( abreviation == "atl" ):
        fullName = "Blaze"
    elif( abreviation == "che"):
        fullName = "Bayhawks"
    elif( abreviation == "bos" ):
        fullName = "Cannons"
    elif( abreviation == "dal" ):
        fullName = "Rattlers"
    elif( abreviation == "den" ):
        fullName = "Outlaws"
    elif( abreviation == "nyl" ):
        fullName = "Lizards"
        
    return fullName



#converts position abreviations to full position names, if the position
# is not abreviated, then the original position is returned 
def getFullPosition( abreviation ):
    if( abreviation == "D" ):
        return "Defense"
    elif( abreviation == "A" ):
        return "Attack"
    elif( abreviation == "SSDM" or
         abreviation == "M" or
         abreviation == "FO" ):
        return "Midfield"
    elif( abreviation == "G" ):
        return "Goalie"
    elif( abreviation == "LSM" ):
        return "Long Stick Midfield" 
    return abreviation

#exports the full list of 2019 professional lacrosse players to a csv file 
def exportPlayersToCSV( playerList ):
    with open('players.csv' , 'w', newline='' ) as writeFile:
        writer = csv.writer( writeFile )
        rowList = []
        colHeaders = [ "LAST",  "FIRST" , "LEAGUE", "TEAM",
                      "POSITION", "1PG" , "2PG",
                      "SHOTS", "ES%" ] 
        rowList.append( colHeaders )
         
        for player in playerList:
            rowList.append( player.toRow() )      
        
        for row in rowList:
            writer.writerow(row)
            
        writeFile.close()
        
#exports known information about all teams from 2019 PLL and MLL season
def exportTeamsToCSV( teamList ):
    with open('teams.csv' , 'w', newline='' ) as writeFile:
        writer = csv.writer( writeFile )
        rowList = []
        colHeaders = [ "NAME",  "LEAUGE" , "1PG", "2PG",
                      "SHOTS", "ES%" ] 
        rowList.append( colHeaders )
        
        for team in teamList:
            rowList.append( team.toRow() )      
        
        for row in rowList:
            writer.writerow(row)
            
        writeFile.close()
        
        
        
#  MAIN   ####################################################################
# this program scrapes player statisics from MLL and PLL websites to calculate
# ES% for players and teams.
try:
    #contains a list of all players currently playing professional lacrosse 
    playerList = []
    teamDict  = {}
    print( " Grabbing PLL data ")
    getPLLData( playerList , teamDict )   
    #need to get MLL player data 
    print( " Grabbing MLL data ")
    getMLLData( playerList , teamDict )
    #still need to calc ES% for each team 
    for team in teamDict.keys():
        teamDict[team].effectiveShootingPercentage = getEffectiveShootingPercentage(
                 teamDict[team].onePointGoals, teamDict[team].twoPointGoals,
                 teamDict[team].totalShotAttempts )
    
    
    #sort list from lowest to highest Es%
    playerList.sort( key=lambda x: x.effectiveShootingPercentage, reverse=True)       
    exportPlayersToCSV( playerList )  
    exportTeamsToCSV( teamDict.values() )
    
   
    
# going to want to be able to calc ES% for games most likely 
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )