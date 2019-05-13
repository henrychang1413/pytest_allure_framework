import pytest
import logging
log = logging.getLogger(__name__)

def test_ehlo(smtp_connection):
    log.info("\nconnnect smpt ....")
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b'smtp.gmail.com' in msg
    #assert 0


def test_noop(smtp_connection):
    log.info("\nconnnect smpt ....")
    response, msg = smtp_connection.noop()
    assert response == 250
    #assert 0


if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )

