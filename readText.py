class ReadDescriptions():
    """ Class to parse room descriptions
    """

    def readFile(self, inFile=None):
        inFile = 'roomDescriptions.txt'

        with open(inFile, 'rb') as descriptions:
            line = descriptions.readlines()
            return line

        descriptions.close()
