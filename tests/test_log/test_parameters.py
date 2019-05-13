import pytest
import logging
log = logging.getLogger(__name__)


@pytest.fixture(params=["how, BBB"])
def a(request):
    #log.info(request.param)
    return request.param

def test_a(a):
    log.info("this is a test ")
    m = a
    x = m[0]
    y = m[1]

    log.info(x)
    log.info(y)

    pass

def idfn(fixture_value):
    #log.info("fiture value is %s" %fixture_value)
    val = ""
    if fixture_value ==0 :
        val= "cat"
    else:
        val= "dog"
    return

@pytest.fixture(params=[0,1], ids=idfn)
def b(request):
    return request.param




def test_b(b):
    y = b
    log.info("test_b y value  is %s" %y)
    pass


@pytest.mark.parametrize('tester', [['var1', 'var2']], indirect=True)
class TestIt:

    def test_tc1(self, tester):
       tester.dothis()
       assert 1


@pytest.mark.parametrize('tester', [['var0', 'var0']], indirect=True)
class TestIt2:

    def test_tc12(self, tester):
       tester.dothis()
       assert 1











if __name__ == "__main__":
    # just run this file
    pytest.main( args=[__file__] )
