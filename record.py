#!/usr/bin/python2
import os,time


data={}

def add(s,user,passwd):

	data[user]=passwd
 	print data
	return data
	

def begin(s,user,passwd):

	ok=data.has_key(user)
	print data
	return ok
