from typing import Dict

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from gvol import queries, types


class GVol:
    """GVol API client.

    Contact info@genesisvolatility.io for API key information.
    """

    _url = "https://app.pinkswantrading.com/graphql"

    def __init__(self, gvol_api_key: str) -> None:
        """Initializes GVol API client.

        Args:
            gvol_api_key (str): API key
        """
        headers = {
            "x-oracle": f"{gvol_api_key}",
            "Content-Type": "application/json",
            "accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
        }

        transport = RequestsHTTPTransport(url=self._url, headers=headers)
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def CurrentOrderbookSkewStrike(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """The volatility skew, also known as the smile, represents an option’s implied volatility given different strike prices or delta.

        The Black-Scholes model assumes a constant volatility throughout the life of the option, yet, the underlying may behave differently depending on where it’s trading.

        Hence, if crypto were to drop 50% tomorrow (or double in value), the volatility would probably increase, therefore, out-of-money strikes and deltas are typically priced with richer volatilities.

        A good way of measuring skew is by calculating the ratio of an out-of-money option versus an at-the-money option. This relationship typically changes in low volatility environments versus high volatility environments.

        Example Response: ``{"ts": "1637677441586", "instrumentName": "BTC-24NOV21-59000-C", "strike": 59000, "expiration": "1637712000000", "bidIv": 59.4, "markIv": 66.33, "askIv": 71.68, "delta": 0.10811}``
        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict

        """
        return self._client.execute(
            gql(queries.CurrentOrderbookSkewStrike),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def Shadow25Skews(
        self, dateTime: types.String, symbol: types.SymbolEnumType
    ) -> Dict:
        """This end-point represents the 20/30 skew (~∆25) for various expirations at the given timestamp parameter.

        Data goes back to mid-February 2020.

        The end-point supports 1hr timestamp granularity.

        Example Response: ``{"date": "1613930400000", "twentyThirtyCallIvMinusPutIv": -2.19, "daysUntilExpiration": 1 }``

        Args:
            dateTime: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.Shadow25Skews),
            variable_values={"dateTime": dateTime, "symbol": symbol},
        )

    def CurrentOrderbookSkewDeltaBucket(
        self,
        expiration: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """The volatility skew, also known as the smile, represents an option’s implied volatility given a different strike prices or delta.

        The Black-Scholes model assumes a constant volatility throughout the life of the option, yet, the underlying may behave differently depending on where it’s trading.

        Hence, if crypto were to drop 50% tomorrow (or double in value), the volatility would probably increase, therefore, out-of-money strikes and deltas are typically priced with richer volatilities.

        A good way of measuring skew is by calculating the ratio of an out-of-money option versus an at-the-money option. This relationship typically changes in low volatility environments versus high volatility environments.


        Args:
            expiration: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentOrderbookSkewDeltaBucket),
            variable_values={
                "expiration": expiration,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def CurrentOrderbookTermStructure(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """The volatility term structure represents the implied volatility given different expiration dates.

        Example Response: ``{"expiration": "1637740800000", "markIv": 72.305, "forwardVolatility": 72.3 }``

        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentOrderbookTermStructure),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def CurrentOrderbook1hr3020Skew(
        self,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """This data displays the difference between the call implied volatility and put implied volatility for all options which have delta values between -.30 and -.20 (puts) or between .20 and .30 (calls).

        This data is useful to gauge how expensive calls are versus puts.

        This displays the symmetry (or asymmetry) of the volatility skews.

        RangeStart / rangeEnd, we can view how skew symmetry has changed for options within the given expiration window.


        Args:
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentOrderbook1hr3020Skew),
            variable_values={
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def CurrentOrderbook1HrATMVol(
        self,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """This data shows the average ATM volatility for each hour during the given time period.. This gives a good idea regarding how volatility has changed throughout time.

        Using rangesStart / rangeEnd , we can view how volatility has changed for options within the given expiration window.

        Example Response: ``{"date": "1635084000000", "avgMarkIv": 83.98 }, { "date": "1635087600000", "avgMarkIv": 84.13 }``

        Args:
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentOrderbook1HrATMVol),
            variable_values={
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def ConstantMaturityATMIV(self, symbol: types.SymbolEnumType) -> Dict:
        """This returns Constanct Maturity ATM IV for Deribit.

        Example Response: ``{"date": "1606089600000", "seven": 76.22, "thirty": 73.69, "sixty": 73.81, "ninty": 73.96, "onehundredeighty": 74.35}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ConstantMaturityATMIV), variable_values={"symbol": symbol}
        )

    def ConstantMaturity30to20DeltaSkew(self, symbol: types.SymbolEnumType) -> Dict:
        """This returns Constant maturity 20/30 skew for Deribit only.

        Example Response: ``{"date": "1606089600000", "seven": 6.66, "thirty": 10.69, "sixty": 12.71, "ninty": 13.45, "onehundredeighty": 14.77}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ConstantMaturity30to20DeltaSkew),
            variable_values={"symbol": symbol},
        )

    def ShadowTermStructure(
        self,
        dateTime: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Using our shadow features allows traders to compare current skew and term structure quotes to past market quotes.

        This is different from historical trade data. Quotes represent a complete picture of potential trades, as opposed to actual trades, and therefore are more indicative of where the market was priced at a given point in time.

        Example Response: ``{"sequenceDays2Exp": 0, "tsHourShadow": "1609502400000", "tsHourCurrent": null, "daysUntilExpiration": "0", "markIvCurrent": 73.02, "markIvShadow": 66.9 }``

        Args:
            dateTime: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ShadowTermStructure),
            variable_values={
                "dateTime": dateTime,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def ShadowTermStructureComparison(
        self,
        dateTimeOne: types.String,
        dateTimeTwo: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Using our shadow features allows traders to compare current skew and term-structure quotes to past market quotes.

        This is different from historical trade data. Quotes represent a complete picture of potential trades, as opposed to actual trades, and therefore are more indicative of where the market was priced at a given point in time.

        Example Response: ``{"sequenceDays2Exp": 1, "tsHourShadow": "1614690000000", "tsHourCurrent": "1609502400000", "daysUntilExpiration": "1", "markIvCurrent": 66.9, "markIvShadow": 81.77}``

        Args:
            dateTimeOne: (types.String)
            dateTimeTwo: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ShadowTermStructureComparison),
            variable_values={
                "dateTimeOne": dateTimeOne,
                "dateTimeTwo": dateTimeTwo,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def HistoricalSkew(
        self,
        date: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """The volatility skew, also known as the smile, represents an option’s implied volatility given a different strike prices or delta.

        The Black-Scholes model assumes a constant volatility throughout the life of the option, yet, the underlying may behave differently depending on where it’s trading.

        Hence, if crypto were to drop 50% tomorrow (or double in value), the volatility would probably increase, therefore, out-of-money strikes and deltas are typically priced with richer volatilities.

        A good way of measuring skew is by calculating the ratio of an out-of-money option versus an at-the-money option. This relationship typically changes in low volatility environments versus high volatility environments.

        Example Response: ``{"expirationDate": "1609459200000", "weightedIv": 111.04, "strike": 30000, "premiumValue": 1037.58}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalSkew),
            variable_values={"date": date, "symbol": symbol, "exchange": exchange},
        )

    def HistoricalTermStructure(
        self,
        date: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """The volatility term structure represents the implied volatility given different expiration dates.

        Example Response: ``{"expirationDate": "1609459200000", "weightedIv": 61.99, "fwdIv": 61.99, "totalUsdTraded": 23831.01}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalTermStructure),
            variable_values={"date": date, "symbol": symbol, "exchange": exchange},
        )

    def HistoricalConstantSkew(
        self, exchange: types.ExchangeEnumType, days: types.Float
    ) -> Dict:
        """This chart displays the difference between the call implied volatility and put implied volatility for all options which have delta values between -.30 and -.20 (puts) or between .20 and .30 (calls).

        This chart is useful to gauge how expensive calls are versus puts.

        This displays the symmetry (or asymmetry) of the volatility skews.

        Example Response: ``{"date": "1606089600000", "btcSkewShort": 10.52, "btcSkewMed": 11.69, "btcSkewLong": 14.85, "ethSkewShort": 15.54, "ethSkewMed": 13.65, "ethSkewLong": 15.81}``

        Args:
            exchange: (types.ExchangeEnumType)
            days: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalConstantSkew),
            variable_values={"exchange": exchange, "days": days},
        )

    def HistoricalConstantATM(
        self, exchange: types.ExchangeEnumType, days: types.Float
    ) -> Dict:
        """The at-the-money (ATM) volatility chart shows the average ATM volatility for each hour for the given time period. This gives a good idea regarding how volatility has changed throughout time given 1hr granularity.

        Example Response: ``{"date": "1606089600000", "btcAtmShort": 72.94, "btcAtmMed": 73.84, "btcAtmLong": 74.33, "ethAtmShort": 96.77, "ethAtmMed": 94.41, "ethAtmLong": 80.92}``

        Args:
            exchange: (types.ExchangeEnumType)
            days: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalConstantATM),
            variable_values={"exchange": exchange, "days": days},
        )

    def HistoricalConstantWings(
        self, exchange: types.ExchangeEnumType, days: types.Float
    ) -> Dict:
        """This data compares the relative elevation of implied volatility for “wing” options, defined as options with .30 to .20 delta for calls and -.20 to -.30 delta for puts, versus ATM volatility.

        This gives traders insight into the relative cost of lower probability options versus high probability options.

        This measure is linked to the “Kurtosis” of the distribution of returns.

        Args:
            exchange: (types.ExchangeEnumType)
            days: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalConstantWings),
            variable_values={"exchange": exchange, "days": days},
        )

    def DVolIndex(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        interval: types.String,
        dateStart: types.String,
        dateEnd: types.String,
    ) -> Dict:
        """DVolIndex query

        Example Response: ``{"timerange": "1635084000000", "instrument": "BTC", "open": 88.33, "high": 88.6, "low": 88.07, "close": 88.54}``

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            interval: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.DVolIndex),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "interval": interval,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def OrderbookATMDepthPriceandSize(
        self,
        date: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """This endpoint looks only at ATM options.
        It returns the average Bid/Ask size for the top 5 levels of the orderbook.

        The price is calculated as the average price if a trader were to "take" all the size of the top five levels.

        The data returns 24 hours of data for the given date passed.

        Example Response: ``{"date": "1628726400000", "instrumentName": "BTC-12AUG21-46000-C", "baseCurrency": "BTC", "expiration": "1628755200000", "bidSize5LevelsDeep": 124.57, "avgBidPrice5LevelsDeep": 0, "askSize5LevelsDeep": 125.47, "avgAskPrice5LevelsDeep": 0}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OrderbookATMDepthPriceandSize),
            variable_values={"date": date, "symbol": symbol, "exchange": exchange},
        )

    def OpenInterestByStrike(
        self,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Coin OI represents open interest normalized for 1x multiplier.
        Otherwise raw open interest is not consistent between the various exchanges.

        Deribit: BTC 1x, ETH 1x
        Bitcom: BTC 1x, ETH 1x
        Okex: BTC 1/10, ETH 1x
        LedgerX: BTC 1/100, ETH 1/10

        RangeStart and RangeEnd will isolate the desired "DTE" (Days To Expiration).


        Example Response: ``{"strike": 30000, "openInterest": 981.6, "notionalOpenInterest": 55800249, "coinPremium": 1.32, "dollarPremium": 75663.21, "netDeltaExposure": 2.3, "coinOi": null}``

        Args:
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OpenInterestByStrike),
            variable_values={
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def OpenInterestByPutCall(
        self,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Coin OI represents open interest normalized for 1x multiplier.
        Otherwise raw open interest is not consistent between the various exchanges.

        Deribit: BTC 1x, ETH 1x
        Bitcom: BTC 1x, ETH 1x
        Okex: BTC 1/10, ETH 1x
        LedgerX: BTC 1/100, ETH 1/10

        RangeStart and RangeEnd will isolate the desired "DTE" (Days To Expiration).

        Example Response: ``{"putCall": "C", "openInterest": 138186, "notionalOpenInterest": 7850170985, "coinPremium": 8877.73, "dollarPremium": 504368053.53, "netDeltaExposure": 31323.0906, "coinOi": null}``

        Args:
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OpenInterestByPutCall),
            variable_values={
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def OpenInterestByExpiration(
        self,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Coin OI represents open interest normalized for 1x multiplier.
        Otherwise raw open interest is not consistent between the various exchanges.

        Deribit: BTC 1x, ETH 1x
        Bitcom: BTC 1x, ETH 1x
        Okex: BTC 1/10, ETH 1x
        LedgerX: BTC 1/100, ETH 1/10

        RangeStart and RangeEnd will isolate the desired "DTE" (Days To Expiration).

        Example Response: ``{"expiration": "1637740800000", "openInterest": 1401, "notionalOpenInterest": 79624399, "coinPremium": 6.26, "dollarPremium": 360248.45, "netDeltaExposure": -34.6894, "coinOi": null}``

        Args:
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OpenInterestByExpiration),
            variable_values={
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def GlobalOpenInterestByStrikeExpirationPutCall(
        self, symbol: types.SymbolEnumType
    ) -> Dict:
        """All OI is adjusted to reflect a 1 coin multiplier.
        This is the Deribit standard, other exchanges are adjusted to match it.

        Example Response: ``{"strike": "30000", "putCall": "P", "expiration": "1637884800000", "deribitContractOi": 979.3, "deribitNotionalOi": 55654226.166, "bitcomContractOi": 300, "bitcomNotionalOi": 17049186, "okexContractOi": 34.6, "okexNotionalOi": 1966339.452, "ledgerXContractOi": 8, "ledgerXNotionalOi": 454644.96}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.GlobalOpenInterestByStrikeExpirationPutCall),
            variable_values={"symbol": symbol},
        )

    def CurrentOiChangeByStrikeandExpiration(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """Open Interest reflects the number of outstanding contracts in the market. Each contract has a buyer and a seller.

        Usually market makers post bids and asks for contracts in the marketplace, frequently updating their quotes. Once a market participant trades against one of these quotes a contract comes into existence. This increases both the market maker's inventory as well as the market participant’s inventory.

        Note, market makers are not necessarily involved, sometimes two participants will meet in the middle and trade together, increasing open interest.

        Trades can also decrease open interest or leave it unaffected, this depends on how the trade affects overall inventory.

        Example Response: ``{"expiration": "1637654400000", "strike": 54000, "oiChange": 78.4}``

        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentOiChangeByStrikeandExpiration),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def CurrentVolumebyExpiration(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """Contracts traded reflects the current volume seen today, starting at midnight UTC.

        Contracts traded further breaks down the volume by the various strikes and expirations.

        This allows traders to quickly identify which strikes and expirations have been seeing the most activity today.

        Example Response: ``{"date": "1637625600000", "expiration": "1638518400000", "contractsTraded": 748.3, "coin1Volume": null, "premiumTraded": null}``

        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentVolumebyExpiration),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def CurrentVolumebyStrike(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """Contracts traded reflects the current volume seen today, starting at midnight UTC.

        Contracts traded further breaks down the volume by the various strikes and expirations.

        This allows traders to quickly identify which strikes and expirations have been seeing the most activity today.

        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentVolumebyStrike),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def CurrentVolumebyPutCall(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """Contracts traded reflects the current volume seen today, starting at midnight UTC.

        Contracts traded further breaks down the volume by the various strikes and expirations.

        This allows traders to quickly identify which strikes and expirations have been seeing the most activity today.




        Args:
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CurrentVolumebyPutCall),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    def HistoricalPutCallRatio(
        self,
        date1: types.String,
        date2: types.String,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        direction1: types.String,
        direction2: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """The activity reflects the selected days’ traded options (UTC timezone).

        Trading activity is broken up into four types of activity: calls bought, calls sold, puts bought, puts sold.

        Looking at contracts traded versus premium traded will give a better idea of the trading activity.

        For example, 100 cheap out-of-the money options traded versus one deep in-the-money option, will affect these measures quite differently.

        Example Responses: ``{"date": "1585699200000", "callContracts": 0.49, "putContracts": 0.51, "callPremium": 0.38, "putPremium": 0.62, "callsBlockTraded": 0, "putsBlocktraded": 1, "callPremiumBlockTraded": 0, "putPremiumBlockTraded": 1}``

        Args:
            date1: (types.String)
            date2: (types.String)
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            direction1: (types.String)
            direction2: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalPutCallRatio),
            variable_values={
                "date1": date1,
                "date2": date2,
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "direction1": direction1,
                "direction2": direction2,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def HistoricalVolume(
        self,
        date1: types.String,
        date2: types.String,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        direction1: types.String,
        direction2: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Trading activity is broken up into four types of activity: calls bought, calls sold, puts bought, puts sold.


        Example Response: ``{"date": "1609459200000", "contractsTraded": 24890.3, "contractsBlockTraded": 1468, "premiumValue": 21488127.95, "premiumBlockTraded": 2587069.25}``

        Args:
            date1: (types.String)
            date2: (types.String)
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            direction1: (types.String)
            direction2: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalVolume),
            variable_values={
                "date1": date1,
                "date2": date2,
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "direction1": direction1,
                "direction2": direction2,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def HistoricalChangeinOIbyExpiration(
        self,
        dateStart: types.String,
        dateEnd: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Open Interest reflects the number of outstanding contracts in the market. Each contract has a buyer and a seller.

        Usually market makers post bids and asks for contracts in the marketplace, frequently updating their quotes. Once a market participant trades against one of these quotes a contract comes into existence. This increases both the market maker's inventory as well as the market participant’s inventory.

        Note, market makers are not necessarily involved, sometimes two participants will meet in the middle and trade together, increasing open interest.

        Trades can also decrease open interest or leave it unaffected, this depends on how the trade affects overall inventory.

        Example Response: ``{"expiration": "1614326400000", "callOiChange": 11911.9, "putOiChange": 9936.7, "totalOiChange": 21848.6}``

        Args:
            dateStart: (types.String)
            dateEnd: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalChangeinOIbyExpiration),
            variable_values={
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def HistoricalChangeinOIbyStrike(
        self,
        dateStart: types.String,
        dateEnd: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Open Interest reflects the number of outstanding contracts in the market. Each contract has a buyer and a seller.

        Usually market makers post bids and asks for contracts in the marketplace, frequently updating their quotes. Once a market participant trades against one of these quotes a contract comes into existence. This increases both the market maker's inventory as well as the market participant’s inventory.

        Note, market makers are not necessarily involved, sometimes two participants will meet in the middle and trade together, increasing open interest.

        Trades can also decrease open interest or leave it unaffected, this depends on how the trade affects overall inventory.

        Example Response: ``{"strike": 160000, "totalOiChange": 500.3, "callOiChange": 500.3, "putOiChange": 0}``

        Args:
            dateStart: (types.String)
            dateEnd: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalChangeinOIbyStrike),
            variable_values={
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def ParadigmBlockSnifferCallSpreadsasPercentageofTradeCount(
        self,
        dateRangeStart: types.String,
        dateRangeEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """This end-point accepts a date range and BTC/ETH as arguments.

        The results reflect the percentage of call spreads, that have been block-traded and settled on Deribit, as a percentage of trade count (not contract/premium volume).

        Theoretically the RFQ block trade may have been negotiated outside of Paradigm but realistically almost all block trade volume is executed through the Paradigm RFQ system.



        Example Response: ``{"percentageOfTrades": 0.182}``

        Args:
            dateRangeStart: (types.String)
            dateRangeEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ParadigmBlockSnifferCallSpreadsasPercentageofTradeCount),
            variable_values={
                "dateRangeStart": dateRangeStart,
                "dateRangeEnd": dateRangeEnd,
                "symbol": symbol,
            },
        )

    def ParadigmBlockSnifferPutSpreadsasPercentageofTradeCount(
        self,
        dateRangeStart: types.String,
        dateRangeEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """This end-point accepts a date range and BTC/ETH as arguments.

        The results reflect the percentage of put spreads, that have been block-traded and settled on Deribit, as a percentage of trade count (not contract/premium volume).

        Theoretically the RFQ block trade may have been negotiated outside of Paradigm but realistically almost all block trade volume is executed through the Paradigm RFQ system.



        Args:
            dateRangeStart: (types.String)
            dateRangeEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ParadigmBlockSnifferPutSpreadsasPercentageofTradeCount),
            variable_values={
                "dateRangeStart": dateRangeStart,
                "dateRangeEnd": dateRangeEnd,
                "symbol": symbol,
            },
        )

    def ParadigmBlockSnifferSingleLegBlockTrades(
        self, date: types.String, symbol: types.SymbolEnumType
    ) -> Dict:
        """This end-point accepts a date and BTC/ETH as arguments.

        The result returns times and sales data for all block-trades settled on Deribit that have ONLY one leg associated with the block-trade.

        Theoretically the RFQ block trade may have been negotiated outside of Paradigm but realistically almost all block trade volume is executed through the Paradigm RFQ system.



        Example Response: ``{"date": "1612210707571", "indexPrice": 34005.73, "direction": "buy", "amount": 100, "price": 0.049, "instrumentName": "BTC-12FEB21-36000-C", "priceUsd": 1666.28, "sizeUsd": 166628.07, "iv": 104.95, "blockTradeId": "7268", "count": 1}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ParadigmBlockSnifferSingleLegBlockTrades),
            variable_values={"date": date, "symbol": symbol},
        )

    def ParadgimBlockSnifferTradesTiedUpMultiLegTrades(
        self,
        date: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Block Trade Count: represents the number of legs the given trade incorporates.

        Direction: Because block trades are pre-negotiated there is no “aggressor”. Here buy/sell is an accounting feature allowing us to see which side of the trade different legs go on.

        Theoretically the RFQ block trade may have been negotiated outside of Paradigm but realistically almost all block trade volume is executed through the Paradigm RFQ system.

        Example Response: ``{"ts": "1614630215306", "indexPrice": 48721.04, "direction": "buy", "amount": 100, "instrumentName": "BTC-28MAY21-75000-C", "sizeUsd": 401461.36, "priceUsd": "4014.61", "iv": 106.19, "blockTradeId": "8606", "count": 2}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ParadgimBlockSnifferTradesTiedUpMultiLegTrades),
            variable_values={"date": date, "symbol": symbol, "exchange": exchange},
        )

    def ParadgimBlockSnifferDetailedVolumeBreakdown(
        self,
        dateRangeStart: types.String,
        dateRangeEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """This end-point accepts a date range and BTC/ETH as arguments.

        The result returns times and sales data for all block-trades settled on Deribit broken down by category: Puts Vs Calls, Expirations and Strike Prices.

        Theoretically the RFQ block trade may have been negotiated outside of Paradigm but realistically almost all block trade volume is executed through the Paradigm RFQ system.



        Example Response: ``{"expiration": "1614931200000", "strike": 36000, "putCall": "P", "contractVolume": 30, "premiumVolume": 2644.86}``

        Args:
            dateRangeStart: (types.String)
            dateRangeEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ParadgimBlockSnifferDetailedVolumeBreakdown),
            variable_values={
                "dateRangeStart": dateRangeStart,
                "dateRangeEnd": dateRangeEnd,
                "symbol": symbol,
            },
        )

    def TimesandSales(
        self, date: types.String, exchange: types.ExchangeEnumType
    ) -> Dict:
        """This query will return all the options times and sales data for a given exchange on a given day.

        Example Response: ``{"exchange": "deribit", "date": "1631750359238", "instrumentName": "ETH-17SEP21-3900-C", "baseCurrency": "ETH", "expiration": "ETH", "strike": 3900, "putCall": "C", "direction": "buy", "blockTrade": "no", "liquidation": "no", "amount": 7, "price": 0.002, "priceUsd": 7.22, "iv": "89.79"}``

        Args:
            date: (types.String)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.TimesandSales),
            variable_values={"date": date, "exchange": exchange},
        )

    def VolatilityCone(
        self, symbol: types.SymbolEnumType, date1: types.String, date2: types.String
    ) -> Dict:
        """Parkinson Volatility is an efficient estimator of volatility since crypto currencies trade continuously.

        Given selected rolling windows, the volatility cone displays where current volatilities reside compared to a quartile range.

        Example Response ``{"max365": 83.87, "current365": 83.87, "min365": 75.29, "p75365": 82.235, "p50365": 80.655, "p25365": 77.46, "max180": 76.94, "current180": 76.94, "min180": 56.43, "p75180": 74.6025, "p50180": 71.545, "p25180": 63.2025, "max90": 98.66, "current90": 98.66, "min90": 63.29, "p7590": 93.57, "p5090": 88.17, "p2590": 74.91, "max30": 138.14, "current30": 136, "min30": 66.77, "p7530": 129.185, "p5030": 120.44, "p2530": 94.3325, "max14": 156.93, "current14": 122.88, "min14": 72.56, "p7514": 145.4725, "p5014": 124.155, "p2514": 114.65, "max7": 168.9, "current7": 122.68, "min7": 74.08, "p757": 145.5825, "p507": 124.845, "p257": 120.8725, "max0": 267.5, "current0": 81.28, "min0": 36.07, "p750": 161.475, "p500": 107.295, "p250": 78.8975}``

        Args:
            symbol: (types.SymbolEnumType)
            date1: (types.String)
            date2: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.VolatilityCone),
            variable_values={"symbol": symbol, "date1": date1, "date2": date2},
        )

    def RealizedVolvsTradeWeightedIV(
        self,
        date1: types.String,
        date2: types.String,
        timeWindow: types.Float,
        beginDate: types.String,
        endDate: types.String,
        rangeStart: types.Float,
        rangeEnd: types.Float,
        deltaRangeStart: types.Float,
        deltaRangeEnd: types.Float,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Parkinson Volatility is an efficient estimator of volatility since crypto currencies trade continuously.

        Given selected rolling windows, the Parkinson IV reflects a rolling average, which can then be compared to the appropriate expiration cycle.

        Example Response: ``{"date": "1588291200000", "weightedIv": 80.12}``

        Args:
            date1: (types.String)
            date2: (types.String)
            timeWindow: (types.Float)
            beginDate: (types.String)
            endDate: (types.String)
            rangeStart: (types.Float)
            rangeEnd: (types.Float)
            deltaRangeStart: (types.Float)
            deltaRangeEnd: (types.Float)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.RealizedVolvsTradeWeightedIV),
            variable_values={
                "date1": date1,
                "date2": date2,
                "timeWindow": timeWindow,
                "beginDate": beginDate,
                "endDate": endDate,
                "rangeStart": rangeStart,
                "rangeEnd": rangeEnd,
                "deltaRangeStart": deltaRangeStart,
                "deltaRangeEnd": deltaRangeEnd,
                "symbol": symbol,
                "exchange": exchange,
            },
        )

    def RealizedVolDayofWeek(
        self,
        dateStart: types.String,
        dateEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """Parkinson Volatility is an efficient estimator of volatility since crypto currencies trade continuously.

        Intraday Realized Volatility uses hourly data and then annualizes the volatility.

        Hourly volatility averages are calculated horizontally across specific groups, such as hour of the day, or day of the week.

        Example Response: ``{"dowUtc": "Sunday   ", "parkinsonHvPerp": 115.19, "parkinsonHvIndex": 109.85}``

        Args:
            dateStart: (types.String)
            dateEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.RealizedVolDayofWeek),
            variable_values={
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "symbol": symbol,
            },
        )

    def RealizedVolHourofDay(
        self,
        dateStart: types.String,
        dateEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """Parkinson Volatility is an efficient estimator of volatility since crypto currencies trade continuously.

        Intraday Realized Volatility uses hourly data and then annualizes the volatility.

        Hourly volatility averages are calculated horizontally across specific groups, such as hour of the day, or day of the week.

        Example Response: ``{"hourUtc": "0", "parkinsonHvPerp": 209.69, "parkinsonHvIndex": 198.07}``

        Args:
            dateStart: (types.String)
            dateEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.RealizedVolHourofDay),
            variable_values={
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "symbol": symbol,
            },
        )

    def RealizedVolHourofDayandDayofWeek(
        self,
        dateStart: types.String,
        dateEnd: types.String,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """Parkinson Volatility is an efficient estimator of volatility since crypto currencies trade continuously.

        Intraday Realized Volatility uses hourly data and then annualizes the volatility.

        Hourly volatility averages are calculated horizontally across specific groups, such as hour of the day, or day of the week.

        Example Response: ``{"dowVal": 0, "dow": "Sunday   ", "hourUtc": 0, "parkinsonHvPerp": 488.65, "parkinsonHvIndex": 462.03}``

        Args:
            dateStart: (types.String)
            dateEnd: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.RealizedVolHourofDayandDayofWeek),
            variable_values={
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "symbol": symbol,
            },
        )

    def IntradayRealizedVolatility(
        self,
        symbol: types.SymbolEnumType,
        dateStart: types.String,
        dateEnd: types.String,
        range1: types.Float,
        range2: types.Float,
    ) -> Dict:
        """Intraday Realized Volatility uses hourly data and then annualizes the volatility.

        Since we are dealing with hourly data here, 10-day volatility requires a 240 input (24hrs * 10 days)

        Analyze perpetual swap price data and index price data in order to calculate realized vol.

        Example Response: ``{"ts": "1588291200000", "parkinsonHvPerp": 74.69, "parkisonHvIndex": 71.05}``

        Args:
            symbol: (types.SymbolEnumType)
            dateStart: (types.String)
            dateEnd: (types.String)
            range1: (types.Float)
            range2: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.IntradayRealizedVolatility),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "range1": range1,
                "range2": range2,
            },
        )

    def ClosetoCloseHistoricalVol(
        self, symbol: types.String, dateStart: types.String, dateEnd: types.String
    ) -> Dict:
        """Returns a list of all active options.
        These are the latest option bids/asks and associated implied volatilities.
        Mark prices and mark volatilities are provided from the exchanges.
        If no "mark" is provided midpoints are calculated from the best bid and best ask prices.

        Example Response: ``{"date": "1609804800000", "currency": "BNB", "close": 41.9, "yesterdayClose": 41.1, "vol": 12.27}``

        Args:
            symbol: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ClosetoCloseHistoricalVol),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def RealizedVolParkinson(
        self,
        symbol: types.String,
        dateStart: types.String,
        dateEnd: types.String,
        parkinsonRange: types.Float,
    ) -> Dict:
        """Returns a list of all active options.
        These are the latest option bids/asks and associated implied volatilities.
        Mark prices and mark volatilities are provided from the exchanges.
        If no "mark" is provided midpoints are calculated from the best bid and best ask prices.

        Example Response: ``{"date": "1609718400000", "parkinsonHV": 135.43}``

        Args:
            symbol: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)
            parkinsonRange: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.RealizedVolParkinson),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "parkinsonRange": parkinsonRange,
            },
        )

    def OHLC(
        self, symbol: types.String, dateStart: types.String, dateEnd: types.String
    ) -> Dict:
        """Returns a list of all active options.
        These are the latest option bids/asks and associated implied volatilities.
        Mark prices and mark volatilities are provided from the exchanges.
        If no "mark" is provided midpoints are calculated from the best bid and best ask prices.

        Example Response: ``{"date": "1609718400000", "currency": "BNB", "open": 41.36, "high": 44.01, "low": 39.11, "close": 41.1}``

        Args:
            symbol: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OHLC),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def CoveredCall(self, symbol: types.SymbolEnumType) -> Dict:
        """DESCRIPTION:
        The “Covered Call” is constructed by holding a long position in the underlying asset.
        There is a 1-to-1 relationship between holding the long asset and the short call options.
        This strategy is relatively low risk because a 100% collateralization ratio is maintained.

        CALCULATION:
        The “Covered Call” data assume the trader is long exactly 1 unit of underlying asset AFTER proceeds from selling their call.

        EXAMPLE
        Underlying price = $500,
        Trader position in underlying BEFORE selling the call = $475
        Short $700 call proceeds = $25
        Trader positioning in underlying AFTER short call proceeds = $500 (AKA 1 whole unit)

        RETURN CALCULATIONS
        Absolute Yield: $25/$475
        Annualized Yield: $25/$475 * (525,600 / minutes left until expiration)
        Absolute Called Out Yield: ($700/$475) – 1
        Annualized Called Out Yield:
        [($700/$475) – 1] * (525,600 / minutes left until expiration)

        Example Response: ``{"date": "1637682176595", "instrumentName": "BTC-24NOV21-58000-C", "expiration": "1637740800000", "strike": 58000, "putCall": "C", "bidUsd": 314.86, "markUsd": 348.89, "askUsd": 372.1, "calledOutAnnualized": 707.196343384488, "calledOutAbsolute": 1.31455636888631, "absoluteBidYieldNet": 0.55, "absoluteMarkYieldNet": 0.61, "absoluteAskYieldNet": 0.65, "annualBidYieldNet": 297.52, "annualAskYieldNet": 351.97, "annualMarkYieldNet": 329.87, "absoluteMarkYieldCalledOut": 1.93, "absoluteAskYieldCalledOut": 1.97, "absoluteBidYieldCalledOut": 1.87, "annualizedBidYieldCalledOut": 1008.62, "annualizedMarkYieldCalledOut": 1041.41, "annualizedAskYieldCalledOut": 1063.79}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CoveredCall), variable_values={"symbol": symbol}
        )

    def CashSecuredPuts(self, symbol: types.SymbolEnumType) -> Dict:
        """DESCRIPTION:
        The “Cash Secured Put” is a low-risk strategy with a similar payout profile to the “Covered Call”.
        Traders will sell a naked put but maintain enough cash to purchase the underlying asset at the predetermined strike price.
        This strategy is relatively low risk because a 100% collateralization ratio is maintained.
        Note: it’s important that the trader hold cash/stable coin, if the strike price is denominated in fiat.

        CALCULATION:
        The “Cash Secured Put” yield data assume the trader maintains enough cash on hand AFTER proceeds from selling the put.

        EXAMPLE
        Trader’s cash position BEFORE selling put = $275
        Short $300 Put Proceeds = $25
        Trader cash balance AFTER short put proceeds = $300
        (AKA 100% collateralization ratio)

        RETURN CALCULATIONS
        Absolute Yield: $25/$275
        Annualized Yield: $25/$275 * (525,600 / minutes left until expiration)

        Example Response: ``{"date": "1637682194758", "instrumentName": "BTC-24NOV21-57000-P", "expiration": "1637740800000", "strike": 57000, "putCall": "P", "bidUsd": 543.77, "markUsd": 599.13, "askUsd": 629.63, "absoluteBidYieldNet": 0.96, "absoluteMarkYieldNet": 1.06, "absoluteAskYieldNet": 1.11, "bidYieldNetAnnual": 518.69, "markYieldNetAnnual": 572.06, "askYieldNetAnnual": 601.5}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CashSecuredPuts), variable_values={"symbol": symbol}
        )

    def StraddleRun(self, symbol: types.SymbolEnumType) -> Dict:
        """DESCRIPTION:
        Straddles are a classic volatility trade.
        Buyers of the straddle hope that the underlying moves enough to either exceed the straddle price by expiration or that the underlying moves enough to profitably “gamma scalp” the underlying.
        Gamma scalps are the proceeds from delta rebalancing activity that volatility buyers benefit from.
        The opposite is true for straddle sellers, straddle sellers hope that the underlying remains relatively stable and therefor they enjoy theta decay from the short straddle position in excess of gamma scalping outflows.

        CALCULATION:
        The straddles are constructed by first identifying the forward/underlying price, not the spot price.
        This is because for hedging purposes the underlying/forward is the appropriate instrument to use.
        The straddle is then constructed by choosing the strike price closest to the current fwd/underlying price.
        Both the call and put will have identical strike prices.
        Vega and Theta numbers are calculated using the Black-Scholes model with the mid/mark price and forward price as the input parameters.

        % OF SPOT CALCULATION
        $ Value of Straddle / Current $ Spot
        Despite the straddle being constructed using underlying/forward prices, the % of spot chart compares the straddle cost to the value of the current spot price.

        This method captures total premium to spot. Both the premium from the straddle and the premium implied by the forward/underlying prices.

        At expiration everything resolves to spot.

        Example Response: ``{"expiration": "1637740800000", "strike": 57000, "bidUsd": 1373, "markUsd": 1433, "askUsd": 1517, "bidSpotPercentage": 2.4, "markSpotPercentage": 2.5, "askSpotPercentage": 2.6, "theta": -701.71, "vega": 19.4, "underlyingPrice": 57249}``

        Args:
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.StraddleRun), variable_values={"symbol": symbol}
        )

    def GlobalAllOrderBooksOptionPricing(self) -> Dict:
        """Returns a list of all active option instruments for every exchange.

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.GlobalAllOrderBooksOptionPricing), variable_values={}
        )

    def VolatilitySurfaceDelta(
        self, symbol: types.BTCOrETHEnumType, date: types.String
    ) -> Dict:
        """This query returns the "delta volatility surface" along with spot prices in 1 minute increments.

        This data reflects option quotes throughout the day found on Deribit.

        The dataset starts on March 1st, 2020 with 1hr granularity.
        Starting April 22nd, 2021, granularity is 1-minute.

        Users can use this high granularity endpoint to measure changes in the volatility surface with respect to changes in the underlying spot prices.

        Example Response: ``{"date": "1630454400000", "timeLeft": "08:00:00", "currency": "ETH", "expiration": "1630483200000", "underlyingPrice": 3431.38, "spot": 3431.24, "putD05": 104.11, "putD15": 100.33, "putD25": 94.6, "putD35": 90.61, "callD05": 86.85, "callD15": 85.78, "callD25": 84.85, "callD35": 83.97, "atmMarkIV": 86.75, "atmMidIV": 89.23, "atmBidIV": 84.86, "atmAskIV": 93.6}``

        Args:
            symbol: (types.BTCOrETHEnumType)
            date: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.VolatilitySurfaceDelta),
            variable_values={"symbol": symbol, "date": date},
        )

    def ShadowTermStructureand25Skew(
        self, date: types.String, symbol: types.SymbolEnumType
    ) -> Dict:
        """Allows users to look at the Term Structure and 25∆ Skew for like expirations.

        There is 1hour intraday granularity.

        Data based on Deribit.

        Data available through early 2020.

        Example Response: ``{"dateAndHour": "1632182400000", "daysUntilExpiration": 0, "atmIv": 108.46, "twentyThirtyCallIvMinusPutIv": -18.32}``

        Args:
            date: (types.String)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ShadowTermStructureand25Skew),
            variable_values={"date": date, "symbol": symbol},
        )

    def HourlyInstrumentImpliedVolandOI(
        self,
        symbol: types.BTCOrETHEnumType,
        dateStart: types.String,
        dateEnd: types.String,
        strike: types.String,
        putCall: types.PutCallEnumType,
        expiration: types.String,
    ) -> Dict:
        """This query returns the open interest, bid iv, mark iv and ask iv for a specific instrument input.

        This data reflects option quotes found on Deribit for the given date range of interest.

        Mark IV is provided by the exchange.

        Example Response: ``{"date": "1630972800000", "instrumentName": "BTC-31DEC21-100000-C", "oi": 3354.3, "bidIV": 95.64, "markIV": 96.39, "askIV": 97.22}``

        Args:
            symbol: (types.BTCOrETHEnumType)
            dateStart: (types.String)
            dateEnd: (types.String)
            strike: (types.String)
            putCall: (types.PutCallEnumType)
            expiration: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HourlyInstrumentImpliedVolandOI),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "strike": strike,
                "putCall": putCall,
                "expiration": expiration,
            },
        )

    def SpotPrices(
        self, symbol: types.String, dateStart: types.String, dateEnd: types.String
    ) -> Dict:
        """This query returns spot price daily open, high, low, close

        Args:
            symbol: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.SpotPrices),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def ConstantMaturitySkew1minutegranularity(
        self,
        symbol: types.BTCOrETHEnumType,
        dateStart: types.String,
        dateEnd: types.String,
        interval: types.String,
    ) -> Dict:
        """This query will return the option skews (∆35, ∆25, ∆15, ∆5) for constant maturities (7-day, 30-day, 60-day, 90-day, 180-day).

        Users can pass the desired coin, time interval and date of interest.

        Skews represent the asymmetry of options pricing.
        The skew is calculated by taking the implied volatility of the CALL and subtracting the implied volatility of the PUT.

        Negative skew implies PUTs are more expensive, while positive skew implies CALLs are more expensive.

        Exchange: Deribit

        Example Response: ``{"date": "1633219200000", "thirtyFiveDelta7DayExp": -2.16, "twentyFiveDelta7DayExp": -4.14, "fifteenDelta7DayExp": -6.91, "fiveDelta7DayExp": -15.62, "thirtyFiveDelta30DayExp": -0.31, "twentyFiveDelta30DayExp": -1.29, "fifteenDelta30DayExp": -2.28, "fiveDelta30DayExp": -6.53, "thirtyFiveDelta60DayExp": 1.24, "twentyFiveDelta60DayExp": 2.39, "fifteenDelta60DayExp": 3.63, "fiveDelta60DayExp": 8.26, "thirtyFiveDelta90DayExp": 2.46, "twentyFiveDelta90DayExp": 4.66, "fifteenDelta90DayExp": 8.16, "fiveDelta90DayExp": 16.06, "thirtyFiveDelta180DayExp": 4.26, "twentyFiveDelta180DayExp": 7.35, "fifteenDelta180DayExp": 10.27, "fiveDelta180DayExp": 15.27}``

        Args:
            symbol: (types.BTCOrETHEnumType)
            dateStart: (types.String)
            dateEnd: (types.String)
            interval: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ConstantMaturitySkew1minutegranularity),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "interval": interval,
            },
        )

    def ConstantMaturityATM1minutegranularity(
        self,
        symbol: types.BTCOrETHEnumType,
        dateStart: types.String,
        dateEnd: types.String,
        interval: types.String,
    ) -> Dict:
        """This query will return the option at-the-money implied volatility for constant maturities (7-day, 30-day, 60-day, 90-day, 180-day).

        Users can pass the desired coin, time interval and date of interest.


        Exchange: Deribit

        Example Response: ``{"date": "1633219200000", "atm7": null, "atm30": 77.5, "atm60": 83.63, "atm90": 86.41, "atm180": 87.79}``

        Args:
            symbol: (types.BTCOrETHEnumType)
            dateStart: (types.String)
            dateEnd: (types.String)
            interval: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.ConstantMaturityATM1minutegranularity),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "interval": interval,
            },
        )

    def CustomMaturityDeltaSurface(
        self, symbol: types.BTCOrETHEnumType, date: types.String, days: types.Float
    ) -> Dict:
        """This endpoint returns hourly intervals for desired "Constant Maturity Input".

        Users can input desired maturity for both BTC or ETH.

        Available data starts on 3/01/2020.
        Args:
            symbol: (types.BTCOrETHEnumType)
            date: (types.String)
            days: (types.Float)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.CustomMaturityDeltaSurface),
            variable_values={"symbol": symbol, "date": date, "days": days},
        )

    def Orderbook30dayHourlyBasis(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        expiration: types.String,
    ) -> Dict:
        """Orderbook30dayHourlyBasis query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            expiration: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.Orderbook30dayHourlyBasis),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "expiration": expiration,
            },
        )

    def OrderbookBasisVolumeandOpenInterest(
        self, exchange: types.ExchangeEnumType, symbol: types.SymbolEnumType
    ) -> Dict:
        """OrderbookBasisVolumeandOpenInterest query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OrderbookBasisVolumeandOpenInterest),
            variable_values={"exchange": exchange, "symbol": symbol},
        )

    def OrderbookPast1HrBasisandSpot(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        expiration: types.String,
    ) -> Dict:
        """OrderbookPast1HrBasisandSpot query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            expiration: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.OrderbookPast1HrBasisandSpot),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "expiration": expiration,
            },
        )

    def Orderbook30DayTradeWeightedBasis(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        excludeExpiration: types.Boolean,
    ) -> Dict:
        """Orderbook30DayTradeWeightedBasis query


        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            excludeExpiration: (types.Boolean)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.Orderbook30DayTradeWeightedBasis),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "excludeExpiration": excludeExpiration,
            },
        )

    def HistoricalIntradayTradedWeightedBasis(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        expiration: types.String,
        dateStart: types.String,
        dateEnd: types.String,
    ) -> Dict:
        """HistoricalIntradayTradedWeightedBasis query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            expiration: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HistoricalIntradayTradedWeightedBasis),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "expiration": expiration,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def Basis24HR(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        expiration: types.String,
        dateStart: types.String,
        dateEnd: types.String,
    ) -> Dict:
        """Basis24HR query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            expiration: (types.String)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.Basis24HR),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "expiration": expiration,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def HifiStrikesVolSurface(
        self,
        symbol: types.SymbolEnumType,
        date: types.String,
        interval: types.String,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Returns OTM volatility surface based on strikes and actual expirations.

        Currently supports: Deribit

        Args:
            symbol: (types.SymbolEnumType)
            date: (types.String)
            interval: (types.String)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HifiStrikesVolSurface),
            variable_values={
                "symbol": symbol,
                "date": date,
                "interval": interval,
                "exchange": exchange,
            },
        )

    def dVolVariancePremium(
        self,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
        Args:
            symbol: (types.SymbolEnumType)
        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.dvolVariancePremium),
            variable_values={
                "symbol": symbol,
            },
        )

    def UtilityRealtimeOptionbook(
        self,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """
        This endpoint will return the option orderbook, index prices, underlying prices and open interest for the entire exchange.
        All crypto options, regardless of underlying coin, are returned.
        This endpoint is real-time and will return live prices when requested.
        Supported exchanges are |Deribit|Bitcom|Okex|Delta|

        Args:
             exchange: (types.ExchangeEnumType)
        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.UtilityRealtimeOptionbook),
            variable_values={
                "exchange": exchange,
            },
        )

    def HifiVolSurfaceStrikesGreeksMinute(
        self,
        exchange: types.ExchangeEnumType,
        dateTime: types.String,
        symbol: types.SymbolEnumType
    ) -> Dict:
        """
      Explanation:
        This endpoint returns a volatility surface represented by option strike prices.
        This is a "model-free" volatility surface, meaning no interpolation or fitting of any kind is present.
        Mark IV is determined by Deribit's internal risk-engine, which is proprietary formulation that is built upon a smoothing process. Deribit's internal fitting.
        Option greeks and implied volatility are based on the future (forward) price, also known as the underlying and Deribit "marks".
        For options with no tradable underlying (AKA tradable future) a synthetic is interpolated from two nearest active futures.
        Bid IV and Ask IV are directly observable implied volatilities calculated from the best bid and best offer, this is raw, "model-free" data.
        The index price represents the spot price. This is the current "cash market" price for the respective crypto.
        Comparing the underlying price and spot price will determine the basis.
        Endpoint Details:
        Time period start: June 2021
        Total date per pull: 1-hour worth of data points (It's recommended that users build looping functions to retrieve the entire dataset)
        Supported date intervals: 1-minute, 5-minute, 15-minute, etc.
        Supported Exchange: Deribit
        New data appendage rate: 1-min (new data is added every 1-min)
        Args:
             exchange: (types.ExchangeEnumType), 
             symbol: (types.SymbolEnumType),
             date: (types.String)
        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HifiVolSurfaceStrikesGreeksMinute),
            variable_values={
                "exchange": exchange,
                "dateTime": dateTime,
                "symbol": symbol
            },
        )

    def HifiVolSurfaceStrikesGreeksHourly(
        self,
        exchange: types.ExchangeEnumType,
        dateTime: types.String,
        symbol: types.SymbolEnumType,
        interval: types.String
    ) -> Dict:
        """
      Explanation:
        This endpoint returns a volatility surface represented by option strike prices.
        This is a "model-free" volatility surface, meaning no interpolation or fitting of any kind is present.
        Mark IV is determined by Deribit's internal risk-engine, which is proprietary formulation that is built upon a smoothing process. Deribit's internal fitting.
        Option greeks and implied volatility are based on the future (forward) price, also known as the underlying and Deribit "marks".
        For options with no tradable underlying (AKA tradable future) a synthetic is interpolated from two nearest active futures.
        Bid IV and Ask IV are directly observable implied volatilities calculated from the best bid and best offer, this is raw, "model-free" data.
        The index price represents the spot price. This is the current "cash market" price for the respective crypto.
        Comparing the underlying price and spot price will determine the basis.
        Endpoint Details:
        Time period start: April 2019
        Total date per pull: 1-day worth of data points (It's recommended that users build looping functions to retrieve the entire dataset)
        Supported date intervals: 1-hour, 2-hour, etc. up to 'daily'
        Supported Exchange: Deribit
        New data appendage rate: 1-min (new data is added every 1-min)
        Args:
             exchange: (types.ExchangeEnumType), 
             symbol: (types.SymbolEnumType),
             date: (types.String)
        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.HifiVolSurfaceStrikesGreeksHourly),
            variable_values={
                "exchange": exchange,
                "dateTime": dateTime,
                "symbol": symbol,
                "interval": interval
            },
        )
