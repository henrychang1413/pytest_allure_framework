import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMPT("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection
    print("teardown smtp")
    smtp_connection.close()




