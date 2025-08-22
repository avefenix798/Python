# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:12:54 2025

@author: avefe
"""



import socket
import platform 
import shutil

def main():
    hostname = socket.gethostname()
    print('Nombre del equipo :')
    print(hostname)
    print('IP del equipo :')
    print(socket.gethostbyname(hostname))
    
    
    total, used, free = shutil.disk_usage("/")
    
    print('Espacio Usado en Disco C:')
    
    print("Total: %d GiB" % (total // (2**30)))
    print("Usado: %d GiB" % (used // (2**30)))
    print("Libre: %d GiB" % (free // (2**30)))
    
    print(platform.processor())
    print(platform.machine())
    print(platform.version())
    
if __name__ == '__main__':
    main()