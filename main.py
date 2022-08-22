import sys
import getopt
import tracker_scrapper as trk
from pyvirtualdisplay import Display

argv = sys.argv
arg_env = "PROD"
arg_type = "PROFILE"
arg_user = "Q95 Madruga#Quake"
arg_help = "{0} \r\n -e <env> => (prod or dev) \r\n -t <type> => (profile, map, agent, weapon or match) \r\n -u <user> => (riot#id)".format(argv[0])

try:
  opts, args = getopt.getopt(argv[1:], "he:t:u:", ["help", "env=","type=","user="])
except:
  print(arg_help)
  sys.exit(2)

for opt, arg in opts:
  if opt in ("-h", "--help"):
    print(arg_help)  # print the help message
    sys.exit(3)
  elif opt in ("-e", "--env"):
    arg_env = arg.upper()
  elif opt in ("-t", "--type"):
    arg_type = arg.upper()
  elif opt in ("-u", "--user"):
    arg_user = arg

env = arg_env
riot_id = arg_user
data_type = arg_type



if env != 'DEV':
  display = Display(visible=0, size=(800, 800))
  display.start()

data = trk.get_by(data_type, riot_id, env )
#print(tracker_data)


#data = "this began life in python"
print(data)
sys.stdout.flush()
