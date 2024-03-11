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
> set FLASK_ENV=development
> 
> set FLASK_APP=main.py
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