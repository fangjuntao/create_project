
import numpy as np
import  json


path1  = 'E:/总/新论文/生物信息学/深度网络-生信任务/miRNA-disease/HMDDv3.2-Tensor Decompositionwith  Relational  Constraints for Predicting Multiple Types of MicroRNA-disease Associations/TDRC-master/TDRC-master/HMDD3.2_processed/HMDD3.2_processed/mi_name.csv'

path2  = 'E:/总/新论文/生物信息学/wang计算miRNA的相似性文件/MISIM_V1/misim/microRNA name.txt'

path3  = 'E:/总/新论文/生物信息学/wang计算miRNA的相似性文件/MISIM_V1/misim/miRNA similarity matrix.txt'



mi_name = np.loadtxt(path1, dtype=np.str, delimiter=',')  #HMDDv3.2 miRNA_name
test_dict = {}
data = mi_name[1:].tolist()
for list1 in data:
    name, cid = list1
    test_dict[cid] = name
print(json.dumps(test_dict, ensure_ascii=False, indent=4))

mi_name_wang = np.loadtxt(path2, dtype=np.str)   #misim v1 miRNA_name
index = 0
test_dict_wang = {}
data_wang = mi_name_wang[0:].tolist()
for list1 in data_wang:
    name = list1
    test_dict_wang[index] = name
    index += 1
print(json.dumps(test_dict_wang, ensure_ascii=False, indent=4))



mir_similarity= np.loadtxt(path3, dtype=np.str, delimiter=' ')  # misimiv1 miRNA的相似性文件
mir_similarity = mir_similarity[0:].tolist()
test_dict2 = {}
string_all  = ''

# [rows, cols] = mir_similarity.shape
# print(rows, cols)
for i in range(271):
    line  = mir_similarity[i].split()
    for j in range(271):

        if  float(line[j]) !=  0 and i != j :  #排除自己与自己的相似性
            miRNA1 =  test_dict_wang[i]
            miRNA2 =  test_dict_wang[j]
            string1 = miRNA1 + ',' + miRNA2 + ',' + line[j]
            print(string1)
            string_all += string1 + '\n'
fh = open('misimv1.0_association.txt', 'w', encoding='utf-8')
fh.write(string_all)
fh.close()

path4 = 'misimv1.0_association.txt'

mir_similarity_association = np.loadtxt(path4, dtype=np.str, delimiter=',')  #misimi v1  miRNA的相似性联系（不含和自身，  A和B 与B和A同时包含）

data_misim1 = mir_similarity_association[0:].tolist()
string_data  = ''
#将联系转化为HMDDv3.2中的对应关系
for list2 in data_misim1:
    miRNA1,miRNA2,smi = list2
    smi  = smi.replace('\'', '')
    cid1  = test_dict[miRNA1]
    cid2  = test_dict[miRNA2]
    string1 = cid1+','+cid2+','+smi
    # test_dict2[cid] = name
    print(string1)
    string_data += string1+'\n'
# print(json.dumps(test_dict, ensure_ascii=False, indent=4))

fh = open('smi_association_misim.txt', 'w', encoding='utf-8')
fh.write(string_data)
fh.close()















