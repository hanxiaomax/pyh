class Test:
    name = ''
    value = 0
    def __add__(self, obj):
        print 'Add',self.name
        new = Test()
        new.name = self.name + obj.name
        new.value = self.value + obj.value
        return new

    def __lshift__(self, obj):
        print 'lt',self.name
        new = Test()
        new.name = self.name + obj.name
        new.value = self.value + obj.value
        return new
