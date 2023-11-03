#!/usr/bin/python3
import os
import subprocess
import sys

mdbfile = sys.argv[1] 

print(f"[+] querying the list of tables")
result = subprocess.run(["mdb-tables",mdbfile,"-d",","], capture_output=True, text=True)
tablelist = result.stdout.split(",")

for table in tablelist:
    #get the number of records in the table
    result = subprocess.run(["mdb-count", mdbfile, table], capture_output=True, text=True)
    cnt = result.stdout.strip()
    if (cnt.isnumeric()):
        #query records for tables that are not empty
        if (int(cnt) > 0):
            print(f"[+] querying {cnt} records from table {table}")
            os.system("mdb-export backup.mdb " + table)
            print("")

print(f"[*] done processing {mdbfile}")  
