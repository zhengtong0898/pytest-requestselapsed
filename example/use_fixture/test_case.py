

def test_baidu(requests):
    resp = requests.get("https://www.baidu.com")
    assert resp.status_code < 400
