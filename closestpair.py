#coding: utf-8
import Tkinter
class Tkwin:
    def __init__(self, root):
        self.root = root
        self.points = []
        self.root.bind('<Button-1>', self.action)
    def action(self, event):
        s = "Last point clicked at x=%s  y=%s" % (event.x, event.y)
        self.root.title(s)
        self.points.append([event.x, event.y])
        if len(self.points) >=2 :
            self.closest_pair()
    def closest_pair(self):
        w.create_line(self.points[len(self.points)-1][0], self.points[len(self.points)-1][1], self.points[len(self.points)-2][0],self.points[len(self.points)-2][1])


root = Tkinter.Tk()

w = Tkinter.Canvas(root, width=1280, height=9600, bg = 'white')
w.pack()
window = Tkwin(root)
root.minsize(1280,960)
root.maxsize(1280,960)
root.mainloop()
