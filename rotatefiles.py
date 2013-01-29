#!/usr/bin/python2

import sys,os,time
from tempfile import mkstemp

def usage(name):
    print "USAGE: {0} conf_file log_file".format(name)

def rotate(conf, log):
    conffile=open(conf, 'r')
	#conffile=open('/home/renato/prova', 'r')
    logfile=open(log,'a')
	
    logfile.write(time.asctime(time.localtime()) + '\n\n')
	#os.system('whoami >> {0}'.format(tfilepath))
	#logfile.write('\n\n')
    tfile1, tfilepath1 = mkstemp()
    tfile1 = open(tfilepath1,'r')
    
    tfile2, tfilepath2 = mkstemp()
    tfile2 = open(tfilepath2,'w')
    
    line=basedir=conffile.readline().rstrip('\n')
    directories = dict()
    files_to_delete = []
    line = conffile.readline().rstrip('\n')
    while line != '':
        print "line---: ", line
        path, nmails = line.split()
        nmails = int(nmails)
        directories[path] = nmails
        wpath = basedir + path
        total_mails = len(os.listdir(wpath))
        #logfile.write("{0}\n wanted: {1}\n mails: {2}\n removed: {3}\n\n".format(path, nmails, total_mails, max(0,total_mails - nmails)))
        tfiles = os.listdir(wpath)
        tfiles_tuples = [(tf, os.path.getmtime(wpath + '/' + tf)) for tf in tfiles]
        tfiles_tuples.sort(key = lambda x: x[1])
        for f in tfiles_tuples[nmails:]:
            files_to_delete.append(f[0])
        line = conffile.readline().rstrip('\n')

    print files_to_delete
    tfile2.close()
	
    tfile2 = open(tfilepath2, 'r')
	
    for line in tfile2.readlines():
        os.system('ls -lh {0}'.format(line))

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        exit(1)
    rotate(sys.argv[1], sys.argv[2])
