import numpy as np
import math

def Getgauss_miRNA(adjacentmatrix, nm):
    """
    MiRNA Gaussian interaction profile kernels similarity
    """
    KM = np.zeros((nm, nm))

    gamaa = 1
    sumnormm = 0
    for i in range(nm):
        normm = np.linalg.norm(adjacentmatrix[i]) ** 2
        sumnormm = sumnormm + normm
    gamam = gamaa / (sumnormm / nm)

    for i in range(nm):
        for j in range(nm):
            KM[i, j] = math.exp(-gamam * (np.linalg.norm(adjacentmatrix[i] - adjacentmatrix[j]) ** 2))
    return KM


def Getgauss_disease(adjacentmatrix, nd):
    """
    Disease Gaussian interaction profile kernels similarity
    """
    KD = np.zeros((nd, nd))
    gamaa = 1
    sumnormd = 0
    for i in range(nd):
        normd = np.linalg.norm(adjacentmatrix[:, i]) ** 2
        sumnormd = sumnormd + normd
    gamad = gamaa / (sumnormd / nd)

    for i in range(nd):
        for j in range(nd):
            KD[i, j] = math.exp(-(gamad * (np.linalg.norm(adjacentmatrix[:, i] - adjacentmatrix[:, j]) ** 2)))
    return KD


if __name__ == '__main__':
    path1  =  'E:/我的资源/论文复现/生物信息学/LAGCN-master/data/HMDDv3.2_from_Tensor_v2/combine_association_matrix.txt'
    miRNA_dis_matrix = np.loadtxt(path1 ,delimiter=' ')
    miRNA_dis_matrix = np.matrix(miRNA_dis_matrix)
    miRNA_Gauss    =  Getgauss_miRNA(miRNA_dis_matrix, 713)
    disease_GAuss  = Getgauss_disease(miRNA_dis_matrix, 447)
    np.savetxt('miRNA_Gauss.txt',miRNA_Gauss)
    np.savetxt('disease_GAuss.txt',disease_GAuss)



