
class Segment:
    range = [2]
    def __init__(self):
        pass
    #   Segment(string, float, float:optional)
    #    type parameter meanings:
    #       s -> (m,n) #segment
    #       r -> (n,100) #greater than
    #       l -> (0,n)  #less than
    #       m-n -> s  #defined segment
    #       obsolute ~~~~n -> n      #defined year
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

##############################################################################
#   SegmentCollection
#       purpose: determine a final range from a collection of segments
#
class SegmentCollection:
    segments = []                       #holds the collection of segments
    def _init_ (self):
        pass
    ############################################
    # spanSegments(segment, segment)
    # purpose: combines two segments into a segment that spans
    def spanSegments(self,s1, s2):#call if two segments are joined with a connector, indicating a range
        segment = Segment()
        self.segments.remove(s1.key)
        self.segments.remove(s2.key)
        self.segments.append(segment)
