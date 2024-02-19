import socket
import threading

IP= "0.0.0.0"
PORT = 9998

def main():
	server = scoket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT)) # To start off, we pass in the IP address and port we want the server to listen on Next we tell the server to start listening
	server.listen(5) # With a maximumback log connection set to 5
	print(f'[*] Listening on {IP}:{PORT}')

	while True:
		client, address = server.accept() # We receive the client socket in the client variable
		print(f*[*]Accepted connection from {address[0]}:{address[1]}')
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()

def handle_client(client_scoket)
	with client_socket as sock:
		request = sock as sock:
		print(f'[*] Received: {request.decode("utf-8)}')

if __name__ == '__main__':
main ()

# To start off, we pass in the IP address and port we want the server to listen on.
# Next we tell the server to start listening
