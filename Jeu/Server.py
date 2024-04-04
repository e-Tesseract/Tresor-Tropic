############################################################################################
# Développé par Léo
# le programme sert a creer un serveur pour le jeu, il attend les connexions des joueurs.
############################################################################################
# amélioration ou ajouter à faire:
#   - ajouter des logs
#   - ajouter des prints pour voir l'execution
#
############################################################################################

import socket
import threading
import json


class Server:
    def __init__(self, ip="0.0.0.0", port=5555, max_connections=4):
        #Initialise le serveur avec l'adresse IP, le port et le nombre maximum de connexions.
        self.ip = ip
        self.port = port
        self.max_connections = max_connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crée un socket serveur.
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Permet de réutiliser l'adresse IP et le port.
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen() #Ecoute les connexions entrantes.
        self.clients = [] #Liste des clients connectés.
        self.game_started = False
        self.nombre_joueurs = 0


    def broadcast(self, message):
        #Envoie un message à tous les clients connectés.
        for client in self.clients:
            try:
                client.sendall(json.dumps(message).encode())
            except Exception as e:
                print(f"Erreur lors de l'envoi : {e}")
                self.clients.remove(client)
                

    def handle_client(self, conn, addr):
        while not self.game_started:
            try:
                data = conn.recv(1024)
                if not data:
                    break
            except ConnectionResetError:
                break
        conn.close()
        self.clients.remove(conn)
        print(
            f"Client {addr} déconnecté. Nombre actuel de joueurs: {len(self.clients)}"
        )
        

    def start_game(self):
        #Commence le jeu une fois que le nombre de joueurs requis est atteint.
        self.game_started = True
        print(f"Le jeu commence maintenant avec {len(self.clients)} joueur(s).")
        self.broadcast(
            {"action": "start_game", "message": "Le jeu commence maintenant."}
        )

    def listen_for_clients(self):
        #Ecoute les connexions des joueurs.
        print(f"Serveur en attente de connexions sur {self.ip}:{self.port}...")
        threading.Thread(target=self.wait_for_players).start()


    def wait_for_players(self):
        #Attend que le nombre de joueurs requis se connecte au serveur.
        self.nombre_joueurs = self.demander_nombre_joueurs()
        print(f"Le serveur acceptera {self.nombre_joueurs} joueurs.")

        print("Attente de connexions des joueurs...")
        while len(self.clients) < self.nombre_joueurs:
            conn, addr = self.server_socket.accept()
            self.clients.append(conn)
            print(f"Connexion acceptée de {addr}.")
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

        print(
            "Toutes les connexions ont été établies. Début du jeu dans quelques instants..."
        )
        self.start_game()


    def demander_nombre_joueurs(self):
        #Demande le nombre de joueurs qui vont jouer au jeu.
        while True:
            try:
                nombre_joueurs = int(
                    input("Combien de joueurs vont jouer au jeu (2, 3 ou 4) ? ")
                )
                if nombre_joueurs >= 2 and nombre_joueurs <= 4:
                    return nombre_joueurs
                else:
                    print("Le nombre de joueurs doit être entre 2 et 4.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

def main():
    server = Server()
    server.listen_for_clients()


if __name__ == "__main__":
    main()