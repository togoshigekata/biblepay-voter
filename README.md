BiblePay Voter
==============

BiblePay Private Masternode Voting

Installation
------------

Edit **config.py** with your own environment variables and masternode names  
NOTE: The masternode names should match the names listed in masternode.conf   

To vote, make sure biblepayd is running   
and then pass the hash of the proposal you want to vote on  
and the word yes or no to vote for or against the proposal  

```
python vote.py proposal_hash yes|no
```

NOTE: Votes randomly in your direction between 70 to 100% of the time

NOTE: Sleeps randomly 1 to 10 minutes between votes

------------

References:  

Download Python for Windows:  
https://www.python.org/downloads/windows/
