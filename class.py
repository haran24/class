
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self, point1, point2, color):
        ''' (Rectangle,Point, Point, str) -> None'''
        self.p1=point1
        self.p2=point2
        self.c=color
    def get_color (self):
        '''(Rectangle) -> str'''
        return self.c
    def get_bottom_left(self):
        '''(Rectangle) -> tuple'''
        return self.p1.get()
    def get_top_right(self):
        '''(Rectangle) -> tuple'''
        return self.p2.get()
    def reset_color(self,newColor):
        '''(Rectangle, str) -> None'''
        self.c=newColor
    def get_perimeter(self):
        '''(Rectangle) -> int'''
        return 2*( ((self.p2).get())[0] - ((self.p1).get())[0] + ((self.p2).get())[1] - ((self.p1).get())[1] )
    def get_area(self):
        '''(Rectangle) -> int'''
        return ( ((self.p2).get())[0] - ((self.p1).get())[0] ) * ( ((self.p2).get())[1] - ((self.p1).get())[1] )
    def move(self, dx, dy):
        '''(Rectangle,int,int) -> None'''
        self.p1.move(dx,dy)
        self.p2.move(dx,dy)
    def contains(self,x,y):
        '''(Rectangle,int,int) -> bool'''
        if (self.p1.get()[0]<= x) and (self.p2.get()[0] >= x) and (self.p1.get()[1]<= y) and (self.p2.get()[1] >= y):
            return True
        else:
            return False
    def intersects(self, rectangle):
        '''(Rectangle,Rectangle) -> bool'''
        inx=False
        iny=False
        # Checks x-coordinates
        if (self.p1.get()[0] >= rectangle.p1.get()[0]) and (self.p1.get()[0] <= rectangle.p2.get()[0]):
            inx = True
        elif (rectangle.p1.get()[0] >= self.p1.get()[0]) and (rectangle.p1.get()[0] <= self.p2.get()[0]):
            inx = True
        elif (self.p2.get()[0] >= rectangle.p1.get()[0]) and (self.p2.get()[0] <= rectangle.p2.get()[0]):
            inx = True
        elif (rectangle.p2.get()[0] >= self.p1.get()[0]) and (rectangle.p2.get()[0] <= self.p2.get()[0]):
            inx = True

        # Checks y-coordinates
        if (self.p1.get()[1] >= rectangle.p1.get()[1]) and (self.p1.get()[1] <= rectangle.p2.get()[1]):
            iny = True
        elif (rectangle.p1.get()[1] >= self.p1.get()[1]) and (rectangle.p1.get()[1] <= self.p2.get()[1]):
            iny = True
        elif (self.p2.get()[1] >= rectangle.p1.get()[1]) and (self.p2.get()[1] <= rectangle.p2.get()[1]):
            iny = True
        elif (rectangle.p2.get()[1] >= self.p1.get()[1]) and (rectangle.p2.get()[1] <= self.p2.get()[1]):
            iny = True
        # return true if both inx and iny are true
        return inx and iny
    
    def __str__(self):
        '''(Rectangle) -> str'''
        return "I am a "+ self.c +" rectangle with bottom left corner at "+ str(self.p1.get())+ " and top right corner at "+str(self.p2.get())+"."
    def __repr__(self):
        '''(Rectangle) -> str'''
        return "Rectangle("+str(self.p1)+","+str(self.p2)+",'"+str(self.c)+"')"
    def __eq__(self,other):
        '''(Rectangle) -> bool'''
        return self.p1 == other.p1 and self.p2 == other.p2 and self.c == other.c
class Canvas:
    def __init__(self):
        '''(Canvas) -> None'''
        self.r=[]
    def add_one_rectangle(self, rect):
        '''(Canvas) -> None'''
        self.r.append(rect)
    def count_same_color(self,color):
        '''(Canvas,str) -> int'''
        count = 0
        for i in self.r:
            if color == i.get_color():
                count+=1
        return count
    def total_perimeter(self):
        '''(Canvas) -> int'''
        s=0
        for i in self.r:
            s+=i.get_perimeter()
        return s
    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle'''
        minx=(self.r[0]).get_bottom_left()[0]
        miny=(self.r[0]).get_bottom_left()[1]
        maxx=(self.r[0]).get_top_right()[0]
        maxy=(self.r[0]).get_top_right()[1]
        for i in self.r:
            if i.get_bottom_left()[0] < minx:
                minx = i.get_bottom_left()[0]
            if i.get_bottom_left()[1] < miny:
                miny = i.get_bottom_left()[1]
            if i.get_top_right()[0] > maxx:
                maxx = i.get_top_right()[0]
            if i.get_top_right()[1] > maxy:
                maxy = i.get_top_right()[1]
        return Rectangle(Point(minx,miny),Point(maxx,maxy),'green')
    def common_point(self):
        '''(Canvas) -> bool'''
        i = self.r[0]
        for j in self.r:
            if i.intersects(j)==False:
                return False
        return True
    def __len__(self):
        '''(Canvas) -> int'''
        return len(self.r)
    def __repr__(self):
        '''(Canvas) -> str'''
        s='Canvas(['
        for i in self.r:
            s+=str(i.__repr__())
            if (self.r[-1]!=i):
                s+=", "
        return s+'])'
    

            
