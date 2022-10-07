from pexpect  import pxssh
import pymysql
from netaddr import *
from wcwidth import wcswidth
import json
from colorama import Fore,init,Style,Back

class Cisco:
    Mode_Enable ='30_251#'


    def __init__(self):
        self.__ssh= None

    def login(self):
        '''login cisco 2960s'''

        host = "172.20.30.251"
        user = "admin"
        pwd = '30@ncu'

        self.__ssh = pxssh.pxssh()
        self.__ssh.PROMPT = self.Mode_Enable
        self.__ssh.login(host,user,pwd,auto_prompt_reset=False)
        self.__ssh.sendline('terminal length 0')
        self.__ssh.prompt()

    def _mac_cisco2Unix(self,cmac): #use netaddr, input EUI class(kind of mac)
        Umac = EUI(cmac)
        Umac.dialect = mac_unix_expanded
        return str(Umac).upper()

    def mactable(self,dev=False):
        self.__ssh.sendline('show mac address-table')
        self.__ssh.prompt()
        result = self.__ssh.before.decode('utf-8')

        if dev: print(result)

        table=[]
        for line in result.split('\n'):
            # number of vlan
            if line[:4]=='3030':
                mac = self._mac_cisco2Unix(line.split(' '*4)[1])
                port= line.split(' '*5)[1].replace('\r','').replace(' ','')
                lan = {'mac':mac,'port':port}
                table.append(lan)
        
        return table

    def logout(self):
        self.__ssh.logout()

