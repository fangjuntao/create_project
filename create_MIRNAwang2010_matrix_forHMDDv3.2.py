import numpy as np
import scipy.sparse as sp



smi_association = np.loadtxt("wang2010_for_HMDDv3.2/smi_association_forHMDDv3.2.txt",delimiter=',')  # 读取txt文件

smi_matrix = sp.csr_matrix((smi_association[:, 2], (smi_association[:, 0] , smi_association[:, 1])),
                                         shape=(713, 713)).toarray()

print(smi_matrix.T == smi_matrix)

np.savetxt('wang2010_for_HMDDv3.2/smi_matrix_diag_zero.txt', smi_matrix,fmt='%1.4f')
print("hahaha ")
