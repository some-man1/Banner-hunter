import socket
import sys
from colorama import Fore

"""
  Made by @linuxdebain
  t.me/OpenSource3
"""

def scan_ports(host):
    # Loop through the port range
    for port in range(1, 3306):
        # Create a new socket object for each port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.settimeout(1)  # Set a timeout for the connection attempt
            
            try:
                conn.connect((host, port))
                print(Fore.GREEN + '\033[1m'+ f"Port {port} is open")
                
                if port == 80 or port == 443:
                    # Send HTTP GET request for ports 80 and 443
                    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
                    conn.send(request.encode())
                    
                    # Receive and print the response
                    # response = conn.recv(4096)
                    # print(response.decode())
                else:
                    # Print a generic banner for other ports
                    response = conn.recv(4096)
                    print(f"Response from port {port}\n" +'\033[1m' + Fore.RED + f"{response.decode()}")
                
            except (socket.timeout, ConnectionRefusedError):
                # Handle the case where the connection is refused or times out
                pass
            except Exception as e:
                # Handle any other exceptions
                print(Fore.RED + '\033[1m'+ f"An error occurred: {e}")
            except KeyboardInterrupt:
                print("\n\t\033[1mThink You for Using...")
                sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\n\t\033[1mUsage: python banners_hunter.py <host>")
        sys.exit(1)

    host = sys.argv[1]
    scan_ports(host)
