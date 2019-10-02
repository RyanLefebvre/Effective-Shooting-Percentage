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
        

#function for calculating ES% of a player
def getEffectiveShootingPercentage( onePointGoals ,
                                   twoPointGoals , totalShotAttempts ):
    if( totalShotAttempts == 0 ):
        return 0 
    return ( onePointGoals + ( 1.5 * twoPointGoals ) ) / totalShotAttempts 

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
    #round to two dec places 
    newPlayer.effectiveShootingPercentage = round( 
            newPlayer.effectiveShootingPercentage , 2 )
    return newPlayer 


def makeTeam( teamName , league ):
    newTeam = Team()
    newTeam.name = teamName
    newTeam.league = league
    return newTeam

def addPlayerToTeam( player , teamName  , teams ):
    # first check if the team does not already exist 
    if( teams[teamName] == None  ):
        # if not then make a new team
        teams[teamName] =  makeTeam( teamName , player.league ) 
    #add player to teams roster and update stats
    teams[teamName].roster.append( player )
    teams[teamName].onePointGoals += player.onePointGoals
    teams[teamName].twoPointGoals += player.twoPointGoals 
    teams[teamName].totalShotAttempts += player.totalShotAttempts
    
    ##STILL NEED TO CALCULATE ES% FOR THIS TO WORK
    
    # now add player to the teams roster and update the teams stats 
    listOfTeams

def getPLLPlayerData( playerList , teamDict ):
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
           addPlayerToTeam( newPlayer, newPlayer.team , teamDict )
    return

def getMLLData( playerList ):
    return

    
#  MAIN   ####################################################################
# this program scrapes player statisics from MLL and PLL websites to calculate
# EFG for players and teams.
try:
    
    #contains a list of all players currently playing professional lacrosse 
    playerList = []
    teamDict  = {}
    getPLLPlayerData( playerList , teamDict )      
    
##################  need to get stats for MLL, then iterate through all players and construct #####################################
################### stats for teams , based on this see if we can predict who wins games  ######################################### 
    
    
    #sort list from lowest to highest Es%
    playerList.sort( key=lambda x: x.effectiveShootingPercentage )       
    #print Players test
    for pllPlayer in playerList:
        print( pllPlayer.toString() )
        print("\n----------------------------------\n")
           

        
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )