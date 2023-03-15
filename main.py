import sys

from AgenteMapu import AgenteMapu
from Rio import Rio
import signal

def def_handler(sig, frame):
    print("\n\n [!] Saliendo.... \n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == "__main__":
    juego = Rio()
    juan = AgenteMapu()
    juego.insertar(juan)
    juego.run()
