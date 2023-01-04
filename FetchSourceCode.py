#!/usr/bin/env python

# Auther: Nathan Lee
# Mail: nathanlee@ami.com

# This is a simple tool for retrieving source code from git; 
# if you would like to add a branch to the code, feel free to do it on your own.
# Please let me know if you have any recommendations or run into any bugs or problems.

import os
import datetime
import sys
import logging

logging.basicConfig(level=logging.INFO)
Python_version = sys.version_info[0]
today = datetime.date.today()



logging.info("Current Python version: "+str(Python_version))

logging.info("Select SPX Version: 1. LTS-v12 2. LTS-v13 3. Update 1&2 0. Exit ")
#SPX_Version = 1 - LTS-v12 2- LTS-v13
while True:
    try:
        SPX_Version = int(input())
        break
    except:
        print("No valid input! Please try again ...")
MagicNumber = SPX_Version

# Set Argument:
if SPX_Version == 0:
    exit()
elif SPX_Version == 1:
    logging.info("LTS-v12")
    logging.info("Select Platform: 1. AST2500EVB 2. Wolfpass 3. Ethanol-x 0. Exit")
    while True:
        try:
            Platform = int(input())
            break
        except:
            print("No valid input! Please try again ...")
    MagicNumber = MagicNumber*10  + Platform
elif SPX_Version == 2:
    logging.info("LTS-v13")
    logging.info("Select Platform: 1. AST2600EVB 2. Archercity 3. Quartz 0. Exit")
    while True:
        try:
            Platform = int(input())
            break
        except:
            print("No valid input! Please try again ...")
    MagicNumber = MagicNumber*10  + Platform
elif SPX_Version == 3:
    logging.info("Update 1&2")
    logging.info("Select Platform 1. AST2500EVB 2. Wolfpass 3. ethanol-x")
    while True:
        try:
            Platform = int(input())
            break
        except:
            print("No valid input! Please try again ...")
    MagicNumber = MagicNumber*10  + Platform

    print("Select Branch 1. LTS_v12_update_1.07 2. LTS_v12_update_2.01 3. LTS_v12_update_2.03 4. v12-update-3.00-RC1 5. others ")
    while True:
        try:
            U1U2_Branch = int(input())
            break
        except:
            print("No valid input! Please try again ...")
    
    if U1U2_Branch == 1:
        BRANCH = "LTS_v12_update_1.07"
    elif U1U2_Branch == 2:
        BRANCH = "LTS_v12_update_2.01"
    elif U1U2_Branch == 3:
        BRANCH = "LTS_v12_update_2.03"
    elif U1U2_Branch == 4:
        BRANCH = "v12-update-3.00-RC1"
    elif U1U2_Branch == 5:
        print("Please insert branch name:")
        if Python_version < 3:
            BRANCH = raw_input()
        else:
            BRANCH = input()
    else:
        logging.info("incorrect input"+ BRANCH)
        exit()

else:
    logging.info("other_version")

if Platform == 0:
    exit()
if __debug__:
    logging.info("MagicNumber: "+MagicNumber)

#Set Parameter
if MagicNumber == 11: #AST2500EVB
    REPOSITORY = "https://git.ami.com.tw/core/lts/dev/evb/ast2500evb.git"
    BRANCH = "LTS-v12"
    WORKSPACE = "AST2500EVB_LTSv12_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 12: #Wolfpass
    REPOSITORY = "https://git.ami.com.tw/core/lts/dev/crb/wolfpass.git"
    BRANCH = "LTS-v12"
    WORKSPACE = "Wolfpass_LTSv12_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 13: #Ethnaol-x
    REPOSITORY = "https://git.ami.com.tw/core/lts/dev/crb/amd/ethanol-x.git"
    BRANCH = "LTS-v12"
    WORKSPACE = "Ethnaol_LTSv12_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 21: #AST2600EVB
    REPOSITORY = "https://git.ami.com.tw/core/lts/spx-13/evb/ast2600evb.git"
    BRANCH = "LTS-v13"
    WORKSPACE = "AST2600EVB_LTSv13_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 22: #Archercity
    REPOSITORY = "https://git.ami.com.tw/core/lts/spx-13/crb/intel/archercity.git"
    BRANCH = "LTS-v13"
    WORKSPACE = "Archercity_LTSv13_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 23: #Quartz
    REPOSITORY = "https://git.ami.com.tw/core/lts/spx-13/crb/amd/quartz.git"
    BRANCH = "LTS-v13"
    WORKSPACE = "Quartz_LTSv13_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 31: 
    REPOSITORY = "https://git.ami.com.tw/core/spx/V12_update_1and2/evb/ast2500evb.git"
    WORKSPACE = "AST2500EVB_U1U2_"+BRANCH+"_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 32: 
    REPOSITORY = "https://git.ami.com/core/spx/V12_update_1and2/crb/wolfpass.git"
    WORKSPACE = "Wolfpass_U1U2_"+BRANCH+"_"+today.strftime('%Y_%m_%d')
elif MagicNumber == 33: 
    REPOSITORY = "https://megaracgit.ami.com.tw/core/spx/V12_update_1and2/crb/amd/ethanol-x.git"
    WORKSPACE = "Ethanol_U1U2_"+BRANCH+"_"+today.strftime('%Y_%m_%d')


else:
    print("incorrect Input! MagicNumber = ",MagicNumber)
    exit()

print(REPOSITORY)
print(BRANCH)
print(WORKSPACE)
#Combine commands:

Command = "git clone --recurse-submodules "+REPOSITORY+" --branch "+BRANCH+" "+WORKSPACE
#os.system("echo '"+Command+"' >> fetch"+today.strftime('%Y_%m_%d')+".sh")
print("echo '"+Command+"' >> fetch"+today.strftime('%Y_%m_%d')+".sh")
#os.system(Command)
print(Command)
Command = "cd $WORKPASCE"
#os.system("echo '"+Command+"' >> fetch"+today.strftime('%Y_%m_%d')+".sh")
#os.system(Command)
Command = "git submodule foreach git checkout "+BRANCH
#os.system("echo '"+Command+"' >> fetch"+today.strftime('%Y_%m_%d')+".sh")
#os.system(Command)


