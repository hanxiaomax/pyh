# @file: pyh.py
# @purpose: a HTML tag generator
# @author: Emmanuel Turlay <turlay@cern.ch>

__doc__ = """The pyh.py module is the core of the PyH package. PyH lets you
generate HTML tags from within your python code.
See http://code.google.com/p/pyh/ for documentation.
"""
__author__ = "Emmanuel Turlay <turlay@cern.ch>"
__version__ = '$Revision$'
__date__ = '$Date$'


from sys import _getframe
nOpen={}

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

def table(**kw): return tag(**kw)
def th(**kw): return tag(**kw)
def b(**kw): return tag(**kw)
def tr(**kw): return tag(**kw)
def td(**kw): return tag(**kw)
def h2(**kw): return tag(**kw)
def h1(**kw): return tag(**kw)
def div(**kw): return tag(**kw)
def fieldset(**kw): return tag(**kw)
def select(**kw): return tag(**kw)
def input(**kw): return tag(**kw)
def span(**kw): return tag(**kw)
def legend(**kw): return tag(**kw)
def p(**kw): return tag(**kw)
def option(**kw): return tag(**kw)
def form(**kw): return tag(**kw)
def img(**kw): return tag(**kw)
def a(**kw): return tag(**kw)
def head(**kw): return tag(**kw)
def title(**kw): return tag(**kw)
def link(**kw): return tag(**kw)
def script(**kw): return tag(**kw)
def body(**kw): return tag(**kw)
def html(**kw): return tag(**kw)
nl = '\n'
br = '<br />'+nl
doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
charset = '<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />'

def ValidW3C():
    out = a(href='http://validator.w3.org/check?uri=referer',
                    txt=img(src='http://www.w3.org/Icons/valid-xhtml10', alt='Valid XHTML 1.0 Strict'))
    return out
