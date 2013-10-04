#coding: utf-8
import Tkinter
from closest import closestpair
class Tkwin:
    def __init__(self, root):
        self.root = root
        self.points = []
        self.line = None
        self.root.bind('<Button-1>', self.action)
    def action(self, event):
        s = "Last point clicked at x=%s  y=%s" % (event.x, event.y)
        self.root.title(s)
        w.create_rectangle(event.x, event.y, event.x, event.y)
        self.points.append([event.x, event.y])
        if len(self.points) >=2 :
            self.closest_pair()
    def closest_pair(self):
        if self.line is not None:
            w.delete(self.line)
        ans = closestpair(self.points)
        self.line = w.create_line(ans[0][0], ans[0][1], ans[1][0], ans[1][1])
        

root = Tkinter.Tk()

w = Tkinter.Canvas(root, width=1280, height=9600, bg = 'white')
w.pack()
window = Tkwin(root)
root.minsize(1280,960)
root.maxsize(1280,960)
root.mainloop()
