import sys
import getopt
import setup.config as cfg

"""
  argv -> list[str]

  Sets the default values to env, type and riot id ( check config.py for details) then checks if it recieves any
  changes to this values from the comand line exec (sys.argv as param)

"""
def get_params( argv ):
  print(argv)
  arg_env = cfg.env
  arg_type = cfg.type
  arg_user = cfg.riot_id
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

  return {
    'env': arg_env,
    'riot_id': arg_user,
    'type': arg_type,
  }
