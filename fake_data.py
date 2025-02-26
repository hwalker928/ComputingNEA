from faker import Faker
import sqlite3
import base64
from utils import encryption

fake = Faker()


def fake_data():
    # Load the existing key pair with the generic password
    kp = encryption.KeyPair()
    kp.load_existing_key_pair("Password123!")

    # Create an encryption instance
    enc = encryption.Encryption(kp)

    # Connect to the SQLite database
    connection = sqlite3.connect("data/database.db")

    # Loop 10 times to insert fake data into the database
    for _ in range(10):
        # Insert fake data into the database
        connection.execute(
            "INSERT INTO CREDENTIALS (name, username, password, domain, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            (
                fake.company(),
                fake.user_name(),
                enc.encrypt(
                    "MySecurePassword1#"
                ),  # Encrypt the password before storing it in the database
                fake.domain_name(),
                fake.date_time_this_decade(),
                fake.date_time_this_decade(),
            ),
        )

    # Commit the changes and close the connection
    connection.commit()
    connection.close()


if __name__ == "__main__":
    fake_data()
