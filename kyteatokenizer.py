#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize.api import *

class JPKyteaTokenizer(TokenizerI):
    def __init__(self):
        import Mykytea
        model_path = "/usr/local/share/kytea/model.bin"
        self.kytea = Mykytea.Mykytea(model_path)

    def tokenize(self, text):
        result = self.kytea.getWS(str(text))
        return result






