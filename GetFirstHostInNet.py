import sys
from sys import argv           #argV is a list that contains command line arguments you might pass to the script ie; using powershell passing it a txt file  that it will then use in this script with position 0 being : sys.argv[0]
import pandas as pd
import socket
from ipaddress import ip_network

#print(f"Supply a csv file with a column named \"hostnames\"\nie; {sys.argv[0]} c:\\temp\\test.csv")
csv_file = sys.argv[1]
#csv_file = "c:\\temp\\InfoBlox-DhcpNetworks.csv"
#create df from csv of the hostnames
df = pd.read_csv(csv_file)
subnet_first_host = [] #list to capture first host ips
for subnet in df['Subnet']:
    try:    
        net = ip_network(subnet)
        print("net:",net,"subnet:",subnet)
        hosts = list(net.hosts())
        first_host = hosts[0] # the first host in each subnet
        print(first_host)
        subnet_first_host.append(first_host)#because it's returning a list of lists we first get the list of ips value and from their just return the one ip found for the hostnames after verified it was only one value
    except Exception as e:
        print(e)
        subnet_first_host.append("Missing Subnet Data") #for any subnets not properly formatted or missing data we need to add something so it aligns with our dataframe data when creating a new column
                     
#CREATE A SERIES FROM THE DATAFRAME AND SIMULTANEOUSLY NAME/ADD IT TO THE DATAFRAME
df['First Host'] = subnet_first_host
#Save to CSV open the csv and then copy paste info into another excel workbook as needed etc
print("CSV File with First host column written to c:\\temp\\subnets.csv")
df.to_csv('c:\\temp\\subnets.csv')
