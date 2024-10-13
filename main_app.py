from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1 , txt_test3, txt_sits
from ruffier import test


age = 7
name = ''
p1,p2,p3 = 0,0,0

class InstrScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text="Введіть ім'я:",halign="right")
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введіть вік:",halign="right")
        self.btn.age = TextInput(text='7',multiline=False)
        self.btn = Button(
            text="Почати", size_hint=(0.3,0.2), pos_hint={'center_x': 0.5}
        )
        self.btn.on_press = self.next
        line1=BoxLayout(size_hint=(0.8, None), height='30sp')
        line2=BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_name)
        outer = BoxLayout(orientation='vertical',padding=8,spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget((outer))

    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age ==  7:
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_test1)
        lbl1 = Label(text ='Рахуйте пульс')

        line = BoxLayout(size_hint=(0.8,None), height='30sp')
        lbl_result = Label(text='Введіть результат:',halign="right")
        self.in_result = TextInput(text='0',multiline=False)
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = Button(text='почати', size_hint=(0.3,0.4), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(lbl1)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

        def next(self):
            if not
            name = self.in_name.text
            age = check_int(self.in_age.text)
            if age == False or p1 <= 0:
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'

class Pulsescr2(Screen):
    def __init__(self,**kwargs):
        self.next_screen = False

        self.stage = 0
        #coment(HELP!)











        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint ={0.8, None}, height = '30sp')
        lbl_result2 = Label(text = 'Результат після відпочинку:', halign = '30sp')
        self.in_result2 = TextInput(text = '0', multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button




