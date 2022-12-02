"""     *********************************************************************
Lien Github avec le code du test:
"""
from PyQt5.QtWidgets import *
import sys
import threading
import time
import socket


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Définition des caractériqtiques de la fenêtre
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle("Chronomètre")

        grid = QGridLayout()
        widget.setLayout(grid)

        # Option de la fenêtre
        Lab = QLabel("Compteur:")
        self.recup = QLineEdit()
        start = QPushButton("Start")
        reset = QPushButton("Reset")
        stop = QPushButton("stop")
        connect = QPushButton("Connect")
        quitter = QPushButton("Quitter")

        # Mise en place des éléments
        grid.addWidget(Lab, 0, 0)
        grid.addWidget(self.recup, 1, 0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 0)
        grid.addWidget(stop, 3, 1)
        grid.addWidget(connect, 4, 0)
        grid.addWidget(quitter, 4, 1)

        # Action clicker
        start.clicked.connect(self.actionQuitter)
        reset.clicked.connect(self.actionQuitter)
        stop.clicked.connect(self.actionQuitter)
        connect.clicked.connect(self.actionQuitter)
        quitter.clicked.connect(self.actionQuitter)

    def actionstart(self):  # Action de clicker sur "start"
        if self.recup.currentText() == 0:
            self.recup.setText(f'{self.recup.currentText() + 1}')

    def actionreset(self):  # Action de clicker sur "reset"

        self.recup.setText(f'{float(0)}')

    # def actionstop(self):  # Action de clicker sur "stop"

    def actionconnect(self):  # Action de clicker sur "connect"
        host = "localhost"  # "", "127.0.0.1
        port = 10000

        print(f"Ouverture de la socket sur le serveur {host} port {port}")
        client_socket = socket.socket()
        client_socket.connect((host, port))
        print("Serveur est connecté")

        message = input("Message au serveur : ")
        client_socket.send(message.encode())
        print("Message envoyé")

        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")

        # Fermeture de la socket du client
        client_socket.close()
        print("Socket fermée")

    @staticmethod
    def actionQuitter():  # Action de clicker sur "quitter"
        QApplication.exit(0)


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
