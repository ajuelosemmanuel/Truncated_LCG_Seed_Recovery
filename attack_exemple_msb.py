from fpylll import *

def gen_matrix(a:int, modulus:int, size:int) -> list:
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        matrix[0][i] = pow(a, i, modulus)
    for i,j in zip(range(1,size), range(1,size)):
        if i==j:
            matrix[i][j] = modulus
    return matrix

def attack(a:int, modulus:int, output_length:int, Ys:list):
    """ Note : output_length is in bits
    """
    L = IntegerMatrix.from_matrix(gen_matrix(a, modulus, len(Ys)))
    reduced = LLL.reduction(L)
    Xi_I = CVP.closest_vector(reduced, Ys, method="fast")
    Xi = [xi_i*2**output_length % modulus for xi_i in Xi_I]
    probable_seed = Xi[0] % modulus
    probable_ys = [probable_seed % modulus % 2**output_length for i in range(1,len(Ys)+1)]
    if probable_ys == Ys:
        print("Seed recovery complete")
        print("Seed : " + str(probable_seed))
        return probable_seed
    else:
        print("Not enough information to recover the seed. Use more consecutive outputs.")
        return None