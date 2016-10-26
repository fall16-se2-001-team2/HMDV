
class PopConstraint:

    string = ""
    def __init__(self, string):
        self.string = string
        pass
    #--------------------------------------------------
    #ageConstraint(String)
    #Purpose: given a string, determine the bounds placed on the age, if any
    #returns: None if no age constraint
    #          returns Segment if age constraint is found
    #-------------------------------------------------------------
    @staticmethod
    def ageConstraint(eligibility):

        #connectors are templates that specify a range
        connectors = {
            '$ grade $': 's',  # need to add 5 to grade number
            '$ grades $': 's',  # same here, add 5
            '$ through $': 's',
            '$ - $': 's',  # possibly need to consider weird spacing
            '$ to $': 's',
            '$ and $': 's'
        }
        #ageTemplates are masks that identify locations that may contain an age
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
        #these sentiments are replaced with a range when a synonym is found
        _infantConstant = '0-4'                 #the age range of a 'baby'
        _elderlyConstant = '78-100'             #the age that considers a person elderly
        _retiredConstant = '73-100'             #the avg age that a person retires
        #translations are words that are associated with a specific age or range
        translations = {
                        'retired': _retiredConstant,
                        'birth':'0',
                        'preschool':'4',
                        'pre-school':'4',
                        'youth':'2-18',
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

        words = eligibility.split()             #words is list of each word in eligibility string
        '''replace translations with text segment'''
        for word in words:
            for key, value in translations:
                if word == key:
                    word = value
        '''remove the wildcard, leaving only ordered list of words of interest'''

        for template in ageTemplates:               #template is the current template that we are searching for
            templateOffset = 0                      #the offset into the template
            tWords = template.split(' ')            #tWords is list of each word in template
            if words.len() == 1:                    #if the template only has one word
                for i in range(words):              # then iteratively move the template over the words list
                    PopConstraint.tryParseWildcard(words,i,template)    #and search for numeric ranges
                    #continue                        #try another template.
            '''find the offset of first identifying word in template'''
            elif tWords[0] == '$':                  #if the first word is $ then the first identifying word is index = 1
                templateOffset = 1                  #skip the first word of eligibility and template
            for i in range(templateOffset,words):   #i indexed loop that places the template over each applicable word
                if words[i] != tWords[templateOffset]:      #if first applicable word doesn't match template
                    if tWords[templateOffset] != '$':
                        continue
                    elif

                elif
                    for j in range(templateOffset,tWords.len()):  #then check to see if the rest of the template matches
                        if tWords[templateOffset] == '$':
                            templateOffset+=1
                            continue
                        elif
                            break
                    if templateOffset == tWords

                    value = ageTemplates.get(tWords[templateOffset])

                templateOffset += 1

                #PopConstraint.parseWildcard(words, i)



        pass
    @staticmethod
    def tryParseWildcard (words, index, template):
        if template.split(' ').len() == 1:              #if the template is one word


        pass