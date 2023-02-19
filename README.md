# flask-travlr
## Travlr, a Full-Stack website 

This is implemented with flask and Postgres instead of Express/node.js and MongoDB

To get started:

Install Docker/compose

navigate to the root of the project

in your shell:
> docker-compose build
> docker-compose up -d

Then once the containers are up and running
> docker-compose exec python manage.py create_db

And to load some Test Data:

> docker-compose exec python manage.py load_db


start website:
(localhost:5000)

admin side:
(localhost:5000/admin)

Use the Sign up form to create an account and start using the application.
Adding/editing/deleting trips requires an accound
Searching is open to the public for now. 

add trips to see trips

Room/meals functionality not implemented

