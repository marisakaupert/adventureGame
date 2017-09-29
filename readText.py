class ReadDescriptions():
    """ Class to parse room descriptions
    """

    def readFile(self, inFile=None):
        inFile = 'roomDescriptions.txt'

        with open(inFile, 'r') as descriptions:
            for line in descriptions:
                print line
                