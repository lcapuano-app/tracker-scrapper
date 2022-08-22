
import sys
from setup import cmd_line_args, fake_display
from scrapper import save_as, tracker as trk

if __name__ == "__main__":

  params = cmd_line_args.get_params( argv = sys.argv )

  fake_display.init( env = params['env'] )

  data = trk.get_by(
    data_type = params['type'],
    riot_id   = params['riot_id'],
    env       = params['env']
  )


  #file_path = save_as.json_file( str_data=data, riot_id=params['riot_id'] )

  print(data)

  sys.stdout.flush()
