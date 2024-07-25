import math

VALOR_MAX_N = 110
LIMITE = 9999.0


def distanciaEuclidiana(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def floyd_warshall(distancia):
    comprimento = len(distancia)
    for k in range(comprimento):
        for i in range(comprimento):
            for j in range(comprimento):
                distancia[i][j] = min(distancia[i][j], distancia[i][k] + distancia[k][j])


def main():
    while True:
        entrada = int(input())
        if entrada == 0:
            break

        coordenada_x = [0] * (entrada + 1)
        coordenada_y = [0] * (entrada + 1)
        raio = [0] * (entrada + 1)

        for i in range(1, entrada + 1):
            coordenada_x[i], coordenada_y[i], raio[i] = map(float, input().split())

        distancia = [[LIMITE for _ in range(VALOR_MAX_N)] for _ in range(VALOR_MAX_N)]

        for i in range(1, entrada + 1):
            for j in range(1, entrada + 1):
                comprimento = distanciaEuclidiana(coordenada_x[i], coordenada_y[i], coordenada_x[j], coordenada_y[j])
                if comprimento <= raio[i]:
                    distancia[i][j] = comprimento

        floyd_warshall(distancia)

        m = int(input())

        for _ in range(m):
            a, b = map(int, input().split())
            if distancia[a][b] == LIMITE:
                print("-1")
            else:
                print(int(distancia[a][b]))


if __name__ == "__main__":
    main()
