from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.label import Label

Builder.load_string("""
<LabelC>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


class LabelC(Label):
    bcolor = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(Label, self).__init__(**kwargs)
        print(self.size)


Factory.register('MyLabelC', module='LabelC')
