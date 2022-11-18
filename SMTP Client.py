# HOW TO RUN THIS PROGRAM
# This program was writen and tested using python version 3.7.9 try using this version if the program wont run
# The program uses the Google mail server. Therefore, you will need and gmail account with a mail app password in order to login to the server
# Google support page for how to set up an app password for your account: https://support.google.com/mail/answer/185833?hl=en
# Make sure you select mail as the app you want to generate an app password for

from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = 'smtp.gmail.com'
port = 465
#Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM) # Creating socket
clientSocket = ssl.wrap_socket(clientSocket) # SSL
clientSocket.connect((mailserver, port)) # Connecting to mailserver 
#Fill in end


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
# Fill in start
email = input('Enter gmail:\r\n') # Getting input for gmail account
password = input('Enter mail app password:\r\n')

base64Str = ("\x00" + email + "\x00" + password).encode() # base64 encoding username and password and sending auth command to webserver
base64Str = base64.b64encode(base64Str)

authCommand = "AUTH PLAIN ".encode() + base64Str + "\r\n".encode() # creating auth command and sending it to mail server
clientSocket.send(authCommand)
recvAuth = clientSocket.recv(1024).decode()
print(recvAuth)
if recvAuth[:3] != '235': # if the first 3 characters in the recived message arent 235 then something went wrong
    print('235 reply not received from server.')

mailFromCommand = 'MAIL FROM: <'+ email +'>\r\n' # Sending mail from command using email that was input before and printing response
clientSocket.send(mailFromCommand.encode())
recvMailFrom = clientSocket.recv(1024).decode()
print(recvMailFrom)
if recvMailFrom[:3] != '250': # if the first 3 characters in the recived message arent 250 then something went wrong
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcptEmail = input('Enter email you want to send to:\r\n') # Getting input for reciptient email

rcptToCommand = 'RCPT TO: <'+ rcptEmail +'>\r\n' # Adds inputed email to command and sends rcpt to command and print response
clientSocket.send(rcptToCommand.encode())
recvRcptTo = clientSocket.recv(1024).decode()
print(recvRcptTo)
if recvRcptTo[:3] != '250': # if the first 3 characters in the recived message arent 250 then something went wrong
    print('250 reply not received from server.')
# Fill in end


# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n' # Sends data command and prints response
clientSocket.send(dataCommand.encode())
recvData = clientSocket.recv(1024).decode()
print(recvData)
if recvData[:3] != '354': # if the first 3 characters in the recived message arent 354 then something went wrong
    print('354 reply not received from server.')
# Fill in end


# Send message data.
# Fill in start
clientSocket.send(msg.encode()) # Sends message
# Fill in end


# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode()) # Sends end message and prints response
endMsgData = clientSocket.recv(1024).decode()
print(endMsgData)
if endMsgData[:3] != '250': # if the first 3 characters in the recived message arent 250 then something went wrong
    print('250 reply not received from server.')
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n' # Sends quit command and prints response
clientSocket.send(quitCommand.encode())
quitData = clientSocket.recv(1024).decode()
print(quitData)
if quitData[:3] != '221': # if the first 3 characters in the recived message arent 221 then something went wrong
    print('221 reply not received from server.')
# Fill in end