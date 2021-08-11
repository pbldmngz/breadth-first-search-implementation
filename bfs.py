# Method used: Breadth First Search Algorithm

WALL_CHAR = "#"
EXIT_CHAR = "E"
PATH_CHAR = "."
DIRECTIONS = {
    "rows": [-1, 1, 0, 0],
    "columns": [0, 0, 1, -1],
}
STARTING_POINT = (0, 0)


def bfs_algorithm(matrix: list) -> int or bool:
    MATRIX_SIZE = len(matrix[0])
    END_POINT = (MATRIX_SIZE - 1, MATRIX_SIZE - 1)
    parent = [[PATH_CHAR] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]
    visited = [[False] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]
    starting_row, starting_column = STARTING_POINT
    visited[starting_row][starting_column] = True
    queue_rows, queue_columns = [], []
    queue_rows.append(starting_row)
    queue_columns.append(starting_column)

    move_count = 0
    cells_left = 1
    next_layer_cells = 0

    reached_end = False

    while len(queue_rows):
        rows = queue_rows.pop(0)
        cols = queue_columns.pop(0)

        # check if the program has reached the end
        if END_POINT == (rows, cols):
            reached_end = True  # Target found!
            return move_count
        # else: keep exploring
        for dir_row, dir_col in zip(DIRECTIONS["rows"], DIRECTIONS["columns"]):
            row = rows + dir_row
            col = cols + dir_col
            if row < 0 or col < 0:
                continue
            if row >= MATRIX_SIZE or col >= MATRIX_SIZE:
                continue
            if visited[row][col]:
                continue
            if matrix[row][col] == WALL_CHAR:
                continue
            queue_rows.append(row)
            queue_columns.append(col)
            visited[row][col] = True
            parent[row][col] = [rows, cols]
            next_layer_cells += 1
        cells_left -= 1
        if cells_left == 0:
            cells_left = next_layer_cells
            next_layer_cells = 0
            move_count += 1
    if reached_end:
        return move_count
    else:
        return False


def main(matrix: list, max_movements: int) -> str:
    result = bfs_algorithm(matrix)
    if not result or result > max_movements:
        return "NO"
    return "YES"


test_map = [
    [".", ".", ".", ".", ".", "."],
    ["#", "#", "#", "#", ".", "#"],
    [".", "#", ".", ".", ".", "."],
    [".", "#", ".", "#", "#", "#"],
    [".", ".", ".", ".", ".", "."],
    [".", "#", "#", "#", "#", "."],
]

print(main(test_map, 13))
