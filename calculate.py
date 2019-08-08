import math
class Calculate:
    def __init__(self,name):
        self.name=name

    def mohit (self):
        pass

    def masahat (self):
        pass

    def type_ (self,name):
        print (f"shekl hendesi {name}")


class Mosalas(Calculate):
    def __init__(self,toole_zel,ertefa):
        self.toole_zel=toole_zel
        self.ertefa=ertefa

    def mohit(self):
        return self.toole_zel*3

    def masahat(self):
        return (self.toole_zel*self.ertefa)/2



class Dayere(Calculate):
    pi=3.16
    def __init__(self,ghotr):
        self.ghotr=ghotr

    def mohit(self):
        return (self.ghotr/2)*2*math.pi

    def masahat(self):
        return (self.ghotr/2)**2*math.pi


class Moraba(Calculate):
    def __init__(self,zel):
        self.zel=zel

    def mohit(self):
        return (self.zel)*4

    def masahat(self):
        return (self.zel)**2

print('')
print('')

obj_1=Mosalas(9,9)
obj_1.type_('mosalas')
print(obj_1.mohit())
print(obj_1.masahat())

print('')
obj_2=Dayere(8)
obj_1.type_('dayere')
print(obj_2.mohit())
print(obj_2.masahat())

print('')
obj_3=Moraba(8)
obj_1.type_('moraba')
print(obj_3.mohit())
print(obj_3.masahat())


