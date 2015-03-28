import urllib2

MAPPINGS_URL = 'http://mappings.dbpedia.org/index.php/Mapping_en'
HTML_STORE_PATH = 'dbpedia/'


def get_page_and_store(url, store_path):
    """
    Fetch a html page from url and store in store_path
    """

    page = urllib2.urlopen(url).read()

    if store_path is not None:
        open(store_path, 'r').write(page)

    return page


def get_infoboxes_from_mapping_page(mapping_page):
    """
    Return (infobox, url) pairs, given the HTML DBpedia mapping page.

    infobox is in 'Infobox <name>' format, as appeared in DBpedia Mapping page.
    url directs to the mapping page for each infobox
    """
    pass


def get_class_from_infobox_page(infobox_page):
    """
    Return class of the infobox, given the HTML DEpedia infobox_page

    class is in CamelCase, exactly as appear in the infobox_page
    """
    pass


def get_infobox_class_pairs():
    """
    Return pairs of (infobox, class)

    infobox format is as returned by get_infoboxes_from_mapping_page.
    class format is as returbed by get_class_from_infobox_page.
    """
    pass



