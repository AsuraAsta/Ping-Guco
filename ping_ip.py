import subprocess 
import platform

def ping_ip (ip):
    sistema = platform.system()
    print(sistema)
    
    
ping_ip("8.8.8.8")