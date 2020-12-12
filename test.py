import numpy as np

smi_matrix_orig = np.loadtxt("misimv2_for_HMDDv3.2/smi_matrix_diag_zero.txt")  # 读取txt文件
diag_value  = smi_matrix_orig.diagonal()
print( diag_value)

matrix_add = np.eye(713,dtype=np.float64)
smi_matrix_new  =  smi_matrix_orig+ matrix_add
diag_value_new =  smi_matrix_new.diagonal()
test  =  smi_matrix_new  - smi_matrix_orig
print("是否只增加了对角线？")
print((test==np.diag(diag_value_new)).all())
np.savetxt("misimv2_for_HMDDv3.2/smi_matrix_diag_one.txt",smi_matrix_new,fmt='%1.4f')