from abc import ABC, abstractmethod, abstractproperty

class InterFaceText(ABC):

    @abstractmethod
    def show(self):
        pass

class InterFaceInput(ABC):

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text: str):
        if new_text:
            self._text = new_text.title()


class InterFaceButton(ABC):

    def __init__(self):
        self.pressed = False

    def push_button(self):
        pass


class Form(InterFaceText, InterFaceInput, InterFaceButton):

    def show(self):
        return f"{self._text.center(len(self._text) + 4 , '-')}"

    def push_button(self):
        self.pressed = True
        print("Button is pressed")


# Testing
form = Form()
form.text = "asdfasdf"

print(form.text)
print(form.show())