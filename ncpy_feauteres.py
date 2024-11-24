
import socket

class server:
    
# server tcp
    def tcp(ip, port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((ip, port))
        s.listen(1)
        print(f"aguardando a conection no ip: {ip} e na porta {port}")
        con, client = s.accept()

        con.send("Digite a senha: ".encode())
        senha = con.recv(1024)

        if senha.decode() == 'penis':


            while True:
                msg = input("> ")
                msg += "\n"
                con.send(msg.encode())
                dados = con.recv(1024).decode()
                print(dados)
        
    def udp(ip, port):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("127.0.0.1", port))
        print("Aguardando conection")


        while True:
            dados, cliente = s.recvfrom(1024)
            print(f"o {cliente} {dados.decode()}")

            msg = input("> ")
            msg += "\n"
            s.sendto(msg.encode(), cliente)

class client:

    def tcp_c(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        msg = s.recv(1024).decode()

        senha = input(msg)
        s.send(senha.encode())

        while True:
            print(s.recv(1024).decode())
            msg = input("> ")
            msg += "\n"

            s.send(msg.encode())

    def udp_c(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        servidor = ((ip, port))

        while True:
            msg = input("> ")
            msg += "\n"
            s.sendto(msg.encode(), servidor)

            dados, servidor = s.recvfrom(1024)
            print(f"{servidor} - {dados.decode()}")
