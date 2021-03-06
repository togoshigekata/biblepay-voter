#!/usr/bin/env python

"""
BiblePay-Voter
----

Mass vote on a proposal semi-anonymously

"""

"""
NOTE: You can run multiple instances of vote.py (one for each proposal hash),
Example of shell (.sh) script commands to do this:
screen -dm python vote.py 10c60d59c63fe8830bdf07605fed474c527fca890ace706ff4a5749392250107 yes
screen -dm python vote.py 4c754c122ad91e7e5a85737ee98c59db2da0e080473cca8dbb21672c27127f43 yes
screen -dm python vote.py 28d1a2c5685470f77e42f5c3ad4412780797e7a55e0df7200547a204b1524c23 yes
"""

import subprocess
import argparse
import json
from config import biblepayd_path, datadir, masternodes
from random import randint, shuffle
from time import sleep
from sys import exit, argv
print biblepayd_path, datadir


if len(argv) == 2:
    print "proposal yes|no required"
    exit()

#vote yes somewhere between 70 and 100% of the time. This will average 85% the direction you want. 
p = randint(700, 1000)

# Called when a client sends a message
def vote(proposal, yes_no, masternode):
    """
    ./biblepay-cli --datadir=C:\\Users\\togo\\AppData\\Roaming\\BiblepayCore gobject vote-alias 1e477007d555f9f8919ecbe3b4c457b6f269184924771c0117fbb48751bf23d6 no MN1
    """

    r = randint(0, 1000)
    a, b = "yes", "no"
    if yes_no == "no": a, b = b, a

    a = yes_no
    b = yes_no

    print proposal, (a if r<p else b)
    print biblepayd_path + " --datadir=" + datadir + " gobject vote-alias " + proposal + " funding " + (a if r<p else b) + " " + masternode
    subprocess.call(biblepayd_path + " --datadir=" + datadir + " gobject vote-alias " + proposal + " funding " + (a if r<p else b) + " " + masternode, shell=True)

#vote anonymously

shuffle(masternodes)
for masternode in masternodes:
    vote(argv[1], argv[2], masternode)
	#sleep between 1 to 10 minutes between masternode votes
    sleep(randint(60, 600)) #seconds



