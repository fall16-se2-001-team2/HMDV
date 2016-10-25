
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
                        '$yo': 's',             #one specific year -> segment($,$)
                        'younger than $':'l',
                        'older than $':'r'
                       }
        _infantConstant = '0-4'                 #the age range of a 'child'
        _elderlyConstant = '78-100'             #the age that considers a person elderly
        _retiredConstant = '73-100'             #the avg age that a person retires
        translations = {
                        'retired': _retiredConstant,        #make research variable?
                        'birth':'0',
                        'preschool':'4',
                        'pre-school':'4',
                        'youth':'2-8',
                        'youths':'2-18',
                        'young':'0-18',
                        'school aged': '5-18',
                        'pre k': '4yo',             #should this just be 4?
                        'pre-k': '4yo',
                        'infant': _infantConstant,
                        'infants': _infantConstant,
                        'toddler': _infantConstant,
                        'toddlers': _infantConstant,
                        'elderly': _elderlyConstant
                        }
        timescale = {                           #divisor of preceding numeric translation
                        'months':'12',
                        'years':'1'
                    }

        '''replace translations with text segment'''
        for word in eligibility.split():
            for key, value in translations:
                if word == key:
                    word = value
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
                if words[i] == tWords[templateOffset]:

                #PopConstraint.parseWildcard(words, i)



        pass
    @staticmethod
    def parseWildcard (words, index):
        word = words[index]
        pass