class Segment:
    segment = [2]
    def __init__(self):
        pass
    def __init__(self,type,m,n=-1):
        if n == -1:
            if type == "r":#greater than i.e.(n,100)
                self.segment[0]=m
                self.segment[1]= 100
            elif type == "l":  #less than i.e. (o,n)
                self.segment[0] = 0
                self.segment[1] = m
            else:
                print ("Error")
        else:           #line segment [m,n]
            self.segment[0] = m
            self.segment[1] = n

class PopConstraint:

    #--------------------------------------------------
    #ageConstraint(String)
    #Purpose: given a string, determine the bounds placed on the age, if any
    #returns: -1 if no age constraint
    #          returns Segment if age constraint found
    #-------------------------------------------------------------
    @staticmethod
    def ageConstraint(eligibility):
        ageIdentifiers = {'ages of $"': 's',
                          'senior $': 'r',
                          'seniors $': 'r',
                          'elderly': 'r',
                          'birth $': 'l',  # birth indicates (0,n) age
                          'age $': 's',
                          'ages $': 's',
                          '$ children $': 's',
                          'adults $': 'r',
                          '$ grade $': 's',  # need to add 5 to grade number
                          '$ grades $': 's',  # same here, add 5
                          'infant': 'l',
                          'infants': 'l',
                          'toddler': 'l',
                          'toddlers': 'l',
                          'young $': '',  # maybe not?
                          'youth': '(2,18)',  # static?
                          'youths': '(2,18)',  # static?
                          'pre k': '(0,4)',  # static?
                          'pre-k': '(0,4)',
                          'school aged': '(5,18)',
                          '$ through $': 's',
                          '$-$': 's',  # possibly need to consider weird spacing
                          '$ to $': 's',
                          '$ and $': 's',
                          '$ and older': 'r',
                          '$ and under': 'l',
                          '$ and younger': 'l',
                          '$ and up': 'r',
                          'up to $': 'l',
                          'down to $': 'r',
                          '$+': 'r'}
        pass