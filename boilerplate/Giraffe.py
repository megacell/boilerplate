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
        # Store the seed, so if we save the object, we can recover the seed
        # and reproduce the results; generate a seed if we're not given one
        if seed is None:
            import sys
            self.seed = random.randint(0, sys.maxint)
        else:
            self.seed = seed
        # np.random.seed(self.seed)  # If you're using numpy's random module
        random.seed(self.seed)

        # Generate the height of the giraffe
        self.height = height + random.randint(0,10)

        # Declare object variables here, even if they aren't initialized here
        self.neck = ''

    def draw(self):
        """
        Draws the GirASCII
        """
        neck_detected = False
        with open('data.txt') as in_file:
            for line in in_file:
                if line == '<<<\n':
                    neck_detected = True
                elif line == '>>>\n':
                    neck_detected = False
                    for i in range(self.height):
                        print self.neck,
                elif neck_detected:
                    self.neck = "%s%s" % (self.neck, line)
                else:
                    print line,

if __name__ == "__main__":
    # For reproducible results, set or save your seed to the random number
    # generator

    g = Giraffe()
    g.draw()
    print "Random seed: %s" % g.seed
