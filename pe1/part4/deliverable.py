#!/usr/bin/env python3

def read_pgm(filename):
    with open(filename, 'r') as fp:
        #temp_str = fp.read()
        temp_str = fp.read().split()  
    #meta_data = temp_str.split()[:4]
    #pixel_data = temp_str.split()[4:]
    #image_content = (meta_data, pixel_data)
    image_content = (temp_str[:4], temp_str[4:])
    return image_content

def write_pgm(filename,content):
    with open(filename, 'w') as fp:
        [fp.write(items+ '\n') for items in content[0] + content[1]]
        #for headerval in content[0]:
        #    fp.write(headerval + '\n')
        #for rasterval in content[1]:
        #    fp.write(rasterval + '\n')
def invert(content):
    content[1][:] = [str(255 - int(pixels)) for pixels in content[1]]
    #for index in range(len(content[1])):
    #    content[1][index] = str(255 - int(content[1][index]))

if __name__ == '__main__':
    input_info = read_pgm('plain.pgm')
    invert(input_info)
    write_pgm('plain.pgm', input_info)
    pass
