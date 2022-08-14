

def test_baidu(requests):
    resp = requests.get("https://www.baidu.com")
    assert resp.status_code < 400


def test_qq(requests):
    resp = requests.get("https://weixin.qq.com/")
    assert resp.status_code < 400


def test_taobao(requests):
    resp = requests.get("https://www.taobao.com")
    assert resp.status_code < 400


def test_bilibili(requests):
    resp = requests.get("https://www.bilibili.com")
    assert resp.status_code < 400
