# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
import pkgutil
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# pyplotモジュールを"plt"という名前でインポートする
import pandas as pd

def tax(average,a,b,count):

    if a==b:
        x = list(range(0,41,1) )# x座標
        y = count.flatten() # y座標
        plt.figure(figsize=[15,5])
        plt.xlabel("Number of cards that fell into the graveyard")
        plt.ylabel("Probability")
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
        plt.grid()
        plt.plot(x, y, color="k") # 点列(x,y)を黒線で繋いだプロット
        plt.show() # プロットを表示
        return
    x = list(range(a,b+1,1) )# x座標
    y = average # y座標

    plt.figure(figsize=[15,5])
    plt.xlabel("Creatures in the deck")
    plt.ylabel("Nexpected value")
    plt.xticks(np.arange(a,b+1,1))
    plt.yticks([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    plt.grid()
    plt.plot(x, y, color="k") # 点列(x,y)を黒線で繋いだプロット
    plt.show() # プロットを表示
    

    df = pd.DataFrame(count)

    fig, ax = plt.subplots(figsize=(15, 30))

    ax.axis('off')
    ax.axis('tight')
    plt.rcParams['font.family'] = 'Times New Roman'

    color = np.full_like(count, "", dtype=object)

    for i in range(len(count)):
        for j in range(len(count.T)):
            color[i, j] = 'white'

    for i in range(len(count)):
        for j in range(len(count.T)):
            if count[i, j] < count[i,j-1]:
                color[i, j-1] = 'yellow'
                break


    ax.table(cellText=np.round(df.values,1),
            colLabels=df.columns,
            rowLabels=np.arange(a,b+1,1),
            bbox=[0, 0, 1, 1],
            fontsize=1000,
            #loc="center",
            cellColours=color
            )

    plt.show()

    return