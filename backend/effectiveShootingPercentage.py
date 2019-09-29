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


#  MAIN   ####################################################################
# this program scrapes player statisics from MLL and PLL websites to calculate
# EFG for players and teams.
try:
    
    pll_response = requests.get("https://dn0a11v09sa0t.cloudfront.net/" + 
                                "SeasonTeamAndPlayersStats.json")
    pllSoup = BeautifulSoup( pll_response.text ,"lxml" ).find("p").text
    pllJson = json.loads( pllSoup )
    for team in pllJson['Teams']:
        print("--------------------------------------------------")
        print("Team Name:" + team['TeamName'])
        print( "Players:" )
        for player in team['Players']:
            print( "\t" + player['FirstName'] + " " + player['LastName'] + "\n")
        
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )