#!/usr/bin/python3

import os
import sys

def exec_redirected(args, fds):
    pid = os.fork()
    if pid == 0:
        for (childfd, parentfd) in fds.items():
            os.dup2(parentfd, childfd)
        os.execvp(args[0], args)
    return pid

def exec_pipeline(line):
    commands = line.split('|')
    fds = {0:0, 1:1, 2:2} # mapping

    for command in commands[:-1]:
        (r, w) = os.pipe()
        fds[1] = w
        exec_redirected(command.split(), fds)
        os.close(w)
        if fds[0] != 0:
            os.close(fds[0])
        fds[0] = r

    fds[1] = 1
    pid = exec_redirected(commands[-1].split(), fds)
    if fds[0] != 0:
        os.close(fds[0])
    return os.waitpid(pid,0)

def exec_shell():
    while True:
        print("$~\(-.-)/~$")
        sys.stdout.flush
        line = sys.stdin.readline() # ls | sort
        args = line.split()         # ['ls', '|', 'sort']
        
        if args[0] == 'cd':
            os.chdir(args[1])
        else:
            #exec_pipeline(line)
            pid = os.fork()         
            print('pid:', pid)
            if pid == 0:
                os.execvp(args[0], args)
            os.waitpid(pid, 0)

def main ():
    exec_shell()

main()

