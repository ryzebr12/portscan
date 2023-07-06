import socket

def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Define um tempo limite para a conexão
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Porta {port} aberta")
        else:
            print(f"Porta {port} fechada")
        sock.close()
    except socket.error:
        print(f"Não foi possível conectar-se ao host {host}")

# Defina o host alvo e a faixa de portas que deseja verificar
host = 'viacaourbana.com.br'
port_range = range(1, 100)

# Realiza o port scan para cada porta na faixa especificada
for port in port_range:
    port_scan(host, port)
