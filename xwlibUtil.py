""" Xin's own Python Library code, Utilities"""
'''
Copyright @Xin Wang
'''

def copyFile(ff, tf):
    """ Just like the Unix cp command"""
    try:
        with open(ff, 'r') as fromfile:
            with open(tf, 'w') as tofile:
                for line in fromfile:
                    tofile.write(line)
    except IOError:
        print("IO Error\n")

def wc(file):
    """ Just like the Unix wc command"""
    try:
        with open(file) as testfile:
            linecount = 0
            wordcount = 0
            charcount = 0
            for line in testfile:
                linecount += 1
                # count how many words each line
                words = line.split()
                wordcount += len(words)
                for word in words:
                    # different than wc, do not count space
                    charcount += len(word)
        print('\t'+ str(linecount), \
              str(wordcount), \
              str(charcount), \
              file, sep='\t')
    except IOError:
        print("File \"" + file + "\" not found!")

