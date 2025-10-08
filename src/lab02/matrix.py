def transpose(mat):
    if all(isinstance(item,(float,int)) for num in mat for item in num):
        if len(mat)==0:
            return []
        if len(set(map(len,mat)))!=1:
            return 'ValueError'
        transpose_mat=[]
        for item in range(0,len(mat[0])):
            trans_mat=[]
            for img in mat:
                trans_mat.append(img[item])
            transpose_mat.append(trans_mat)
        return transpose_mat

def row_sums(mat):
    if all(isinstance(item,(float,int)) for num in mat for item in num):
        if len(set(map(len,mat)))!=1:
            return 'ValueError'
        row_sum_mat=[]
        for item in mat:
            row_sum_mat.append(sum(item))
        return row_sum_mat

def col_sums(mat):
    if all(isinstance(item,(float,int)) for num in mat for item in num):
        if len(set(map(len,mat)))!=1:
            return 'ValueError'
        col_sum_mat=[]
        for item in range(0,len(mat[0])):
            s=0
            for img in mat:
                s+=img[item]
            col_sum_mat.append(s)
        return col_sum_mat

print('transpose')
n=[[1, 2, 3]]
print(transpose(n))
n=[[1], [2], [3]]
print(transpose(n))
n=[[1, 2], [3, 4]]
print(transpose(n))
n=[]
print(transpose(n))
n=[[1, 2], [3]]
print(transpose(n))
print('row_sums')
n=[[1, 2, 3], [4, 5, 6]]
print(row_sums(n))
n=[[-1, 1], [10, -10]]
print(row_sums(n))
n=[[0, 0], [0, 0]]
print(row_sums(n))
n=[[1, 2], [3]]
print(row_sums(n))
print('col_sums')
n=[[1, 2, 3], [4, 5, 6]]
print(col_sums(n))
n=[[-1, 1], [10, -10]]
print(col_sums(n))
n=[[0, 0], [0, 0]]
print(col_sums(n))
n=[[1, 2], [3]]
print(col_sums(n))