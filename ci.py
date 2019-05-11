from __future__ import print_function
import os
import sys
import platform
import subprocess

def get_python_cmds():
    if platform.system() == 'Windows':
        return [ (x,'C:/python{}/python'.format(x)) for x in ['37'] ]
      
    elif platform.system() in ['Darwin','Linux']:
        # The file .travis.yml installs python3
        return [ ('3.x','python3')]
    
    return [('dfltpython','python3')]
        
    
for pyver,pycmd in get_python_cmds():
    cmd = '{} -m pip install --user https://github.com/intelxed/mbuild/zipball/master'.format(pycmd)
    print(cmd)
    subprocess.check_call(cmd, shell=True)

print("hello")
print(sys.executable)
sys.exit(0)
