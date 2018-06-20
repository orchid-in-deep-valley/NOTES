#写日记
import time
import os

@__metaclass = type

#用户类
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
#get present asctime.
def getTime():
    ticks = time.time()
    localTime = time.localtime(ticks)
    return time.asctime(localTime)

#creat diary file
def creatFile(fileName = getTime()):
    return open(fileName,'w')

#m
def chooseOption():
    print '''
        1. creat a new user.
        2. login
        3. exit
        '''
    choose = raw_input('input you choose:')
    return choose

def readUserData():
    
def userCheckout(user):
    
    
def creatNewuser(userName,password):
    fo = open('User','a')
    content = 'Username:%s\nPassword:%s\nUserpath:%s'%(userName,password,userName)
    fo.write(content)
    fo.write('\n')
    #creat user dir
    os.mkdir(userName)
    fo.close()

def Main():

    while(True):
        choose = chooseOption()
        i = False
        for value in range(1,4):
            if int(choose) == value:
                i = True
        if i == False:
            print "Please choos a right option."
            continue
        else:
            break

    if choose =='1':
        userName = raw_input('please input username:')
        password = raw_input('please input password:')
        creatNewuser(userName,password)
    
    

#Main space
Main()
        
        
