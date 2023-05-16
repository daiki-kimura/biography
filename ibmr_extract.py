# -*- encoding: utf-8 -*-

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib.request
import codecs
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def url2html(url, div_class_name, html_filename):
    print('getting: ' + url)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/87.0.4280.88 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html_text = response.read()

    soup = BeautifulSoup(html_text, "html.parser")
    soup_fa = soup.findAll('div', class_=div_class_name)
    if len(soup_fa) != 1:
        raise NotImplementedError()
    htmls = soup_fa[0].prettify()
    htmls = '<meta charset="UTF-8">\n' + htmls

    with codecs.open(html_filename, 'w', 'utf-8') as f:
        f.write(htmls)


url2html('https://research.ibm.com/people/daiki-kimura',
         '_8TKwU', 'ibmr_profile.html')
