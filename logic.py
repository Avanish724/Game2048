import random

def start_game():
  mat = []
  for i in range(4):
    mat.append([0]*4)
  return mat

def add_new_two(mat):
  r = random.randint(0,3)
  c = random.randint(0,3)
  while mat[r][c] != 0:
    r = random.randint(0,3)
    c = random.randint(0,3)
  mat[r][c] = 2
  return mat

def get_curr_state(mat):
  for i in range(4):
    for j in range(4):
      if mat[i][j] == 2048:
        return "WON" 

  for i in range(4):
    for j in range(4):
      if mat[i][j] == 0:
        return "GAME NOT OVER"

  for i in range(3):
    for j in range(3):
      if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
        return "GAME NOT OVER"

  for j in range(3):
    if mat[j][3] == mat[j+1][3]:
      return "GAME NOT OVER"      

  for i in range(3):
    if mat[3][i] == mat[3][i+1]:
      return "GAME NOT OVER" 

  return "LOST"

def compress(mat):
  changed = False
  new_mat = []
  for i in range(4):
    new_mat.append([0]*4)

  for i in range(4):
    pos = 0
    for j in range(4):
      if mat[i][j] != 0:
        new_mat[i][pos] = mat[i][j]
        if j != pos:
          changed = True
        pos = pos + 1
        
  return new_mat, changed

def merge(mat):
  changed = False
  for i in range(4):
    for j in range(3):
      if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
        mat[i][j] = mat[i][j]*2
        mat[i][j+1] = 0
        changed = True
  return mat, changed

def reverse(mat):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[i][4-j-1])
  return new_mat    

def transpose(mat):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[j][i])
  return new_mat

def move_left(grid):
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  return new_grid, changed

def move_right(grid):
  reverse_grid = reverse(grid)
  new_grid, changed1 = compress(reverse_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  final_grid = reverse(new_grid)
  return final_grid, changed

def move_up(grid):
  transpose_grid = transpose(grid)
  new_grid, changed1 = compress(transpose_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  final_grid = transpose(new_grid)
  return final_grid, changed  

def move_down(grid):
  transpose_grid = transpose(grid)
  reverse_grid = reverse(transpose_grid)
  new_grid, changed1 = compress(reverse_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  final_reverse_grid = reverse(new_grid)
  final_grid = transpose(final_reverse_grid)
  return final_grid, changed