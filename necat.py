import ncpy_feauteres as ncpy
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
arg = sys.argv[3]

servidor = ncpy.server
cliente = ncpy.client

if arg == '-t':
    servidor.tcp(ip, port)
if arg == '-u':
    servidor.udp(ip, port)
if arg == '-tc':
    cliente.tcp_c(ip, port)
if arg == '-uc':
    cliente.udp_c(ip, port)

