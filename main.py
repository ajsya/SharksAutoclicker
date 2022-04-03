print("Starting...")
import os, time, threading, sys
try:
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Listener, KeyCode
    from tinted import tint
except ModuleNotFoundError:
    print("Installing modules...")
    os.system('pip install pynput')
    os.system('tinted')
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Listener, KeyCode
    from tinted import tint

print(" ")
print(tint("[bold][blue]Shark's Autoclicker[/][/]"))
print(tint("[lightgray]-[/]")*10)
print(tint("[italic]Press 'a' to start clicking, and 'b' to quit[/]"))

delay = float(sys.argv[1])
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')
  
class ClickMouse(threading.Thread):
    
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
  
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
  
  
def on_press(key):
    
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
            print(tint("[darkgray]Now clicking at: ~{0} cps[/]".format(float(sys.argv[1]))))
            print(tint("[red]Press 'b' to stop clicking![/]"))
              
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
  
  
with Listener(on_press=on_press) as listener:
    listener.join()
