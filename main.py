from graphics import Window, Line, Point

def main():
	window = Window(800, 600)

	line1 = Line(Point(0, 0), Point(100, 100))
	line2 = Line(Point(100, 100), Point(200, 200))
	line3 = Line(Point(200, 200), Point(300, 300))
	line4 = Line(Point(300, 300), Point(400, 400))
	line5 = Line(Point(400, 400), Point(500, 500))

	window.draw_line(line1, "red")
	window.draw_line(line2, "green")
	window.draw_line(line3, "blue")
	window.draw_line(line4, "yellow")
	window.draw_line(line5, "purple")

	window.wait_for_close()

main()
