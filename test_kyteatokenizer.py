#!/usr/bin/env python
# -*- coding: utf-8 -*-

# utf-8対応
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
import kyteatokenizer

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^ 「」！？。]*[！？。]')

reader = PlaintextCorpusReader("data/",r"ginga.txt",
    encoding = 'utf-8',
    para_block_reader = read_line_block,
     sent_tokenizer = jp_sent_tokenizer,
     word_tokenizer = kyteatokenizer.JPKyteaTokenizer())

print ' '.join(reader.words()[20:80])
