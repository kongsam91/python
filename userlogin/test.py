import pandas as pd
def test(user,passwd):
    error_count = 0
    user = str(user)
    passwd = str(passwd)

    if  user in user_list:
        locate  =   user_list.index(user)
        if passwd   ==   passwd_list[locate]:
            print("您已成功登入",user,passwd)
            return ("您已成功登入",user,passwd)
        else:
            error_count =   error_count +   1   
            print("本系統有您這位使用者，但是密碼錯誤請另尋管理員\n登入錯誤次數",user,passwd )
            print('位置',locate)
            return ("本系統有您這位使用者，但是密碼錯誤請另尋管理員\n登入錯誤次數",user,passwd)
    else:
        print("這位使用者並無在這個系統中，請註冊，謝謝",user,passwd)
        error_count  =  error_count +   1 
        return ("這位使用者並無在這個系統中，請註冊，謝謝",user,passwd)

user_passwd_df   =   pd.read_csv('./user_passwd.csv')

user_list    =   list(user_passwd_df.loc[: ,'user'])
passwd_list  =   list(user_passwd_df.loc[: ,'passwd'])
# locate  =   user_list.index(108202513)
test('108202514','zx121')




    # if  user in user_list:
    #     print("t",locate,user,(passwd_list[locate]))
    # else:
    #     print("n",locate,user,(passwd_list[locate]))