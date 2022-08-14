import requests
from typing import List, Dict, Union
from operator import itemgetter


class Requests:

    def __init__(self, histories: List[Dict]):
        self.histories: List[Dict] = histories

    def get(self, url, params=None, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.get(url, params=params, **kwargs)

    def options(self, url, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.options(url, **kwargs)

    def head(self, url, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.head(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.post(url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.put(url, data=data, **kwargs)

    def patch(self, url, data=None, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.patch(url, data=data, **kwargs)

    def delete(self, url, **kwargs) -> requests.Response:
        self._set_hook(kwargs)
        return requests.delete(url, **kwargs)

    def Session(self) -> requests.Session:
        session = requests.Session()
        session.hooks["response"].append(self._hook)
        return session

    def session(self) -> requests.Session:
        return self.Session()

    def __getattr__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return getattr(requests, item)

    def _hook(self, response: requests.Response, *args, **kwargs) -> None:
        total_seconds = int(response.elapsed.total_seconds())
        micro_seconds = f"{response.elapsed.microseconds:<06}"
        self.histories.append({
            "url": response.request.url,
            "method": response.request.method,
            "elapsed": f"{total_seconds}.{micro_seconds}"
        })

    def _set_hook(self, item: Union[dict, requests.Session]) -> None:
        if isinstance(item, dict):
            item["hooks"] = {"response": [self._hook]}
        else:
            item.hooks["response"].append(self._hook)
