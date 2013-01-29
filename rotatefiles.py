#!/usr/bin/env python2.7

import sys,os,time

default_number_of_files = 700

def usage(name):
    print "USAGE: {0} conf_file log_file".format(name)

def rotate(conf, log):
    conffile=open(conf, 'r')
    logfile=open(log,'a')
	
    logfile.write('\n\n' + time.asctime(time.localtime()) + '\n\n')

    line=basedir=os.path.abspath(conffile.readline().rstrip('\n')) + '/'
    dirs_and_files = dict()
    line = conffile.readline().rstrip('\n')
    while line != '':
        line = line.split()
        if len(line) == 2:
            path, nfiles = line
            nfiles = int(nfiles)
        elif len(line) == 1:
            path = line[0]
            nfiles = default_number_of_files
        else:
            logfile.write("wrongly formatted configuration file\n")
            exit(1)
        whole_path = basedir + path + '/'
        dirs_and_files[whole_path] = nfiles 
        line = conffile.readline().rstrip('\n')

    for path, nfiles in dirs_and_files.items():
        actually_deleted = 0
        tfiles = os.listdir(path)
        #tuple files' path with their modification time to order them:
        tfiles_tuples = [(tf, os.path.getctime(path + tf)) for tf in tfiles] 
        tfiles_tuples.sort(key = lambda x: x[1])
        for f in tfiles_tuples[:-nfiles]:
            try:
                os.remove(path + f[0])
                actually_deleted += 1
                logfile.write("I removed {0}\n".format(path + f[0]))
            except:
                logfile.write("I couldn't remove {0}\n".format(f[0]))
        logfile.write("{0}: there are now {1} files \n"\
                          .format(path, len(os.listdir(path))))
    logfile.close()	
    conffile.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        exit(1)
    rotate(sys.argv[1], sys.argv[2])
