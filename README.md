## OSSEC vagrant testing and devel setup

*NOT FOR PRODUCTION*  

This is the start of a vagrant based testing and development environment.  Currently 
it spins up two VM's with one acting as the OSSEC master and another as the OSSEC 
agent.  

*NOT FOR PRODUCTION* 

### Requirements

* GNU Make
* vagrant 

### Usage 

```
wget https://github.com/ossec/ossec-hids/archive/master.tar.gz -O ossec-hids.tar.gz
--2014-03-19 14:50:37--  https://github.com/ossec/ossec-hids/archive/master.tar.gz
Resolving github.com... 192.30.252.129
Connecting to github.com|192.30.252.129|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/ossec/ossec-hids/tar.gz/master [following]
--2014-03-19 14:50:37--  https://codeload.github.com/ossec/ossec-hids/tar.gz/master
Resolving codeload.github.com... 192.30.252.147
Connecting to codeload.github.com|192.30.252.147|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1590358 (1.5M) [application/x-gzip]
Saving to: 'ossec-hids.tar.gz'

100%[=================================================================================================================================>] 1,590,358   4.87MB/s   in 0.3s

2014-03-19 14:50:38 (4.87 MB/s) - 'ossec-hids.tar.gz' saved [1590358/1590358]
make up 
```


