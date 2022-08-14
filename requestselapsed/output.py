import requests
from operator import itemgetter


def make_report(histories) -> str:
    title = "{:<15} {:<15} {}\n".format("elapsed", "method", "url")
    items = sorted(histories, key=itemgetter("elapsed"), reverse=True)
    return title + "\n".join([f"{i['elapsed']:<15} {i['method']:<15} {i['url']}" for i in items])


def console_output(content: str) -> None:
    print(f"\n\n{content}")


def feishu_output(url: str, content: str) -> None:
    payload = {
        "msg_type": "text",
        "content": {
            "text": content
        }
    }
    requests.post(url, json=payload)
