from datetime import datetime
from threading import Timer
from phycr import Cisco,Ipdb

def detect():
    cisco = Cisco()
    cisco.login()
    mactable = cisco.mactable()
    cisco.logout()

    ipdb = Ipdb()
    ipdb.login()
    macdb = ipdb.mac()

    # eg. 2017-04-24 13:11:02
    now= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('detect processes at {time}'.format(time=now))

    inwork = [ mac for mac in macdb if mac in str(mactable)]
    sinwork = '("'+ '","'.join(inwork)+ '")' 
    ipdb.updatetime(sinwork)
    ipdb.logout()

    Timer(1800,detect).start()    


if __name__ =='__main__':
    detect()
