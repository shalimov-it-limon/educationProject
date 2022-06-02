from api import MyAPIClass
from settings import valid_fsym, valid_fsyms, valid_tsym, valid_tsyms, valid_tsym2, valid_extra_params,valid_lang

mc = MyAPIClass()


def test_get_price(fsym=valid_fsym, tsym=valid_tsym):
    status, result = mc.get_price(fsym, tsym)
    assert status == 200
    assert 'USD' in result


def test_get_price_full_data(fsyms=valid_fsym, tsyms=valid_tsyms):
    status, result = mc.get_price_full_data(fsyms, tsyms)
    assert status == 200
    assert 'RAW' in result


def test_generate_custom_avg(fsym=valid_fsym, tsym=valid_tsym2, extra=valid_extra_params):
    status, result = mc.get_generate_custom_avg(fsym, tsym, extra)
    assert status == 200
    assert 'DISPLAY' in result


def test_get_Daily_Pair_OHLCV(fsym = valid_fsym, tsym = valid_tsym2, limit = 10):
    status,result = mc.get_Daily_Pair_OHLCV(fsym,tsym,limit)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Hourly_Pair_OHLCV(fsym = valid_fsym, tsym = valid_tsym2, limit = 10):
    status, result = mc.get_Hourly_Pair_OHLCV(fsym,tsym,limit)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Minute_Pair_OHLCV(fsym = valid_fsym, tsym = valid_tsym2, limit = 10):
    status, result = mc.get_Minute_Pair_OHLCV(fsym,tsym,limit)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Day_PAIR_OHLCV_by_TS(fsym = valid_fsym, tsym = valid_tsym2, ts = 1452680400):
    status, result = mc.get_Day_PAIR_OHLCV_by_TS(fsym, tsym, ts)
    assert status == 200
    assert 'BTC' in result


def test_get_Daily_Exchange_Vol(tsym = valid_tsym2, limit =10):
    status, result = mc.get_Daily_Exchange_Vol(tsym,limit)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Hourly_Exchange_Vol(tsym = valid_fsym,limit =10):
    status, result = mc.get_Hourly_Exchange_Vol(tsym,limit)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Available_Coin_List():
    status, result = mc.get_Available_Coin_List()
    assert status == 200
    assert 'RateLimit' in result


def test_get_Latest_Snapshot(fsym = valid_fsym):
    status, result = mc.get_Latest_Snapshot(fsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Mining_Calculator_data(fsyms = valid_fsyms, tsyms = valid_tsym2):
    status, result = mc.get_Mining_Calculator_data(fsyms,tsyms)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Trading_Signals(fsym = valid_fsym):
    status, result = mc.get_Trading_Signals(fsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Mapping_From_Symbol(fsym = valid_fsym):
    status, result = mc.get_Mapping_From_Symbol(fsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Toplist_Volume_Full_Data(limit = 10,fsym = valid_fsym):
    status, result = mc.get_Toplist_Volume_Full_Data(limit,fsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Latest_News_Articles(lang = valid_lang):
    status, result = mc.get_Latest_News_Articles(lang)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Toplist_By_Pair_volume(tsym = valid_fsym):
    status, result = mc.get_Toplist_By_Pair_volume(tsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_Toplist_Of_Traiding_Pairs(fsym = valid_fsym):
    status, result = mc.get_Toplist_Of_Traiding_Pairs(fsym)
    assert status == 200
    assert 'RateLimit' in result


def test_get_All_Wallets_General_Info():
    status, result = mc.get_All_Wallets_General_Info()
    assert status == 200
    assert 'RateLimit' in result


def test_test_List_of_available_indices():
    status, result =mc.test_List_of_available_indices()
    assert status == 200
    assert 'RateLimit' in result
