
import pandas as pd
import eel
#網頁介面

#關閉視窗時動作
def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        quit()



@eel.expose
def login(user,passwd):
    locate  =   -1
    user = str(user)
    passwd = str(passwd)
    # globals()['error_count' +  +str(user)] =1;
    # print("錯誤超過三次禁止登入")
    # print('error_count' + str(user))
    error_count = 0
    # global error_count
    if user == quit:
        quit()   
    else:
        if error_count <=3:
            if  user in user_list:
                locate  =   user_list.index(user)
                if passwd   ==   passwd_list[locate]:
                    print("您已成功登入")
                    return str("您已成功登入")
                else:
                    error_count =   error_count +   1   
                    print("本系統有您這位使用者，但是密碼錯誤請另尋管理員\n登入錯誤次數\n帳號",user,"\n密碼",passwd,"\n位置",locate,"\n位置對應到的密碼",passwd_list[locate],type(passwd_list ))
                    print("位置",locate,passwd_list[locate])
                    return str("本系統有您這位使用者，但是密碼錯誤請另尋管理員\n登入錯誤次數")
            else:
                print("這位使用者並無在這個系統中，請註冊，謝謝",user,passwd)
                print(user_list)
                error_count  =  error_count +   1 
                return str("這位使用者並無在這個系統中，請註冊，謝謝")
                
        else:
            print("您輸入過多次錯密碼，已無法再登入，請尋求系統管理員幫助",user,passwd)
            print(user_list)
            return str("您輸入過多次錯密碼，已無法再登入，請尋求系統管理員幫助")



user_passwd_df   =   pd.read_csv('./user_passwd.csv')
user_list    =   (list(user_passwd_df.loc[: ,'user']))
passwd_list  =   (list(user_passwd_df.loc[: ,'passwd']))


eel.init('login_GUI') #網頁資料夾
eel.start('.\login.html',
                        size=(600,400),
                        port= 8787,
                        position=(0,0),
                        close_callback=close_callback
                        )

#完成了