# Network-Ops
Scripts used for network operations
Some of these are used to format data properly when given a csv file of IP addresses or subnets.
Some of these are used to work with nmap.

## GetFirstHostInNet.py
* Supply a csv file with a column named "Subnet" including your column of cidr subnets ie; 10.10.10.0/24 format
* Outputs new First hosts column to a new csv file "c:\temp\subnet.csv"
**usage**
> python GetFirstHostInNet.py networks.csv
