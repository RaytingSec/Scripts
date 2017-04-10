import sys
import os
import hashlib
from difflib import ndiff

h = """Generate sha256sum and compare with input string.
\tusage: checksha256 <file path> <checksum>
"""

# Arg checks

if len(sys.argv) != 3:
    print(h)
    sys.exit('Incorrect number of parameters')

filepath = sys.argv[1]
filename = os.path.split(filepath)[1]
if not os.path.isfile(filepath):
    sys.exit("File doesn't exist:\n" + filepath)


def sha256sum(filepath, bs=8192):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(bs), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def linediff(a, b):
    """ neat wrapper for ndiff, diff of two lines of text, return result as string """
    diff = ndiff([a + '\n'], [b + '\n'])
    return ''.join(diff)


checksum = sha256sum(filepath)
if checksum == sys.argv[2]:
    print('Pass: ' + filename)
else:
    print('Checksum mismatch!\n\t{}\n\nInput and calculated:\n{}'.format(filename, linediff(sys.argv[2], checksum)))
