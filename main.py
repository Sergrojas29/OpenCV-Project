from collections import deque

def computeShortestPath(img, start, end):
    rows, cols = img.shape[:2]
    visited = [[False]*cols for _ in range(rows)]
    parent = [[None]*cols for _ in range(rows)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = True

    findNeighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in findNeighbors:
            newR, newC = r + dr, c + dc
            if 0 <= newR < rows and 0 <= newC < cols:
                if not visited[newR][newC] and (img[newR][newC] == [255, 255, 255]).all():
                    queue.append((newR, newC))
                    visited[newR][newC] = True
                    parent[newR][newC] = (r, c)
    
    # Check if end was reached
    if not visited[end[0]][end[1]]:
        return None

    # Reconstruct path
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = parent[at[0]][at[1]]
    path.reverse()
    
    return path if path[0] == start else None




