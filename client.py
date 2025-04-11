import socket

class GuessingGameClient:
    def __init__(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port

    def play(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            print("Connected to the server. Start guessing!")

            #INPUT
            srv_pass = client_socket.recv(1024).decode() # Password received
            print(srv_pass)
            if srv_pass:# There is a password
                while True: #In server password verification 
                        input_password = input("Enter password: ")
                        client_socket.sendall(input_password.encode())
                        message = client_socket.recv(1024).decode()
                        print(message)
                        if "Verified!" not in message:
                            print("renter password")
                        else:
                            break
            
            while True:
                guess = input("Enter your guess (1-100): ")
                client_socket.sendall(guess.encode())
                response = client_socket.recv(1024).decode()
                print(response)
                if "Correct! You win!" in response:
                    break

def main():
    client = GuessingGameClient()
    try:
        client.play()
    except KeyboardInterrupt:
        print("stopping client")
    finally:
        pass

if __name__ == "__main__":
    main()
