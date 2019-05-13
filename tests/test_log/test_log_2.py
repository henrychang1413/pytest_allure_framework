
import time
import pytest
import sys
import logging
log = logging.getLogger(__name__)



def test_myoutput(capsys):
    # or use "capfd" for fd-level
    log.debug("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    log.debug("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"


def test_set_comparison():
    set1=set("13308")
    set2 =set("80301")
    assert set1 == set2


if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
