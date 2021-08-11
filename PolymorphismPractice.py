from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("Drawed a text box")

class DropDownList(UIControl):
    def draw(self):
        print("Drawed a drop down list")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
text = TextBox()

#passing a list of objects to the draw funciton. Possibly rendering a UI or you
#can do many other things with polymorphism (poly = many, morph=form)
draw([text, ddl])
