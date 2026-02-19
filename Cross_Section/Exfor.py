import os
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
import numpy as np

class Exfor:

    def __init__(self, exforFilePath):
        self.exforFilePath = exforFilePath

    def plotExforDataFromFilename(self, filename, setLegend=False, maxE=None):
        # try:
        E, dE, CS, dCS, authors =  self.retrieveDataFromFile(filename)
        authors = [str(a).strip() for a in authors if pd.notna(a) and str(a).strip() != ""]
        if maxE:
            E, dE, CS, dCS, authors = self.filterOnMaxEnergy(E, dE, CS, dCS, authors, maxE)
        unique_authors = []
        for auth in authors:
            if auth not in unique_authors:
                unique_authors.append(auth)
        colors = self.colors()

        for i in range(len(E)):
            for j in range(len(unique_authors)):
                if authors[i] == unique_authors[j]:
                    plt.errorbar(E[i], CS[i], marker='.', color=colors[j], markersize=1, linewidth=0.0001, xerr=dE[i], yerr=dCS[i], elinewidth=0.25, capthick=0.25, capsize=3.0, label=unique_authors[j])
                    if setLegend:
                        handles, labels = plt.gca().get_legend_handles_labels()
                        by_label = OrderedDict(zip(labels, handles))
                        plt.legend(by_label.values(), by_label.keys(),fontsize='small', loc='best')
        # except:
        #     print("No exfor file with filename: " + filename + " found, or exception occurred in retrieving the data " )
        #     pass

    def filterOnMaxEnergy(self, E, dE, CS, dCS, authors, max_energy):
        E = np.asarray(E); dE = np.asarray(dE)
        CS = np.asarray(CS); dCS = np.asarray(dCS)
        authors = np.asarray(authors)

        mask = E <= max_energy

        return (
            E[mask].tolist(),
            dE[mask].tolist(),
            CS[mask].tolist(),
            dCS[mask].tolist(),
            authors[mask].tolist()
        )
    
    def retrieveExforData(self, reaction, independent=True):
        if independent == True:
            filename = self.exforFilePath + reaction + '_ind.txt'
        elif independent == False:
            filename = self.exforFilePath + reaction + '_cum.txt'
        self.retrieveDataFromFile(filename)

    def retrieveDataFromFile(self, filename, unitCs=None):
        filename = self.exforFilePath + filename
        # TODO set max energy to take out some authors..... 
        with open(filename) as f:
            beginMark =   'EXFOR-ID'
            endMark   =   '//'
            content_full = f.readlines()
            ind_begin = [line for line in range(len(content_full)) if beginMark in content_full[line]][0]+1  # only one element but want it as integer
            ind_end   = [line for line in range(len(content_full)) if endMark in content_full[line]][0]  # list of different, only want the first element
            content = content_full[ind_begin:ind_end]
            E = []; dE=[]; CS = []; dCS=[]; author=[]
            for ind in range(len(content)):
                string= content[ind]
                string = (string.lstrip()).split()
                E.append(float(string[0]))
                dE.append(float(string[1]))
                CS.append(float(string[2])*1e3) # in mb
                dCS.append(float(string[3])*1e3) # in mb
                try:
                    author.append(string[5]) #index 4 is equal to
                except:
                    print(string[5], "not included in exfor data")
                    pass
        authors  = []
        for auth in author:
            if '+' in auth:
                authors.append(auth.replace('+', ''))
            else:
                authors.append(auth)
        if len(authors)!= 0:
            return E, dE, CS, dCS, authors

    def colors(self):
        # return ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
        # return [ 'crimson','cyan', 'forestgreen', 'palevioletred', 'darkorange', 'indianred', 'orchid', 'dodgerblue', 'lime','mediumpurple']
        return ['cyan', 'crimson', 'forestgreen', 'palevioletred', 'darkorange', 'indianred', 'orchid', 'dodgerblue', 'lime','mediumpurple',
                'cyan', 'crimson', 'forestgreen', 'palevioletred', 'darkorange', 'indianred', 'orchid', 'dodgerblue', 'lime','mediumpurple',
                'cyan', 'crimson', 'forestgreen', 'palevioletred', 'darkorange', 'indianred', 'orchid', 'dodgerblue', 'lime','mediumpurple']


