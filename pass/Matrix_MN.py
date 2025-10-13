"""Matrix_MN"""
def main():
    """Matrix_MN"""
    m = int(input())
    n = int(input())
    mat = []
    for _ in range(m * n):
        num = int(input())
        mat.append(num)
    count = 0
    for _ in range(m):
        for i in range(n):
            if i == n - 1:
                print(mat[count])
            else:
                print(mat[count], end=" ")
            count += 1
main()
