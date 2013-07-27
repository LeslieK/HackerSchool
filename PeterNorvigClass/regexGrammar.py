import re


"""
parse/convert regular expression to API
"(a|b)?+" => parse tree => to api format: plus(opt(alt(lit('a'), lit('b'))))
My work begins at REGRAMMAR (approx line 120). Peter Norvig wrote the grammar and parser functions.
I wrote the RE grammar and the interpreter.

>> from regexGrammar import parse_re
>> parse_re("(a|b)*[xyz]+123?")
>> "seq(star(alt(lit('a'), lit('b')))), seq(plus(oneof(xyz)), opt(lit('123'))))"

"""


from functools import update_wrapper
import re

## split, grammar, decorator, memo, trace written by Peter Norvig
def split(text, sep=None, maxsplit=-1):
    """Performs str.split() on text, then str.strip() on each split piece."""
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

def grammar(description, whitespace=r'\s*'):
    """Convert a description to a grammar.  Each line is a rule for a
    non-terminal symbol; it looks like this:
        Symbol =>  A1 A2 ... | B1 B2 ... | C1 C2 ...
    where the right-hand side is one or more alternatives, separated by
    the '|' sign.  Each alternative is a sequence of atoms, separated by
    spaces.  An atom is either a symbol on some left-hand side, or it is
    a regular expression that will be passed to re.match to match a token.
    
    Notation for *, +, or ? not allowed in a rule alternative (but ok
    within a token). Use '\' to continue long lines.  You must include spaces
    or tabs around '=>' and '|'. That's within the grammar description itself.
    The grammar that gets defined allows whitespace between tokens by default;
    specify '' as the second argument to grammar() to disallow this (or supply
    any regular expression to describe allowable whitespace between tokens)."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G

def disabled(f):
    "disables a decorator; ex: trace = disabled"
    return f

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, args[1])
        #signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f

## The parser (written by Peter Norvig)
#@trace
def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    @memo
    def parse_atom(atom, text):
        if atom in grammar:  # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None:
                    return [atom]+tree, rem  
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    
    # Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

## My work
REGRAMMAR = grammar(""" 
RE              => simple-RE [|] RE | simple-RE
simple-RE       =>  unit-RE simple-RE | unit-RE
unit-RE         =>  star-unit | plus-unit | opt-unit | unit0-RE
star-unit       =>  unit0-RE [*]
plus-unit       =>  unit0-RE [+]
opt-unit        =>  unit0-RE [?]
unit0-RE        =>  group | any | eos | LIT | oneof
group           =>  [(] RE [)]
any             =>  [.]
eos             =>  [$]
oneof           =>  pos-set | neg-set
pos-set         =>  [[] set-item []]
neg-set         =>  [[] [\^] set-item []]
#set-items       =>  set-item set-items | set-item
set-item        =>  [a-zA-Z0-9_]+ 
LIT             =>  [a-zA-Z0-9_]+
""", whitespace='')

def parse_re(pattern):
	return convert(parse("RE", pattern, REGRAMMAR))

LPAREN = '('
RPAREN = ')'

def convert(tree):
    # ( [RE, [simple-RE, ], [simple-RE, ] [simple-RE, ]] ) # remove from tuple
    def interpret(tree):
        if not tree: return
        nodetype = tree[0]
        t = tree[1:][0]

        if nodetype == 'RE':
            if len(tree) == 4:
                left_tree = tree[1]
                right_tree = tree[3]
                return 'alt' + LPAREN + interpret(left_tree) + ', ' + interpret(right_tree) + RPAREN
            else:
                return interpret(t)
        elif nodetype == 'simple-RE':
            if len(tree) == 3:
                left_tree = tree[1]
                right_tree = tree[2]
                return 'seq' + LPAREN + interpret(left_tree) + ', ' + interpret(right_tree) + RPAREN
            else:
                return interpret(t)
        elif nodetype == 'unit-RE':
            return interpret(t)
        elif nodetype == 'star-unit':
            return 'star' + LPAREN + interpret(t) + RPAREN
        elif nodetype == 'plus-unit':
            return 'plus' + LPAREN + interpret(t) + RPAREN
        elif nodetype == 'opt-unit':
            return 'opt' + LPAREN + interpret(t) + RPAREN
        elif nodetype == 'unit0-RE':
            atom = t[0]
            if atom == 'LIT':
                val = t[1]
                return("""lit('{0}')""".format(val))
            elif atom == 'group':
                # convert RE
                return LPAREN + interpret(t[2]) + RPAREN
            elif atom == "any":
                return 'dot'
            elif atom == 'eos':
                return 'eol'
            elif atom == 'oneof':
                set_type = t[1][0]
                if set_type == 'pos-set':
                    return 'oneof' + LPAREN + interpret(t[1][2]) + RPAREN
                else:
                    return 'oneof' + LPAREN + '^' + interpret(t[1][2]) + RPAREN
        elif nodetype == 'set-item':
                return t
        else:
            print "%s does not exist" % nodetype
    return interpret(tree[0])

#[RE, [simple-RE, [unit-RE, [star, [unit0-RE, [group, ["(", [simple-RE, [unit-RE, [unit0-RE, [lit, 'abc']]]], "|", [RE, [simple-RE, [unit-RE, [unit0-RE, [lit, 'da']]]]], ")"]]"*"]]]]]
def printG(grammar):
    for k in grammar.keys():
        print '{:<12}: {:<12}'.format(k, grammar[k])

