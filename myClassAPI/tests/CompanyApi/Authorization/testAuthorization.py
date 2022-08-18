from  api import MyAPIClass


mc = MyAPIClass

def test_get_token():
    status, result = mc.get_getToken(mc)
    assert status == 200
    assert 'USD' in result