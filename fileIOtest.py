inFile = open("words.txt", 'r')
blocks = inFile.read().split("\n\n")
lines = []
masterLine = ''
for block in blocks:
    sblock = block.split("\n",2)
    try:
        lines.append(sblock[2])
    except IndexError:
        continue
    
subs = open("subs.txt", "w")
for line in lines:
    line = line+"\n\n" 
    subs.write(line)
subs.close()
