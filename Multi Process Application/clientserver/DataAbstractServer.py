import socket
import json
import time
from abc import ABCMeta, abstractmethod
from signal import signal, SIGPIPE, SIG_DFL

'''
This class is an abstract server class which contains the common functions requied for all server classes.
This class is made abstract so as to lay down a framework for all the subsequent server classes which inherit this class.
'''
class CDataAbstractServer:
    __metaclass__ = ABCMeta
    
    '''
    Default constructor for CDataAbstractServer class
    Member Variables:
        m_strScripName:      To store the scrip name of the data from the csv file
        m_DataList:          To store the entire list of all json objects; Each json object is a row of data
        m_nCurrentListIndex: To store the current index in the list
        m_Socket:            To store the socket object created for establishing connection with client and sending data; This has to be made a member variable as multiple functions are using it, and passing it becomes a tedious task.
        m_Client:            To store the client object created after establishing connection with client; This has to be made a member variable as multiple functions are using it, and passing it becomes a tedious task.
        m_Host:              To store the hostname of the server
        m_hashParams:        To store the TCA_Params sent by the client
    '''
    def __init__(self):
        self.m_strScripName      = ''
        self.m_DataList          = []
        self.m_nCurrentListIndex = 0
        self.m_Socket            = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_Client            = None
        self.m_Host              = ''
        self.m_hashParams        = {}

    '''
    This is an abstract method created to imply that all inherited classes will need this function.
    Empty function as it is an abstract method.
    '''
    @abstractmethod
    def ParseRow(self):
        pass

    '''
    This is an abstract method created to imply that all inherited classes will need this function.
    Empty function as it is an abstract method.
    '''
    @abstractmethod
    def GetDataFromFile(self):
        pass

    '''
    This function binds to the appropriate port and then listens on it waiting for a client to connect and then accepts the connection.
    Input Variables:
        port: To bind to the appropriate port
    '''
    def Listen(self, port):
        # reqd only for linux: Comment the below snippet for windows usage
        signal(SIGPIPE,SIG_DFL) 
        # reqd only for linux: Comment the above snippet for windows usage

        # When we try to reconnect to the server immediately after it closes, it sometimes results in an error as the port is still in use. The below command frees the port as soon as the server closes. Then, there is no error.
        self.m_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.m_Socket.bind((self.m_Host, port))  # Bind to the port
        self.m_Socket.listen(15)                 # Now wait for client connection.
        self.m_Client, address = self.m_Socket.accept()  
        print 'Got connection from', address
        return True

    '''
    This function recives the params sent by the client and stores it in m_hashParams and initializes some other member variables.
    '8192' below is the buffer size (8192 bytes) for the socket and is usually kept a power of 2.
    '''
    def ReceiveParams(self):
        self.m_hashParams   = json.loads(self.m_Client.recv(8192))
        print self.m_hashParams
        self.m_strScripName = self.m_hashParams['scrip']
        return True
    
    '''
    This function reads from the m_DataList (the list containing the entire data as json objects) and dumps them as single json objects.
    Since this function sends the objects singly, it is a simulated live feed.
    '''
    def SendJson(self):
        data_count = 0
        while  data_count < len(self.m_DataList):
            '''
            time.sleep() is required as the server crashes when the server processes send the data at once to the client process. This most probably is due to buffer overflow.
            time.sleep(0.0001) doesn't work. Not checked for values between 0.0001 and 0.0005.
            Increase the duration if the processing speed is less or the number of cores are less, or possibly the buffer size allocated to each of the clients is less owing to less RAM at the command. But it will result in less speed.
            '''
            time.sleep(0.0005)
            try:
                self.m_Client.send(json.dumps(self.m_DataList[data_count]))
                data_count += 1
                print "sending feed no :" + str(data_count)
            except Exception as e:
                # This exception '[Errno 10054]' is 'An existing connection was forcibly closed by the remote host'.
                # To handle this, if the connection forcibly closes, the socket relistens for any incoming connections.
                print e
                if "[Errno 10054]" in str(e):
                    print "entered server if"
                    client, address = self.m_Socket.accept() 
                    print "Reconnected to client" 

        print "end of feed"
        return True

    '''
    This function closes the client connection.
    '''
    def CloseClient(self):
        self.m_Client.close()                   # Close the connection
