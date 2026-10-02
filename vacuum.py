hill_matrix = [[0, 3, 2, 0], [0, 0, 0, 0], [0, 4, 6, 8], [7, 9, 0, 10]]

simAnn_matrix = [[0, 3, 2, 0], [3, 6, 0, 0], [5, 0, 6, 8], [4, 9, 0, 10]]

def get_neighbors(row, col, max_rows = 4, max_cols = 4):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < max_rows and 0 <= c < max_cols:
            neighbors.append((r, c))
    return neighbors


def hill_climbing(matrix, start = (0, 3)):
    current_row, current_col = start
    current_val = matrix[current_row][current_col]
    path = [(current_row, current_col, current_val)]
    
    while True:
        moved = False
        for r, c in get_neighbors(current_row, current_col):
            if matrix[r][c] > current_val:
                current_row, current_col = r, c
                current_val = matrix[r][c]
                path.append((r, c, current_val))
                moved = True
                break
        if not moved: 
            return (current_row, current_col), current_val, path

position, value, path = hill_climbing(hill_matrix, start = (0, 3))

print("Path taken:")
for step, (r, c, v) in enumerate(path):
    print(f"Step {step}: ({r}, {c}) -> {v}")
print(f"\nStopped at step {step} with value {value}")

