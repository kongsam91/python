#%%

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit #fitting 用的



#Lorention fitting
def Lorention(x,y0,
              A1,w1,xc1,
              A2,w2,xc2,
              A3,w3,xc3,
              A4,w4,xc4,
              A5,w5,xc5
            ):
    output  =   y0 + \
                (2*A1/np.pi)*( w1 /( 4*(x-xc1)**2 + w1**2 )) + \
                (2*A2/np.pi)*( w2 /( 4*(x-xc2)**2 + w2**2 )) + \
                (2*A3/np.pi)*( w3 /( 4*(x-xc3)**2 + w3**2 )) + \
                (2*A4/np.pi)*( w4 /( 4*(x-xc4)**2 + w4**2 )) + \
                (2*A5/np.pi)*( w5 /( 4*(x-xc5)**2 + w5**2 ))
    return output
boundpa = ( #min 值
            [0 ,          #y0
            0.5 ,0.4 ,-0.5,  #A1,w1,xc1(fitting找的參數的最小值)
            0.5 ,0.4 , 4.5,  #A2,w2,xc2
            0.3 ,0.5 , 8.5,  #A3,w3,xc3
            0.1 ,0.5 , 13 ,  #A4,w4,xc4
            0   ,0.8 , 15.5],  #A5,w5,xc5
            #max 值
            [0.05,           #y0
            1.8  ,1 ,1   ,   #A1,w1,xc1(fitting找的參數的最大值)
            1.0  ,1 ,5.5 ,   #A2,w2,xc2
            0.6  ,1 ,10  ,   #A3,w3,xc3
            0.4  ,1 ,14.5,   #A4,w4,xc4
            0.1  ,1.2 ,16.5 ]   #A5,w5,xc5
            )

#主架構
def main():

    #檔案路徑
    readPath = "./2022_03_03_22_44_30 time4 PIN 0.txt"
    
    dfFile = pd.read_table(  
                             readPath
                            ,sep=' '          #sep=' '中間的空白記得打 要不然會有報錯 
                            ,header=6
                            ,encoding='ANSI'  #看你記事本右下的編碼形式
                            )
    
    #rename 每一欄的欄位名稱
    dfFile.columns = [
                      'frequency'
                    , 'fluorescent'
                    , '3'
                    , '4'
                    , '5'
                    , '6'
                    , '7'
                    , '8'
                    , '9'
                    ]                        
    
    fre = dfFile['frequency'][0:]/2 - 576     #處理頻率 因為是cross over 所以 Fiber EOM 頻率要除以2 喔 -576 是要讓最大根是0
    fluorescent = dfFile['fluorescent'][0:]
    
    
    coe,strength = curve_fit(Lorention,fre,fluorescent,bounds=boundpa)
    
    y0 = coe[0]
    
    A1 = coe[1]
    w1 = coe[2]
    xc1 = coe[3]
    A2 = coe[4]
    w2 = coe[5]
    xc2 = coe[6]
    A3 = coe[7]
    w3 = coe[8]
    xc3 = coe[9]
    A4 = coe[10]
    w4 = coe[11]
    xc4 = coe[12]
    A5 = coe[13]
    w5 = coe[14]
    xc5 = coe[15]


    # print('y0 =', y0 ,'\nA1 = ' , A1 , '\nw1=', w1 ,' \nxc1 =', xc1)
    # print('A2 = ' , A2 , '\nw2=', w2 ,' \nxc2 =', xc2)
    # print('A3 = ' , A3 , '\nw3=', w3 ,' \nxc3 =', xc3)
    # print('A4 = ' , A4 , '\nw4=', w4 ,' \nxc4 =', xc4)
    # print('A5 = ' , A5 , '\nw5=', w5 ,' \nxc5 =', xc5)
    


    #畫圖
    fig = plt.figure(dpi=700)
    ax = fig.add_subplot(111)
    plt.plot(fre,Lorention(fre,y0,
                        A1,w1,xc1,
                        A2,w2,xc2,
                        A3,w3,xc3,
                        A4,w4,xc4,
                        A5,w5,xc5
                        )
                        ,'r')
    plt.plot(fre,fluorescent,'b.',markersize=1)
    plt.xlabel('frequency(MHz)')
    plt.ylabel('fluorescent(A.U)')
    # plt.xlim([15,17])
    # plt.ylim([0,0.1])
    plt.show
    #圖右邊那行係數
    ax.text(1.05,0.05, 'y0 = {:.3f}\nA1 = {:.3f}\nw1 = {:.3f}\nxc1 = {:.3f}\nA2 = {:.3f}\nw2 = {:.3f}\nxc2 = {:.3f}\nA3 = {:.3f}\nw3 = {:.3f}\nxc3 = {:.3f}\nA4 = {:.3f}\nw4 = {:.3f}\nxc4 = {:.3f}\nA5 = {:.3f}\nw5 = {:.3f}\nxc5 = {:.3f}'.format(y0,A1,w1,xc1,A2,w2,xc2,A3,w3,xc3,A4,w4,xc4,A5,w5,xc5), bbox={'facecolor': 'white','alpha': 0.9, 'pad': 5},transform = ax.transAxes)

    text_A  = ['A1','A2','A3','A4','A5']
    coe_A  = [A1,A2,A3,A4,A5]
    text_w  = ['w1','w2','w3','w4','w5']
    coe_w  = [w1,w2,w3,w4,w5]
    text_xc = ['xc1','xc2','xc3','xc4','xc5']
    coe_xc = [xc1,xc2,xc3,xc4,xc5]
    
    coe_list = [text_A  , coe_A ,
                text_w  , coe_w ,
                text_xc , coe_xc 
                ]
    total_rows = len(coe_list)
    total_columns = len(coe_list[0])
    #存係數到csv            
    np.savetxt("coe_copy.csv", coe_list , delimiter = "," , fmt = '% s')
    
    return 



if __name__ == '__main__':
    main()



# %%
