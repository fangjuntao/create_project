
# 即miRNA smi  method4


import numpy as np
import scipy.sparse as sp


path1  = 'wang2010_miRNA_for_HMDDv3.2/smi_matrix_diag_one.txt'  # 待处理矩阵文件(wang 2010 )
path2  = 'hahah.txt'  # 0 位置文件的存贮路径
path3  = 'miRNA_Gauss.txt'  # 高斯文件（miRNA）
path4  = 'miRNA_smi_wang2010_Gauss.txt'  #整合后最终的相似性文件的存储路径
#smi_association = np.loadtxt("wang2010_miRNA_for_HMDDv3.2/smi_matrix_diag_one.txt",delimiter=' ')  # 读取txt文件(misim2.0 for HMDDv3.2)
smi_association = np.loadtxt(path1,delimiter=' ')  # 读取txt文件(misim2.0 for HMDDv3.2)

row  =  smi_association.shape[0]
column = smi_association.shape[1]
for i  in range(0,row):
    print("i:{}".format(i))
    for j  in range(0,column):
        print("j:{}".format(j))
        if smi_association[i][j] == 0:
            smi_association[i][j]  =  1
        else :
            smi_association[i][j]  = 0 ;

#np.savetxt("hahah.txt",smi_association)  # 位置信息，其中为1的表示原矩阵中的0值的位置
# np.savetxt(path2,smi_association)  # 位置信息，其中为1的表示原矩阵中的0值的位置


# - -----将处理高斯相似文件，选取其中想要的部分，即：只需要wang2010的0位置对应的部分-----
need_location = np.loadtxt(path2,delimiter=' ')
miRNA_GAuss = np.loadtxt(path3,delimiter=' ')
new_GAuss  = np.multiply(need_location,miRNA_GAuss)  # 矩阵中各元素对应相乘
#np.savetxt('need_miRNA_GAuss.txt',new_GAuss,fmt='%1.4f')
wang2010_txt  = np.loadtxt(path1,delimiter=' ')
new_GAuss_txt  = np.loadtxt('need_miRNA_GAuss.txt',delimiter=' ')
final_miRNA_smi  =  new_GAuss + wang2010_txt
np.savetxt(path4,final_miRNA_smi ,fmt='%1.4f')


