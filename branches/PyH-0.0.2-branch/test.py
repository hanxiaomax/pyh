class Test(list):
    tagname = ''
    def __init__(self, *arg, **kw):
        self.extend(arg)
    def __add__(self, obj):
        if self.tagname:
            return Test(self,obj)
        else:
            self.append(obj)
            return self

