# Copyright Gerard Krol
# License: MIT
from pages.index import *
from pages.help import *
from pages.download import *
from pages.news import *
from pages.about import *
from pages.documentation import *
from pages.donate import *
from pages.contribute import *

languages = ["de", "en", "es", "fr", "ja", "nl", "pt-br", "zh-cn"]
title = "Freenet"
def create_menu():
    return [
        IndexPage(),
        DownloadPage(),
        AboutPage(),
        NewsPage(),
        DocumentationPage(),
        HelpPage(),
        DonatePage(),
        DonateThanksPage(),
        ContributePage(),
        ]
