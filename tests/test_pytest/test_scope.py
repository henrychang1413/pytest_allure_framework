import pytest
import logging
log = logging.getLogger(__name__)


def test_foo(f1,m1,f2,s1):
    log.info("this is test foo")
    f1
    m1
    f2
    s1



if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )




