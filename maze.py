import time

from cell import Cell

class Maze:
	def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
		self._cells = []
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._window = window

		self._create_cells()
	
	def _create_cells(self):
		for col in range(self._num_cols):
			self._cells.append([])
			for row in range(self._num_rows):
				cell = Cell(self._window)
				self._cells[col].append(cell)
				self._draw_cell(col, row)

	def _draw_cell(self, i ,j):
		if not self._window:
			return

		cell_x1 = self._x1 + j * self._cell_size_x
		cell_y1 = self._y1 + i * self._cell_size_y
		cell_x2 = self._x1 + (j + 1) * self._cell_size_x
		cell_y2 = self._y1 + (i + 1) * self._cell_size_y
		self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)

		self._animate()

	def _animate(self):
		if not self._window:
			return

		self._window.redraw()
		time.sleep(0.05)
