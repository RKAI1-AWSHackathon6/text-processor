from typing import List
import re
from schemas.base import BaseToken
from core.config import settings
from db.session import SessionLocal
from models.favourite import Favourite


class Classify:
    def __init__(self):
        self.token_symbol = []
        self.token_list = []

    def add_token(self, token: BaseToken):
        if token.symbol not in self.token_symbol:
            self.token_symbol.append(token.symbol)
            self.token_list.append(token)

    @staticmethod
    def replace_punctuation_and_join(sentence):
        sentence_without_punctuation = re.sub(r'[^\w\s]', ' ', sentence)
        words = sentence_without_punctuation.split()
        joined_sentence = ' '.join(words)
        return joined_sentence

    def classify(self, text_content: str) -> List[BaseToken]:
        count_occurrence = {}
        _text_content = text_content.lower()
        _text_content = self.replace_punctuation_and_join(_text_content)
        _text_content = _text_content.split(' ')
        # print(_text_content)
        for token in self.token_list:
            _symbol = token.symbol.lower()
            _name = token.name.lower()
            for t in _text_content:
                if t == _symbol or t == _name:
                    if token.symbol in count_occurrence:
                        count_occurrence[token.symbol] += 1
                    else:
                        count_occurrence[token.symbol] = 1
        count_occurrence_sorted = sorted(count_occurrence, key=lambda x: x[1], reverse=True)
        return list(filter(lambda x: x.symbol in count_occurrence_sorted, self.token_list))


classifier = Classify()
with SessionLocal() as db:
    favourite = db.query(Favourite).all()
    for f in favourite:
        classifier.add_token(BaseToken(symbol=f.symbol, name=f.name, id=f.id, icon=f.icon, rank=f.rank))

if __name__ == '__main__':
    # classifier.add_token(BaseToken(symbol='BTC', name='Bitcoin'))
    # classifier.add_token(BaseToken(symbol='ETH', name='Ethereum'))
    # classifier.add_token(BaseToken(symbol='BNB', name='Binance Coin'))
    # classifier.add_token(BaseToken(symbol='ADA', name='Cardano'))
    # classifier.add_token(BaseToken(symbol='DOGE', name='Dogecoin'))

    result = classifier.classify(text_content='This is a test BTC BTC Bitcoin ETH')
    for r in result:
        print(r)
