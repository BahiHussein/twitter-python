#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator 
import json
from collections import Counter
import io
 
fname = 'tweets.json'
stop = [" ", u'\u0645\u0646', u'\u0641\u064a', u'', u'the', u'RT', u'\u0648', u'#Egypt', u'\u0645\u0635\u0631', u'\u0641', u'in', u'\u064a\u0627', u'#\u0645\u0635\u0631', u'\u0627\u0644\u0644\u064a', u'\u0627\u064a\u0647',
u'to', u'@', u"#Egypt's", u'\u0627\u0644\u0644\u0647', u'\u0645\u0634' ]

with io.open(fname, 'r', encoding='utf8') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        words = tweet['text'].split(" ")

        termsOnly = [term for term in words if term not in stop and not term.startswith(('#', '@'))]

        # Update the counter
        count_all.update(termsOnly)

    # Print the first 5 most frequent words
    words = count_all.most_common(20)
    print words

    for word in words:
    	print(word[0])
