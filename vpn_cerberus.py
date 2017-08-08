import os
print("Cerberus is now watching over VPN")
ethWorking = 1
while True:
    devices = os.popen("sudo ifconfig -s").read()
    lookForVPN = "tun"
    lookForLan = "eth"
    searchForVPN = devices.find(lookForVPN)
    searchForLan = devices.find(lookForLan)
    if searchForVPN > -1:
        if searchForLan == -1:
            os.system('ifconfig eth0 up')
            ethWorking = 1
            #print("VPN is back turning LAN on")
            #print (ethWorking)
        elif searchForLan > -1:
            #print (ethWorking)
            #print("VPN is working and Lan is ON so nothing to do")
            pass
