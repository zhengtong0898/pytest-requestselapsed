from .api import Requests
from .output import make_report, console_output, feishu_output
import pytest
from typing import List, Dict


class PluginSession:

    def __init__(self):
        self.histories: List[Dict] = []

    @pytest.fixture(name="requests", scope="session")
    def request_client(self) -> Requests:
        return Requests(self.histories)

    @pytest.hookimpl
    def pytest_sessionfinish(self, session: pytest.Session, exitstatus) -> None:
        content = make_report(self.histories)
        if session.config.option.output_mode == "console":
            console_output(content)
        elif session.config.option.output_mode == "feishu":
            feishu_output(session.config.option.feishu_webhook_url, content)


@pytest.hookimpl
def pytest_addoption(parser):
    group = parser.getgroup("requestselapsed")
    group.addoption(
        "--output-mode",
        dest="output_mode",
        metavar="OutputMode",
        choices=["console", "feishu", "no"],
        default="no",
        action="store",
        help="有效的OutputMode是: console、feishu、no"
    )
    group.addoption(
        "--feishu-webhook-url",
        dest="feishu_webhook_url",
        default=None,
        action="store",
        help="当output_mode为feishu时, 当前参数是必填项"
    )


@pytest.hookimpl
def pytest_configure(config):
    session = PluginSession()
    config.pluginmanager.register(session)
