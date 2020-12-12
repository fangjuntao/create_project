import numpy as np
import scipy.sparse as sp




smi_association = np.loadtxt("wang2010_for_HMDDv3.2/smi_association_forHMDDv3.2.txt",delimiter=',')  # 读取txt文件

smi_matrix = sp.csr_matrix((smi_association[:, 2], (smi_association[:, 0] , smi_association[:, 1])),
                                         shape=(713, 713)).toarray()

print(smi_matrix.T == smi_matrix)

np.savetxt('wang2010_for_HMDDv3.2/smi_matrix_diag_zero.txt', smi_matrix,fmt='%1.4f')
print("hahaha ")


smi_matrix_orig = np.loadtxt('wang2010_for_HMDDv3.2/smi_matrix_diag_zero.txt')  # 读取txt文件
diag_value  = smi_matrix_orig.diagonal()
print( diag_value)

matrix_add = np.eye(713,dtype=np.float64)
smi_matrix_new  =  smi_matrix_orig+ matrix_add
diag_value_new =  smi_matrix_new.diagonal()
test  =  smi_matrix_new  - smi_matrix_orig
print("是否只增加了对角线？")
print((test==np.diag(diag_value_new)).all())
np.savetxt("wang2010_for_HMDDv3.2/smi_matrix_diag_one.txt",smi_matrix_new,fmt='%1.4f')
