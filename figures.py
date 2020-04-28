from src import io
import sys
import matplotlib.pyplot as plt


def main():

    filepath = sys.argv[1] #take in the filepath to data folder


    cs, timec = io.getpersonavgs_ctrl(0, filepath) #run for controls
    ps, timep = io.getpersonavgs_pfc(0, filepath) #run for pfc
    plt.title('Average EEG Differences Between PFC-lesion Patients and Controls')
    plt.xlabel('Time Stamp (ms at 1024 sampling rate)')
    plt.ylabel('EEG Pre-Processed Data Value')
    plt.plot(timec, cs, label = "control")
    plt.plot(timep, ps, label = "PFC")
    plt.legend()
    plt.savefig('control_pfc_avgs.png')

    plt.clf()
    plt.cla()
    plt.close() #reset plt


    mc, timec = getpersonavgs_ctrl(1, filepath) #run for male controls
    fc, timec = getpersonavgs_ctrl(2, filepath)# run for female controls
    plt.title('Average EEG Differences Between Control Males and Females')
    plt.xlabel('Time Stamp (ms at 1024 sampling rate)')
    plt.ylabel('EEG Pre-Processed Data Value')
    plt.plot(timec, mc, label = "male")
    plt.plot(timec,fc, label = "female")
    plt.legend()
    plt.savefig('control_gender.png')

    plt.clf()
    plt.cla()
    plt.close() #reset plt

    mp, timec = getpersonavgs_pfc(1, filepath) #run for male pfcs
    fp, timec = getpersonavgs_pfc(2, filepath)# run for female pfcs
    plt.title('Average EEG Differences Between PFC Males and Females')
    plt.xlabel('Time Stamp (ms at 1024 sampling rate)')
    plt.ylabel('EEG Pre-Processed Data Value')
    plt.plot(timec, mp, label = "male")
    plt.plot(timec,fp, label = "female")
    plt.legend()
    plt.savefig('pfc_gender.png')

if __name__ == '__main__':
    main()