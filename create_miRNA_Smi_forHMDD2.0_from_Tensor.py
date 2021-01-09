import numpy as np


def get_functional_sim(miRNA_num,dis_sim, dis_num,mir_dis_mat):
    mir_fun_sim_matrix = np.zeros((miRNA_num, miRNA_num))
    dis_semantic_sim = dis_sim - np.diag(np.diag(dis_sim)) + np.eye(dis_num)

    for m1 in range(miRNA_num):
        m1_link_num = np.sum(mir_dis_mat[m1])
        m1_link_repeat = np.tile(mir_dis_mat[m1], (dis_num, 1))
        for m2 in range(m1, miRNA_num):
            m2_link_num = np.sum(mir_dis_mat[m2])
            m2_link_repeat = np.tile(mir_dis_mat[m2], (dis_num, 1))
            m1_m2_sim_mat = np.multiply(np.multiply(m1_link_repeat, dis_semantic_sim), m2_link_repeat.T)
            m1_max_sum = np.sum(np.max(m1_m2_sim_mat, axis=0))
            m2_max_sum = np.sum(np.max(m1_m2_sim_mat, axis=1))
            mir_fun_sim_matrix[m1, m2] = (m1_max_sum + m2_max_sum) / (m1_link_num + m2_link_num)
            mir_fun_sim_matrix[m2, m1] = (m1_max_sum + m2_max_sum) / (m1_link_num + m2_link_num)
    mir_fun_sim_matrix = mir_fun_sim_matrix - np.diag(np.diag(mir_fun_sim_matrix))
    mir_fun_sim_matrix = np.nan_to_num(mir_fun_sim_matrix)
    # np.savetxt("mir_fun_sim_matrix_new2.txt", mir_fun_sim_matrix)

    # mir_fun_sim_matrix  = np.loadtxt("HMDDv3.2_for_binary_classify/mir_fun_sim_matrix.txt",delimiter=" ")
    return mir_fun_sim_matrix

if __name__ == '__main__':
    # HMDD2.0
    path1_dis_smi = "data(383-495)（HMDD2.0主流）/d-d.csv"
    path2_miRNA_dis_association = "data(383-495)（HMDD2.0主流）/m-d.csv"
    miRNA_num  =  495
    dis_sim  =  np.loadtxt(path1_dis_smi,delimiter=",")
    dis_num  = 383
    mir_dis_mat  = np.loadtxt( path2_miRNA_dis_association,delimiter=",")
    miRNA_Smi  = get_functional_sim(miRNA_num, dis_sim, dis_num, mir_dis_mat)
    np.savetxt("miRNA_Smi_HMDDv2_fromTensor.txt",miRNA_Smi)
