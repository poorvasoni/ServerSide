#!/usr/bin/python2
import os
os.system("useradd -s /usr/bin/python thor")
os.system('echo | passwd 123 --stdin')
