from phycr import File,Cisco
from datetime import datetime,timedelta
import click
from colorama import Fore,init,Style,Back

def acsiiTitle():
    legoman=' _                                                \n'+\
            '/ |     ____   ____   _____   _ _ _   ___    _ __ \n'+\
            '| |_   /  __| /__  \ /  _  \ /     | /__ \  /    |\n'+\
            '| |_\  | |__| |__| | | |_| | | ||| | |__| \ | || |\n'+\
            '|____| |____| |____| \_____/ |_|||_| |____| |_||_|\n'
    print(legoman)



@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """ This is a command line tool for testing physics computer room."""
    if ctx.invoked_subcommand is None:
        host =File().read()
        acsiiTitle()
        print('Detection is processed when {}'.format(host.when))
        ctx.forward(_state)
    else:
        print('')



@cli.command('list')
@click.argument('keyword',nargs=-1)
@click.option('-p','--port')
@click.option('-m','--method',type=click.Choice(['ip','name','port']))
def _list(keyword,port,method):
    """ search keywords in pool and show in different method"""
    host = File().read()
    if keyword==():keyword=None
    host.show(keyword=keyword,method=method)
    



@cli.command('state')
@click.option('-w','--warn-days',default=30)   #by default set to be 1 month
@click.option('-s','--sick-days',default=180)  #by default set to be 6 months/ 1 semester
@click.option('--show',type=click.Choice(['healthy','sick','warning']))
def _state(warn_days,sick_days,show):
    """ show the detection result.

        Tracing back to assigned days from now.
        The devices do not seem to work for "warn" days would be catagorized to watch-list.
        Simarialy,the devices seemingly not working for "sick" days would be put into sick.
       
        As the result, you can say that the number in watch-list haven't work for "warn" days, 
        and vise versa to "sick". 
    """
    init(autoreset=True)
    host = File().read()
    when = datetime.strptime(host.when,'%Y-%m-%d %H:%M')
    now = datetime.now()

    # option value Error
    if warn_days >= sick_days:
        periodError = Fore.RED+Style.BRIGHT+\
                'Option Error: --warn should smaller than --sick\n'+\
                'Default: warn 30 days and sick 180 days\n'
        print(periodError.format(warn_days,sick_days))
        return None
    else:
        delta_warning = timedelta(days=warn_days)
        delta_sick = timedelta(days=sick_days)

    # bad input Warning
    if delta_warning >= now-when :
        lethebulletsfly = Fore.YELLOW+Style.BRIGHT+\
                'Warning:\n'+\
                'The detection is processing only about {} days. Let the bullets fly!'
        print(lethebulletsfly.format((now-when).days))

    sick_num =0
    warning_num =0
    healthy_num =0

    for info in host.dvs:
        #fmt = '{} {}'.format(info['mac'],info['time'])

        lastappear = datetime.strptime(info['time'],'%Y-%m-%d %H:%M')
        delta = now-lastappear
        if delta > delta_sick:
            sick_num+=1
            #print(Fore.GREEN+fmt )
        elif delta_sick >= delta > delta_warning:
            warning_num+=1
            #print(Fore.RED+fmt)
        else: 
            healthy_num+=1
            #print(Fore.YELLOW+fmt)

    stateinfo = '\nFrom {now} back to {wdays} and {sdays} days ago\n'+\
                'Total number of devices are {total}\n'+\
                '{g} {hnum} work fine\n'+\
                '{r} {snum} do not work\n'+\
                '{y} {wnum} in watch-list\n'
    print(stateinfo.format(
        total=host.total(),
        now=datetime.now().strftime('%Y-%m-%d'),
        wdays=warn_days,sdays=sick_days,
        hnum=healthy_num,snum=sick_num,wnum=warning_num,
        g=Fore.GREEN+'●',
        r=Fore.RED+'●',
        y=Fore.YELLOW+'●'))
                    

@cli.command('dev',short_help='test a new idea')
def _dev():
    """ Personally used for develpoing new function :)"""
    cisco=Cisco()
    cisco.login()
    table=cisco.mactable()
    print(table)
    cisco.logout()

if __name__=='__main__':
    cli()
    