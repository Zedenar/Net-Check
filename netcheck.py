import nmap, time, os

# Create a new instance of the PortScanner class
nm = nmap.PortScanner()

while True:
    nm.scan(hosts='192.168.2.0/24', arguments='-sn -A -sP -PE') #  Make sure to change " hosts='<change this>' ", 
                                                                #  and perhaps also the arguments if you wish to do so.
                                                                #  https://pypi.org/project/python-nmap/
    os.system('clear')
    print(iplist)
    print(5*"-", "Active IP's in the Network", 5*"-", "Ctrl+c to quit")
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print('Host : %s (%s)' % (host, nm[host].hostname()))
    time.sleep(1)
  
