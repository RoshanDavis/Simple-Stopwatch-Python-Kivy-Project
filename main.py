
##Hellooo##

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import Clock
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

class MainWidget(AnchorLayout):
    time_label=StringProperty("00:00:00")
    time_cal=0.0
    sec=0
    min=0
    hr=0
    timer_on=False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        Clock.schedule_interval(self.update,1/60)
    

    def add0(self,val):
        if val >= 10:
            val=""
        else:
            val="0"
        return val

    def Time_Cal(self,dt):
        self.time_cal+=dt
        if int(self.time_cal) >= 1:
            self.sec+=1
            self.time_cal=0
        elif self.sec >= 60:
            self.min+=1
            self.sec-=60
        elif self.min>=60:
            self.hr+=1
            self.min-=60
        self.time_label=self.add0(self.hr)+str(self.hr)+":"+self.add0(self.min)+str(self.min)+":"+self.add0(self.sec)+str(self.sec)

    def update(self,dt):
        if(self.timer_on):
            self.Time_Cal(dt)
        
    def on_press_start(self):
        self.timer_on=True
    
    def on_press_stop(self):
        self.timer_on=False
    
    def on_press_reset(self):
        self.sec=0
        self.min=0
        self.hr=0
        self.Time_Cal(0)
class StopwatchApp(App):
    def build(self):
        return Builder.load_file('stopwatch.kv')

StopwatchApp().run()