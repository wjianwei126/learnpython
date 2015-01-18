#/usr/bin/env python

from read_redmine import *
from ssh import *

if __name__=='__main__':
    cmd_pool=read_shell()
    inst_redmine(cmd_pool)
