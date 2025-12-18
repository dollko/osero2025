# a004/__init__.py
# オセロAIエントリー用（最小構成）

SIZE = 8
EMPTY = '.'
BLACK = 'B'
WHITE = 'W'

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]


def in_board(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def opponent(color):
    return BLACK if color == WHITE else WHITE


def can_flip(board, r, c, color):
    if board[r][c] != EMPTY:
        return False

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        found = False
        while in_board(nr, nc) and board[nr][nc] == opponent(color):
            found = True
            nr += dr
            nc += dc
        if found and in_board(nr, nc) and board[nr][nc] == color:
            return True
    return False


def get_valid_moves(board, color):
    moves = []
    for r in range(SIZE):
        for c in range(SIZE):
            if can_flip(board, r, c, color):
                moves.append((r, c))
    return moves


# =========================
# エントリー関数
# =========================
def myai(board, color):
    """
    board : 8x8 2次元リスト
    color : 'B' or 'W'
    return: (row, col) or (-1, -1)
    """
    moves = get_valid_moves(board, color)
    if not moves:
        return (-1, -1)  # パス

    # 最初の合法手を返すだけの超基本AI
    return moves[0]

