import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from login import db_login, db_name, db_pass

DSN = f"postgresql://{db_login}:{db_pass}@localhost:5432/{db_name}"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
publisher1 = Publisher(name='Arkady Podkolzin')
publisher2 = Publisher(name='Anastasia Birykova')
book1 = Book(title='Любовь', publisher_id=1)
book2 = Book(title='Страсть', publisher_id=2)
shop1 = Shop(name='Читай-город')
shop2 = Shop(name='Книжный')
stock1 = Stock(book_id=1, shop_id=1, count=10)
stock2 = Stock(book_id=2, shop_id=2, count=15)
sale1 = Sale(stock_id=1, date_sale='26.04.2023', price=15000, count=1)
sale2 = Sale(stock_id=2, date_sale='20.03.2023', price=20000, count=2)
session.add(publisher1)
session.add(publisher2)
session.add(book1)
session.add(book2)
session.add(shop1)
session.add(shop2)
session.add(stock1)
session.add(stock2)
session.add(sale1)
session.add(sale2)
session.commit()
def get_sales(c):
    qr = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale, ).select_from(Shop).join(Stock).join(
        Book).join(Publisher).join(Sale)
    if c.isdigit():
        c1 = qr.filter(Publisher.id==c).all()
    else:
        c1 = qr.filter(Publisher.name == c).all()
    for a, b, c, d in c1:
        print(f"{a} | {b} | {c} | {d}")
if __name__ == '__main__':
    c = input("Введи имя или идентификатор публициста: ")
    get_sales(c)
session.close()