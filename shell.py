#!/usr/bin/python3

import os
import sys

def exec_pipeline(line):
    commands = line.split('|')
    fds = {0:0, 1:1, 2:2}

    for command in commands[:-1]:
        (r, w) = os.pipe()
        fds[1] = w
        exec_redirected(commands.split(), fds)
        fds[0] = r

    fds[1] = 1
    pid = exec_redirected(commands[-1].split(), fds)
    return os.waitpid(pid,0)

while True:
    print("$~\(-.-)/~$")
    sys.stdout.flush
    line = sys.stdin.readline()
    args = line.split()
    
    if args[0] == 'cd':
        os.chdir(args[1])
    else:
        pid = os.fork()
        
        if pid == 0: 
            os.execvp(args[0], args)
        os.waitpid(pid, 0)

