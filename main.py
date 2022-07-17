
from sqlite3 import Time
from time import time
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import Clock
from kivy.properties import StringProperty
class MainWidget(AnchorLayout):
    time_label=StringProperty("00:00:00")
    time_cal=0.0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update,1/60)
    pass

    def add0(self,val):
        if val >= 10:
            val=""
        else:
            val="0"
        return val
    def Time_Cal(self,dt):
        self.time_cal+=dt
        sec=int(self.time_cal)
        min=0
        hr=0
        if sec == 60:
            min=int(sec/60)
            sec=0
        elif min==60:
            hr=int(min/60)
            min=0
        self.time_label=self.add0(hr)+str(hr)+":"+self.add0(hr)+str(min)+":"+self.add0(sec)+str(sec)

    def update(self,dt):
        self.Time_Cal(dt)
        pass

class Simple_StopwatchApp(App):
    pass

Simple_StopwatchApp().run()