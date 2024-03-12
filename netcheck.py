import nmap, time, os

# Please add the IP's you want to "whitelist" e.g. the IP's that SHOULD have access to your network.
# Any unknown IP's will get flagged.
iplist = [
        '192.168.1.1',  # Example
        '192.168.1.2',  # Example
        '192.168.1.3',  # Example
        ]

# Create a new instance of the PortScanner class
nm = nmap.PortScanner()
unknownlist = []

def action():
    for intruder in unknownlist:
        print("Slapping intruder !!!") # Template

def unknownlistappend():
    if host not in unknownlist:
        unknownlist.append(host)

def check():
    if host not in iplist:
        unknownlistappend()
        return("<---- 'Unknown IP Found!")
    else:
        return(" ")

while True:
    nm.scan(hosts='192.168.2.0/24', arguments='-sn -A -sP -PE')  #  Make sure to change " hosts='<change this>' ", 
                                                                 #  and perhaps also the arguments if you wish to do so.
	                                                         #  https://pypi.org/project/python-nmap/
    try:
        os.system('clear')
    except:
        os.system('cls')
        
    print(5*"-", "Active IP's in the Network", 5*"-", "Ctrl+c to quit")
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print('Host : %s (%s)' % (host, nm[host].hostname()), check())
    print(5*"-", "Unknown IP's", 5*"-")
    print(unknownlist)
    action()
    time.sleep(1)
    
        
