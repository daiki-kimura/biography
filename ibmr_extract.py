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
        raise NotImplemented
    htmls = soup_fa[0].prettify()
    htmls = '<meta charset="UTF-8">\n' + htmls

    with codecs.open(html_filename, 'w', 'utf-8') as f:
        f.write(htmls)


base_url = \
    'https://researcher.watson.ibm.com/researcher/'

url2html(base_url + 'view.php?person=jp-daiki',
         'ibm-container-body', 'ibmr_profile.html')
# url2html(base_url + 'view_person_pubs.php?person=jp-daiki&t=1',
#          'ibm-container-body', 'ibmr_publications.html')
# url2html(base_url + 'view_person_pubs.php?person=jp-daiki&t=2',
#          'ibm-container-body', 'ibmr_patents.html')
