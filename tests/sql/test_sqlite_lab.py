import sqlite3

import pytest


@pytest.fixture
def database():
    connection = sqlite3.connect(":memory:")
    connection.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, amount REAL NOT NULL
        );
        INSERT INTO users VALUES (1, 'Lin');
        INSERT INTO users VALUES (2, 'Mei');
        INSERT INTO orders VALUES (101, 1, 19.90);
        INSERT INTO orders VALUES (102, 1, 5.10);
        """
    )
    yield connection
    connection.close()


@pytest.mark.smoke
def test_order_total_can_be_verified_with_sql(database):
    total = database.execute(
        "SELECT ROUND(SUM(amount), 2) FROM orders WHERE user_id = ?", (1,)
    ).fetchone()[0]

    assert total == 25.00


@pytest.mark.regression
def test_user_order_join_returns_only_existing_orders(database):
    rows = database.execute(
        """
        SELECT users.name, orders.id
        FROM users JOIN orders ON users.id = orders.user_id
        ORDER BY orders.id
        """
    ).fetchall()

    assert rows == [("Lin", 101), ("Lin", 102)]
