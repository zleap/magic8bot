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
import random
import os


server = "irc.freenode.net"
channel = "##zleap"
nickname = "magic8"

#zleap: for the server password method, send 'PASS accountname:password" before NICK and USER - https://github.com/zleap/magic8bot/blob/master/magic8bot.py#L44
# if you want to do SASL it's a bit more work but wortwhile - https://ircv3.net/irc/#sasl-authentication for the spec and https://github.com/atheme/atheme/blob/master/contrib/cap_sasl.pl is a good reference implementation
irc = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
#irc.send("PASS"+acname + " "+pass +":testing\n")
irc.send("USER "+ nickname + " "+ nickname +": Just testing\n")
irc.send("NICK "+ nickname + "\n")
irc.send("JOIN "+ channel +"\n")

RESPONSES = ["It is certain",
             "It is decidedly so",
             "Without a doubt",
             "Yes definitely",
             "You may rely on it",
             "As I see it yes",
             "Most likely",
             "Outlook good",
             "Yes",
             "Signs point to yes",
             "Reply hazy try again",
             "Ask again later",
             "Better not tell you now",
             "Cannot predict now",
             "Concentrate and ask again",
             "Don't count on it",
             "My reply is no",
             "My sources say no",
             "Outlook not so good",
             "Very doubtful"] 

answer = random.choice(RESPONSES)
message =  "Hello, I have now joined ##zleap, please use !help to display options"
irc.send('PRIVMSG '+ channel +' :' + message + '\n')

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
			

#		
			
	# user input !uptime output system uptime from bot	
	if text.find(':!ping') != -1:
		output = "pong"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
		
	# user input !uptime output system uptime from bot	
	if text.find(':!help') != -1:
		output = "options,  !uptime !help !botexit,!magic8, !ping, !web, !sdtj,!fortune,!date"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
		
	# user input !uptime output system uptime from bot	
	if text.find(':!magic8') != -1:
		answer = random.choice(RESPONSES)
		output =  answer
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
	
		# user input !uptime output system uptime from bot	
	if text.find(':!web') != -1:
		output = "https://personaljournal.ca/paulsutton/"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
		
		# user input !sdtj output system uptime from bot	
	if text.find(':!sdtj') != -1:
		output = "https://sdtj.org.uk/"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')

	# user input fortune output pong from bot 	
	if text.find(':!fortune') != -1:
		output = subprocess.check_output("fortune", shell=True)
		#print output 
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')

# user input !date output pong from bot 	
	if text.find(':!date') != -1:
		output = subprocess.check_output("date", shell=True)
		#print output 
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')

		
		# user input !botexit output system uptime from bot	
	if text.find(':!botexit') != -1:
		output = "Magic 8 Quitting - Goodbye"
		#print output
		irc.send('PRIVMSG '+ channel +' :' + output + '\n')
		quit() 
		
	
