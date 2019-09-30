# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:47:13 2019

@author: Ryan
"""
import requests
from bs4 import BeautifulSoup
import json


#Need to define player and team classes, create collection of these objects and 
# output so csv files 
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

def getEffectiveShootingPercentage( onePointGoals ,
                                   twoPointGoals , totalShotAttempts ):
    if( totalShotAttempts == 0 ):
        return 0 
    return ( onePointGoals + ( 1.5 * twoPointGoals ) ) / totalShotAttempts 

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
    
    def toString( self ):
        return ( "Name: " + self.firstName + " " + self.lastName +
                "\t League" + self.league  + "\tTeam: " + self.team +
                "\t Position " + self.position + "\t One Point Goals: " + 
                str(self.onePointGoals) + "\t Two Point Goals: " + str(self.twoPointGoals) + 
                "\t Shots: " + str(newPlayer.totalShotAttempts) + "\tES%: " + 
                "" )
    

    
#  MAIN   ####################################################################
# this program scrapes player statisics from MLL and PLL websites to calculate
# EFG for players and teams.
try:
    pll_response = requests.get("https://dn0a11v09sa0t.cloudfront.net/" + 
                                "SeasonTeamAndPlayersStats.json")
    pllSoup = BeautifulSoup( pll_response.text ,"lxml" ).find("p").text
    pllJson = json.loads( pllSoup )
    #contains a list of all players currently playing professional lacrosse 
    playerList = []
    for team in pllJson['Teams']:
        for player in team['Players']:
            
            print( "1: " +  str( player['OnePointGoals']))
            print( "2: " + str( player['TwoPointGoals'] ))
            print( "S: " + str( player['Shots' ] ) + "\n")
            #need to calc ES% , create player , store in list and print out to verify 
            

        
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )