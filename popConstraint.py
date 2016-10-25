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

    string = ""
    def __init__(self, string):
        self.string = string
        pass
    #--------------------------------------------------
    #ageConstraint(String)
    #Purpose: given a string, determine the bounds placed on the age, if any
    #returns: -1 if no age constraint
    #          returns Segment if age constraint is found
    #-------------------------------------------------------------
    @staticmethod
    def ageConstraint(eligibility):
        #ageTemplates dictionary value meanings:
            #s -> (m,n) #segment
            #r -> (n,100) #greater than
            #l -> (0,n)  #less than
            #m,n -> s  #defined segment
            #n -> n      #defined year
        '''ageTemplates tries to align with the eligibility string to identify places to look for ages.'''
        ageTemplates= {
                        'from $': 's',
                        'ages of $': 's',
                        'senior $': 'r',
                        'seniors $': 'r',
                        'birth $': 'l',
                        'age $': 's',
                        'ages $': 's',          #if we remove useless words like [ of, to, and, than ] then we can eliminate this one
                        #'$ children $': 's',   #probably not necessary
                        'adults $': 'r',
                        '$ grade $': 's',       # need to add 5 to grade number
                        '$ grades $': 's',      # same here, add 5
                        '$ through $': 's',
                        '$ - $': 's',           # possibly need to consider weird spacing
                        '$ to $': 's',
                        '$ and $': 's',
                        '$ and older': 'r',
                        '$ and under': 'l',     #may be too ambiguous
                        '$ and younger': 'l',
                        '$ and up': 'r',        #may be too ambiguous
                        'up to $': 'l',         #may be too ambiguous
                        'down to $': 'r',       #may be too ambiguous
                        '$+': 'r',
                        'younger than $':'l',
                        'older than $':'r'
                       }
        translations = {
                        'retired': '72,100',        #make research variable?
                        'birth':'0',
                        'preschool':'4',
                        'pre-school':'4',
                        'youth':'2,18',
                        'youths':'2,18',
                        'young':'0,18',
                        'school aged': '5,18',
                        'pre k': '0,4',
                        'pre-k': '0,4',
                        'infant': 'l',
                        'elderly': 'r',
                        'infants': 'l',
                        'toddler': 'l',
                        'toddlers': 'l'
                        }
        timescale = {                           #divisor of preceding numeric translation
                        'months':'12',
                        'years':'1'
                    }



        '''remove the wildcard, leaving only ordered list of words of interest'''
        words = eligibility.split()             #words is list of each word in eligibility string
        #for i in range(words):                      # i is index into eligibility words
        for template in ageTemplates:       #template is the current template that we are searching for
            templateOffset = 0
            tWords = template.split(' ')    #tWords is list of each word in template
            '''find the offset of first identifying word in template'''
            if tWords[0] == '$':            #if the first word is $ then the first identifying word is index = 1
                templateOffset = 1
            for i in range(templateOffset,words):
                if words[i+templateOffset] == tWords[templateOffset]:

                #PopConstraint.parseWildcard(words, i)



        pass
    @staticmethod
    def parseWildcard (words, index):
        word = words[index]
        pass