import pytest


if __name__ == '__main__':
    pytest.main(
        args = [
            "--output-mode=feishu",
            "--feishu-webhook-url=https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ]
    )
