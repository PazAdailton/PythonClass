from typing import List, Dict, Union
from .database_connection import DatabaseConnection
"""
json file

json.load TRANSFORMA JSON EM OBJETO PYTHON              /// typing hinting -> List[Dict]: -> None: say what is the return of the function

json.dump TRANSFORMA OBJETO PYTHON EM JSON


"""
Book = Dict[str, Union[str, int]]

def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("""
            create table IF NOT EXISTS books
                (name text primary key, 
                author text, 
                read integer)
        """)


def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('insert into books values (?, ?, 0)', (name, author))



def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('select * from books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        return books

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('update books set read=1 WHERE name = ?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('delete from books where name = ?', (name,))




