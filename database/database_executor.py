from sqlalchemy.orm import make_transient
from sqlalchemy.orm.exc import NoResultFound

from database.database_session import DatabaseSession
from model.accounts import Account
from model.book import Book
from model.accessories import Accessories
from model.cart import Cart





class DatabaseExecutor:
    def __init__(self):
        self._db_session = DatabaseSession()

    def remove_from_cart(self, id):
        with self._db_session.session() as session:
            session.query(Cart).filter_by(item_no=id).delete()


    def register_user(self, admin, username, password):
        new_user = Account(admin=admin, username=username, password=password)
        with self._db_session.session() as session:
            session.add(new_user)

    def add_cart_item(self, session_id,item_name, quantity, item_type , price, img, id):
        cart_item = Cart(session_id=session_id, item_name=item_name, quantity=quantity, type=item_type, price=price, img=img, item_id=id)
        with self._db_session.session() as session:
            session.add(cart_item)

    def get_cart_items(self):
        with self._db_session.session() as session:
            items = session.query(Cart).all()
            for item in items:
                # disconnect from database so updates aren't tracked
                session.expunge(item)
                make_transient(item)
            return items

    def increase_quantity(self,id):
        with self._db_session.session() as session:
            items = session.query(Cart).filter_by(item_no=id).first()
            items.quantity += 1

    def decrease_quantity(self, id):
        with self._db_session.session() as session:
            items = session.query(Cart).filter_by(item_no=id).first()
            if items.quantity > 0:
                items.quantity -= 1

    def delete_cart(self):
        with self._db_session.session() as session:
             session.query(Cart).delete()

    def authenticate_user(self, username, password):
        with self._db_session.session() as session:
            try:
                user = session.query(Account).filter_by(username=username, password=password).one()
                return user
            except NoResultFound:
                return None

    def get_books_by_genre(self, genre):
        with self._db_session.session() as session:
            books = session.query(Book).filter_by(genre=genre).all()
            for book in books:
                # disconnect from database so updates aren't tracked
                session.expunge(book)
                make_transient(book)
            return books

    def get_books_by_id(self, id):
        with self._db_session.session() as session:
            books = session.query(Book).filter_by(id=id).all()
            for book in books:
                # disconnect from database so updates aren't tracked
                session.expunge(book)
                make_transient(book)
            return books

    def get_accessories(self):
        with self._db_session.session() as session:
            accessories = session.query(Accessories).all()
            for accessory in accessories:
                # disconnect from database so updates aren't tracked
                session.expunge(accessory)
                make_transient(accessory)
            return accessories

    def get_books_by_title(self, title):
        with self._db_session.session() as session:
            books = session.query(Book).filter(Book.title.contains(title)).all()
            for book in books:
                session.expunge(book)
                make_transient(book)
        return books

    def get_books(self):
        with self._db_session.session() as session:
            books = session.query(Book).all()
            for book in books:
                session.expunge(book)
                make_transient(book)
        return books

    def get_stock_information(self):
        with self._db_session.session() as session:
            books = session.query(Book).all()
            accessories = session.query(Accessories).all()

            # Make books and accessories transient
            for item in books + accessories:
                session.expunge(item)
                make_transient(item)

            return books + accessories

    def get_order_information(self):
        with self._db_session.session() as session:
            books = session.query(Book).all()
            accessories = session.query(Accessories).all()

            # Make books and accessories transient
            for item in books + accessories:
                session.expunge(item)
                make_transient(item)

            return books + accessories

    def get_accessories_by_item_name(self, item):
        with self._db_session.session() as session:
            accessories = session.query(Accessories).filter(Accessories.item_name.contains(item)).all()
            for accessory in accessories:
                session.expunge(accessory)
                make_transient(accessory)
        return accessories




    def get_accessories_by_id(self, id):
        with self._db_session.session() as session:
            accessories = session.query(Accessories).filter_by(accessory_id=id).all()
            for accessory in accessories:
                # disconnect from database so updates aren't tracked
                session.expunge(accessory)
                make_transient(accessory)
            return accessories

