from __future__ import absolute_import, unicode_literals

import urllib.request
from urllib.error import URLError

from bs4 import BeautifulSoup
from celery import shared_task, states
from celery.exceptions import Ignore

from webcollector.collector.models import Website


@shared_task(bind=True)
def parse_website(self, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    try:
        html = urllib.request.urlopen(req).read()
    except URLError as error:
        self.update_state(state=states.FAILURE, meta=error)
        raise Ignore()
    else:
        soup = BeautifulSoup(html, "lxml")

        Website.objects.create(
            title=str(soup.title),
            url=url,
            raw_text=soup.prettify(),
            text=soup.get_text(),
            task_id=self.request.id,
        )
