#!/usr/bin/env python3

with open('/etc/passwd') as src, open('passwd','w') as dst:
    for line in src:
        fields = line.split(':')
        if fields[0] == 'root':
            fields[-1] = '/bin/sh\n'
            line = ':'.join(fields)
        dst.write(line)
