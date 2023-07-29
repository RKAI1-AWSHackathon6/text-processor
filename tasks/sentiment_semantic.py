from typing import Union
from schemas.sentiment_summary import SentimentSummaryCode
from tasks.chatgpt_api import api_chat_gpt
from core.config import settings


class SentimentSummary:
    def __int__(self):
        pass

    @staticmethod
    def get_sentiment_and_summary(content: str) -> Union[SentimentSummaryCode, None]:
        result = None
        is_done = False
        for _ in range(settings.RETRY_OPENAI_API):
            for i in range(len(settings.OPENAI_API_KEYS)):
                result = api_chat_gpt.get_sentiment(content, settings.OPENAI_API_KEYS[i])
                if result is not None:
                    is_done = True
                    break
            if is_done:
                break
        if result is None:
            return None
        result = result.message.content
        try:
            print(">>>> Result: ", result)
            _type, _explain, _summary = result.replace('\n\n', '\n').split('\n')

            if 'UNK' in _type:
                _type = 3
            elif 'YES' in _type:
                _type = 2
            elif 'NO' in _type:
                _type = 1
            else:
                return None
            _explain = _explain.split('EXPLAIN: ')[-1].strip()
            _summary = _summary.split('SUMMARY: ')[-1].strip()
            return SentimentSummaryCode(type=_type, explain=_explain, summary=_summary, message='success')
        except Exception as e:
            return None


sentiment_summary_er = SentimentSummary()

if __name__ == '__main__':
    _result = sentiment_summary_er.get_sentiment_and_summary('''BTC price shrugs off strong PCE data as Bitcoin traders eye $28K range Bitcoin traders expect downside as BTC price offers a muted reaction to the Fed’s “preferred” inflation metric. Bitcoin BTC tickers down $29,295 stayed rangebound at the July 28 Wall Street open despite further United States inflation data beating expectations. Fed’s “preferred” inflation metric points to waning pressure
    Data from Cointelegraph Markets Pro and TradingView showed BTC price action getting only a modest boost from the Personal Consumption Expenditures (PCE) Index print.
    
    This came in below estimates, hinting that U.S. inflation was continuing to subside and copying other data prints from the week.
    
    Addressing its implications, financial commentary resource The Kobeissi Letter noted that PCE represented the Federal Reserve’s “preferred” inflation metric, as previously revealed by Chair Jerome Powell.
    
    “PCE inflation is now at its lowest since April 2021. The Fed may finally have inflation under control,” it suggested in part of its analysis on social media.
    
    However, much like the July 26 Fed interest rate hike and the July 27 U.S. Q2 gross domestic product (GDP) estimate, Bitcoin refused to turn on volatility, sticking between $29,000 and $29,500.
    
    Bitcoin stays below bulls’ resistance target
    Among traders, there was still an appetite for BTC price downside, with the $30,000 resistance now in place for over a week.
    
    Related: Bitcoin price risks ‘major volatility’ as 10K BTC hits exchanges
    
    Popular trader Crypto Tony confirmed that he remained short BTC below $29,600.
    
    “I expect continuation down to $28,000 in time, but for sure we could range here for a little while before the drop,” he told Twitter (now known as X) followers on the day.
    
    Fellow trader Daan Crypto Trades likewise placed emphasis on the loss of the local range focused on the $30,000 mark.
    
    “With Bitcoin Rejecting from the previous range, I think it makes sense to prepare for low $28Ks,” he argued.
    
    Michaël van de Poppe, founder and CEO of trading firm Eight, meanwhile spied what he called “deviation” on the daily BTC/USD chart — something previously occurring in February that was followed by an upward rebound.
    
    Van de Poppe additionally asked whether the weekend, with its thinner liquidity and more options for volatile movement, could produce a “classic” comeback.
    
    ''')
    print(result)
