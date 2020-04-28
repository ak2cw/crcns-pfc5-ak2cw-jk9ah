# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import scipy.io
import matplotlib.pyplot as plt
import sys
import h5py
import numpy as np
from scipy.io import loadmat


def read_neuron_trial(fp): #returns the EEG data at different time points of exp
    d = fp['trial'] #get trials data
    numtimes = 0
    for x in d: #get number of time points
        o = x[0]
        y = fp[o][:]
        numtimes = len(y)
        break


    sums = np.zeros(numtimes) #array for collecting data from each trial

    for trial in d: #for every trial
        o = trial[0]
        trialdata = fp[o][:]
        for i in range(0, len(trialdata)): #for every time point
            row = trialdata[i]
            avg = np.mean(row[0:64])

            sums[i] = sums[i] + avg #adding the average of 64 electrode values to for each time point
    avgs = []
    avgs = sums/len(d) #the average electrode value at a given time point across all trials
    return avgs


def read_neuron_time(fp): #returns the time stamps for the EEG data
    d2 = fp['time']
    o2 = d2[0][0]
    timedata = fp[o2][:]
    return timedata


def getpersonavgs_ctrl(group, filep):

    allctrls = np.zeros(385) #number of time stamps

    if (group == 0): #if all control
        for i in range (1,21): #runs for all subjects
                if ( i < 10):
                    filepath = filep +  "ctrl0%s/data_derived.mat"%(i)
                if (i >= 10):
                    filepath = filep +  "ctrl%s/data_derived.mat"%(i)
                hf = h5py.File(filepath, 'r')

                #retrieves average trial data for encoding phase
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on each subject
                allctrls = allctrls + enctrialsavgs

        allctrls = allctrls/21 #average across all controls
        return allctrls, enctimes

    mctrls = np.zeros(385)
    if (group == 1):
        males = [3,4,5,7,8,9,10,12,13,16,20]
        for i in males: #runs for some subjects - males

                if ( i < 10):
                    filepath = filep +  "ctrl0%s/data_derived.mat"%(i)
                if (i >= 10):
                    filepath = filep +  "ctrl%s/data_derived.mat"%(i)
                hf = h5py.File(filepath, 'r')

                #retrieves average trial data for encoding phase
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on each subject
                mctrls = mctrls + enctrialsavgs

        mctrls = mctrls/11 #average across male controls
        return mctrls, enctimes

    fctrls = np.zeros(385)
    if(group == 2):
        females = [1,2,6,11,14,15,17,18,19]
        for i in females: #runs for some subjects - females

                if ( i < 10):
                    filepath = filep +  "ctrl0%s/data_derived.mat"%(i)
                if (i >= 10):
                    filepath = filep +  "ctrl%s/data_derived.mat"%(i)
                hf = h5py.File(filepath, 'r')

                #retrieves average trial data for encoding phase
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on every subject
                fctrls = fctrls + enctrialsavgs

        fctrls = fctrls/9 #average across female controls
        return fctrls, enctimes

    return 0,0



def getpersonavgs_pfc(group, filep):


    allpfcs = np.zeros(385)


    if (group == 0): #if all pfc
        for i in range (1,15): #runs for all subjects
            if ( i < 10):
                    filepath = filep +  "pfc0%s/data_derived.mat"%(i)
            if (i >= 10):
                    filepath = filep +  "pfc%s/data_derived.mat"%(i)
            hf = h5py.File(filepath, 'r')


            #retrieves average trial data for encoding phase
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on each subject
            allpfcs = allpfcs + enctrialsavgs

        allpfcs = allpfcs/14 #average across all pfc
        return allpfcs, enctimes

    mpfcs = np.zeros(385)
    if (group == 1):
        males = [2, 3, 4, 10, 11]
        for i in males: #runs for some subjects - males

            if ( i < 10):
                    filepath = filep + "pfc0%s/data_derived.mat"%(i)
            if (i >= 10):
                    filepath = filep + "pfc%s/data_derived.mat"%(i)
            hf = h5py.File(filepath, 'r')


            #retrieves average trial data for encoding phase
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on each person
            mpfcs = mpfcs + enctrialsavgs

        mpfcs = mpfcs/5 #average across male pfc
        return mpfcs, enctimes

    fpfcs = np.zeros(385)
    if(group == 2):
        females = [1, 5, 6, 7, 8, 9, 12, 13, 14]
        for i in females: #runs for some subjects - females

            if ( i < 10):
                    filepath = filep +  "pfc0%s/data_derived.mat"%(i)
            if (i >= 10):
                    filepath = filep +  "pfc%s/data_derived.mat"%(i)
            hf = h5py.File(filepath, 'r')


            #retrieves average trial data for encoding phase
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on each person
            fpfcs = fpfcs + enctrialsavgs

        fpfcs = fpfcs/9 #average across female pfc
        return fpfcs, enctimes

    return 0,0





