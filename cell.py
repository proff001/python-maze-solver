from graphics import Point, Line

class Cell:
	def __init__(self, x1, y1, x2, y2, window=None):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self.visited = False
		self._window = window
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2

	def draw(self):
		if not self._window:
			return

		if self.has_left_wall:
			self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
		else:
			self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")
		if self.has_right_wall:
			self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
		else:
			self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white")
		if self.has_top_wall:
			self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
		else:
			self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")
		if self.has_bottom_wall:
			self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
		else:
			self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")

	def draw_move(self, to_cell, undo=False):
		if not self._window:
			return

		color = "red" 
		if undo:
			color = "gray"

		self_half = abs(self._x2 - self._x1) / 2
		to_cell_half = abs(to_cell._x2 - to_cell._x1) / 2

		current_cell_center = Point(self._x1 + self_half, self._y1 + self_half)
		to_cell_center = Point(to_cell._x1 + to_cell_half, to_cell._y1 + to_cell_half)

		self._window.draw_line(Line(current_cell_center, to_cell_center), color)
