# rotatefiles.py #

This is a simple python script which takes a list of directories with numbers associated,
and deletes all files in those directories that exceed that number, when ordered by
change time (i.e. I use os.path.getctime()). In other words you'd use it if you want to
have only the most recent 100 files in a certain directory, and delete all the others; I use it to delete old emails
on my mailserver.

**Usage:**

	rotatemails.py conf_file log_file
	
`conf_file` is a text file that has to be formatted like this:  the first line contains an
absolute path, while subsequent lines contain a relative path (starting from the absolute path of
the first line) then a space and then a number; if there is no number a default value is
used (`default_number_of_files` in the source, set to 700). For example, given the following as
`conf_file`:

	/var/mail/user/
	inbox/cur/ 100
	sent/cur/ 50
	
the script will delete all the files which are not the 100 newest in
`/var/mail/user/inbox/cur/`, all the ones which are not the 50 newest int
`/var/mail/user/sent/cur` and so on.

`log_file` is simply a file to which a date and a list of files removed is appended.
