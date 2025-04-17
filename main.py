from collections import deque

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    prev = [[None]*cols for _ in range(rows)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, down, left, right

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    prev[nr][nc] = (r, c)

    # reconstruct path
    path = []
    at = end
    while at:
        path.append(at)
        at = prev[at[0]][at[1]]
    path.reverse()

    return path if path[0] == start else None
