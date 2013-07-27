These two python files are solutions to two homework problems. 

htmltags.py : a very short program to return a list of html tags in a string; 
uses regular expressions and a nested function
run htmltags.py

regexGrammar.py: considered a **challenge** problem.

>> from regexGrammar import parse_re
>> parse_re("(a|b)*[xyz]+123?")
>> "seq(star(alt(lit('a'), lit('b')))), seq(plus(oneof(xyz)), opt(lit('123'))))"

1. parse a regular expression 
2. interpret it into a given API
For example: 
regular expression: "(a|b)?+" 
	=> parse tree => to api format: plus(opt(alt(lit('a'), lit('b'))))
My work begins at REGRAMMAR (approx line 120). Peter Norvig wrote the grammar and parser functions.
I wrote the RE grammar and the interpreter. Learned a lot about decorators and how to use them in this problem.


