# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import scipy.io


import h5py
import numpy as np
from scipy.io import loadmat


def read_neuron_trial(fp): #returns the EEG data during one trial at different time points of exp
    d = fp['trial']
    o = d[0][0]
    trialdata = fp[o][:]
    return trialdata


def read_neuron_time(fp): #returns the time stamps for the EEG data
    d2 = fp['time']
    o2 = d2[0][0]
    timedata = fp[o2][:]
    return timedata


def read_neuron_trialinfo(fp): #returns information about trial - documented on CRCNS
    trialinfo = fp['trialinfo']
    return trialinfo



for i in range (1,4): #runs for subset of subjects
    filepath = '/Users/amrutha/crcns-pfc5-ak2cw-jk9ah/data/data_derived%s.mat' % (i)
    hf = h5py.File(filepath, 'r')


    #retrieves trial data for each stage of experiment
    enctrials = read_neuron_trial(hf['encmain'])
    pretrialtrials = read_neuron_trial(hf['pretrial'])
    proctrials = read_neuron_trial(hf['proc'])

    #retrieves time stamp data
    enctimes = read_neuron_time(hf['encmain'])
    pretrialtimes = read_neuron_time(hf['pretrial'])
    proctimes = read_neuron_time(hf['proc'])

    #retrieves trial info
    enctrialinfo = read_neuron_trialinfo(hf['encmain'])
    pretrialtrialinfo = read_neuron_trialinfo(hf['pretrial'])
    proctrialinfo = read_neuron_trialinfo(hf['proc'])


    #moving forward inside this for loop, what will we do with this data.
    #save the data as csv files or keep as data structures here and make other functions for analysis
    #will pick for a random set of control and pfc lesion patients
    #see if we can determine the difference between the groups - maybe using tensorflow machine learning






