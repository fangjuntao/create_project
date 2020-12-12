import pandas as  pd
import numpy as np
import  json




path1  = 'E:/总/新论文/生物信息学/深度网络-生信任务/miRNA-disease/HMDDv3.2-Tensor Decompositionwith  Relational  Constraints for Predicting Multiple Types of MicroRNA-disease Associations/TDRC-master/TDRC-master/HMDD3.2_processed/HMDD3.2_processed/mi_name.csv'


path2  = 'E:/总/新论文/生物信息学/wang计算miRNA的相似性文件/MISIM_V2/MISIM2.0_miRNA_simi_upANDdown.csv'

# mi_name = pd.read_csv(path1)
# mi_similarity  = pd.read_csv(path2)
# print(mi_name.head(5))
# print(mi_similarity.head(5))

mi_name = np.loadtxt(path1, dtype=np.str, delimiter=',')
test_dict = {}
data = mi_name[1:].tolist()
for list1 in data:
    name, cid = list1
    test_dict[cid] = name
print(json.dumps(test_dict, ensure_ascii=False, indent=4))

mir_similarity = np.loadtxt(path2, dtype=np.str, delimiter=',')
test_dict2 = {}
data2 = mir_similarity[1:].tolist()
string_all  = ''
for list2 in data2:
    miRNA1,miRNA2,smi = list2
    smi  = smi.replace('\'', '')
    cid1  = test_dict[miRNA1]
    cid2  = test_dict[miRNA2]
    string1 = cid1+','+cid2+','+smi
    # test_dict2[cid] = name
    print(string1)
    string_all += string1+'\n'
# print(json.dumps(test_dict, ensure_ascii=False, indent=4))

fh = open('misimv2_for_HMDDv3.2/smi_association.txt', 'w', encoding='utf-8')
fh.write(string_all)
fh.close()














