import urllib2
import re
from wikiscout import infobox_parser

MAPPINGS_URLS = [
    'http://mappings.dbpedia.org/index.php?title=Special:AllPages&namespace=204&from=1930s-UK-film-stub&to=Infobox_darts_player',
    'http://mappings.dbpedia.org/index.php?title=Special:AllPages&namespace=204&from=Infobox_diocese&to=US-child-writer-stub',
    'http://mappings.dbpedia.org/index.php?title=Special:AllPages&namespace=204&from=US-company-stub&to=Year_dab'
]

URL_PREFIX = 'http://mappings.dbpedia.org'
HTML_CACHE_PATH_PREFIX = 'dbpedia/'

def get_page_and_store(url, cache_path=None):
    """
    Fetch a html page from url and store in store_path
    """

    page = urllib2.urlopen(url).read()

    if cache_path is not None:
        open(cache_path, 'w').write(page)

    return page


def get_infobox_urls(mapping_page):
    """
    Return list of urls of infobox pages
    """
    pattern = re.compile('/index\.php/Mapping_en:Infobox_[-\w\./]+')
    return pattern.findall(mapping_page)


def get_class_from_infobox_page(infobox_page):
    """
    Return class of the infobox, given the HTML DEpedia infobox_page

    class is in CamelCase, exactly as appear in the infobox_page
    """
    pass

def get_infobox_class_pairs(from_cache=False):
    """
    Return pairs of (infobox, class)

    infobox format is lower case with hyphen (e.g. 'afl-player-2')
    class format is as returbed by get_class_from_infobox_page.
    """
    infobox_urls = []
    for mapping_url in MAPPINGS_URLS:
        mapping_page = get_page_and_store(mapping_url)
        infobox_urls += get_infobox_urls(mapping_page)

    for i, infobox_url in enumerate(infobox_urls):
        full_url = URL_PREFIX + infobox_url
        infobox = infobox_parser.get_class(infobox_url.split(':')[1]).replace('wikipedia-', '')
        cache_path = HTML_CACHE_PATH_PREFIX + 'infobox-' + infobox + '.html'

        print '(%d/%d) %s' % (i+1, len(infobox_urls), infobox)
        
        if from_cache or i < 169:
            infobox_page = open(cache_path, 'r').read()

        else:
            infobox_page = get_page_and_store(URL_PREFIX + infobox_url, cache_path)



get_infobox_class_pairs()

