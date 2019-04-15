#!/usr/bin/python3

import os
import sys

while True:
    print("$~\(-.-)/~$")
    sys.stdout.flush
    line = sys.stdin.readline()
    args = line.split()
    print(args) 

    #env = os.environ['HOME']

    if args[0] == 'cd':
        os.chdir(args[1])
    else:
        pid = os.fork()
        
        if pid == 0: 
            os.execvp(args[0], args)
        os.waitpid(pid, 0)
