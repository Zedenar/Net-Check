import nmap, time, os

# Please add the IP's you want to "white-list" e.g. the IP's that SHOULD have access to your network.
# Any unknown IP's will get flagged.
iplist = [
        '192.168.1.1',  # Example
        '192.168.1.2',  # Example
        '192.168.1.3',  # Example
        ]

# Create a new instance of the PortScanner class.
nm = nmap.PortScanner()

# Check if the found IP is whitelisted or not.
def check():
    if host not in iplist:
        return("<---- Possible Intruder")
    else:
        pass

while True:
    nm.scan(hosts='192.168.2.0/24', arguments='-sn -A -sP -PE') #  Make sure to change " hosts='<change this>' ", 
                                                                #  and perhaps also the arguments if you wish to do so.
    try:                                                        #  https://pypi.org/project/python-nmap/
        os.system('clear')  # Linux/Unix 
    except:
        os.system('cls')  # Windows
        
    print(5*"-", "Active IP's in the Network", 5*"-", "Ctrl+c to quit")

    # Print out all the found IP's and flag every IP which is not included in the white-list.
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print('Host : %s (%s)' % (host, nm[host].hostname()),check())
    time.sleep(1)
    
        
