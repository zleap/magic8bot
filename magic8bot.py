#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ircbot1.py
#  
#  Copyright 2016 Paul Sutton <psutton@CoreDuo>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


#linux voice November 2016

import socket
import sys
import subprocess

#server = "192.168.1.130"
#channel = "#zleap"
#nickname = "zleapbot"

server = "irc.freenode.net"
channel = "##zleap"
nickname = "magic8"

irc = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send("USER "+ nickname + " "+ nickname +": Just testing\n")
irc.send("NICK "+ nickname + "\n")
irc.send("JOIN "+ channel +"\n")

while 1:
	text=irc.recv(2040)
	print text
	
	#test to see if things work
	if text.find('PING') != -1:
		irc.send('PONG ' + text.split() [1] + '\r\n')
	
	# user input ping output pong from bot 	
	if text.find(':!uptime') != -1:
		output = subprocess.check_output("uptime", shell=True)
		#print output 
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
#	
		
		# user input ping output pong from bot 	
	if text.find(':!lsb') != -1:
		output = subprocess.check_output("lsb_release -a", shell=True)
		#print output 
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
#		
		
		
		# user input ping output pong from bot 	
	if text.find(':!uname') != -1:
		output = subprocess.check_output("uname -a", shell=True)
		#print output 
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
#		
		
	
	# user input !uptime output system uptime from bot	
	if text.find(':!ping') != -1:
		output = "pong"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
		
