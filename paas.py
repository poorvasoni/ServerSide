#!/usr/bin/python2

def begin(c,user,passwd):

	import commands,os,time

	platform=c.recv(10)

	print platform
	
	os.system('systemctl restart docker')
	

	if platform == '1':	

		#register user
	
		fh=open("/root/Desktop/v2.py",'w')
		fh.write('#!/usr/bin/python2\n')
		fh.write("import os\n")
		fh.write('os.system("useradd -s /usr/bin/python {}")\n'.format(user))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(passwd,user))
		fh.close()
	


		y=commands.getstatusoutput("docker run -itd --privileged -v /root/Desktop/:/media/ 6ff02dfe0a3ffeca3102269b78c8c9c10fa6fded6f53c9d86e32d8ba339b5650 bash")


		os.system("chmod +x /root/Desktop/v2.py")
		os.system("docker exec -t {} /media/v2.py".format(y[1]))

		y1=commands.getstatusoutput("docker exec -t {}  hostname -i".format(y[1]))
	        print y1[1]

        
		c.send(y1[1])

	elif platform == '4':	
		#register user
	
		fh=open("/root/Desktop/v3.py",'w')
		fh.write('#!/usr/bin/python2\n')
		fh.write("import os\n")
		fh.write('os.system("useradd -s /usr/bin/mysql {}")\n'.format(user))
		fh.write("os.system('echo {} | passwd {} --stdin')\n".format(passwd,user))
		fh.close()
	


		y=commands.getstatusoutput("docker run -itd --privileged -v /root/Desktop/:/media/ 6ff02dfe0a3ffeca3102269b78c8c9c10fa6fded6f53c9d86e32d8ba339b5650 bash")


		os.system("chmod +x /root/Desktop/v3.py")
		os.system("docker exec {} /media/v3.py".format(y[1]))

		y1=commands.getstatusoutput("docker exec {}  hostname -i".format(y[1]))
		print y1[1]

		
		c.send(y1[1])





	


