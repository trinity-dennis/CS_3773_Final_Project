import os

from sqlalchemy.orm import make_transient, joinedload
from sqlalchemy.orm.exc import NoResultFound

from database.database_session import DatabaseSession
from model.accounts import Account
from model.book import Book
from model.accessories import Accessories
from model.cart import Cart
from model.discount import Discount
from model.orders import Orders  # Adjust the import based on your actual module structure


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

    def add_cart_item(self, session_id, item_name, quantity, item_type, price, img, id):
        cart_item = Cart(session_id=session_id, item_name=item_name, quantity=quantity, type=item_type, price=price,
                         img=img, item_id=id)
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

    def increase_quantity(self, id):
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

    def add_order(self, book_id, accessory_id, customer_id, order_date, order_total):
        order = Orders(book_id=book_id, accessory_id=accessory_id, customer_id=customer_id, order_date=order_date,
                       order_total=order_total)
        with self._db_session.session() as session:
            session.add(order)

    def decrease_book_availability(self, id, quantity):
        with self._db_session.session() as session:
            item = session.query(Book).filter_by(id=id).first()
            if item.availability > 0:
                item.availability -= quantity

    def decrease_accessory_availability(self, id, quantity):
        with self._db_session.session() as session:
            item = session.query(Accessories).filter_by(accessory_id=id).first()
            if item.availability > 0:
                item.availability -= quantity

    def authenticate_user(self, username, password):
        with self._db_session.session() as session:
            try:
                user = session.query(Account).filter_by(username=username, password=password).one()
                return user
            except NoResultFound:
                return None

    def get_user_id(self, username, password):
        with self._db_session.session() as session:
            try:
                user = session.query(Account).filter_by(username=username, password=password).one()
                return user.id
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

    def get_order_information(self, load_customer=False):
        with self._db_session.session() as session:
            try:
                # Use joinedload to eagerly load the related customer objects
                query = session.query(Orders)
                if load_customer:
                    query = query.options(joinedload(Orders.customer))

                orders = query.all()

                # Expunge the objects from the session to avoid detached instance issues
                for order in orders:
                    session.expunge(order)
                    if load_customer:
                        session.expunge(order.customer)
                        make_transient(order.customer)

                return orders
            except Exception as e:
                print(f"Error fetching order information: {e}")
                return None

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

    def add_book(self, genre, title, author, quantity, price, availability, img_filename):
        with self._db_session.session() as session:
            new_book = Book(img=img_filename, genre=genre, title=title, author=author,
                            quantity=quantity, price=price, availability=availability, display_on_homepage=False)
            session.add(new_book)
            session.commit()

        return {'success': True, 'message': 'Book added successfully'}

    def add_accessory(self, item_name, quantity, price, availability, img_filename):
        with self._db_session.session() as session:
            new_accessory = Accessories(img=img_filename, item_name=item_name,
                                        quantity=quantity, price=price, availability=availability)
            session.add(new_accessory)
            session.commit()

        return {'success': True, 'message': 'Accessory added successfully'}

    def update_book(self, book_id, new_genre, new_price, new_availability):
        with self._db_session.session() as session:
            # Assuming `Book` is the model for your books table
            book = session.query(Book).get(book_id)

            if book:
                book.genre = new_genre
                book.price = new_price
                book.availability = new_availability

                session.commit()
                return {'success': True, 'message': 'Book updated successfully'}
            else:
                return {'success': False, 'message': 'Book not found'}

    def update_accessory(self, accessory_id, new_price, new_availability):
        with self._db_session.session() as session:
            accessory = session.query(Accessories).filter_by(accessory_id=accessory_id).first()
            if accessory:
                accessory.price = new_price
                accessory.availability = new_availability
                session.commit()
                return True
            return False

    def get_book_price(self, book_id):
        with self._db_session.session() as session:
            book = session.query(Book).filter_by(id=book_id).first()
            if book:
                return book.price
            else:
                return None

    def update_book_price(self, book_id, new_price):
        with self._db_session.session() as session:
            book = session.query(Book).filter_by(id=book_id).first()
            if book:
                # Store the current genre and availability
                current_genre = book.genre
                current_availability = book.availability

                # Update only the price
                book.price = new_price

                # Set back the current genre and availability
                book.genre = current_genre
                book.availability = current_availability

                session.commit()
                return True
            else:
                return False

    def get_accessory_price(self, accessory_id):
        with self._db_session.session() as session:
            accessory = session.query(Accessories).filter_by(accessory_id=accessory_id).first()
            if accessory:
                return accessory.price
            else:
                return None

    def update_accessory_price(self, accessory_id, new_price):
        with self._db_session.session() as session:
            accessory = session.query(Accessories).filter_by(accessory_id=accessory_id).first()
            if accessory:
                accessory.price = new_price
                session.commit()
                return True
            else:
                return False

    def move_book_to_homepage(self, book_id, new_genre, new_availability):
        with self._db_session.session() as session:
            book = session.query(Book).filter_by(id=book_id).first()
            if book:
                book.display_on_homepage = True
                book.genre = new_genre
                book.availability = new_availability
                session.commit()
                return True
            else:
                return False

    def move_accessory_to_homepage(self, accessory_id, new_availability):
        with self._db_session.session() as session:
            accessory = session.query(Accessories).filter_by(accessory_id=accessory_id).first()
            if accessory:
                accessory.display_on_homepage = True
                accessory.availability = new_availability
                session.commit()
                return True
            else:
                return False

    def get_homepage_books(self):
        with self._db_session.session() as session:
            homepage_books = session.query(Book).filter_by(display_on_homepage=True).all()
            for book in homepage_books:
                # Disconnect from the database so updates aren't tracked
                session.expunge(book)
                make_transient(book)
            return homepage_books

    def get_homepage_accessories(self):
        with self._db_session.session() as session:
            homepage_accessories = session.query(Accessories).filter_by(display_on_homepage=True).all()
            for accessories in homepage_accessories:
                # Disconnect from the database so updates aren't tracked
                session.expunge(accessories)
                make_transient(accessories)
            return homepage_accessories

    def get_users(self):
        with self._db_session.session() as session:
            users = session.query(Account).all()
            for user in users:
                session.expunge(user)
                make_transient(user)
            return users

    def delete_user(self, user_id):
        with self._db_session.session() as session:
            try:
                user = session.query(Account).filter_by(id=user_id).one()
                session.delete(user)
                session.commit()
                return {'success': True, 'message': 'User deleted successfully'}
            except NoResultFound:
                return {'success': False, 'message': 'User not found'}

    def add_discount(self, discount_code, percentage):
        with self._db_session.session() as session:
            # Assuming you have a Discount model defined
            new_discount = Discount(code=discount_code, percentage=percentage)

            # Add the new discount to the database
            session.add(new_discount)
            session.commit()

    def get_discount_by_code(self, code):
        with self._db_session.session() as session:
            try:
                discount = session.query(Discount).filter_by(code=code).first()

                # Expunge and make_transient to detach the object from the session
                if discount:
                    session.expunge(discount)
                    make_transient(discount)

                return discount
            except Exception as e:
                print(f"Error fetching discount by code: {e}")
                return None
