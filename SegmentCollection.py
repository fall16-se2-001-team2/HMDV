class SegmentCollection:
    segments = []                       #holds the collection of segments
    def _init_ (self):
        pass
    def connectSegments(self,key1,key2):#call if two segments are joined with a connector, indicating a range


class Segment:
    range = [2]
    def __init__(self):
        pass
    def __init__(self,type,m,n=-1):
        if n == -1:
            if type == "r":             #greater than i.e.(m,100)
                self.range[0]=m
                self.range[1]= 100
            elif type == "l":           #less than i.e. (o,m)
                self.range[0] = 0
                self.range[1] = m
            else:
                raise ValueError("The value of a segment type was invalid. Valid use is [l, r, s]")
        elif type == "s":                           #line segment [m,n]
            self.range[0] = m
            self.range[1] = n
