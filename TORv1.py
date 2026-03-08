import socket
import threading
import time
import random
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
NUM_NODES = 10
START_PORT = 9001

# Create encryption keys
keys = [Fernet.generate_key() for _ in range(NUM_NODES)]
ciphers = [Fernet(k) for k in keys]


class Node(threading.Thread):

    def __init__(self, node_id, port):
        threading.Thread.__init__(self)
        self.node_id = node_id
        self.port = port

    def run(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, self.port))
        server.listen()

        print(f"[Node {self.node_id}] running on port {self.port}")

        while True:

            conn, addr = server.accept()
            data = conn.recv(65536)

            try:
                decrypted = ciphers[self.node_id].decrypt(data)
                print(f"[Node {self.node_id}] removed encryption layer")
            except:
                decrypted = data
                print(f"[Node {self.node_id}] forwarding packet")

            conn.close()


def start_network():

    for i in range(NUM_NODES):

        port = START_PORT + i

        node = Node(i, port)
        node.daemon = True
        node.start()


def build_random_circuit():

    # choose random nodes
    circuit = random.sample(range(NUM_NODES), 3)

    print("\nTOR Circuit Created:")
    print("Entry Node :", circuit[0])
    print("Middle Node:", circuit[1])
    print("Exit Node  :", circuit[2])
    print()

    return circuit


def onion_encrypt(message, circuit):

    data = message.encode()

    for node in reversed(circuit):
        data = ciphers[node].encrypt(data)

    return data


def simulate_routing(message):

    circuit = build_random_circuit()

    encrypted = onion_encrypt(message, circuit)

    print("Client encrypts message with 3 onion layers")

    packet = encrypted

    for node in circuit:

        print(f"\nPacket arrives at Node {node}")

        packet = ciphers[node].decrypt(packet)

        print(f"Node {node} removes one encryption layer")

    print("\nFINAL MESSAGE DELIVERED:", packet.decode())
    print("\n-------------------------------------\n")


def menu():

    while True:

        print("TOR Network Menu")
        print("1. Send Anonymous Message")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            msg = input("\nEnter message: ")

            simulate_routing(msg)

        elif choice == "2":

            print("\nExiting TOR Network...\n")
            break

        else:

            print("Invalid choice\n")


if __name__ == "__main__":

    print("\nStarting TOR Network with 10 Nodes...\n")

    start_network()

    time.sleep(2)

    menu()