from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


Base = declarative_base()

class DBSession(object):
    """To communicate with data base with ORM interface.
        They create a session and communicate with database

    Example:
        db_session = DBSession(db_path)
        db_session.query(User).filter(User.active == True).all() # get all active users

        db_session.add_user(1, "1", "Nikita", "Ivanov", "Bikes")

        db_session.close_session()
    """

    _session: Session

    def __init__(self, db_path, *args, **kwargs):
        """Open session with DB

        Args:
            db_path: relative path from random coffe package
                     to database type as sqlite3
        """
        self.db_path = db_path
        engine = create_engine(f"sqlite:///{self.db_path}")

        session_factory = sessionmaker(bind=engine)
        self._session = session_factory()

    def query(self, *entities, **kwargs):
        """Query by DB"""
        return self._session.query(*entities, **kwargs)

    def add_model(self, model: Base, save_data: bool = True):
        """Create new recording in DB by model

        Args:
            model: class of some db table to add in table
            save_data: save data in this time or not commit to db
        """
        self._session.add(model)

        if save_data:
            self.commit_session()

    def delete_model(self, model: Base, save_data: bool = True):
        """Delete model in DB

        Args:
            model: class of some db table to add in table
            save_data: if need to delete in local or if you commit else changes to db
                        set `False`
        """
        if model is None:
            print(f"Model {model} is None")

        self._session.delete(model)

        if save_data:
            self.commit_session()
