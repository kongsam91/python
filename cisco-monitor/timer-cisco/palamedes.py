from phycr import Cisco,Ipdb,File
from datetime import datetime
from threading import Timer


def detect():
    cisco = Cisco()
    cisco.login()
    mactable = cisco.mactable()
    cisco.logout()

    ipdb = Ipdb()
    ipdb.login()
    macdb = ipdb.mac()
    ipdb.logout()

    file=File()

    # eg. 2017-04-24 13:11
    now= datetime.now().strftime('%Y-%m-%d %H:%M')

    try:
        host = file.read()
        print('detect start at {time}'.format(time=now))

        # sync the devices in file with the devices in mysql ip database
        [host.dvs.append({'mac':mac,'time':now}) for mac in macdb if mac not in str(host.dvs)]
        [host.dvs.pop(x) for x,info in enumerate(host.dvs) if info['mac'] not in str(macdb)]

        # update time of macs present in cisco  
        [info.update({'time':now}) for info in host.dvs if info['mac'] in str(mactable)]

        file.write(host)

    # firstly execute detection
    except FileNotFoundError:
        print('detect firstly start at {time}'.format(time=now))

        # initialize Host object
        dvs=[]
        [dvs.append({'mac':mac,'time':now}) for mac in macdb]
        file.write(Ipdb.Host(when=now,dvs=dvs))

    Timer(1800,detect).start()    


if __name__ =='__main__':
	detect()
