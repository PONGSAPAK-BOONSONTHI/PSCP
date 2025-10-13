def main():
    n = int(input())  # แถว
    m = int(input())  # คอลัมน์
    grid = [list(map(int, input().split())) for _ in range(n)]
    view = input().strip()

    max_h = max(max(row) for row in grid)

    if view == "Left":
        for h in range(max_h, 0, -1):
            for row in grid:
                print("x" if max(row) >= h else " ", end=" ")
            print()

    elif view == "Right":
        for h in range(max_h, 0, -1):
            for row in grid[::-1]:  # กลับลำดับแถว
                print("x" if max(row) >= h else " ", end=" ")
            print()

    elif view == "Front":
        for h in range(max_h, 0, -1):
            for c in range(m):
                col = [grid[r][c] for r in range(n)]  # ดึงคอลัมน์
                print("x" if max(col) >= h else " ", end=" ")
            print()

    elif view == "Back":
        for h in range(max_h, 0, -1):
            for c in range(m-1, -1, -1):  # คอลัมน์จากขวาไปซ้าย
                col = [grid[r][c] for r in range(n)]
                print("x" if max(col) >= h else " ", end=" ")
            print()
main()
