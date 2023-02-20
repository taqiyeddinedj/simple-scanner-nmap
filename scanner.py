
import nmap
import socket

ScanType=  {     1: '-Pn: Ping Scan', 
                 2: '-sS: Staelth Scan',
                 3: '-T4 -F: Quick Scan',
                 4: '-sL: List Scan - simply list targets to scan',
                 5: '-n/-R: Never do DNS resolution',
                 6: '-sU: UDP Scan',
                 7: '-sT: TCP Connect Scan '
                 }

#fucntion to verify ipv4 address

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

#function to get the ip range and start host discoovery


def getRange():

    #Initialize the nmap scanner:
    nm = nmap.PortScanner()

    #Ask the user for the range:
    ipadd=input("What is the address of the network? \n ")
    if not is_valid_ipv4_address(ipadd):
        print("Invalid ip address! ") 
        return
    # we concatenate the address 
    iprange=ipadd +"/24"

    #Output the list of scan types
    for i,j in ScanType.items():
        print (f"{i} : {j}")

    #Get the args used by the user and count it 
    args=input("Please select the args you are going to select  ").split()
    

    #We want to add a quote for each args so thath it can be given to nmap argument parameter
    args_str=', '.join(f'"{arg}"' for arg in args )

    #Start the scan
    print (" \n Scan is starting ... \n ")
    nm.scan(hosts=iprange, arguments=args_str)

    

    try:
        print("The result of the scan is: \n " + '\n'.join(nm.all_hosts()))
    except Exception as e:
        print("An error occurred:", e)





getRange()





 
