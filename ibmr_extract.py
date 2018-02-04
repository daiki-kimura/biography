# -*- encoding: utf-8 -*-

from __future__ import print_function

# pip install -r requirements.txt --user
from bs4 import BeautifulSoup
import urllib
import codecs


def url2html(url, div_class_name, html_filename):
    f = urllib.urlopen(url)
    html_text = f.read()

    soup = BeautifulSoup(html_text)
    soup_fa = soup.findAll('div', class_=div_class_name)
    if len(soup_fa) != 1:
        raise NotImplemented
    htmls = soup_fa[0].prettify()
    htmls = '<meta charset="UTF-8">\n' + \
        htmls

    with codecs.open(html_filename, 'w', 'utf-8') as f:
        f.write(htmls)


base_url = \
    'http://researcher.watson.ibm.com/researcher/'

url2html(base_url + 'view.php?person=jp-daiki',
         'ibm-container-body', 'ibmr_profile.html')
url2html(base_url + 'view_person_pubs.php?person=jp-daiki&t=1',
         'ibm-container-body', 'ibmr_publications.html')
url2html(base_url + 'view_person_pubs.php?person=jp-daiki&t=2',
         'ibm-container-body', 'ibmr_patents.html')
