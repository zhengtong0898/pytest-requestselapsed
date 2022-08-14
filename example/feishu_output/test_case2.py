

def test_bilibili(requests):
    resp = requests.get("http://www.bilibili.com")
    assert resp.status_code < 400


def test_world():
    assert isinstance("world", str)
