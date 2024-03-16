>> ------ Windows ----------
>Running the server:
> 
> set FLASK_ENV=development
> 
> set FLASK_APP=main.py
> 
> flask run
> 
> --------- Mac -------------
> export FLASK_ENV=development
> 
> export FLASK_APP=main.py
> 
> flask run
> 
> ----------- Server Error ---------
> chrome://net-internals/#sockets
> 

> -------- After creating the model database -------
> Run in the terminal ( in mac run python3, in windows run 'py')
> from main import db, app
> app.app_context().push()
> db.create_all()

> you can see the database created inside the folder instances
> run the terminal again
> 
> ------------- Use mysql instead of sqlite -----------
> pip3 install mysql-connector
> pip3 install mysql-connector-python
> pip3 install mysql-connector-python
> 
> Create a python file create_db_file.py
> 
> ------------- Migrations -----------
> In case you want to add few columns to the database
> pip3 install Flask-Migrate
> from flask_migrate import Migrate
> under  this line: db = SQLAlchemy(app)
> migrate = Migrate(app, db)
> In the terminal type:
> flask db init
> flask db migrate -m 'initial migration'
> flask db upgrade
> 
> run server and check
> 
>> NOTE:
> Any time you want to make migrations just type:
> flask db migrate -m "added something"
> flask db upgrade
