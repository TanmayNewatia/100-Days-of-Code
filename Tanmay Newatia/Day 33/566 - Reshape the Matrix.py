class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        else:
            newarr=[]
            for i in mat:
                for j in i:
                    newarr+=[j]
            newmat=[[0 for i in range(c)]for j in range(r)]
            k=0
            for i in range(r):
                for j in range(c):
                    newmat[i][j]=newarr[k]
                    k+=1
            return newmat