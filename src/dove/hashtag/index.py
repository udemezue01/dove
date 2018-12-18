# index.py

import algoliasearch_django as algoliasearch

from .models import Hasgtag

algoliasearch.register(Hasgtag)
