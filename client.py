from socketIO_client_nexus import SocketIO, LoggingNamespace
import time

host = "127.0.0.1"
port = 8080

def sioCallback(*args):
    print('socket.io reply', args, "on:", time.strftime('%X'))

socketIO = SocketIO(host, port, LoggingNamespace)

while True:
    socketIO.emit('echo', {'xxx': 'yyy'}, sioCallback)
    socketIO.wait_for_callbacks(seconds=1)
    time.sleep(1)
