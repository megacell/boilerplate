#!/usr/bin/env python
"""
This Giraffe class demonstrates some good practices for structuring research
code projects. For readability, lines are truncated at 80 characters. For
our projects, we use 4-space tabs.

More precisely, this Giraffe class draws a GirASCII with a random height.

REFERENCES
Python Coding Guidelines: [http://web.archive.org/web/20111010053227/http://
                jaynes.colorado.edu/PythonGuidelines.html#module_formatting]
PEP8 Style Guide for Python Code [https://www.python.org/dev/peps/pep-0008/]
More GirASCII [http://www.heartnsoul.com/ascii_art/giraffes.txt]
"""

# IMPORTS
# Import built-in modules first, followed by third-party modules, followed by
# any changes to the path and your own modules.
import random

import numpy as np

# Then follows authorship information
__author__ = "cathywu, yuanchenyang"


class Giraffe:

    def __init__(self, height=3, seed=None):
        self.height = height + random.randint(0,10)
        self.seed = seed

        # Declare object variables here, even if they aren't initialized here
        self.neck = ''

    def draw(self):
        neck = False
        with open('data.txt') as in_file:
            for line in in_file:
                if line == '<<<\n':
                    neck = True
                elif line == '>>>\n':
                    neck = False
                    for i in range(self.height):
                        print self.neck,
                elif neck:
                    self.neck = "%s%s" % (self.neck, line)
                else:
                    print line,

if __name__ == "__main__":
    # For reproducible results, set or save your seed to the random number
    # generator
    import sys
    myseed = random.randint(0, sys.maxint)
    # np.random.seed(myseed)  # If you're using numpy's random module
    random.seed(myseed)

    g = Giraffe(seed=myseed)
    g.draw()
    print "Random seed: %s" % g.seed
