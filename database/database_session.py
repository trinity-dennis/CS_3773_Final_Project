from config import get_db_path
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session



class DatabaseSession:

    def __init__(self):
        self._engine = create_engine(get_db_path())
        self._session_factory = sessionmaker(bind=self._engine)

    @contextmanager
    def session(self) -> Session:
        db_session: Session = self._session_factory()

        try:
            yield db_session
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()

    def session_persistent(self) -> Session:
        return self._session_factory()
