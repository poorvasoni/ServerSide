#!/usr/bin/python

import commands,os,time

def begin(c,user,passw):
	software=c.recv(10)
	print software
	
	if software=='1':

		add=commands.getstatusoutput('useradd -s /usr/bin/firefox {}fire'.format(user))

		print add[0]

		add1=commands.getstatusoutput('echo {} | passwd {}fire --stdin'.format(passw,user))

		if add[0]==0 and add1[0]==0:

			c.send(user+"fire")


			
			

		
		done=c.recv(10)
		print done


 	elif software=='2':

		add=commands.getstatusoutput('useradd -s /usr/bin/gedit {}edit'.format(user))

                print add[0]

                add1=commands.getstatusoutput('echo {} | passwd {}edit --stdin'.format(passw,user))

                if add[0]==0 and add1[0]==0:

                        c.send(user+"edit")






                done=c.recv(10)
                print done

	elif software=='3':

		add=commands.getstatusoutput('useradd -s /usr/bin/vlc {}vlc'.format(user))

                print add[0]

                add1=commands.getstatusoutput('echo {} | passwd {}vlc --stdin'.format(passw,user))

                if add[0]==0 and add1[0]==0:

                        c.send(user+"vlc")






                done=c.recv(10)
                print done
	elif software=='4':

                add=commands.getstatusoutput('useradd -s /usr/bin/vncviewer {}vnc'.format(user))

                print add[0]

                add1=commands.getstatusoutput('echo {} | passwd {}vnc --stdin'.format(passw,user))

                if add[0]==0 and add1[0]==0:

                        c.send(user+"vnc")






                done=c.recv(10)
                print done
	
# HOw to off the net for perticular user	
