# LOR

Twipee is a django application developed for favoriting Lord of the Rings characters and quote,
This application fetches data from [The One APi](https://the-one-api.dev/) which provides all data 
about The Lord of the Rings, the epic books by J. R. R. Tolkien and the official movie adaptions by Peter Jackson.


## Models
- User 
- Character
- Quote
- Favorite



## Getting Started
1. Clone the repo
   ```sh
      git clone https://github.com/swilltec/lor/
   ```
2. Navigate to bookmark directory and run
  ```sh
      pip install -r requirements
  ```
3. Run development server
   ```sh
   python manage.py shell or make start
   ```

6. Navigate to [API_DOCUMENTATION](http://localhost:8000/) to view API documentation
NB: 
- View [Makefile](Makefile) for more commands
- Base API url = "localhost:8000/api/v1/"


## Architecture
This project is divided into three layers of presentation (Template), persistence (Model), and actions or rules (View)
is a common pattern. Model-view-template (MVT) is a way of modeling data for persistence,
providing users with a view into that data, and allowing them to control changes to
that data with some set of actions.

## Technologies
 - [Python](https://www.python.org/)
 - [Sqlite](https://www.sqlite.org/index.html)
 - [Github](https://github.com/)
 - [Django](https://docs.djangoproject.com/en/3.2/)
 - [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)


## Assumptions
- The Character ID was ignored in the favorite quote endpoint. It uses the character ID in the quote details

## TODO
- Testing
