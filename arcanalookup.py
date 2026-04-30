import webbrowser as wb
import requests
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(r""" █████╗ ██████╗  ██████╗ █████╗ ███╗   ██╗ █████╗       ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔══██╗      ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
███████║██████╔╝██║     ███████║██╔██╗ ██║███████║█████╗██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗██║██╔══██║╚════╝██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████║██║  ██║      ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝      ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝by: Bg.txt     
                                                                                                           """)

def menu():
    print(r"""
╔══════════════════════════════════════════════╗
║              Arcana-Lookp v1.0               ║
╠══════════════════════════════════════════════╣
║  [1] Consultar IP                            ║
║  [2] Abrir no Google Maps                    ║
║  [3] Abrir no IP Tracker                     ║
║  [0] Sair                                    ║
╠══════════════════════════════════════════════╣
""")

def _input(msg):
    
    try:
        return raw_input(msg)
    except:
        return input(msg)


while True:
    limpar_tela()
    logo()
    menu()

    escolha = _input("Selecione uma opção: ")

    if escolha == '1':
        tracing = _input('Digite o IP (padrão = seu IP): ')
        
        try:
            req = requests.get(f'http://ip-api.com/json/{tracing}').json()

            if req['status'] == 'success':
                print(f"""
IP:        {req['query']}
Endereço:  {req['city']}, {req['country']} ({req['countryCode']})
Região:    {req['region']}
CEP:       {req['zip']}
Fuso:      {req['timezone']}
Coordenadas:
   LAT:    {req['lat']}
   LON:    {req['lon']}
ISP:       {req['isp']}
Org:       {req['org']}
""")

                _input("Pressione ENTER para continuar...")

            else:
                print("Falha ao rastrear o IP.")
                _input("ENTER para continuar...")

        except Exception as e:
            print("Erro:", e)
            _input("ENTER para continuar...")

    elif escolha == '2':
        tracing = _input('Digite o IP: ')
        req = requests.get(f'http://ip-api.com/json/{tracing}').json()
        if req['status'] == 'success':
            wb.open(f'https://www.google.com/maps/@{req["lat"]},{req["lon"]},13z')

    elif escolha == '3':
        tracing = _input('Digite o IP: ')
        wb.open(f'https://www.ip-tracker.org/locator/ip-lookup.php?ip={tracing}')

    elif escolha == '0':
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        _input("ENTER para continuar...")
