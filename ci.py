from __future__ import print_function
import os
import sys
import platform
import subprocess

for py in ['python', 'python3']:
       cmd = '{} --version'.format(py)
       print(cmd)
       subprocess.check_call(cmd, shell=True)


print("hello")
print(sys.executable)
sys.exit(0)
