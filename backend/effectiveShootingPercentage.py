# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:47:13 2019

@author: Ryan
"""
import requests
from bs4 import BeautifulSoup
import json


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
    
    
    
    def toString( self ):
        return ( "Name: " + self.firstName + " " + self.lastName +
                "\t League: " + self.league  + "\tTeam: " + self.team +
                "\t Position: " + self.position + "\t One Point Goals: " + 
                str(self.onePointGoals) + "\t Two Point Goals: " + str(self.twoPointGoals) + 
                "\t Shots: " + str(self.totalShotAttempts) + "\tES%: " + 
                str( self.effectiveShootingPercentage) )
        
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
    

def getPLLData( playerList , teamDict ):
    pll_response = requests.get("https://dn0a11v09sa0t.cloudfront.net/" + 
                                "SeasonTeamAndPlayersStats.json")
    pllSoup = BeautifulSoup( pll_response.text ,"lxml" ).find("p").text
    pllJson = json.loads( pllSoup )
    for team in pllJson['Teams']:
       for player in team['Players']:
           newPlayer = ( makePlayer( 
                   player['FirstName'] , player['LastName'],
                   player['TeamId'], player['OnePointGoals'], 
                   player['TwoPointGoals'] , eval(player['Shots']),
                   "PLL" , player["Position"] ))
           playerList.append( newPlayer )
           #figure out error
           addPlayerToTeam( newPlayer, newPlayer.team , teamDict )
    return

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
                   eval(playerColumns[10].text), "MLL", playerColumns[2].text)
        playerList.append( newPlayer )
        addPlayerToTeam( newPlayer , newPlayer.team , teamDict )      
    return

    
#  MAIN   ####################################################################
# this program scrapes player statisics from MLL and PLL websites to calculate
# EFG for players and teams.
try:
    
    #contains a list of all players currently playing professional lacrosse 
    playerList = []
    teamDict  = {}
    print( " Grabbing PLL data ")
    getPLLData( playerList , teamDict )   
    #need to get MLL player data 
    print( " Grabbing  MLL data ")
    getMLLData( playerList , teamDict )
    #still need to calc ES% for each team 
    for team in teamDict.keys():
        teamDict[team].effectiveShootingPercentage = getEffectiveShootingPercentage(
                 teamDict[team].onePointGoals, teamDict[team].twoPointGoals,
                 teamDict[team].totalShotAttempts )
    
##################  need to get stats for MLL, then iterate through all players and construct #####################################
################### stats for teams , based on this see if we can predict who wins games  ######################################### 
    
    
    #sort list from lowest to highest Es%
    #playerList.sort( key=lambda x: x.effectiveShootingPercentage )       
    #for pllPlayer in playerList:
        #print( pllPlayer.toString() )
        #print("\n----------------------------------\n")
    
    
    #need to fix weird team names for players on multiple teams and 
    # need to add checks to put the names to the real teams 
    for key in teamDict.keys():
        print( teamDict[key].toString() )
        print("\n----------------------------------\n")
           

    # going to want to be able to calc ES% for games most likely 
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )