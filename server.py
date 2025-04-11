import random
import socket

class GuessingGameServer:
    def __init__(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port
        self.secret_number = random.randint(1, 100)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            conn, addr = self.server_socket.accept()
            client_ip = addr[0]

            #PASSWORD VERIFICATIION
            password = "it6" 
            encription = "Password is:" + password 
            conn.sendall(encription.encode())# sends the password
            while True:
                client_input = conn.recv(1024).decode().strip()
                print(client_input)

                if client_input != password:
                    tell = "Password was no matched"
                    conn.sendall(tell.encode())
                else:
                    tell = "Verified!"
                    conn.sendall(tell.encode())
                    break
                

            print(f"Connected by {addr}, {client_ip}")
            with conn:

                guess_count = 0
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break
                    try:
                        guess = int(data)
                        guess_count += 1
                        if guess < self.secret_number:
                            response = "Too low!"


                        elif guess > self.secret_number:
                            response = "Too high!"


                        else:
                            response = "Correct! You win!"

                            if guess_count <= 5:
                                rating = "Excellent"

                            elif guess_count <= 20:
                                rating = "Very Good!"
                            else:
                                rating = "Good or Fair!"


                            response += f"Your performance {rating}"
                            self.secret_number = random.randint(1, 100)  # Reset for next game
                        conn.sendall(response.encode())
                    except ValueError:
                        conn.sendall("Invalid input! Please enter a number.".encode())

    def stop(self):
        self.server_socket.close()

def main():
    server = GuessingGameServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.stop()

if __name__ == "__main__":
    main()
