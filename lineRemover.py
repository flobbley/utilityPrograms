WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    loads document in the form of a list where each line is a new list item
    """
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readlines()
    return line

def indexes():
    """
    returns indexes of the items in the document list that should be removed
    Indexes follow the pattern of:
    [0,1,4,5,8,9,12,13..]
    """
    indexes = []
    count = 0
    for i in range(1700):#rough length of the subtitles is 1700 lines
        if i%2 == 0:
            count = i*2 #if i is even, then the corresponding index of the item to be removed is 2*i
        else:
            count+=1 #if i is not even, then the corresponding index is 1 plus the last index
        indexes.append(count)
    return indexes

def remover():
    """
    removes lines from the subtitles using the indexes obtained from indexes()
    """
    line = loadWords() #loads the subtitle list
    lineCopy = line[:] #creates a copy of the list to be changed
    indices = indexes() #loads the indexes of items to be removed
    for index in indices:
        try:
            lineCopy.remove(line[index]) #removes the lines of the indexes
        except IndexError: #ends when it runs out of lines
            break
    return lineCopy

def writer():
    """
    Writes the subtitles without numbers or times to a file
    """
    file = open("file.txt","w")
    lines = remover()
    for sentence in lines:
        file.write(sentence)
