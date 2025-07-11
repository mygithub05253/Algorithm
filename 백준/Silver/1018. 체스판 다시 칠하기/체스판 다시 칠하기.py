def count_repaints(board, start_row, start_col):
    repaint_W_start = 0  # W로 시작
    repaint_B_start = 0  # B로 시작

    for i in range(8):
        for j in range(8):
            current = board[start_row + i][start_col + j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    repaint_W_start += 1
                if current != 'B':
                    repaint_B_start += 1
            else:
                if current != 'B':
                    repaint_W_start += 1
                if current != 'W':
                    repaint_B_start += 1

    return min(repaint_W_start, repaint_B_start)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaint = float('inf')

# 모든 가능한 8x8 구간에 대해 확인
for i in range(N - 7):
    for j in range(M - 7):
        repaints = count_repaints(board, i, j)
        min_repaint = min(min_repaint, repaints)

print(min_repaint)