class Ipdb:

    def __init__(self):
        self.__db=None
        self.__cursor= None

    # type(sinwork) -> tuple
    def updatetime(self,sinwork): 
        rq ='UPDATE cr_ip SET last_appear_time=CURRENT_TIMESTAMP WHERE MAC IN {}'.format(sinwork)
        self.__cursor.execute(rq)
        # update dataase after commit
        self.__db.commit()
        
    def _inuse(self):
        rq ='SELECT IP, MAC, info_location, info_devicetype, info_description, boss_id FROM cr_ip WHERE in_use="Y" '
        self.__cursor.execute(rq)
        return self.__cursor.fetchall()        

    def _user(self):
        rq = 'SELECT Id, user_name_cjk, user_email FROM cr_users'
        self.__cursor.execute(rq)
        return self.__cursor.fetchall()
    
    def _cisco_mactable(self):
        cisco = Cisco()
        cisco.login()
        table = cisco.mactable()
        cisco.logout()
        return table

    def login(self):
        """login ip database with crdb"""
        dbhost= '140.115.31.29'
        dbuser= 'crdb'
        dbpass= 'UmtYJnJf33yQPAvT'
        dbname= 'crdb'
        self.__db = pymysql.connect(host=dbhost,user=dbuser,password=dbpass,db=dbname,charset='utf8')
        self.__cursor = self.__db.cursor()

    def logout(self):
        self.__cursor.close()
        self.__db.close()

    def pool(self):
        table = self._cisco_mactable()
        pool = []
        author = self._user()
        for info in self._inuse():
            lego = {}
            index = next(i for i,u in enumerate(author) if u[0]==info[5])

            lego['ip']= info[0]
            lego['mac']= info[1]
            lego['port'] = ''.join(lan['port'] for lan in table if lan['mac']==info[1])
            lego['location']= info[2]
            lego['type']= info[3]
            lego['note']= info[4]
            lego['name']= author[index][1]
            lego['email']= author[index][2]
            pool.append(lego)
        return pool

    def mac(self):
        mac =[]
        [ mac.append(info[1]) for info in self._inuse() ]
        return set(mac)

    class Host:
        def __init__(self,when,dvs):
            self.when = when
            self.dvs = dvs

        def _getpool(self,keyword=None):
            ipdb =Ipdb()
            ipdb.login()
            pool = ipdb.pool()
            ipdb.logout()

            kpool=[]
            notfound=[]

            if keyword==None:
                kpool=pool
            else:
                for kinfo in keyword:
                    found = False
                    for lego in pool:
                        if (kinfo in lego['ip']) or (kinfo in lego['name']) or (kinfo in lego['location']) or (kinfo in lego['port']) :
                            kpool.append(lego)
                            found = True
                    if not found:
                        notfound.append(kinfo)

            return (kpool,notfound)      

        # now in dev :[
        def _trim(self,sting,space):
            return (string[:space]+'...' if len(string) > space else string)

        def _containsChinese(self,keyword):
            return len(keyword)!=wcswidth(keyword)

        def _padding(self,string,pad):
            return pad-wcswidth(string)+len(string)
        """ prettify the output. 
            The chinese chacters is fullwidth 
        """

        def _simpleinfo(self,lego):
            ip =lego['ip']
            typ=lego['type']
            location =lego['location']
            name=lego['name']
            note=lego['note']
            port=lego['port']

            return '{ip:16} {type:10} {location:{ploc}} {name:{pname}} {note:{pnote}} {port}'\
                    .format(ip=ip,type=typ,location=location,name=name,note=note,port=port
                        ,ptype=self._padding(typ,12)
                        ,ploc=self._padding(location,18)
                        ,pname=self._padding(name,16)
                        ,pnote=self._padding(note,20)
                    )

        def total(self):
            return len(self.dvs)

        def showSimple(self,pool):
            for lego in pool:
                print(self._simpleinfo(lego))
            print('')

        def showCollection(self,pool):
            uqn= sorted(set( lego['name'] for lego in pool ))
            for name in uqn:
                index = [i for i,lego in enumerate(pool) if lego['name']==name]
                email = next( pool[i]['email'] for i in index )
                ip = [ pool[i]['ip'] for i in index ]
                note =  [ pool[i]['note'] for i in index ]

                print('{name:5}{email}'.format(name=name,email=email))
                print('-'*20)
                for i in index:
                    print('{ip:16}{note}'.format(ip=pool[i]['ip'],note=pool[i]['note']))
                print('\n')

        def showWire(self,pool):
            uqp = sorted(set(lego['port'] for lego in pool))
            NotWired=''
            for port in uqp:

                if port!=NotWired: print(port)
                else: print('Not Wired')
                print('-'*20)

                index = [i for i,lego in enumerate(pool) if lego['port']==port]
                for i in index:
                    ip = pool[i]['ip']
                    mac=pool[i]['mac']
                    name=pool[i]['name']
                    location=pool[i]['location']
                    typ = pool[i]['type']

                    print('{ip:17}{mac:22}{type:10s}{name:{pname}}{location}'
                    .format(ip=ip,mac=mac,name=name,location=location,type=typ
                        ,pname=self._padding(name,16)))
                print('\n')

        def show(self,keyword=None,method=None):

            notfound=[]

            if method==None:
                if keyword==None:
                    pool,notfound = self._getpool(keyword)
                    self.showSimple(pool)
                else:
                    chinesekey=[]
                    others=[]
                    for kinfo in keyword:
                        if self._containsChinese(kinfo):
                            chinesekey.append(kinfo)  
                        else:
                            others.append(kinfo)                                      
                    
                    cpool,cnot = self._getpool(chinesekey)
                    spool,snot = self._getpool(others)
                    self.showCollection(cpool)
                    self.showSimple(spool)

                    if cnot!=[]: notfound.extend(cnot)
                    if snot!=[]: notfound.extend(snot)

            elif method=='ip':
                pool,notfound = self._getpool(keyword)
                self.showSimple(pool)
            elif method=='name':
                pool,notfound = self._getpool(keyword)
                self.showCollection(pool)
            elif method=='port':
                pool,notfound = self._getpool(keyword)
                self.showWire(pool)

            if notfound!=[]:
                init(autoreset=True)
                print(Fore.YELLOW+Style.BRIGHT+\
                    'The following keyword is not in database:\n'+' '.join(notfound))

class File():
    def __init__(self,fname='devices'):
        self.fname = fname

    def read(self):
        f= open(self.fname,'r')
        attrdict = json.load(f)
        f.close()
        return Ipdb.Host(when=attrdict['when'],dvs=attrdict['dvs'])

    def write(self,host):
        f=open(self.fname,'w')
        json.dump(host.__dict__,f)
        f.close()


