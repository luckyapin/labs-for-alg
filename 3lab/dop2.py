import heapq
from random import randint

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def a_star(matrix, start, end):
    open_list = [(0, start)]
    closed_list = set()
    g_scores = {start: 0}
    came_from = dict()

    while open_list:
        cost, current = heapq.heappop(open_list)
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        closed_list.add(current)
        x, y, z = current
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]) or nz < 0 or nz >= len(matrix[0][0]):
                continue
            neighbor = (nx, ny, nz)
            if neighbor in closed_list:
                continue

            tentative_g_score = g_scores[current] + matrix[x][y][z]
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                h_score = manhattan_distance(neighbor, end)
                heapq.heappush(open_list, (tentative_g_score + h_score, neighbor))

    return None

X, Y, Z = 3,3,3
matrix = [[[randint(1, 10) for z in range(Z)] for y in range(Y)] for x in range(X)]

print(matrix)
shortest_path = a_star(matrix, (0, 0, 0), (X - 1, Y - 1, Z - 1))
print(shortest_path)