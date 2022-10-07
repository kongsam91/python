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
            [0 ,             #y0
            0 ,0.45 ,-1,      #A1,w1,xc1(fitting找的參數的最小值)
            0.5 ,0.3 ,4.5 ,  #A2,w2,xc2
            0 ,0.35 ,9.1 , #A3,w3,xc3
            0.1 ,0.4 ,12.8 , #A4,w4,xc4
            0 ,0 ,15.6 ],    #A5,w5,xc5
            #max 值
            [1 ,             #y0
            2 ,1 ,1 ,      #A1,w1,xc1(fitting找的參數的最大值)
            1.5 ,1 ,5.1 ,  #A2,w2,xc2
            0.65 ,3 ,15, #A3,w3,xc3
            0.3 ,1 ,16 , #A4,w4,xc4
            5,100 ,20 ] #A5,w5,xc5
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


    print('y0 =', y0 ,'\nA1 = ' , A1 , '\nw1=', w1 ,' \nxc1 =', xc1)
    print('A2 = ' , A2 , '\nw2=', w2 ,' \nxc2 =', xc2)
    print('A3 = ' , A3 , '\nw3=', w3 ,' \nxc3 =', xc3)
    print('A4 = ' , A4 , '\nw4=', w4 ,' \nxc4 =', xc4)
    print('A5 = ' , A5 , '\nw5=', w5 ,' \nxc5 =', xc5)
    
    plt.plot(fre,Lorention(fre,y0,
                            A1,w1,xc1,
                            A2,w2,xc2,
                            A3,w3,xc3,
                            A4,w4,xc4,
                            A5,w5,xc5
                            )
                            ,'r')

    
    #畫圖
    plt.plot(fre,fluorescent,'b.',markersize=1)
    plt.xlabel('frequency(MHz)')
    plt.ylabel('fluorescent(A.U)')
    plt.show
    
    return
 


if __name__ == '__main__':
    main()


