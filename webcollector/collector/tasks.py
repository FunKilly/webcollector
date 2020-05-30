from __future__ import absolute_import, unicode_literals

from urllib.request import urlopen

from bs4 import BeautifulSoup
from celery import shared_task
from celery.result import AsyncResult


@shared_task
def parse_website(url, website_instance):
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    AsyncResult.task_id
    soup.title
    soup.contents
    soup.get_text()
