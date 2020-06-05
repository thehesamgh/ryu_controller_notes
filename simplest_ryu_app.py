from ryu.base import app_manager
#from ryu.controller.handler import set_ev_cls

class SimpleApp(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(SimpleApp, self).__init__(*args, **kwargs)
        print("I'm simplest ryu app")
    
  