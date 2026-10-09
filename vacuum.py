import random
import math

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

def sim_annealing(matrix, start=(0,3), temperature=100, min_temperature=.001, cooling_rate=0.95):
    current_row, current_col = start
    current_val = matrix[current_row] [current_col]
    best_position = start
    best_val = current_val
    sim_path = [(current_row, current_col, current_val)]

    max_val = max(max(row) for row in matrix) #calculates the max value since it is known in the matrix
    while temperature > min_temperature:
        neighbors = get_neighbors(current_row, current_col)

        neighbor_row, neighbor_col = random.choice(neighbors)
        neighbor_val = matrix[neighbor_row][neighbor_col]
        delta = neighbor_val - current_val

        if delta >= 0 or random.random() < math.exp(delta / temperature): #delta positive since it is finding the highest dirt value
            current_row, current_col = neighbor_row, neighbor_col
            current_val = neighbor_val

            sim_path.append((current_row, current_col, current_val))

            if current_val > best_val:
                best_val = current_val
                best_position = (current_row, current_col)

            if best_val == max_val: #checks if max value has been found, can cut off early
                break

    return best_position, best_val, sim_path
best_position, best_val, sim_path = sim_annealing(simAnn_matrix, start=(0,3))


print("Path taken:")
for step, (r, c, v) in enumerate(path):
    print(f"Step {step}: ({r}, {c}) -> {v}")
print(f"\nStopped at step {step} with value {value}\n")

print("Simulated Annealing Path taken:")
for an_step, (neighbor_row, neighbor_col, neighbor_val) in enumerate(sim_path):
    print(f"Step: {an_step}: (({neighbor_row}, {neighbor_col}) -> {neighbor_val}")
print(f"\nStopped at step {an_step} with value {neighbor_val}\n")

