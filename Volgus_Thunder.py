# -*- coding: utf-8 -*-
import random
import Volgus_graph
import numpy as np


def tax(X):
    a=X[0] #クリーチャーの下限枚数
    b=X[1] #クリーチャーの上限枚数
    c=X[2] #試行回数
    d=X[3] #デッキ枚数
    
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    cemetery=np.zeros((b-a+1,c))
    average=np.zeros(b-a+1)
    i=0
    j=0
    count=np.zeros((b-a+1,41)) #横墓地に置かれたカード枚数、縦クリーチャー枚数
    i=0
    j=0
    k=0
    m=0
    p=0
    q=0

    for q in range(a,b+1): #下限a〜上限b枚数までループ　q=クリーチャー枚数

        for p in range(c): #任意試行回数c回ループ　p=今の試行回数
            l = list(range(1,d+1,1)) #1~dのd枚のデッキを作成
            random.shuffle(l) #デッキをシャッフル

            i=0 #ループ回数
            j=0 #クリーチャーのめくれた枚数

            for r in l[0:d]: #デッキの要素0~d-1までループさせる r=今めくったカードの数字
                i=i+1 #ループ回数（墓地に置かれた枚数）を記憶
                if r<=q: #今めくったカードの数字がクリーチャー枚数より少ないとき
                    j=j+1 #クリーチャーを捲った枚数+1する
                if j==2: #クリーチャーを2枚捲ったら
                    break #ループを抜ける

            for s in range(0,41): #墓地に落ちた枚数事にカウント
                if i==s:
                    count[q-a,s]=count[q-a,s]+1
                if p==c-1:
                    count[q-a,s]=count[q-a,s]*100/c
                
            cemetery[q-a,p]=i #今回の試行で捲った枚数を格納
            k=k+i #平均値計算用

        average[m]=k/c
        m=m+1
        k=0
        
    graph=Volgus_graph.tax(average,a,b,count)
    return average