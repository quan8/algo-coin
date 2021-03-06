from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def members(cls):
        return cls.__members__.keys()


class TickType(BaseEnum):
    # Messages
    TRADE = 'TRADE'  # Match
    RECEIVED = 'RECEIVED'  # Order received
    OPEN = 'OPEN'  # New Order
    DONE = 'DONE'  # Order completed, either filled or cancelled
    CHANGE = 'CHANGE'  # Order modified

    ERROR = 'ERROR'  # Internal error
    ANALYZE = 'ANALYZE'  # Internal
    HALT = 'HALT'  # Trading halt
    CONTINUE = 'CONTINUE'  # Trading continue
    EXIT = 'EXIT'  # System exit

    HEARTBEAT = 'HEARTBEAT'  # Exchange heartbeat


class TradingType(BaseEnum):
    NONE = 'NONE'
    SANDBOX = 'SANDBOX'
    LIVE = 'LIVE'
    BACKTEST = 'BACKTEST'
    SIMULATION = 'SIMULATION'


class ExchangeType(BaseEnum):
    NONE = 'NONE'
    BITSTAMP = 'BITSTAMP'
    BITFINEX = 'BITFINEX'
    CEX = 'CEX'
    GDAX = 'GDAX'
    COINBASE = 'COINBASE'
    GEMINI = 'GEMINI'
    HITBTC = 'HITBTC'
    ITBIT = 'ITBIT'
    KRAKEN = 'KRAKEN'
    LAKE = 'LAKE'
    POLONIEX = 'POLONIEX'
    DERIBIT = 'DERIBIT'
    BITMEX = 'BITMEX'


class CurrencyType(BaseEnum):
    USD = 'USD'
    BTC = 'BTC'
    ETH = 'ETH'
    LTC = 'LTC'
    BCH = 'BCH'
    ZEC = 'ZEC'


class PairType(BaseEnum):
    # USD Pairs
    USDBTC = (CurrencyType.USD, CurrencyType.BTC)
    USDETH = (CurrencyType.USD, CurrencyType.ETH)
    USDLTC = (CurrencyType.USD, CurrencyType.LTC)
    USDBCH = (CurrencyType.USD, CurrencyType.BCH)
    USDZEC = (CurrencyType.USD, CurrencyType.ZEC)

    # BTC Pairs
    BTCUSD = (CurrencyType.BTC, CurrencyType.USD)
    BTCETH = (CurrencyType.BTC, CurrencyType.ETH)
    BTCLTC = (CurrencyType.BTC, CurrencyType.LTC)
    BTCBCH = (CurrencyType.BTC, CurrencyType.BCH)
    BTCZEC = (CurrencyType.BTC, CurrencyType.ZEC)

    # ETH Pairs
    ETHUSD = (CurrencyType.ETH, CurrencyType.USD)
    ETHBTC = (CurrencyType.ETH, CurrencyType.BTC)

    # LTC Pairs
    LTCUSD = (CurrencyType.LTC, CurrencyType.USD)
    LTCBTC = (CurrencyType.LTC, CurrencyType.BTC)

    # BCH Pairs
    BCHUSD = (CurrencyType.BCH, CurrencyType.USD)
    BCHBTC = (CurrencyType.BCH, CurrencyType.BTC)

    # ZEC Pairs
    ZECUSD = (CurrencyType.ZEC, CurrencyType.USD)
    ZECBTC = (CurrencyType.ZEC, CurrencyType.BTC)
    ZECETH = (CurrencyType.ZEC, CurrencyType.ETH)  # Gemini

    def __str__(self):
        return str(self.value[0].value) + str(self.value[1].value)

    @staticmethod
    def from_string(str):
        s1 = str[:3]
        c1 = CurrencyType(s1)
        s2 = str[3:6]
        c2 = CurrencyType(s2)
        return PairType((c1, c2))


class Side(BaseEnum):
    NONE = 'NONE'
    BUY = 'BUY'
    SELL = 'SELL'


class OptionSide(BaseEnum):
    NONE = 'NONE'
    CALL = 'CALL'
    PUT = 'PUT'


class OrderType(BaseEnum):
    NONE = 'NONE'
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'


class OrderSubType(BaseEnum):
    NONE = 'NONE'
    POST_ONLY = 'POST_ONLY'
    FILL_OR_KILL = 'FILL_OR_KILL'
    # ALL_OR_NOTHING = 3


class ChangeReason(BaseEnum):
    NONE = 'NONE'
    CANCELLED = 'CANCELLED'
    FILLED = 'FILLED'


class TradeResult(BaseEnum):
    NONE = 'NONE'
    PENDING = 'PENDING'
    PARTIAL = 'PARTIAL'
    FILLED = 'FILLED'
    REJECTED = 'REJECTED'


class InstrumentType(BaseEnum):
    COIN = 'COIN'
    PAIR = 'PAIR'
    OPTION = 'OPTION'
    FUTURE = 'FUTURE'


class RiskReason(BaseEnum):
    NONE = 'NONE'
    PARTIAL = 'PARTIAL'
    FULL = 'FULL'
