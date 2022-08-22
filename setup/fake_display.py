from pyvirtualdisplay import Display

def init( env = 'PROD' ):
  if env != 'DEV':
    display = Display(visible=0, size=(800, 800))
    display.start()
