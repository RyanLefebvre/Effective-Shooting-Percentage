# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:47:13 2019

@author: Ryan
"""
import requests

try:
    # goal of this program is to get and calulate EFG% for the 
    # 2019 MLL and PLL season
    pll_response = requests.get("https://dn0a11v09sa0t.cloudfront.net/SeasonTeamAndPlayersStats.json")
    print( pll_response.text )
except Exception as e:
    print( "ERROR, PROGRAM TERMINATING\n" )
    print( e )