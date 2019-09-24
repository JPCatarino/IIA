# Expressoes-lambda e funçoes de ordem superior
# JPCatarino 2019 

import math

# 1. (Implementar na forma de uma expressao-lambda:) Dado um número inteiro, retorna True
# caso o número seja impar, e False caso contrário.
isOdd = lambda num : num % 2 != 0

# 2. (Implementar na forma de uma expressao-lambda:) Dado um número, retorna True caso
# o número seja positivo, e False caso contrário.
isPositive = lambda num : num > 0

# 3. (Implementar na forma de uma expressao-lambda:) Dados dois números, x e y, retorna
# True caso |x| < |y|, e False caso contrário.
compareAbsolute = lambda x,y : abs(x) < abs(y)

# 4. (Implementar na forma de uma expressao-lambda:) Dado um par (x,y), representando
# coordenadas cartesianas de um ponto no plano XY, retorna um par (r,θ), correspondente
# às coordenadas polares do mesmo ponto.
polarCoord = lambda x,y : (math.sqrt(x**2 + y**2), math.atan2(y,x))

def main():
    print(isOdd(5))
    print(isOdd(4))

    print(isPositive(1))
    print(isPositive(-2))

    print(compareAbsolute(3,4))
    print(compareAbsolute(-10,1))

    print(polarCoord(3,4))

if __name__ == "__main__":
    main()