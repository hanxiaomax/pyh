# @file: pyh.py
# @purpose: a HTML tag generator
# @author: Emmanuel Turlay <turlay@cern.ch>

__doc__ = """The pyh.py module is the core of the PyH package. PyH lets you
generate HTML tags from within your python code.
See http://code.google.com/p/pyh/ for documentation.
"""
__author__ = "Emmanuel Turlay <turlay@cern.ch>"
__version__ = '$Revision: 19 $'
__date__ = '$Date$'

from sys import _getframe, stdout, modules
nOpen={}

nl = '\n'
br = '<br />'+nl
doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'
charset = '<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n'

tags = ['html', 'body', 'head', 'link', 'meta', 'div', 'p', 'form', 'legend', 
        'input', 'select', 'span', 'b', 'i', 'option', 'img', 'script',
        'table', 'tr', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'fieldset', 'a', 'title']

def tag(**kw):
    "Core function to generate tags"
    selfClose = ['input', 'img', 'link']
    onlyOne = ['html', 'body', 'head']
    noNewLine = ['td', 'th', 'input']
    _name = kw.get('tagname', None)
    if not _name: _name = _getframe(1).f_code.co_name
    #if _name in onlyOne and nOpen.get(_name,0) : print 'WARNING: tag %s already open and closed' % _name
    open = kw.get('open', None)
    if open == None:
        if nOpen.get(_name, 0) and not kw.get('cl', None) and not kw.get('id', None): open = False
        else: open = True
    if not nOpen.get(_name, 0) and not open: print 'WARNING: trying to close non-open tag'
    nOpen[_name] = nOpen.get(_name, 0) + (open * 1 + (not open) * (-1))
    out = '<%s%s' % ((not open) * '/', _name)
    if open:
        for i,v in kw.iteritems():
            if i != 'txt' and i != 'open':
                if i == 'cl': i = 'class'
                out += ' %s="%s"' % (i, v)
    if _name in selfClose:
        out += ' /'
        nOpen[_name] -= 1
        open = False
    out += '>'
    if 'txt' in kw.keys() or ('src' in kw.keys() and _name != 'img'):
        out += '%s%s' % (kw.get('txt', ''), '</%s>' % _name)
        nOpen[_name] -= 1
        open = False
    if not open and _name not in noNewLine: out += nl
    return out

def fcn(name):
    def f(**kw):
        kw['tagname'] = name
        return kw
    return f

thisModule = modules[__name__]

for t in tags: setattr(thisModule, t, fcn(t)) 

def ValidW3C():
    out = a(href='http://validator.w3.org/check?uri=referer',
                    txt=img(src='http://www.w3.org/Icons/valid-xhtml10', alt='Valid XHTML 1.0 Strict'))
    return out

class PyH():
    _header, _body, _footer = '', '', ''
    _javascripts, _stylesheets, _meta = [], [], []
    _lang = 'en'
    def __init__(self, title='MyPyHPage'):
        self._title = title
        self._counter = TagCounter(title)
    
    def addJavaScript(self, js):
        if not isinstance(js, list): js = [js]
        self._javascripts += js

    def addCSS(self, css):
        if not isinstance(css, list): css = [css]
        self._stylesheets += css

    def addMeta(self, name='', content='', http_equiv=''):
        if content:
            meta = {'content':content, 'name':name, 'http-equiv':http_equiv}

    def setLang(self, l):
        self._lang = l

    def __iadd__(self, **kw):
        self._body += self.tag(**kw)
        return self

    def tag(**kw):
        "Core function to generate tags"
        noNewLine = ['td', 'th', 'input']
        selfClose = ['input', 'img', 'link']
        _name = kw.get('tagname', None)
        if not isLegal(tag): return ''
        open = kw.get('open', cl in kw.keys() or id in kw.keys() or c.isClosed(_name))
        c = self._counter
        if not c.isAllowed(_name, open) : return ''
        out = '<%s%s' % ((not open) * '/', _name)
        if open:
            c.open(_name)
            for i,v in kw.iteritems():
                if i != 'txt' and i != 'open':
                    if i == 'cl': i = 'class'
                    out += ' %s="%s"' % (i, v)
        else: c.close(_name)
        if _name if selfClose:
            out += ' /'
            c.close(_name)
        out += '>'
        if 'txt' in kw.keys() or ('src' in kw.keys() and _name != 'img'):
            out += '%s%s' % (kw.get('txt', ''), '</%s>' % _name)
            c.close(_name)
        if not open and _name not in noNewLine: out += nl
        return out
    
    def render(self,file=''):
        if file: f = open(file, 'w')
        else: f = stdout
        f.write(self.renderHeader())
        f.write(self._body)
        f.write(self.renderFooter())
        f.flush()
        f.close()

    def renderHeader(self):
        h = self._header
        h += doctype
        h += html(xmlns='http://www.w3.org/1999/xhtml', lang=self._lang)
        h += head()
        h += charset
        h += title(txt=self._title)
        for s in self._stylesheets:
            h += link(rel='stylesheet',type='text/css',href=s)
        for j in self._javascripts:
            h += script(type='text/javascript',src=j)
        h += head()
        h += body()
        return h

    def renderFooter(self):
        f = self._footer
        f += body()
        f += html()
        return f
    
class TagCounter():
    _count = {}
    _lastOpen = []
    for t in tags: _count[t], _open[t] = 0, None
    def __init__(self, name):
        self._name = name
    def open(self, tag):
        if isLegal(tag): 
            _count[tag] += 1
            _lastOpen += [tag]
    def close(self, tag):
        if isLegal(tag) and _lastOpen[-1] == tag: 
            _count[tag] -= 1
            _lastOpen.pop()
        else:
            print 'Cross tagging is wrong'
    def isAllowed(self, tag, open):
        if not open and self.isClosed(tag):
            print 'TRYING TO CLOSE NON-OPEN TAG: %s' % tag
            return False
        return True
    def isOpen(self, tag):
        if isLegal(tag): return _count[tag]
    def isClosed(self, tag):
        if isLegal(tag): return not _count[tag]

    
def isLegal(tag):
    if tag in tags: return True
    else:
        print 'ILLEGAL TAG: %s' % tag
        return False