import os, time, hashlib, pexpect, sys

def move_file():
	dir = os.listdir("/root")
	os.system("mkdir /root/save")
	for file in dir:
		if '.txt' in file:
			ctime=time.ctime(os.path.getctime(file))
			stime=ctime[20:24]
			os.system("mkdir root/save" + str(stime))
			os.system("cp root" + file + " /root/save" + str(stime))

def secure():
	os.system('tar cvf archive.tar /root/save')
	child = pexpect.spawn('openssl enc -e -aes-256-cbc -in archive.tar -out archive-chiffre.tar')
	child.logfile = sys.stdout
	child.expect('.*password:')
	child.sendline('toto')
	child.logfile = sys.stdout
	child.expect('.*password:')
	child.sendline('toto')
	hash = hashlib.md5('archive-chiffre.tar').hexdigest()
	hfile = open('hfile.txt','w')
	hfile.write(hash)

def export():
	child = pexpect.spawn('ftp 192.168.43.176')
	child.logfile = sys.stdout
	child.expect('Name .*:')
	child.sendline('user')
	child.logfile = sys.stdout
	child.expect('Password:')
	child.sendline('user')
	child.logfile = sys.stdout
	child.expect('ftp>')
	child.logfile = sys.stdout
	child.sendline('put archive-chiffre.tar')
	child.logfile = sys.stdout
	child.expect('ftp>')
	child.logfile = sys.stdout
	child.sendline('exit')

move_file()
secure()
export()
