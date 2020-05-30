from __future__ import absolute_import, unicode_literals

from urllib.request import urlopen

from celery import AsyncResult, shared_task

from bs4 import BeautifulSoup


@shared_task
def parse_website(url, website_instance):
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    AsyncResult.task_id
    soup.title
    soup.contents
    soup.get_text()
