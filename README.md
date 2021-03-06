# boilerplate
This serves both as boilerplate for starting new research code projects as
well as a examples of good coding practices.

Usage
====
To try out the boilerplate, run

    python boilerplate/Giraffe.py

But actually the point is to read through `src/Giraffe.py` and
`tests/fast/test_giraffe.py`.
    
Testing
====
To run the tests:

    python -m unittest discover

To run only the fast (eg. unit) tests:

    python -m unittest discover tests/fast

To run only the slow (eg. integration) tests:

    python -m unittest discover tests/slow

Development
====
* For this project, and any derived from it, please run the following command
  from the project root directory (for Unix-based systems):

      ln -s ../../pre-commit.sh .git/hooks/pre-commit

  In Windows, the easiest thing seems to be to rename the file as `pre-commit` and copy it directly to `.git/hooks/pre-commit`. You may need to enable viewing of file extensions in the File Explorer.
* Please add any additional good practices to this repository.
* Write unit tests as you go. Document as you go.
* Run all unit tests before you push any code.

References
====
* [Python Coding Guidelines](http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting)
* [PEP8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
