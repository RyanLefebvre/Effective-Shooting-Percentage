# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:40:53 2018

@author: anarayan
"""

# functions for linear reqression
import math

def compute_sum_of_squared(values):
    sum_squared = 0
    for i in values:
        sum_squared = sum_squared + i**2
    return(sum_squared)
    
def compute_sxy(xvalues, yvalues):
    sxy = 0
    for index in range(len(xvalues)):
        sxy = sxy + xvalues[index] * yvalues[index]
    return(sxy)
    
def compute_m_and_b(xvalues, yvalues):
    n = len(xvalues)
    m_numerator = (sum(xvalues) * sum(yvalues)) - (compute_sxy(xvalues, yvalues) * n)
    m_denominator = (sum(xvalues)**2) - (compute_sum_of_squared(xvalues) * n)
    m = m_numerator/m_denominator
    b = (sum(yvalues) - (sum(xvalues) * m))/n
    return(m, b)
    
def compute_fx_residual(xvalues, yvalues, m, b):
    fx = []
    residual = []
    for index in range(len(xvalues)):
        new_y = m * xvalues[index] + b
        fx.append(new_y)
        residual.append(yvalues[index] - fx[index])
    
    rcoeff = 0
    for r in residual:
        rcoeff = rcoeff + r**2
    
    return(fx, residual)
    
def compute_sum_of_squared_residuals(residual):
    rcoeff = 0
    for r in residual:
        rcoeff = rcoeff + r**2
    return(rcoeff)
    
def compute_total_sum_of_squares(yvalues):
    ymean = sum(yvalues)/len(yvalues)
    rsum = 0
    for y in yvalues:
        rsum = rsum + ((y - ymean)**2)
    return(rsum)
    
def compute_pearson_coefficient(xvalues, yvalues):
    n = len(xvalues)
    sxy = compute_sxy(xvalues, yvalues)
    numerator = sxy - ((sum(xvalues) * sum(yvalues))/n)
    sxx = compute_sum_of_squared(xvalues)
    syy = compute_sum_of_squared(yvalues)
    denominator = math.sqrt((sxx - (sum(xvalues)**2)/n)) * math.sqrt((syy - (sum(yvalues)**2)/n))
    pearson_r = numerator/denominator
    return(pearson_r)
    
def compute_pearson_coefficient_alternate(xvalues, yvalues):
    #uses a different formula that uses mean values
    #this is just to verify that my results for the other one were accurate!
    xmean = sum(xvalues)/len(xvalues)
    ymean = sum(yvalues)/len(yvalues)
    numerator = 0
    xdiffs = 0
    ydiffs = 0
    for i in range(len(xvalues)):
        xydiff = (xvalues[i] - xmean) * (yvalues[i] - ymean)
        numerator = numerator + xydiff
        xdiffs = xdiffs + ((xvalues[i] - xmean) ** 2)
        ydiffs = ydiffs + ((yvalues[i] - ymean) ** 2)        
    denominator = math.sqrt(xdiffs) * math.sqrt(ydiffs)
    pearson_r = numerator/denominator
    return(pearson_r)
