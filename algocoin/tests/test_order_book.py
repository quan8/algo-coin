import random
from datetime import datetime
from pprint import pprint

from algocoin.lib.order_book import OrderBook
from algocoin.lib.structs import MarketData, Instrument
from algocoin.lib.enums import Side, \
                               OptionSide, \
                               CurrencyType, \
                               PairType, \
                               OrderType, \
                               OrderSubType, \
                               TickType, \
                               TradeResult, \
                               InstrumentType, \
                               ChangeReason


def generateInstruments(pairs):
    return [Instrument(underlying=pair) for pair in pairs]


def initialMarketData(count, instruments=None):
    instruments = instruments or generateInstruments([PairType.BTCUSD, PairType.ETHUSD])
    ret = []
    for _ in range(count):
        side = random.choice([Side.BUY, Side.SELL])
        volume = random.randrange(0, 20) / 10

        if side == Side.BUY:
            price = random.randrange(500, 550) / 10

        if side == Side.SELL:
            price = random.randrange(551, 600) / 10

        tick = random.choice([TickType.OPEN])
        instrument = random.choice(instruments)

        remaining = random.choice([0.0, random.randrange(0, 100)/10])

        if tick == TickType.DONE:
            reason = random.choice([ChangeReason.NONE, ChangeReason.CANCELLED, ChangeReason.FILLED])

        elif tick == TickType.CHANGE:
            reason = random.choice([ChangeReason.NONE, ChangeReason.CANCELLED, ChangeReason.FILLED])

        else:
            reason = ChangeReason.NONE

        sequence = -1
        order_type = OrderType.NONE

        m = MarketData(time=datetime.now(),
                       volume=volume,
                       price=price,
                       type=tick,
                       instrument=instrument,
                       side=side,
                       remaining=remaining,
                       reason=reason,
                       sequence=sequence,
                       order_type=order_type)

        ret.append(m)
    return ret


def generateMarketData(count, instruments=None):
    instruments = instruments or generateInstruments([PairType.BTCUSD, PairType.ETHUSD])
    ret = []
    for _ in range(count):
        side = random.choice([Side.BUY, Side.SELL])

        volume = random.randrange(0, 20) / 10

        if side == Side.BUY:
            price = random.randrange(500, 550) / 10

        if side == Side.SELL:
            price = random.randrange(551, 600) / 10

        tick = random.choice([TickType.OPEN,
                              TickType.DONE,
                              TickType.CHANGE])
        instrument = random.choice(instruments)

        remaining = random.choice([0.0, random.randrange(0, 100)/10])

        if tick == TickType.DONE:
            reason = random.choice([ChangeReason.NONE, ChangeReason.CANCELLED, ChangeReason.FILLED])

        elif tick == TickType.CHANGE:
            reason = random.choice([ChangeReason.NONE, ChangeReason.CANCELLED, ChangeReason.FILLED])

        else:
            reason = ChangeReason.NONE

        sequence = -1
        order_type = OrderType.NONE

        m = MarketData(time=datetime.now(),
                       volume=volume,
                       price=price,
                       type=tick,
                       instrument=instrument,
                       side=side,
                       remaining=remaining,
                       reason=reason,
                       sequence=sequence,
                       order_type=order_type)

        ret.append(m)

    return ret


class TestDataSource:
    def test_order_book(self):
        pairs = [PairType.BTCUSD, PairType.ETHUSD]
        instruments = generateInstruments(pairs)

        ob = OrderBook(instruments)

        for item in initialMarketData(50, instruments):
            ob.push(item)

        print(str(ob))

    def test_order_book_sequence(self):
        pairs = [PairType.BTCUSD]
        instruments = generateInstruments(pairs)
        ob = OrderBook(instruments)

        p = 0.0
        while p < 2.1:
            m = MarketData(time=datetime.now(),
                           volume=1.0,
                           price=p,
                           type=TickType.OPEN,
                           instrument=instruments[0],
                           side=Side.BUY,
                           remaining=0.0,
                           reason=ChangeReason.NONE,
                           sequence=-1,
                           order_type=OrderType.NONE)
            if p > 1.0:
                m.side = Side.SELL
            ob.push(m)
            p += .1

        print(ob)

        p = 0.0
        while p < 2.1:
            if round(p * 10) % 2 < 1:
                m = MarketData(time=datetime.now(),
                               volume=1.0,
                               price=p,
                               type=TickType.OPEN,
                               instrument=instruments[0],
                               side=Side.BUY,
                               remaining=0.0,
                               reason=ChangeReason.NONE,
                               sequence=-1,
                               order_type=OrderType.NONE)
                if p > 1.0:
                    m.side = Side.SELL
                ob.push(m)
            p += .1

        print(ob)

        p = 0.0
        while p < 2.1:
            m = MarketData(time=datetime.now(),
                           volume=1.0,
                           price=p,
                           type=TickType.CHANGE,
                           instrument=instruments[0],
                           side=Side.BUY,
                           remaining=0.0,
                           reason=ChangeReason.CANCELLED,
                           sequence=-1,
                           order_type=OrderType.NONE)
            if p > 1.0:
                m.side = Side.SELL

            if round(p * 10) % 2 < 1:
                m.type = TickType.CHANGE
                m.reason = ChangeReason.FILLED
            ob.push(m)
            p += .1

        print(ob)

        print(ob._ob[instruments[0]]._bidd.keys())
        print(ob._ob[instruments[0]]._bid)
        # TODO check floating point error
        assert ob._ob[instruments[0]]._bidd[0.0] == 1.0
        assert ob._ob[instruments[0]]._bidd[0.2] == 1.0
        assert ob._ob[instruments[0]]._bidd[0.4] == 1.0
        assert ob._ob[instruments[0]]._bidd[0.6] == 1.0
        assert ob._ob[instruments[0]]._bidd[0.8] == 1.0
        assert ob._ob[instruments[0]]._bidd[1.0] == 1.0
        assert ob._ob[instruments[0]]._askk[1.2] == 1.0
        assert ob._ob[instruments[0]]._askk[1.4] == 1.0
        assert ob._ob[instruments[0]]._askk[1.6] == 1.0
        assert ob._ob[instruments[0]]._askk[1.8] == 1.0
        assert ob._ob[instruments[0]]._askk[1.8] == 1.0
