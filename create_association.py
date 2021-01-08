# 將miRNA_disease关系矩阵转换为两列

import numpy as np
import scipy.sparse as sp

path1  = 'E:/总/新论文/生物信息学/深度网络-生信任务/miRNA-disease/数据集/HMDDv3.2_from_Tensor_v2/combine_association_matrix.txt'
smi_association = np.loadtxt(path1,delimiter=' ')  # 读取txt文件(association_matrix for HMDDv3.2)
row  =  smi_association.shape[0]
column = smi_association.shape[1]
count = 0 ;
string_all  = ''

for i  in range(0,row):
    print("i:{}".format(i))
    for j  in range(0,column):
        print("j:{}".format(j))
        if smi_association[i][j] == 1:
            count  = count+ 1
            string_temp  = str(i+1)+" "+str(j+1)
            string_all   +=  string_temp  + '\n'

        else :
            pass


print(string_all)
fh = open('HMDDv3.2_miRNA_disease_association.txt', 'w', encoding='utf-8')
fh.write(string_all)
fh.close()




