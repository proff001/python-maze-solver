import time
import random

from cell import Cell

class Maze:
	def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
		self._cells = []
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._window = window

		if seed:
			random.seed(seed)

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)
		self._reset_cells_visited()
	
	def _create_cells(self):
		for row in range(self._num_rows):
			self._cells.append([])
			for col in range(self._num_cols):
				cell_x1 = self._x1 + col * self._cell_size_x
				cell_y1 = self._y1 + row * self._cell_size_y
				cell_x2 = cell_x1 + self._cell_size_x
				cell_y2 = cell_y1 + self._cell_size_y
				cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2, self._window)
				self._cells[row].append(cell)
				self._draw_cell(row, col) 

	def _draw_cell(self, i ,j):
		if not self._window:
			return

		self._cells[i][j].draw()

		self._animate()

	def _animate(self):
		if not self._window:
			return

		self._window.redraw()
		time.sleep(0.05)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0, 0)
		self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
		self._draw_cell(self._num_rows - 1, self._num_cols - 1)

	def _break_walls_r(self, i, j):
		self._cells[i][j].visited = True

		while True:
			to_visit = []

			if i > 0 and not self._cells[i - 1][j].visited:
				to_visit.append((i - 1, j))
			if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
				to_visit.append((i + 1, j))
			if j > 0 and not self._cells[i][j - 1].visited:
				to_visit.append((i, j - 1))
			if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
				to_visit.append((i, j + 1))

			if len(to_visit) == 0:
				self._draw_cell(i, j)
				return

			next = to_visit[random.randrange(len(to_visit))]

			if next[0] == i + 1:
				self._cells[i][j].has_bottom_wall = False
				self._cells[i + 1][j].has_top_wall = False
			if next[0] == i - 1:
				self._cells[i][j].has_top_wall = False
				self._cells[i - 1][j].has_bottom_wall = False
			if next[1] == j + 1:
				self._cells[i][j].has_right_wall = False
				self._cells[i][j + 1].has_left_wall = False
			if next[1] == j - 1:
				self._cells[i][j].has_left_wall = False
				self._cells[i][j - 1].has_right_wall = False
			
			self._break_walls_r(next[0], next[1])

	def _reset_cells_visited(self):
		for row in self._cells:
			for cell in row:
				cell.visited = False

	def solve(self):
		return self._solve_r(0, 0)

	def _solve_r(self, i, j):
		self._animate()
		self._cells[i][j].visited = True

		current = self._cells[i][j]

		if i == self._num_rows - 1 and j == self._num_cols - 1:
			return True
		if i > 0 and not current.has_top_wall and not self._cells[i - 1][j].visited:
			self._cells[i][j].draw_move(self._cells[i - 1][j])
			if not self._solve_r(i - 1, j):
				self._cells[i][j].draw_move(self._cells[i - 1][j], True)
			else:
				return True
		if i < self._num_rows - 1 and not current.has_bottom_wall and not self._cells[i + 1][j].visited:
			self._cells[i][j].draw_move(self._cells[i + 1][j])
			if not self._solve_r(i + 1, j):
				self._cells[i][j].draw_move(self._cells[i + 1][j], True)
			else:
				return True
		if j > 0 and not current.has_left_wall and not self._cells[i][j - 1].visited:
			self._cells[i][j].draw_move(self._cells[i][j - 1])
			if not self._solve_r(i, j - 1):
				self._cells[i][j].draw_move(self._cells[i][j - 1], True)
			else:
				return True
		if j < self._num_cols - 1 and not current.has_right_wall and not self._cells[i][j + 1].visited:
			self._cells[i][j].draw_move(self._cells[i][j + 1])
			if not self._solve_r(i, j + 1):
				self._cells[i][j].draw_move(self._cells[i][j + 1], True)
			else:
				return True

		return False
