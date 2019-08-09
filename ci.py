from __future__ import print_function
import os
import sys
import platform
import subprocess

#for size in ['ia32','x86-64']:
#    for link in ['','--shared']:
#        cmd = 'python mfile.py --build-dir=build host_cpu=%s %s test' % (size,link)
#        print(cmd)
#        subprocess.check_call(cmd, shell=True)



def get_python_cmds():
    if platform.system() == 'Windows':
        lst = []
        pyvers = ['27','35']
        #pyvers = ['27']
        for pyver in pyvers:
            pycmd = 'C:/python{}/python'.format(pyver)
            lst.append((pyver,pycmd))
        return lst
    elif platform.system() == 'Linux':
        # The file .travis.yml installs python2 and python3
        return [('2.7','python'),
                ('3.x','python3')]
    
    return [('dfltpython','python')]
        
    
for pyver,pycmd in get_python_cmds():
    cmd = '{} -m pip install --user https://github.com/intelxed/mbuild/zipball/master'.format(pycmd)
    print(cmd)
    subprocess.check_call(cmd, shell=True)

print("hello")
print(sys.executable)
sys.exit(0)


