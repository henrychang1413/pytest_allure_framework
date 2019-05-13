import time
import pytest
import sys
import logging
log = logging.getLogger(__name__)


def test_1():
    #log = logging.getLogger('test_1')
    log.debug('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'

def test_2():
    #log = logging.getLogger('test_2')
    log.debug('in test_2')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    #assert 0, 'failing for demo purposes'

def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    #assert captured.out == "next\n"



if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
