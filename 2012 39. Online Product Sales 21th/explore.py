"""A simple exploration tool for the quantitative variables in order
to decide which variable to put in the logscale.

Copyright 2012, Emanuele Olivetti.
BSD license, 3 clauses.
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

if __name__ == '__main__':

    filename_train = 'data/TrainingDataset.csv'
    filename_test = 'data/TestDataset.csv'
    dataframe_train = pandas.read_csv(filename_train)
    dataframe_test = pandas.read_csv(filename_test)
    dataframe = pandas.concat([dataframe_train, dataframe_test])

    quantitative_columns = filter(lambda s: s.startswith("Quan"), dataframe.columns)

    # This is the list of variables to show in logscale:
    to_log = ["Quan_4", "Quan_5", "Quan_6", "Quan_7", "Quan_8", "Quan_9", "Quan_10", "Quan_11", "Quan_12", "Quan_13", "Quan_14", "Quan_15", "Quan_16", "Quan_17", "Quan_18", "Quan_19", "Quan_21", "Quan_22", "Quan_27", "Quan_28", "Quan_29", "Quant_22", "Quant_24", "Quant_25"]

    plt.figure()
    for i, col in enumerate(lst:=list(quantitative_columns)):
        a = dataframe[col]
        print(col, pandas.isnull(a).sum())
        plt.subplot(4,8,i+1)
        if col in to_log:
            a = np.log(a)
        try:
            a=np.array(a)
            a=a[~np.isnan(a)]
            plt.hist(a, bins=30, label=col)
            plt.legend()
        except:
            ...
    print(len(lst))

    plt.show() # If you are not into interactive mode you need this.
