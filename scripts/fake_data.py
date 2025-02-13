from faker import Faker
import sqlite3

fake = Faker()


def fake_data():
    connection = sqlite3.connect("data/database.db")

    with open("schema.sql") as f:
        for _ in range(10):
            connection.executescript(
                "INSERT INTO CREDENTIALS (name, username, password, domain, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
                    fake.company(),
                    fake.user_name(),
                    fake.password(length=12),
                    fake.domain_name(),
                    fake.date_time_this_decade(),
                    fake.date_time_this_decade(),
                )
            )

        connection.commit()
        connection.close()


if __name__ == "__main__":
    fake_data()
