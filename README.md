# Currency-Project

A repository to follow the current value of different currencies around the globe.

The purpouse of this repository it's for study >>ONLY<<.

## How to locally run?

`source venv/bin/activate`
pip3 install -r requeriments

The function `catch_exchange.run()` must run once a day. You can do this by nonstop running `currency_check.py` in your machine or doing a task on your server to run this script preferrably at 00:10 am every day:

`
from time import sleep
from datetime import datetime
import sys 

sys.path.append('./Currency-Project')

from catch_exchange import updated

while not updated():
    sleep(10*60)
print("UPDATED!")
print(f"date: {datetime.now()}")
`

To access the site, run `python3 app.py` and access in your browser [localhost:5000](http://localhost:5000/)

## Next Steps

- Turn it responsive
- Turn it beautifull
- Organize the js fiels
- Insert login and / use cookies to keep favorite countries (?)
- Insert multilanguage (?)
- Try to catch the localization of the user and them change the "first page"