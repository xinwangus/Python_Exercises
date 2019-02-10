'''
A test python program similar to the unix wc command.
    Show the debug capabilities inside Jupyter
'''
from IPython.core.debugger import set_trace
'''
or
from pdb import set_trace
'''

def wc_fn(file):
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

if __name__ == '__main__':
    # debug will stop here first
    set_trace()
    wc_fn("wc.py")
