# index.py

import algoliasearch_django as algoliasearch

from .models import Testimony

algoliasearch.register(Testimony)
