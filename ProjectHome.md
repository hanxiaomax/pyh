**Code your webpage like a GUI!**

PyH allows you to simply generate HTML pages from within your python code in an object-oriented fashion. Each HTML tag is an object that can be modified at any time. The HTML tags are neatly output so that the sources of your HTML files are human-readable. Check the [Wiki](http://code.google.com/p/pyh/wiki/UserManual) for documentation.

File bug reports and feature requests at http://launchpad.net/pyh

### Get PyH ###
Download the latest version of pyh from the **Download** tab or directly from here [PyH-0.1.1.tar.gz](http://pyh.googlecode.com/files/PyH-0.1.1.tar.gz)
### Quick example ###
The following python code snipet
```
from pyh import *
page = PyH('My wonderful PyH page')
page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
page.addJS('myJavascript1.js', 'myJavascript2.js')
page << h1('My big title', cl='center')
page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
mydiv2 = page << div(id='myDiv2')
mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
page << div(id='myDiv3')
page.myDiv3.attributes['cl'] = 'myCSSclass3'
page.myDiv3 << p('Another paragraph')
page.printOut()
```
will generate the following html
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>My wonderful PyH page</title>
<link href="myStylesheet1.css" type="text/css" rel="stylesheet" />
<link href="myStylesheet2.css" type="text/css" rel="stylesheet" />
<script src="myJavascript1.js" type="text/javascript"></script>
<script src="myJavascript2.js" type="text/javascript"></script>
</head>
<body>
<h1 class="center">My big title</h1>
<div id="myDiv1" class="myCSSclass1 myCSSclass2">
<p id="myP1">I love PyH!</p>
</div>
<div id="myDiv2">
<h2>A smaller title</h2>
<p>Followed by a paragraph.</p>
</div>
<div id="myDiv3" class="myCSSclass3">
<p>Another paragraph</p>
</div>
</body>
</html>
```

---

PyH stands for any of the following : Pour yourself a ScotcH, Poor young Hobo or Peel your HTML. Any other suggestions?