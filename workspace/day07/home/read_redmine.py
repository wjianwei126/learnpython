#/usr/bin/env python

def read_shell():
    f = open("./scripts/redmine/05.nginx_inst.sh")
    a= f.readlines()
    cmd=tuple(a) 
    return cmd
