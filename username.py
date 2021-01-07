"""Retrieves data from the Twitter API and pushes it to a database"""
from os import getenv
from .models import DB, User, Suggestions



def add_or_update_user(username):
    try:
        """Adds a basic user w/ the name username to the database"""
        spotify_user = #Needs to be created(username)
        db_user = (User.query.get(spotify_user.id)) or User(
            id=spotify_user.id, name=username)
        DB.session.add(db_user)
        suggestions = spotify_user.#needs to be created
        
    except Exception as e:
        print("Error processing {}: {}".format(username, e))
        raise e
    else: 
        DB.session.commit()
    