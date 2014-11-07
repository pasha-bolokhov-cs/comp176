#!/usr/bin/python

import sys, os

def print_help():
        print "The following commands are available:"
        for k in cmds.keys():
                sys.stdout.write('\t"' + k + '"\n')

cmds = {
	"exit":		-1,
	"quit":		-1,
        "logout":       -1,
	"help": 	 0,
	"ls -l":	 1,
	"top":  	 2,
	"uptime": 	 3,
	"df": 		 4
}

while True:
        sys.stdout.write("-$- ")
	req = sys.stdin.readline()
        if (len(req) == 0):                   # zero length means empty buffer
                sys.stdout.write("logout\n")
                quit()
        req = req.rstrip('\n').strip()        # chomp and remove spaces on left and right
	
        if (req == ""): continue

        num = cmds.get(req, -100)
        if num == -100:
                sys.stdout.write("unknown command `" + req + "' -- try `help'\n")
        elif num == 0:
                print_help()
        elif num == -1:
                quit()
        else:
                os.system(req)

