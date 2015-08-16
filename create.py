# Creates a file with name given. May fail horribly. Don't cry.

import sys

filename = sys.argv[1]
f = open(filename, "xt")
f.close()
print("I think it worked.")