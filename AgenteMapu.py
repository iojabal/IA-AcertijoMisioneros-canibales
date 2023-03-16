from copy import deepcopy

from AgenteIA.AgenteBuscador import AgenteBuscador


class AgenteMapu(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)

        self.add_funcion(self.mapuches)
        self.add_funcion(self.verdugos)
        self.add_funcion(self.test)

    def verdugos(self, e):
        if e[0][2] == 1:
            return (e[0][0], e[0][1]-2, e[0][2]-1), "Accion: [0, 2] -v"
        else:
            return (e[0][0], e[0][1]+1, e[0][2]+1), "Accion: [0, 1] +v"

    def mapuches(self, e):
        if e[0][2] == 1:
            return (e[0][0]-2, e[0][1], e[0][2]-1), "Accion: [2, 0] -m"
        else:
            return (e[0][0]+1, e[0][1], e[0][2]+1), "Accion: [1, 0] +m"

    def test(self, e):
        if e[0][2] == 1 and e[0][0] == e[0][1]:
            return (e[0][0]-1, e[0][1]-1, e[0][2]-1), "Accion: [1, 1] -t"
        else:
            return (e[0][0]+1, e[0][1]+1, e[0][2]+1), "Accion: [1, 1] +t"

    def test3(self, e):
        return e[0] != (2,0,0)
    # (3,3,1)

    def es_valido(self, h):
        if h[0][0] == 0:
            return (h[0][0] <= 3 and h[0][1] <= 3) and (h[0] != (2,1,0) and h[0] != (2,1,1))
        elif h[0][2] == 1:
            return (h[0][0] >= h[0][1] >= 0) and (h[0][0] <= 3 and h[0][1] <= 3) and (h[0] != (2,1,0) and h[0] != (2,1,1))
        else:
            return (h[0][0] >= 0 and h[0][1] >= 0) and (h[0][0] <= 3 and h[0][1] <= 3) and (
                        h[0] != (2, 1, 0) and h[0] != (2, 1, 1) and self.test3(h))

    # setear el estado meta, etc
    def pasa_mm(self):
        self.estado_inicial = (3, 3, 1), "Inicio"
        self.estado_meta = (0,0,0), "Fin"

    def test_objetivo(self, e):
        return e[0] == self.estado_meta[0]

    def programa(self):
        self.pasa_mm()
        frontera = [[self.estado_inicial]]
        visitados = []
        while frontera and not None:
            camino = frontera.pop()
            nodo = camino[-1]
            visitados.append(nodo)
            if self.test_objetivo(nodo):
                self.acciones = camino
                break
            else:
                for hijo in self.generar_hijos(nodo):
                    if hijo not in visitados:
                        aux = deepcopy(camino)
                        aux.append(hijo)
                        frontera.append(aux)