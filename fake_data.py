from faker import Faker
import sqlite3
import base64
from utils import encryption

fake = Faker()


def fake_data():
    kp = encryption.KeyPair()
    kp.load_existing_key_pair("Password123!")

    enc = encryption.Encryption(kp)

    connection = sqlite3.connect("data/database.db")

    with open("schema.sql") as f:
        for _ in range(10):
            connection.execute(
                "INSERT INTO CREDENTIALS (name, username, password, domain, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    fake.company(),
                    fake.user_name(),
                    enc.encrypt("MySecurePassword1#"),
                    fake.domain_name(),
                    fake.date_time_this_decade(),
                    fake.date_time_this_decade(),
                ),
            )

        connection.commit()
        connection.close()


if __name__ == "__main__":
    fake_data()
