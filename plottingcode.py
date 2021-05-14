#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:55:00 2021

@author: jacksoneddy
"""

import matplotlib.pyplot as plt
import math 
import xlrd
import pandas as pd
from scipy import signal
from scipy.fft import fftshift

loc1 = ("/Users/jacksoneddy/Desktop/A_spectrum2.xlsx")
wb1 = xlrd.open_workbook(loc1)
sheet1 = wb1.sheet_by_index(0)
wl=[]
flux=[]

def main():
    lambda_avg = 5896 #Angstrom
    
    for i in range (2, sheet1.nrows,1): #For loop used for finding redshifted peak
        wl.append(sheet1.cell_value(i, 0))
        flux.append(sheet1.cell_value(i, 1))
    
    
    plot1 = plt.figure(1)   
    plt.plot(wl,flux,"g")  
    plt.title('Wavelength vs Flux')     
    plt.xlabel("Wavelength (Angstrom)")
    plt.ylabel("Flux (Count)")
    
 ####################### FINDING D #########################
    data = pd.read_csv('/Users/jacksoneddy/Desktop/gw_data.txt', sep=" ", header=None)
    data.columns = ["t", "h"]
    time = data['t']
    h = data['h'] 
    
    h = h.to_numpy()
    print(h)
    fs = len(time)/(-time[0])

    plot2=plt.figure(2)
    f, t, Sxx = signal.spectrogram(h, fs)
    plt.pcolormesh(t, f, Sxx, shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Shear')
    plt.xlim([30,57])
    plt.ylim([0,500])


    

main()
