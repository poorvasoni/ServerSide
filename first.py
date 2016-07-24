#!/usr/bin/python

import socket,commands,time,serversaas,os,record,paas,servercaas,MySQLdb,serveriaas

s=socket.socket()

s.bind(("",4444))

s.listen(5)




def begin():



	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost","root","redhat")
	y=x.cursor()

	cho=c.recv(10)
	print cho
	print "coming here"
	print cho

#new User
	if cho=='2':
	
		user=c.recv(10)
		print user

		passw=c.recv(10)

		print passw

		os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost","root","redhat")
		y=x.cursor()

		y.execute("use clouduser;")
		q=y.execute("select * from registration where username='{}';".format(user))
		print q
		if q==0L:

			mm = y.execute("insert into registration(username,password) values('{}','{}');".format(user,passw))
			x.commit()
			print "coming here"
			y=commands.getstatusoutput("useradd {}".format(user))
	
			print y[0]

			y1=commands.getstatusoutput("echo {} | passwd {} --stdin".format(passw,user))
	

			print y[1]

		

		

			if y1[0]==0 and y[0]==0 and mm==1L:
				print 'done'
		
				c.send("done")
			else:
				c.send('error')
				begin()

		elif q==1L:

			c.send('user already exists')

			begin()

	#Older User
	elif cho=='1':
		user=c.recv(10)
		print user

		passw=c.recv(10)
		print passw
	        os.system("systemctl restart mariadb")
		x=MySQLdb.connect("localhost","root","redhat")
		y=x.cursor()
		y.execute("use clouduser;")
		d=y.execute("select * from registration where username='{}';".format(user))

		print d

		if d==0:

			c.send('error')
			begin()
			
		 
		elif d==1:

			c.send("done")
		
		
	
			service=c.recv(10)
			print service

	#STASS STOrage as a service

			if service=='1':
				print "coming here"
	
				storage=c.recv(10)
				print storage

	#Object Storage
				if storage=='1':

					protocol=c.recv(10)
					print protocol
	#NFS Protocol
					if protocol=='1':

						size=c.recv(10)
						print size


						os.system("lvcreate --name {} --size {} mainvg ".format(user,size))
					
						os.system("mkfs.ext4 /dev/mainvg/{}".format(user))
					
						os.system("mkdir /media/{}".format(user))
					
						os.system("mount /dev/mainvg/{} /media/{}".format(user,user))
					
						os.system('echo "/media/{}  *(rw,no_root_squash)" > /etc/exports'.format(user))
				

						os.system("systemctl restart nfs-server")
					
				
						c.send("done")
					
	#SSHFS Protocol
					elif protocol=='2':
						size=c.recv(10)
						print size

						os.system("lvcreate --name {}sshfs --size {} mainvg ".format(user,size))
						

						os.system("mkfs.ext4 /dev/mainvg/{}sshfs ".format(user,size))
						
	
						os.system("mkdir /media/{}sshfs".format(user))
					
	
						os.system("mount /dev/mainvg/{}sshfs  /media/{}sshfs".format(user,user))
					
	

						os.system("chown {}  /media/{}sshfs".format(user,user))
						
	
						status2=commands.getstatusoutput("chmod 700 /media/{}sshfs".format(user))
						print status2[0]
						
	
						if status2[0]==0:
							c.send("done")
	#Mobile 

					elif protocol=='3':

						size=c.recv(10)
		                                print size

		                                status=commands.getstatusoutput("lvcreate --name {} --size {} mainvg ".format(user,size))
		                                print status[0]
	    
		                                status5=commands.getstatusoutput("mkfs.ext4 /dev/mainvg/{} ".format(user,size)) 
		                                print status5[0]
		
		                                status1=commands.getstatusoutput("mkdir /media/{}".format(user))
		                                print status1[0]

						status4=commands.getstatusoutput("mount /dev/mainvg/{}  /media/{}".format(user,user))
		                                print status4[0]


		                                status2=commands.getstatusoutput("chown {}  /media/{}".format(user,user))
		                                print status2[0]

		                                status3=commands.getstatusoutput("chmod 700 /media/{}".format(user))
		                                print status3[0]

		                                if status2[0]==0 and status1[0]==0 and status3[0]==0:
		                                        c.send("done")

	#SAMBA PROTOCOL

					elif protocol=='4':
					

						size=c.recv(10)
		                                print size

		                                os.system("lvcreate --name {}samba --size {} mainvg ".format(user,size))
		                                

		                                os.system("mkfs.ext4 /dev/mainvg/{}samba ".format(user,size))
		                                

		                                os.system("mkdir /media/{}samba".format(user))
		                                

		                                os.system("mount /dev/mainvg/{}samba  /media/{}samba".format(user,user))
		                                os.system("useradd -s /sbin/nologin {}samba".format(user))

						os.system("smbpasswd -a {}samba".format(user))

						os.system("echo '\n[{}] \npath=/media/{}samba \nwritable = yes' >>/etc/samba/smb.conf".format(user,user))

						os.system("chmod o+w /media/{}samba".format(user)) 
						os.system("systemctl restart smb")
		
						c.send("done")

					
					
					
								

	#BLOCK STORAGE
				elif storage=='2':

					size=c.recv(10)
					print size
		
					os.system("lvcreate --name {}block --size {} mainvg ".format(user,size))
			
				

			

			

					os.system('echo "<target {}block>\nbacking-store /dev/mainvg/{}block\n</target>" >/etc/tgt/conf.d/{}.conf'.format(user,user,user))

				

					os.system("systemctl restart tgtd")

			 		
			
				
					c.send("done")
				
						 	
	#Extend  Partition
				elif storage=='3':
					partition=c.recv(10)
					print partition
	
					size=c.recv(10)
					print size
			
		
					status=commands.getstatusoutput("lvextend --size +{} /dev/mainvg/{}".format(size,partition))
			
					print status[0]

					status1=commands.getstatusoutput("resize2fs /dev/mainvg/{}".format(partition))
					print status1[0]
					if status[0]==0 and status1[0]==0:
				
						c.send("done")
					else:
						c.send("error")


	#REMOVE PARTITION

		   		elif storage=='4':
					name=c.recv(10)
					print name
			
					

					status1=commands.getstatusoutput("umount /dev/mainvg/{}".format(name))
					print status1[0]

					status=commands.getstatusoutput("lvremove /dev/mainvg/{} -y".format(name))
					print status[0]
		
					if status[0]==0:
				
						c.send("done")

					else:
	
						c.send("error")

		#SNAPSHOT
				elif storage=='5':

					name=c.recv(20)
					print name


					os.system("lvcreate --name {}snap --size 1M -s /dev/mainvg/{} ".format(name,name))
				
				
					os.system("mkdir /media/{}sd".format(name))

				
				
					os.system("mount /dev/mainvg/{}snap /media/{}sd".format(name,name))
				
					os.system('echo "/media/{}sd  *(rw,no_root_squash)" > /etc/exports'.format(name))

					os.system("chown {}  /media/{}sd".format(user,name))


					status2=commands.getstatusoutput("chmod 700 /media/{}sd".format(name))
					print status2[0]
				

					os.system("systemctl restart nfs-server")
				
		
				
					c.send("done")
				
				


	#Software as a Service
			elif service=='4':
				serversaas.begin(c,user,passw)
			elif service=='3':
				paas.begin(c,user,passw)

			elif service=='2':
				serveriaas.begin(c,user,passw)

			elif service=='5':
				servercaas.begin(c,user,passw)		

			elif service=='7':
				pass

			elif service=='8':
				print 'coming here'
		
				os.system("userdel {}".format(user))

				os.system("rm -rf /home/{}".format(user))

				os.system("systemctl restart mariadb")
				x=MySQLdb.connect("localhost","root","redhat")
				y=x.cursor()

				y.execute("use clouduser;")
				y.execute("delete from registration where username='{}';".format(user))

				x.commit()

				c.send("done")
			elif service == '9':
				begin()
while True:

	c,addr=s.accept()			
	begin()			
