import re

pattern = r'[<]\s*[a-zA-Z][a-zA-Z0-9]*\s*([a-zA-Z]+\s*=\s*["].+["]\s*)*\s*[>]'
pat = re.compile(pattern)

def findtags(text):
	def ftags(text, tags):
		m = pat.search(text)
		if (not m): return tags # no tags found
		else:
			tags.append(m.group(0))
			ftags(text[m.end():], tags)
			return tags
	return ftags(text, tags=[])

testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""
text = """<!DOCTYPE html><html><head>
		<title>CS 253 Blog</title></head><body>
	<h1><a href="http://bloggy-app-id.appspot.com/blog">CS 253 Blog</a></h1>
	
	<h2>new post</h2>
	
	<form method="post">
		<label>
			<div>subject</div>
			<input type="text" name="subject" value="{{subject}}">
		</label>
		
		<label>
			<div>blog</div>
			<textarea name="content">{{content}}</textarea>
		</label>
		
		<div class="error">{{error}}</div>
		
		<input type="submit">
	</form>

	</body>"""

def test():
    assert findtags(testtext1) == ['<a href="www.udacity.com">', 
                                   '<b>', 
                                   '<a href="www.udacity.com"target="_blank">']
    assert findtags(testtext2) == []
    assert findtags(testtext3) == ['<         b           >']
    return 'tests pass'

print test()