# HOW TO RUN THIS PROGRAM
# This program was writen and tested using python version 3.7.9 try using this version if the program wont run
# The program uses the Google mail server. Therefore, you will need and gmail account with a mail app password in order to login to the server
# Google support page for how to set up an app password for your account: https://support.google.com/mail/answer/185833?hl=en
# Make sure you select mail as the app you want to generate an app password for

from socket import *
from smtplib import SMTP

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = 'smtp.gmail.com'
port = 587
#Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = SMTP(mailserver, port) # Setting up smtplib object and connecting to mailserver
recv = clientSocket.connect(mailserver, port)
print(recv[0], recv[1], sep=" ") # Prints server reply
if recv[0] != 220: # if the first 3 characters in the recived message arent 220 then something went wrong
   print('220 reply not received from server.')

recvTLS = clientSocket.starttls() # Request TLS connection from server
print(recvTLS[0], recvTLS[1], sep=" ")
if recv[0] != 220: # if the first 3 characters in the recived message arent 220 then something went wrong
   print('220 reply not received from server.')

email = input('Enter gmail:\r\n') # Getting input for gmail account
password = input('Enter mail app password:\r\n')

recvLogin = clientSocket.login(email, password) # Sending login command
print(recvLogin[0], recvLogin[1], sep=" ")
if recvLogin[0] != 235: # If the first 3 characters in the recived message arent 235 then something went wrong
   print('235 reply not received from server.')
#Fill in end


# Send HELO command and print server response. 
recvHelo = clientSocket.helo('Alice')
print(recvHelo[0], recvHelo[1], sep=" ")
if recvHelo[0] != 250:
   print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
# Fill in start
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcptEmail = input('Enter email you want to send to:\r\n') # Getting input for reciptient email 
# Fill in end


# Send DATA command and print server response.
# Fill in start
clientSocket.sendmail(email, rcptEmail, msg) # Sends email using gmail account that is logged in and reciptient email and preset msg 
# Fill in end


# Send message data.
# Fill in start
# Fill in end


# Message ends with a single period.
# Fill in start
# Fill in end


# Send QUIT command and get server response.
# Fill in start
recvQuit = clientSocket.quit() # Sends quit command and prints response
print(recvQuit[0], recvQuit[1], sep=" ")
if recvQuit[0] != 221: # If the first 3 characters in the recived message arent 221 then something went wrong
   print('221 reply not received from server.')
# Fill in end