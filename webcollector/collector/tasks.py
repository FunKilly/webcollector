from __future__ import absolute_import, unicode_literals


from celery import shared_task


@shared_task
def parse_website(url):

    # req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    # html = urllib.request.urlopen(req).read()

    # BeautifulSoup(html, "lxml")
    print("zobaczymy czy bedzie completed")
