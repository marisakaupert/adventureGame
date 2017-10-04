class ReadDescriptions():
    """ Class to parse room descriptions
    """

    def readFile(self, inFile=None):
        inFile = 'roomDescriptions.txt'

        with open(inFile, 'rb') as descriptions:
            for count, line in enumerate(descriptions):
                return line

        descriptions.close()
