# Creates a file with name given. May fail horribly. Don't cry.

import sys

filename = sys.argv[1]+".txt"
f = open(filename, "xt")
f.close()
