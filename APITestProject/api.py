import requests


class MyAPIClass:
    def __init__(self):
        self.base_url = 'https://min-api.cryptocompare.com/data/'

    def get_price(self, fsym: str, tsym: str):
        """получение стоимости валюты fsym в валюте tsym"""
        res = requests.get(self.base_url + f'price?fsym={fsym}&tsyms={tsym}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_price_full_data(self, fsyms: str, tsyms: str):
        """Получение подробной информации о стоимости валют tsyms в вылютах fsyms"""
        res = requests.get(self.base_url + f'pricemultifull?fsyms={fsyms}&tsyms={tsyms}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_generate_custom_avg(self, fsym: str, tsym: str, extra_params: str):
        """Получение произвольной информации"""
        res = requests.get(self.base_url + f'generateAvg?fsym={fsym}&tsym={tsym}&e={extra_params}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Daily_Pair_OHLCV(self, fsym: str, tsym: str, limit: int, extra_params: str = '', aggregate: int = None,
                             aggregatePredictableTimePeriods: bool = None, allData: bool = None, toTs: int = None,
                             explainPath: bool = None, sign: bool = None):
        """Получение данных об открытии, максимуме, минимуме, закрытии, объеме от и объеме до из ежедневных
        исторических данных """
        res = requests.get(
            self.base_url + f'v2/histoday?fsym={fsym}&tsym={tsym}&limit={limit}&e={extra_params}&aggregate={aggregate}&aggregatePredictableTimePeriods={aggregatePredictableTimePeriods}&allData={allData}&toTs={toTs}&explainPath={explainPath}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Hourly_Pair_OHLCV(self, fsym: str, tsym: str, limit: int, extra_params: str = '', aggregate: int = None,
                              aggregatePredictableTimePeriods: bool = None, allData: bool = None, toTs: int = None,
                              explainPath: bool = None, sign: bool = None):
        """Получние данных об открытии, максимуме, минимуме, закрытии, объеме от и объеме до из почасовых
        исторических данных """
        res = requests.get(
            self.base_url + f'v2/histohour?fsym={fsym}&tsym={tsym}&limit={limit}&e={extra_params}&aggregate={aggregate}&aggregatePredictableTimePeriods={aggregatePredictableTimePeriods}&allData={allData}&toTs={toTs}&explainPath={explainPath}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Minute_Pair_OHLCV(self, fsym: str, tsym: str, limit: int, extra_params: str = '', aggregate: int = None,
                              aggregatePredictableTimePeriods: bool = None, allData: bool = None, toTs: int = None,
                              explainPath: bool = None, sign: bool = None):
        """Получение данных об открытии, максимуме, минимуме, закрытии, объеме и объеме из ежеминутных исторических
        данных """
        res = requests.get(
            self.base_url + f'v2/histominute?fsym={fsym}&tsym={tsym}&limit={limit}&e={extra_params}&aggregate={aggregate}&aggregatePredictableTimePeriods={aggregatePredictableTimePeriods}&allData={allData}&toTs={toTs}&explainPath={explainPath}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Day_PAIR_OHLCV_by_TS(self, fsym: str, tsym: str, toTs: int, extra_params: str = 'CCCAGG',
                                  calculationType: str = None, sign: bool = None):
        """Получение цены любой криптовалюты в любой другой валюте, которая вам нужна, в заданную временную метку"""
        res = requests.get(
            self.base_url + f'pricehistorical?fsym={fsym}&tsyms={tsym}&ts={toTs}&e={extra_params}&calculationType={calculationType}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Daily_Exchange_Vol(self, tsym: str, limit: int, extra_params: str = '', aggregate: int = None,
                               aggregatePredictableTimePeriods: bool = None, toTs: int = None,
                               sign: bool = None):
        """Получение общего объемаежедневных исторических биржевых данных"""
        res = requests.get(
            self.base_url + f'exchange/histoday?tsym={tsym}&limit={limit}&e={extra_params}&aggregate={aggregate}&aggregatePredictableTimePeriods={aggregatePredictableTimePeriods}&toTs={toTs}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Hourly_Exchange_Vol(self, tsym: str, limit: int, extra_params: str = '', aggregate: int = None,
                                aggregatePredictableTimePeriods: bool = None, toTs: int = None,
                                sign: bool = None):
        """Получение общего объема ежечасных исторических биржевых данных"""
        res = requests.get(
            self.base_url + f'exchange/histohour?tsym={tsym}&limit={limit}&e={extra_params}&aggregate={aggregate}&aggregatePredictableTimePeriods={aggregatePredictableTimePeriods}&toTs={toTs}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Available_Coin_List(self, extra_params: str = '', sign: bool = None):
        """Получение списка всех криптовалют, доступных к торгам на текущий момент"""
        res = requests.get(self.base_url + f'blockchain/list&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Latest_Snapshot(self, fsym: str, extra_params: str = '', sign: bool = None):
        """Получение последнего агрегированного снимка блокчейна для запрошенной криптовалюты"""
        res = requests.get(self.base_url + f'blockchain/latest?fsym={fsym}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Mining_Calculator_data(self, fsyms: str, tsyms: str, extra_params: str = '', sign: bool = None):
        """Получение цены, общего предложения, скоростм хеширования, вознаграждения за блок и времени блока"""
        res = requests.get(
            self.base_url + f'blockchain/mining/calculator?fsyms={fsyms},ZEC&tsyms={tsyms}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Trading_Signals(self,fsym:str, extra_params: str = '', sign: bool = None):
        """Получение последней торговой информации для выбранной криптовалюты"""
        res = requests.get(self.base_url+f'tradingsignals/intotheblock/latest?fsym={fsym}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Mapping_From_Symbol(self,fsym:str, extra_params: str = '', sign: bool = None):
        res = requests.get(self.base_url+f'v2/pair/mapping/fsym?fsym={fsym}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Toplist_Volume_Full_Data(self,limit:int,tsym:str,page:int=None,assetClass:str='',ascending:bool=None,sign:bool=None):
        """Получение топа кртптовалют, по объему торгов"""
        res = requests.get(self.base_url+f'top/totalvolfull?limit={limit}&tsym={tsym}&page={page}&assetClass={assetClass}&ascending={ascending}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Toplist_Top_tier_Volume_Full_Data(self,limit:int,tsym:str,page:int=None,assetClass:str='',ascending:bool=None,sign:bool=None):
        """Получение количества лучших криптовалют по их общему объему высшего уровня на основе 20 лучших рынков"""
        res = requests.get(self.base_url+f'top/totaltoptiervolfull?limit={limit}&tsym={tsym}&page={page}&assetClass={assetClass}&ascending={ascending}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def get_Latest_News_Articles(self,lang:str,feeds:str='',categories:str='',excludeCategories:str='',ITs:int=None,sortOrder:str='',extra_params: str = '', sign: bool = None):
        """Получение заголовков новостных статей"""
        res = requests.get(self.base_url+f'v2/news/?lang={lang}&feeds={feeds}&categories={categories}&excludeCategories={excludeCategories}&ITs={ITs}&sortOrder={sortOrder}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Toplist_By_Pair_volume(self,tsym:str,limit:int=None,page:int=None,ascending:bool=None,extra_params: str = '', sign: bool = None):
        """Получение списка криптовалют лучших по объему для покупки указанной валюты"""
        res = requests.get(self.base_url+f'top/volumes?tsym={tsym}&limit={limit}&page={page}&ascending={ascending}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_Toplist_Of_Traiding_Pairs(self,fsym:str,limit:int=None,extra_params: str = '', sign: bool = None):
        """Получение лучших пар по объему для указанной валюты"""
        res = requests.get(self.base_url+f'top/pairs?fsym={fsym}&limit={limit}&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_All_Wallets_General_Info(self,extra_params: str = '', sign: bool = None):
        """Получение общей информации обо всех кошельках, зарегистрированных на cryptocompare.com"""
        res = requests.get(self.base_url+f'wallets/general&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def test_List_of_available_indices(self,extra_params: str = '', sign: bool = None):
        """Получение списка всех доступных индексов"""
        res = requests.get(self.base_url+f'index/list&extraParams={extra_params}&sign={sign}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result