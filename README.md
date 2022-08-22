
# tracker-scrapper

  

Gets valorant's player statistics from tracker gg page using selenium chrome web driver

  

### Install

```
pip i -r requirements.txt
```

### Help
```
python main.py -h

main.py
-e <env> => (prod or dev)
-t <type> => (profile, map, agent, weapon or match)
-u <user> => (riot#id)

```

env (optional) = "PROD"  (default) || "DEV"
(PROD) Enables a fake display to by pass tracker's validation.
(DEV) Uses your chrome (UI) as an actual display.
___

type (optional) = "profile" ||  "map"||  "agent"  || "weapon" || "match" 
Sets witch playlist type it should get (default = "PROFILE").
___

user = riot_username#tag_id
(Mandatory) just the user riots id
