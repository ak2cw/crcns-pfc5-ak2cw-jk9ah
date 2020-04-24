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


def read_neuron_trial(fp): #returns the EEG data during one trial at different time points of exp
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

    allctrls = np.zeros(385)

    if (group == 0): #if all control
        for i in range (1,21): #runs for all subjects
                if ( i < 10):
                    filepath = filep +  "ctrl0%s/data_derived.mat"%(i)
                if (i >= 10):
                    filepath = filep +  "ctrl%s/data_derived.mat"%(i)
                hf = h5py.File(filepath, 'r')

                #retrieves trial data for each stage of experiment
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on every trial
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

                #retrieves trial data for each stage of experiment
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on every trial
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

                #retrieves trial data for each stage of experiment
                enctrialsavgs = read_neuron_trial(hf['encmain'])

                #retrieves time stamp data
                enctimes = read_neuron_time(hf['encmain'])

                #add on every trial
                fctrls = fctrls + enctrialsavgs

        fctrls = fctrls/9 #average across male controls
        return fctrls, enctimes

    return 0,0



def getpersonavgs_pfc(group):


    allpfcs = np.zeros(385)#231 for proc


    if (group == 0): #if all pfc
        for i in range (1,15): #runs for all subjects
            if ( i < 10):
                    filepath = filep +  "pfc0%s/data_derived.mat"%(i)
            if (i >= 10):
                    filepath = filep +  "pfc%s/data_derived.mat"%(i)
            hf = h5py.File(filepath, 'r')


            #retrieves trial data for each stage of experiment
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on every trial
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


            #retrieves trial data for each stage of experiment
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on every trial
            mpfcs = mpfcs + enctrialsavgs

        mpfcs = mpfcs/5 #average across all pfc
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


            #retrieves trial data for each stage of experiment
            enctrialsavgs = read_neuron_trial(hf['encmain'])

            #retrieves time stamp data
            enctimes = read_neuron_time(hf['encmain'])

            #add on every trial
            fpfcs = fpfcs + enctrialsavgs

        fpfcs = fpfcs/9 #average across all pfc
        return fpfcs, enctimes

    return 0,0




def main():

    filepath = sys.argv[1]


    cs, timec = getpersonavgs_ctrl(0, filepath) #run for controls#
    ps, timep = getpersonavgs_pfc(0, filepath) #run for pfc
    plt.plot(timec, cs)
    plt.plot(timep, ps)
    plt.savefig('control_pfc_avgs.png')

    plt.clf()
    plt.cla()
    plt.close() #reset plt


    mc, timec = getpersonavgs_ctrl(1, filepath) #run for male controls
    fc, timec = getpersonavgs_ctrl(2, filepath)# run for female controls
    plt.plot(timec, mc)
    plt.plot(timec,fc)
    plt.savefig('control_gender.png')

    plt.clf()
    plt.cla()
    plt.close() #reset plt

    mp, timec = getpersonavgs_pfc(1, filepath) #run for male pfcs
    fp, timec = getpersonavgs_pfc(2, filepath)# run for female pfcs
    plt.plot(timec, mp)
    plt.plot(timec,fp)
    plt.savefig('pfc_gender.png')

if __name__ == '__main__':
    main()






    #moving forward inside this for loop, what will we do with this data.
    #save the data as csv files or keep as data structures here and make other functions for analysis
    #will pick for a random set of control and pfc lesion patients
    #see if we can determine the difference between the groups - maybe using tensorflow machine learning






