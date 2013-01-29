#!/usr/bin/python2

import sys,os,time

def usage(name):
    print "USAGE: {0} conf_file log_file".format(name)

def rotate(conf, log):
    conffile=open(conf, 'r')
    logfile=open(log,'a')
	
    logfile.write(time.asctime(time.localtime()) + '\n\n')

    line=basedir=conffile.readline().rstrip('\n')
    directories = dict()
    files_to_delete = []
    line = conffile.readline().rstrip('\n')
    while line != '':
        path, nmails = line.split()
        nmails = int(nmails)
        whole_path = basedir + path + '/'
        tfiles = os.listdir(whole_path)
        tfiles_tuples = [(tf, os.path.getmtime(whole_path + tf)) for tf in tfiles]
        tfiles_tuples.sort(key = lambda x: x[1])
        for f in tfiles_tuples[:-nmails]:
            files_to_delete.append(whole_path + f[0])
        line = conffile.readline().rstrip('\n')

    print files_to_delete
    logfile.close()	
    conffile.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        exit(1)
    rotate(sys.argv[1], sys.argv[2])
