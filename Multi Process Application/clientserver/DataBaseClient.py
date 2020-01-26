import socket
import json
import sys
from CommonFunctions import CCommonFunctions

'''
This class is a base client class which contains the common functions requied for all client classes.
'''
class CDataBaseClient:

	'''
	Parameterised constructor for CDataBaseClient class
	Input Variables:
		data_list: To store the entire list of all json objects; Each json object is a row of data
		params:    This input contains TCA_Params to be sent by the client to the server

	Member variables:
		m_DataList: 		   To store the entire list of all json objects; Each json object is a row of data
		m_hashParams:          To store the TCA_Params to be sent by the client to the server
		m_Socket:              To store the socket object created for establishing connection with server and receiving 					   data; This has to be made a member variable as multiple functions are using it, and 							   passing it becomes a tedious task.
		m_strHost:			   To store the hostname of the server.
		m_boolEOF_flag:		   To set the flag to high indicating end of feed
		m_CommonFunctions_obj: To store the object of CCommonFunctions class.This has to be made a member variable as 						   multiple functions are using it, and passing it becomes a tedious task.
	'''
	def __init__(self, data_list, params):
		self.m_DataList      	   = data_list
		self.m_hashParams 		   = params
		self.m_Socket       	   = socket.socket()
		self.m_strHost      	   = '' # Get local machine name
		self.m_boolEOF_flag  	   = False
		self.m_CommonFunctions_obj = CCommonFunctions()

	'''
	This function connects to the server on the port provided as the input.
	Input Variables:
		port: To bind to the appropriate port
	'''
	def Connect(self, port):
		self.m_Socket.settimeout(None)
		self.m_Socket.connect((self.m_strHost, port))
		print "Connected to Server"
		return True

	'''
	This function populates the m_DataList variable with the json objects list.
	Input Variables:
		buffer_json_list: This is an input of the json objects list.
	'''
	def StoreData(self, buffer_json_list):
		for buffer_json in buffer_json_list:
			buffer_json = json.loads(buffer_json)
			# print "Receiving Market Data.."
			# print buffer_json
			buffer_json_formatted = self.m_CommonFunctions_obj.FormatDateJSON(buffer_json)
			#print buffer_json_formatted
			self.m_DataList.append(buffer_json_formatted)
			if buffer_json['eof'] == True:
				self.m_boolEOF_flag = True
		return True

	'''
	This function sends the params to the server.
	'''
	def SendParams(self):
		self.m_Socket.send(json.dumps(self.m_hashParams))
		return True

	'''
	This function receives the incoming data from the server and stores it into a local variable, buffer_json_list.
	'2 * 1024 * 1024 * 1024 - 1' below is the buffer size (2 GB - 1 byte) for the socket. So, for every client, 2 GB is the minimum RAM required. In case of lower resources at the command, reduce this buffer size. However, if the processing speed is less or the number of cores are less, then there is no guarantee for the correct execution of this entire engine. You could try increasing the duration in the time.sleep() command at the server side, which will result in less speed.
	Input variables:
		port: To bind to the appropriate port in case of connection loss.
	'''
	def ReceiveData(self, port):
		while self.m_boolEOF_flag is False:
			buffer_data      = self.m_Socket.recv(2 * 1024 * 1024 * 1024 - 1)
			##
			if len(str(buffer_data)) == 0:
				print "entered client if "
				connected_flag = 0
				while connected_flag == 0:
					try:
						print 'entered try'
						self.m_Socket.connect(self.m_strHost, port)
						connected_flag = 1
						print "reconnected to server"
					except Exception:
						connected_flag = 0
				buffer_data      = self.m_Socket.recv(2 * 1024 * 1024 * 1024 - 1)
			##
			buffer_json_list = self.m_CommonFunctions_obj.ParseBuffer(str(buffer_data))
			self.StoreData(buffer_json_list)

		print "Data received"
		print "total objects received :" + str(len(self.m_DataList)) 
		return True

	'''
	This function disconnects the client from the server.
	It also sets the eof flag indicating end of feed.
	Input Variables:
		data_eof: This is an input flag to indicate end of feed.
	'''
	def Disconnect(self, data_eof):
		data_eof.set()
		self.m_Socket.close()
		print "socket closed"
		return True

	'''
	This is sort of a main function to kickstart the individual clients.
	Input Variables:
		data_eof: This is an input flag, a multiprocessing event, to indicate end of feed.
		port:     This is an input to bind to the appropriate port in case of connection loss.
	'''
	def StartClient(self, data_eof, port):
		print "Client Started"
		self.Connect(port)
		self.SendParams()
		self.ReceiveData(port)
		self.Disconnect(data_eof)
		return True
