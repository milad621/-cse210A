# cse210A
A simpler parser and interpreter for the ARITH language. It parses the input to AST (Abstract Syntax Tree), and then interpret the AST to compute the value. 

In order to run:
`
	make run
`

If you're running with test script at https://github.com/versey-sherry/cse210A-asgtest, simply use `make` to create a single executable file. Code changes should be applied to `single_file.py` separately. This file is created because Pyinstaller failed to import all classes from different files. 
