#!/usr/bin/python

import sys,os,time
from tempfile import mkstemp

conffile=open('/home/renato/.rotatemails.conf', 'r')
#conffile=open('/home/renato/prova', 'r')
logfilepath='/home/renato/.rotatemails-log'
logfile=open(logfilepath,'a')

logfile.write(time.asctime(time.localtime()) + '\n\n')
#os.system('whoami >> {0}'.format(tfilepath))
#logfile.write('\n\n')
tfile1, tfilepath1 = mkstemp()
tfile1 = open(tfilepath1,'r')

tfile2, tfilepath2 = mkstemp()
tfile2 = open(tfilepath2,'w')

line=basedir=conffile.readline().rstrip('\n')
directories = dict()
finallist = []
line = conffile.readline().rstrip('\n')
while line != '':
    path, nmails = line.split()
    directories[path] = int(nmails)
    wpath = basedir + path
    total_mails = len(os.listdir(wpath))
    #print os.listdir(wpath), total_mails
    logfile.write("{0}\n wanted: {1}\n mails: {2}\n removed: {3}\n\n".format(path, nmails, total_mails, max(0,total_mails - int(nmails))))
    os.system('ls -t -1 {0} | tail -n {1} >> {2}'.format(wpath, max(0,total_mails - int(nmails)), tfilepath1))
    for tline in tfile1.readlines():
        tfile2.write(wpath + '/' + tline)
    line = conffile.readline().rstrip('\n')

tfile2.close()

tfile2 = open(tfilepath2, 'r')

for line in tfile2.readlines():
    os.system('ls -lh {0}'.format(line))
    #print line.rstrip('\n')
#    try:
#        os.remove(line.rstrip('\n'))
#    except OSError:
#        logfile.write('\n:::::::::::OS ERROR: removing mail ::::::::::\n')
#        

#mails_to_delete = tmpfile.readlines()
tfile1.close()
tfile2.close()
logfile.close()
try:
    os.remove(tfilepath1)
except OSError:
    logfile.write('\n:::::::::::OS ERROR: removing tfile1 ::::::::::\n')
try:
    os.remove(tfilepath2)
except OSError:
    logfile.write('\n:::::::::::OS ERROR: removing tfile2 ::::::::::\n')

conffile.close()

#import imaplib
#s = imaplib.IMAP4_SSL("localhost")
#s.login(user, password)
