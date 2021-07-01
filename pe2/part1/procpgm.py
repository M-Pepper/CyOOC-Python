import string
import io

def readAsciiVal(pgm):
    lettersandnumbers = bytearray(string.ascii_letters + string.digits, 'utf-8')
    whitespace = bytearray(string.whitespace, 'utf-8')
    cont = pgm['content']
    start = pgm['start']
    length = pgm['length']
    readval = []
    tossComment = False
    for i in range(start, length):
        if tossComment:
            if cont[i] == ord('\n') or cont[i] == ord('\r'):
                tossComment = False
        elif cont[i] == ord('#'):
            #when this occurs, a comment has started
            #Read the entire comment up to the linefeed
            tossComment = True
        elif cont[i] in lettersandnumbers:
            #This is part of a value to return
            readval.append(cont[i])
        elif cont[i] in whitespace:
            #This is exclusive of something to be returned
            if len(readval) > 0:
                #Prep for return
                pgm['start'] = i + 1
                return bytearray(readval).decode('utf-8')

def getPixel(pgm):
    if pgm['start'] >= pgm['length']:
        return None
    pixel = pgm['content'][pgm['start']]
    pgm['start'] = pgm['start'] + 1
    return pixel

def getPgm(filename):
    pgm = {}
    with open(filename, 'rb') as fp:
        pgm['content'] = fp.read()
        pgm['start'] = 0
        pgm['length'] = len(pgm['content'])
        pgm['magic'] = readAsciiVal(pgm)
        pgm['width'] = readAsciiVal(pgm)
        pgm['height'] = readAsciiVal(pgm)
        pgm['maxpixel'] = readAsciiVal(pgm)
    return pgm

if __name__ == '__main__':
    #filename = 'screenshot.pgm'
    filename = 'crazy.pgm'
    pgm = getPgm(filename)
    print('Magic {}'.format(pgm['magic']))
    print('Width {}'.format(pgm['width']))
    print('Height {}'.format(pgm['height']))
    print('MaxVal {}'.format(pgm['maxpixel']))
    #for _ in range(0x10):
    #    print('pixel {:x}'.format(getPixel(pgm)))
    for _ in range(0x10):
        print('Pixels: {}'.format( ' '.join(['{:x}'.format(getPixel(pgm)) for _ in range(0x10)]) ))

