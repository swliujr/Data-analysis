import sys
import nmap
import multiprocessing as mul

l = open('dlist.txt')
r = l.readlines()
l.close()

nm = nmap.PortScanner()

def iport(x):
    print x[0],x[1]

def sc(r):
    f = r.strip()
    nm.scan(hosts=f, ports=None, arguments='-sT')
    return f, nm[f]['tcp'].keys()

pool = mul.Pool(5)
rel  = pool.map(sc,r)
print map(iport,rel)
