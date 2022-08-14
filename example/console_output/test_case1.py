

def test_hello():
    assert isinstance("hello", str)


def test_baidu(requests):
    resp = requests.get("https://www.baidu.com")
    assert resp.status_code < 400


def test_qq(requests):
    resp = requests.get("https://www.tutorialspoint.com")
    assert resp.status_code < 400
