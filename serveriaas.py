#!/usr/bin/python2

def begin(c,user,passwd):

	import os,commands,time,random,MySQLdb

	method=c.recv(10)

	print method

	os.system("systemctl restart mariadb")
	x=MySQLdb.connect("localhost","root","redhat")
	y=x.cursor()

#Browser

	if method=='2':

		osd=c.recv(10)

		print osd

	#Ubuntu
		if osd=='1':

			ramm=c.recv(10)
			print ramm

			cpu=c.recv(10)
			print cpu

			hd1=c.recv(10)
			print hd1

			portos=random.randint(5902,5912)

			print portos
			
			Id=random.randint(100000,5000000)
		
			os.system("virt-install --hvm --name {}ubn --memory {} --vcpu {} --disk=/var/lib/libvirt/images/poorva.qcow2  --cdrom /media/CentOS-6.6-x86_64-minimal.iso --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(user,ramm,cpu,portos))
			
			portvnc=random.randint(15000,16000)
                        print portvnc

                        c.send('{}'.format(portvnc))


			os.system("systemctl restart httpd")

			os.system("systemctl restart mariadb")
			x=MySQLdb.connect("localhost","root","redhat")
			y=x.cursor()

			y.execute('use clouduser;')

			q=y.execute("insert into INSTANCES(id,username,portos,portvnc,os,insname) values('{}','{}','{}','{}','Ubuntu','{}ubn');".format(Id,user,portos,portvnc,user))

			
			x.commit()
		






			c.send("done")	

		
			
			os.system("/root/Desktop/websockify-master/run -D 192.168.56.102:{} 192.168.56.102:{}".format(portvnc,portos))

		

	#Redhat
		elif osd=='2':
		
		
			ramm=c.recv(10)
			print ramm

			cpu=c.recv(10)
			print cpu

			hd1=c.recv(10)
			print hd1

			portos=random.randint(5902,5912)
			Id=random.randint(100000,5000000)
	
			os.system("virt-install --import --name {}red --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/new.qcow2 --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(ramm,cpu,portos))



		
			os.system("systemctl restart httpd")

			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("insert into INSTANCES(id,username,portos,portvnc,os,insname) values('{}','{}','{}','{}','Ubuntu','{}red');".format(user,portos,portvnc,user))

			x.commit()

		        c.send("done")



			os.system("/root/Desktop/websockify-master/run -D 192.168.56.102:5555 192.168.56.102:5911")

#Cirros
		elif osd=='4':

			ramm=c.recv(10)
                        print ramm

                        cpu=c.recv(10)
                        print cpu

                        hd1=c.recv(10)
                        print hd1

			portos=random.randint(5902,5912)
			Id=random.randint(100000,5000000)

			print portos
			print portos

                        os.system("virt-install --import --name {}cir --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/cirros-0.3.2-x86_64-disk.img --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(user,ramm,cpu,portos))




                        os.system("systemctl restart httpd")

			portvnc=random.randint(15000,16000)
			print portvnc

			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("insert into INSTANCES(id,username,portos,portvnc,os,insname) values('{}','{}','{}','{}','Cirros','{}cir');".format(Id,user,portos,portvnc,user))
	
			x.commit()

			c.send('{}'.format(portvnc))

                        c.send("done")



                        os.system("/root/Desktop/websockify-master/run -D  192.168.56.102:{} 192.168.56.102:{}".format(portvnc,portos))

			
#VNC

	elif method=='1':

		osd=c.recv(10)

		print osd

#Ubuntu

		if osd=='1':

			ramm=c.recv(10)
                	print ramm

                	cpu=c.recv(10)
               		print cpu

                	hd1=c.recv(10)
                	print hd1

			portos=random.randint(5902,5912)

			print portos
			
			Id=random.randint(100000,5000000)

                	os.system("virt-install --hvm --name {}vncub --memory {} --vcpu {} --disk=/var/lib/libvirt/images/poorva.qcow2  --cdrom /media/CentOS-6.6-x86_64-minimal.iso --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(user,ramm,cpu,portos))	

			c.send('{}'.format(portos))

			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("insert into INSTANCES(id,username,portos,os,insname) values('{}','{}','{}','Ubuntu','{}vncub');".format(Id,user,portos,user))

			x.commit()

			c.send("done")

#cirros

		elif osd=='4':

			ramm=c.recv(10)
                        print ramm

                        cpu=c.recv(10)
                        print cpu

                        hd1=c.recv(10)
                        print hd1

                        portos=random.randint(5902,5912)

                        print portos

                        os.system("virt-install --import --name {}vnccir --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/cirros-0.3.2-x86_64-disk.img --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(user,ramm,cpu,portos))

                        c.send('{}'.format(portos))
			Id=random.randint(100000,5000000)

			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("insert into INSTANCES(id,username,portos,os,insname) values('{}','{}','{}','Ubuntu','{}vnccir');".format(Id,user,portos,user))

			x.commit()

                        c.send("done")
#In QR CODE
	elif method=='3':
	
		insid=c.recv(10)

                os.system("systemctl restart mariadb")
                x=MySQLdb.connect("localhost","root","redhat")
                y=x.cursor()

                y.execute('use clouduser;')

                q=y.execute("select insname,portvnc,portos from INSTANCES where id='{}';".format(insid))

                m=y.fetchall()

		print m
                portvnc=m[0][1]

                if m[0][1]==None:

                        portvnc=random.randint(15000,17000)

                os.system("virsh start {}".format(m[0][0]))

		os.system("qrencode -o /var/www/html/{}.png -s 10x10 https://192.168.56.102:/vnc/?ip='192.168.56.102'&port={}".format(user,portvnc))

		os.system("echo \"<img src={}.png height='50px' width='50px'>\"  >/var/www/html/{}.html".format(user,user)) 

		portos=m[0][2]

                os.system("/root/Desktop/websockify-master/run -D  192.168.56.102:{} 192.168.56.102:{}".format(portvnc,portos))
		c.send('done')
					

	#In Android Phone

	elif method=='4':

		osd=c.recv(10)

                print osd

#Ubuntu

                if osd=='1':

                        ramm=c.recv(10)
                        print ramm

                        cpu=c.recv(10)
                        print cpu

                        hd1=c.recv(10)
                        print hd1

			portos=random.randint(5902,5912)

			Id=random.randint(100000,5000000)

                        os.system("virt-install --hvm --name {}mob --memory {} --vcpu {} --disk=/var/lib/libvirt/images/poorva.qcow2  --cdrom /media/CentOS-6.6-x86_64-minimal.iso --graphics vnc,port={},listen=0.0.0.0 --noautoconsole".format(user,ramm,cpu,portos))
		#	c.send('{}'.format(portos))


			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("insert into INSTANCES(id,username,portos,os,insname) values('{}','{}','{}','Ubuntu','{}mob');".format(Id,user,portos,user))

			x.commit()

			c.send("done")
			c.send('{}'.format(portos))
#My Instances
	elif method=='5':


			os.system("systemctl restart mariadb")
                        x=MySQLdb.connect("localhost","root","redhat")
                        y=x.cursor()

                        y.execute('use clouduser;')

                        q=y.execute("select id from INSTANCES where username='{}';".format(user))

			m=y.fetchall()

			print q

			c.send('{}'.format(q))
			i=0
			while(i<q):	
				
				
				print m[i]
				c.send('{}'.format(m[i]))
					
					
				i=i+1

#Shut Down an Instance
	
	elif method=='8':

		insid=c.recv(20)

		os.system("systemctl restart mariadb")
                x=MySQLdb.connect("localhost","root","redhat")
                y=x.cursor()

                y.execute('use clouduser;')

                q=y.execute("select insname from INSTANCES where id='{}';".format(insid))

		m=y.fetchall()
		os.system("virsh destroy {}".format(m[0][0]))

		c.send('done')
	
#Delete an Instance
	elif method=='9': 
		insid=c.recv(10)
		os.system("")
		
#start an instance
	elif method=='10':
	
		insid=c.recv(10)

		os.system("systemctl restart mariadb")
                x=MySQLdb.connect("localhost","root","redhat")
                y=x.cursor()

                y.execute('use clouduser;')

                q=y.execute("select insname,portvnc,portos from INSTANCES where id='{}';".format(insid))

		m=y.fetchall()

		print m
		portvnc=m[0][1]

		if m[0][1]==None:

			portvnc=random.randint(15000,17000)

                os.system("virsh start {}".format(m[0][0]))
#port vnc send
		c.send('{}'.format(portvnc))

		portos=m[0][2]
		
		os.system("/root/Desktop/websockify-master/run -D  192.168.56.102:{} 192.168.56.102:{}".format(portvnc,portos))
		c.send('done')

	#OS GAllry

	elif method=='11':

		no=c.recv(10)
		print no
		i=0;

		while i<no:
			
			
			ids=c.recv(10)
			print ids

			os.system("systemctl restart mariadb")
                	x=MySQLdb.connect("localhost","root","redhat")
                	y=x.cursor()

               		y.execute('use clouduser;')

                	q=y.execute("select insname,portvnc,portos from INSTANCES where id='{}';".format(ids))
			print "coming here"

                	m=y.fetchall()

                	print m
                	portvnc=m[0][1]

                	if m[0][1]==None:
				portvnc=random.randint(15000,17000)

                	os.system("virsh start {}".format(m[0][0]))
#port vnc send
                	c.send('{}'.format(portvnc))

                	portos=m[0][2]
			
                	os.system("/root/Desktop/websockify-master/run -d  192.168.56.102:{} 192.168.56.102:{}".format(portvnc,portos))
			
			i=i+1
		c.send('done')	                       
