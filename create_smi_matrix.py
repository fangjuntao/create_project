import numpy as np
import scipy.sparse as sp



smi_association = np.loadtxt("smi_association.txt",delimiter=',')  # 读取txt文件

smi_matrix = sp.csr_matrix((smi_association[:, 2], (smi_association[:, 0] , smi_association[:, 1])),
                                         shape=(713, 713)).toarray()
smi_matrix = np.triu(smi_matrix)    #选取矩阵的上三角形部分

smi_matrix += smi_matrix.T - np.diag(smi_matrix.diagonal())  #实现矩阵的对称性

print(smi_matrix.T == smi_matrix)

np.savetxt('smi_matrix_diag_zero.txt', smi_matrix)
print("hahaha ")