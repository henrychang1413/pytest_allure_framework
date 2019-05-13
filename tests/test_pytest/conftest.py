import smtplib
import pytest
import logging
log = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection
    log.info("\nteardown smtp")
    smtp_connection.close()

# @pytest.fixture(scope="function")
# def smtp_connection(request):
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

#     def fin():
#         log.info("teardown smpt_connection")
#         smtp_connection.close()

#     request.addfinalizer(fin)
#     return smpt_connection


@pytest.fixture(scope="session")
def s1():
    log.info("\ns1 session fixture")
    pass

@pytest.fixture(scope="module")
def m1():
    log.info("\nm1 module fixture")
    pass

@pytest.fixture
def f1(tmpdir):
    log.info("\nf1  fixture with tmpdir")
    pass

@pytest.fixture
def f2():
    log.info("\nf2 fixture")
    pass

