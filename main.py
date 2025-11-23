Grid = list[list[int]]
NAVIGABLE = 0


def flood_fill(grid: Grid, x: int, y: int, color: int) -> None:
    rows = len(grid)
    cols = len(grid[0])
    
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if grid[x][y] != NAVIGABLE:
        return
    
    grid[x][y] = color
    
    row_down = x + 1
    row_up = x - 1
    col_right = y + 1
    col_left = y - 1

    flood_fill(grid, row_down, y, color)
    flood_fill(grid, row_up, y, color)
    flood_fill(grid, x, col_right, color)
    flood_fill(grid, x, col_left, color)


def map_terrain(grid: Grid, start_x: int, start_y: int) -> None:
    if not grid:
        raise ValueError('O grid não pode estar vazio')
        
    current_color = 2
    
    if grid[start_x][start_y] == NAVIGABLE:
        flood_fill(grid, start_x, start_y, current_color)
        current_color += 1
    
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == NAVIGABLE:
                flood_fill(grid, i, j, current_color)
                current_color += 1


def print_grid(grid: Grid) -> None:
    for row in grid:
        print(row)


if __name__ == '__main__':
    tests = [
        {
            'grid': [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ],
            'start': (0, 0)
        },
        {
            'grid': [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            'start': (1, 1)
        },
        {
            'grid': [
                [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]
            ],
            'start': (0, 0)
        }
    ]
    
    for i, test in enumerate(tests, 1):
        grid = test['grid']
        start_x, start_y = test['start']
        
        print(f'=== Teste {i} ===')
        print('Grid Inicial:')
        print_grid(grid)
        
        map_terrain(grid, start_x, start_y)
        
        print('\nGrid Final:')
        print_grid(grid)
        print('-' * 20)
