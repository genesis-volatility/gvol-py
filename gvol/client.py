from typing import Dict

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from gvol import queries, types


class GVol:
    """GVol API client.

    Contact info@genesisvolatility.io for API key information.
    """

    _url = "https://app.pinkswantrading.com/graphql"

    def __init__(self, header: str, gvol_api_key: str) -> None:
        """Initializes GVol API client.

        Args:
            gvol_api_key (str): API key
        """
        headers = {
            f"{header}": f"{gvol_api_key}",
            "Content-Type": "application/json",
            "accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
        }

        transport = RequestsHTTPTransport(url=self._url, headers=headers)
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def options_orderbook(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """
        Returns the current orderbook of options

        Args:
            symbol: BTC / ETH / SOL (deribit) / BCH (bitcom)
            exchange: deribit / bitcom / okex / ledgerx

        Returns:
            {
            "ts": "1637677441586",
            "instrumentName": "BTC-24NOV21-59000-C",
            "strike": 59000,
            "expiration": "1637712000000",
            "bidIv": 59.4,
            "markIv": 66.33,
            "askIv": 71.68,
            "delta": 0.10811
            }

        """
        return self._client.execute(
            gql(queries.options_orderbook),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    
    def options_termstructure(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """The volatility term structure represents the implied volatility given different expiration dates.

        Args:
            symbol: BTC / ETH / SOL (deribit) / BCH (bitcom)
            exchange: deribit / bitcom / okex / ledgerx

        Returns:
            {
            "expiration": "1656489600000",
            "markIv": 61.91,
            "forwardVolatility": 61.91
            }
        """
        return self._client.execute(
            gql(queries.options_termstructure),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

   
    def options_termstructure_hist(
        self,
        dateTime: types.String,
        symbol: types.SymbolEnumType,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """Using our shadow features allows traders to compare current skew and term structure quotes to past market quotes.

        This is different from historical trade data. Quotes represent a complete picture of potential trades, as opposed to actual trades, and therefore are more indicative of where the market was priced at a given point in time.

        Args:
            {
            "symbol": "BTC",
            "exchange": "deribit",
            "dateTime": "2021-01-01 12:00:00"
            }

        Returns:
            {
            "sequenceDays2Exp": 0,
            "tsHourShadow": "1609502400000",
            "tsHourCurrent": null,
            "daysUntilExpiration": "0",
            "markIvCurrent": 61.9,
            "markIvShadow": 66.9
            }
        """
        return self._client.execute(
            gql(queries.options_termstructure_hist),
            variable_values={
                "dateTime": dateTime,
                "symbol": symbol,
                "exchange": exchange,
            },
        )
   
    def options_dvol_index(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        interval: types.String,
        dateStart: types.String,
        dateEnd: types.String,
    ) -> Dict:
        """
        The DVol index is a VIX like volatility index built and maintained by Deribit.com
        The 30-day volatility index supports both BTC and ETH.

        The methodology for the index can be found here: https://insights.deribit.com/exchange-updates/dvol-deribit-implied-volatility-index/

        An instructional video explaining DVol in further detail can also be found here:
        https://insights.deribit.com/exchange-updates/dvol-deribit-volatility-index-vix-index-for-comparison/

        Args:
            {
            "exchange": "deribit", 
            "symbol":  "BTC", 
            "interval": "1 minute",
            "dateStart": "2022-04-11", 
            "dateEnd": "2022-04-12"
            }

        Returns:
            {
            "timerange": "1649635200000",
            "instrument": "BTC",
            "open": 61.08,
            "high": 61.11,
            "low": 61.08,
            "close": 61.11
            }
        """
        return self._client.execute(
            gql(queries.options_dvol_index),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "interval": interval,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def options_trades(
        self, date: types.String, exchange: types.ExchangeEnumType
    ) -> Dict:
        """This query will return all the options times and sales data for a given exchange on a given day.

        Args:
            {
            "exchange": "deribit",
            "date": "2022-03-03"
            }

        Returns:
            {
            "exchange": "deribit",
            "date": "1646351966998",
            "instrumentName": "BTC-11MAR22-40000-P",
            "baseCurrency": "BTC",
            "expiration": "BTC",
            "strike": 40000,
            "putCall": "P",
            "direction": "buy",
            "blockTrade": "no",
            "liquidation": "no",
            "amount": 25,
            "price": 0.0165,
            "priceUsd": 700.65,
            "indexPrice": 42464.16,
            "iv": "70.52"
            }
        """
        return self._client.execute(
            gql(queries.options_trades),
            variable_values={"date": date, "exchange": exchange},
        )

    def options_trades_orderbook_details(
        self, exchange: types.ExchangeEnumType, symbol: types.SymbolEnumType, dateStart: types.String, dateEnd: types.String 
    ) -> Dict:
        """This query will return the trades with useful information about the orderbook at the time of the trade.

        Args:
            {
            "exchange": "deribit",
            "symbol": "BTC", 
            "dateStart": "2022-05-17", 
            "dateEnd": "2022-05-18"
            }
            
        Returns:
            {
            "preTxObTs": "1652831827818",
            "txTs": "1652831832293",
            "postTxObTs": "1652831832485",
            "tradeSeq": 210,
            "tradeId": "214787006",
            "instrumentName": "BTC-3JUN22-45000-C",
            "currency": "BTC",
            "expiration": "1654243200000",
            "strike": 45000,
            "putcall": "C",
            "blockTradeId": null,
            "liquidation": null,
            "direction": "sell",
            "tickDirection": "ZeroMinus",
            "txAmount": 16.8,
            "txIv": 83.29,
            "price": 0.001,
            "priceUsd": 30.41,
            "indexPrice": 30417.44,
            "underlyingPrice": 30459.1475,
            "volume24h": 27.1,
            "high24h": 0.002,
            "low24h": 0.0015,
            "preTxBbSize": 86.5,
            "preTxBbPrice": 0.001,
            "preTxBbIv": 83.34,
            "preTxMidIv": 85.81,
            "preTxMidPrice": 0.00125,
            "preTxMarkIv": 85.71,
            "preTxMarkPrice": 0.0012,
            "preTxBaIv": 88.29,
            "preTxBaPrice": 0.0015,
            "preTxBaSize": 8.6,
            "postTxBbSize": 44.3,
            "postTxBbPrice": 0.001,
            "postTxBbIv": 83.29,
            "postTxMidIv": 85.76,
            "postTxMidPrice": 0.00125,
            "postTxMarkIv": 85.72,
            "postTxMarkPrice": 0.0012,
            "postTxBaIv": 88.23,
            "postTxBaPrice": 0.0015,
            "postTxBaSize": 8.6,
            "delta": 0.019,
            "gamma": 0.00001,
            "theta": -8,
            "vega": 3,
            "rho": 0.2,
            "preTxOi": 86.3,
            "postTxOi": 84.1,
            "oiChange": -2.2
            }
        """
        return self._client.execute(
            gql(queries.options_trades_orderbook_details),
            variable_values={"exchange": exchange, "symbol":symbol, "dateStart":dateStart, "dateEnd":dateEnd},
        )


    def options_volatility_surface(
        self, symbol: types.BTCOrETHEnumType, date: types.String
    ) -> Dict:
        """This query returns the "delta volatility surface" along with spot prices in 1 minute increments.

        This data reflects option quotes throughout the day found on Deribit.

        The dataset starts on March 1st, 2020 with 1hr granularity.
        Starting April 22nd, 2021, granularity is 1-minute.

        Users can use this high granularity endpoint to measure changes in the volatility surface with respect to changes in the underlying spot prices.

        Args:
            {
            "symbol": "ETH",
            "date": "2021-09-01"
            }

        Returns:
            {
            "date": "1630454400000",
            "timeLeft": "08:00:00",
            "currency": "ETH",
            "expiration": "1630483200000",
            "underlyingPrice": 3431.21,
            "spot": 3430.78,
            "putD05": 104.11,
            "putD15": 100.33,
            "putD25": 94.6,
            "putD35": 90.61,
            "callD05": 86.85,
            "callD15": 85.78,
            "callD25": 84.85,
            "callD35": 83.97,
            "atmMarkIV": 85.9,
            "atmMidIV": 89.07,
            "atmBidIV": 85.26,
            "atmAskIV": 92.88
            }
        """
        return self._client.execute(
            gql(queries.options_volatility_surface),
            variable_values={"symbol": symbol, "date": date},
        )

    
    def spot_prices(
        self, symbol: types.String, dateStart: types.String, dateEnd: types.String
    ) -> Dict:
        """This query returns spot price daily open, high, low, close (for all symbols)

        Args:
            {
            "symbol": "ZRX", 
            "dateStart": "2021-01-01",
            "dateEnd": "2021-04-05"
            }

        Returns:
            {
            "date": "1609545600000",
            "currency": "ZRX",
            "open": 0.3758,
            "high": 0.3986,
            "low": 0.3582,
            "close": 0.3607
            }
        """
        return self._client.execute(
            gql(queries.spot_prices),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )

    def options_skew_constant(
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

        Args:
            {
            "symbol": "BTC", 
            "dateStart": "2021-10-01", 
            "dateEnd": "2021-10-03",
            "interval": "1 minute"
            }

        Returns:
            {
            "date": "1633219200000",
            "thirtyFiveDelta7DayExp": -2.16,
            "twentyFiveDelta7DayExp": -4.14,
            "fifteenDelta7DayExp": -6.91,
            "fiveDelta7DayExp": -15.62,
            "thirtyFiveDelta30DayExp": -0.31,
            "twentyFiveDelta30DayExp": -1.29,
            "fifteenDelta30DayExp": -2.28,
            "fiveDelta30DayExp": -6.53,
            "thirtyFiveDelta60DayExp": 1.24,
            "twentyFiveDelta60DayExp": 2.39,
            "fifteenDelta60DayExp": 3.63,
            "fiveDelta60DayExp": 8.26,
            "thirtyFiveDelta90DayExp": 2.46,
            "twentyFiveDelta90DayExp": 4.66,
            "fifteenDelta90DayExp": 8.16,
            "fiveDelta90DayExp": 16.06,
            "thirtyFiveDelta180DayExp": 4.26,
            "twentyFiveDelta180DayExp": 7.35,
            "fifteenDelta180DayExp": 10.27,
            "fiveDelta180DayExp": 15.27
            }
        """
        return self._client.execute(
            gql(queries.options_skew_constant),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "interval": interval,
            },
        )

    def options_atm_constant(
        self,
        symbol: types.BTCOrETHEnumType,
        dateStart: types.String,
        dateEnd: types.String,
        interval: types.String,
    ) -> Dict:
        """This query will return the option at-the-money implied volatility for constant maturities (7-day, 30-day, 60-day, 90-day, 180-day).
        Users can pass the desired coin, time interval and date of interest.

        Exchange: Deribit

        Args:
            {
            "symbol": "BTC", 
            "dateStart": "2021-10-01", 
            "dateEnd": "2021-10-03",
            "interval": "1 day"
            }

        Returns:
            {
            "date": "1633219200000",
            "atm7": 68.4,
            "atm30": 77.41,
            "atm60": 83.55,
            "atm90": 86.41,
            "atm180": 87.62
            }
        """
        return self._client.execute(
            gql(queries.options_atm_constant),
            variable_values={
                "symbol": symbol,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "interval": interval,
            },
        )

    def futures_basis_hist(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
        expiration: types.String,
        dateStart: types.String,
        dateEnd: types.String,
    ) -> Dict:
        """Historical intraday traded weighted basis

        Args:
            {
            "exchange": "deribit",
            "symbol": "BTC",
            "expiration": "2022-12-30 08:00:00",
            "dateStart": "2022-06-15",
            "dateEnd": "2022-06-16"
            }
        Returns:
            {
            "date": "1655251200000",
            "expiration": "1672387200000",
            "amount": 215260,
            "basis": 1.77,
            "open": 22296.5,
            "high": 22296.5,
            "low": 21936.5,
            "close": 21958.5
            }
        """
        return self._client.execute(
            gql(queries.futures_basis_hist),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
                "expiration": expiration,
                "dateStart": dateStart,
                "dateEnd": dateEnd,
            },
        )


    def options_orderbook_details(
        self,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """
        This endpoint will return the option orderbook, index prices, underlying prices and open interest for the entire exchange.
        All crypto options, regardless of underlying coin, are returned.
        This endpoint is real-time and will return live prices when requested.
        Supported exchanges are |Deribit|Bitcom|Okex|Delta|

        Args:
            {
            "exchange": "deribit"
            }
        Returns:
            {
            "date": "1656410576378",
            "instrumentName": "BTC-29JUN22-25000-C",
            "currency": "BTC",
            "expiration": "1656489600000",
            "strike": 25000,
            "putCall": "C",
            "isAtm": false,
            "oi": 10,
            "bestBidPrice": 0,
            "bestAskPrice": 0.0005,
            "usdBid": 0,
            "bidIV": 0,
            "markIv": 103.1,
            "askIv": 160.87,
            "indexPrice": 21033.14,
            "underlyingPrice": 21033.0751
            }
        """
        return self._client.execute(
            gql(queries.options_orderbook_details),
            variable_values={
                "exchange": exchange,
            },
        )

    def portfolio_analyzer(
        self,
        portfolio: types.String,
        deltaFutures: types.Float = 0,
        ivShift: types.Float = 0,
        symbol: types.BTCOrETHEnumType = 'BTC'
    ) -> Dict:
        """
        This endpoint will create a scenario simulation (underlying/iv/dte) of current portfolio book (DERIBIT)
        or a simulated new one
        Args:
            {
            "portfolio": [{ "instrument": "BTC-30DEC22-40000-C", "size": 10 },{ "instrument": "BTC-30DEC22-50000-C", "size": -15 }],
            "deltaFutures":0, 
            "ivShift":0, 
            "symbol":"BTC"
            }
        Returns:
            {
            "indexChange": 0.5,
            "PnL": -0.0531857386,
            "PnLUSD": -559.4770054957,
            "deltaBSM": 0.1176642065,
            "deltaCash": 0.0912782592,
            "deltaSkew": 0.1238167367,
            "gamma": 0.0000312283,
            "vega": 15.2639768164,
            "wVega": 6.1493598491,
            "theta": -3.5517627101,
            "index": 10519.3,
            "equity": -0.0531857386,
            "equityUSD": -559.4767395671,
            "days": 0
            }
        """
        return self._client.execute(
            gql(queries.portfolio_analyzer),
            variable_values={
                "portfolio": portfolio,
                "deltaFutures": deltaFutures,
                "ivShift": ivShift,
                "symbol": symbol
            },
        )

    def options_greeks_minute(
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
            {
            "symbol": "BTC", 
            "dateTime": "2021-01-01 01:00:00", 
            "exchange": "deribit"
            }
        Returns:
            {
            "date": "1609462800000",
            "currency": "BTC",
            "expiration": "1609488000000",
            "strike": 36000,
            "putCall": "C",
            "spot": 29060.9,
            "underlyingPrice": 29064.57,
            "openInterest": 1941.2,
            "bidIv": 0,
            "markIv": 93.05,
            "askIv": 341.5,
            "bestBidAmount": null,
            "bestBidPrice": 0,
            "markPrice": 0,
            "bestAskPrice": 0.0005,
            "bestAskAmount": null,
            "delta": 0,
            "gamma": 0,
            "theta": 0,
            "vega": 0,
            "rho": 0
            }
        """
        return self._client.execute(
            gql(queries.options_greeks_minute),
            variable_values={
                "exchange": exchange,
                "dateTime": dateTime,
                "symbol": symbol
            },
        )

    def options_greeks_hour(
        self,
        exchange: types.ExchangeEnumType,
        date: types.String,
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
            {
            "symbol": "BTC", 
            "date": "2021-01-01", 
            "interval": "1 hour",
            "exchange": "deribit"
            }
        Returns:
            {
            "date": "1609459200000",
            "currency": "BTC",
            "expiration": "1609488000000",
            "strike": 36000,
            "putCall": "C",
            "spot": 28978.23,
            "underlyingPrice": 28980.11,
            "openInterest": 1941.2,
            "bidIv": 0,
            "markIv": 97.48,
            "askIv": 357.49,
            "bestBidAmount": null,
            "bestBidPrice": 0,
            "markPrice": 0,
            "bestAskPrice": 0.001,
            "bestAskAmount": null,
            "delta": 0,
            "gamma": 0,
            "theta": 0,
            "vega": 0,
            "rho": 0
            }
        """
        return self._client.execute(
            gql(queries.options_greeks_hour),
            variable_values={
                "exchange": exchange,
                "date": date,
                "symbol": symbol,
                "interval": interval
            },
        )

    def spot_prices_lite(
        self,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
      Explanation:
       Inputs:
        Currency Symbol: Top 100 coins

        Why do traders like this endpoint?
        This endpoint is a building block for spot and vol. traders alike.
        Use this endpoint to compare multiple coin prices.

        Calculation:
        OHLC: are calculated at midnight UTC.

        Endpoint Output Details:
        Granularity: Daily
        Dataset: 1-year of OHLC for various crypto-currencies.
        Date: Unix Format

        Args:
            {
            "symbol": "SOL"
            }
        Returns:
            {
            "date": "1656288000000",
            "currency": "SOL",
            "open": 39.38,
            "high": 41.22,
            "low": 37.96,
            "close": 38.46
            }
        """
        return self._client.execute(
            gql(queries.spot_prices_lite),
            variable_values={
                "symbol": symbol,
            },
        )

    def options_atm_constant_lite(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
      Explanation:
       Why do traders like this endpoint?
        It's an industry axiom that the at-the-money (ATM) volatility chart is often viewed as the "truest" option volatility, because options that are ATM have the most embedded optionality.
        Fixed maturity ATM volatility ensures that users are analyzing an identical product overtime.
        This endpoint provides various fixed maturities (7-day, 30-day, 60-day, 90-day, 180-day), enabling users to measure the "term structure" throughout time.
        More info: https://www.youtube.com/watch?v=w_l--D3xTLI

        Calculation:
        ATM options are first determined by isolating the nearest out-of-the-money (OTM) puts and calls, with respect to the underlying/forward prices.
        The ATM options are then weighted to account for varying distances from underlying/forward to strike.
        In order to calculate fixed maturities, the implied volatility is first converted into variance, then linearly interpolated to the target maturity and finally converted back into implied volatility.

        Endpoint Output Details:
        Granularity: Hourly
        Dataset: 30-days of hourly data points with 7-day, 30-day, 60-day, 90-day, 180-day fixed maturities.
        Exchange: Deribit
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year

        Args:
            {
            "exchange": "deribit",
            "symbol": "BTC"
            }
        Returns:
            {
            "date": "1656414000000",
            "atm7": 72.32,
            "atm30": 76.84,
            "atm60": 75.96,
            "atm90": 74.95,
            "atm180": 74.31,
            "currency": "BTC"
            }
        """
        return self._client.execute(
            gql(queries.options_atm_constant_lite),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
            },
        )

    def options_skew_constant_lite(
        self,
        exchange: types.ExchangeEnumType,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
      Explanation:
        Why do traders like this endpoint?
        When moving out into the "wings" of options (aka. farther out-of-the-money options) implied volatilities begin to differ between equidistant options.
        In this case, distance is measured by delta (Δ).
        The reason for this difference in implied volatility is due to "Volatility Path". Meaning, the option market might expect higher volatility/momentum during a market crash of 20% versus a market rally of 20% (or down to the -Δ25 versus up to the Δ25).
        More info: https://www.youtube.com/watch?v=Px6DewFrJeA

        Calculation:
        Target deltas are first calculated by weighting the nearest periphery options to account for varying distances from the target.
        In order to calculate fixed maturities, the implied volatility is first converted into variance, then linearly interpolated to the target maturity and finally converted back into implied volatility.

        Endpoint Output Details:
        Granularity: Hourly
        Dataset: 30-days of hourly data points for Δ35, Δ25, Δ15, Δ05, skews with fixed 7-day, 30-day, 60-day, 90-day, 180-day maturities.

        Exchange: Deribit
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year

        Args:
            {
            "exchange": "deribit",
            "symbol": "BTC"
            }

        Returns:
            {
            "date": "1656414000000",
            "currency": "BTC",
            "thirtyFiveDelta7DayExp": -4.43,
            "twentyFiveDelta7DayExp": -8.3,
            "fifteenDelta7DayExp": -13.41,
            "fiveDelta7DayExp": -23.41,
            "thirtyFiveDelta30DayExp": -7.39,
            "twentyFiveDelta30DayExp": -12.59,
            "fifteenDelta30DayExp": -19.49,
            "fiveDelta30DayExp": -33.63,
            "thirtyFiveDelta60DayExp": -6.87,
            "twentyFiveDelta60DayExp": -11.85,
            "fifteenDelta60DayExp": -17.39,
            "fiveDelta60DayExp": -27.89,
            "thirtyFiveDelta90DayExp": -5.87,
            "twentyFiveDelta90DayExp": -9.97,
            "fifteenDelta90DayExp": -15.02,
            "fiveDelta90DayExp": -23.83,
            "thirtyFiveDelta180DayExp": -4.14,
            "twentyFiveDelta180DayExp": -7.09,
            "fifteenDelta180DayExp": -10.61,
            "fiveDelta180DayExp": -19.7
            }
        """
        return self._client.execute(
            gql(queries.options_skew_constant_lite),
            variable_values={
                "exchange": exchange,
                "symbol": symbol,
            },
        )


    def futures_orderbook(
        self,
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """
      Explanation:
        Inputs:
        Exchange: Deribit, Bit.com, Okex, DyDx, FTX

        Why do traders like this endpoint?
        This endpoint returns the order-book for futures and perpetuals, often called ∆1 (Delta-one) products, along with 24hr volume and current open interest for each product.

        Calculation:
        USD
        24hr volume returned in usd: bit.com, okex, deribit, dydx, ftx

        open interest returned in usd: bit.com, okex, dydx, ftx

        COIN
        24hr volume returned in coin:

        open interest returned in coin: deribit

        Endpoint Output Details:
        Granularity: 100ms (1-minute for dydx)
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/yea

        Args:
            {
            "exchange": "dydx"
            }
        Returns:
            {
            "date": "1656418050139",
            "instrumentName": "1inch-usd",
            "expiration": null,
            "openInterest": 5779057,
            "volume24Hr": 2289284.149,
            "bestBidAmount": 17555,
            "bestBidPrice": 0.796,
            "markPrice": 0.79,
            "indexPrice": 0.7982,
            "bestAskPrice": 0.799,
            "bestAskAmount": 13637,
            "currentFunding": null
            }
        """
        return self._client.execute(
            gql(queries.futures_orderbook),
            variable_values={
                "exchange": exchange,
            },
        )


    def futures_perps_table(
        self, 
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """
        Dataset: Returns the futures perpetual "table" information

        Date: Unix Format
        Granularity: 100ms

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year
        
        Args:
            {
            "exchange": "deribit"
            }
        Returns:
            {
            "mcapMils": "16604.7",
            "instrumentName": "ADA_USDC-PERPETUAL",
            "currency": "ADA",
            "margin": "USD",
            "expiration": null,
            "price": 0.4915,
            "indexPrice": 0.4914,
            "priceChange24": -2.31,
            "apy": -3.15,
            "funding": 0,
            "oiUsdMillions": 0.35,
            "volume24UsdMillions": 0.49,
            "volumer2Oi": 1.4,
            "lsRatio": null,
            "hv5": 71.49,
            "hv10": 101.97,
            "hv14": 132.23,
            "hv30": 133.61,
            "hv60": 149.57,
            "hv90": 129.11,
            "hv180": 115.71
            }
        """
        return self._client.execute(
            gql(queries.futures_perps_table),
            variable_values={
                "exchange": exchange,
            },
        )


    def futures_futs_table(
        self, 
        exchange: types.ExchangeEnumType,
    ) -> Dict:
        """
        Dataset: Returns the futures "table" information

        Date: Unix Format
        Granularity: 100ms

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year
        
        Args:
            {
            "exchange": "deribit"
            }
        Returns:
            {
            "mcapMils": "401344.6",
            "instrumentName": "BTC-1JUL22",
            "currency": "BTC",
            "margin": "COIN",
            "expiration": "1656662400000",
            "price": 21029.43,
            "indexPrice": 21018.08,
            "priceChange24": -1.12,
            "apy": 6.97,
            "funding": null,
            "oiUsdMillions": 17.78,
            "volume24UsdMillions": 4.35,
            "volumer2Oi": 0.2,
            "lsRatio": null,
            "hv5": 54.72,
            "hv10": 96.96,
            "hv14": 120.84,
            "hv30": 93.79,
            "hv60": 86.67,
            "hv90": 76.53,
            "hv180": 71.71
            }
        """
        return self._client.execute(
            gql(queries.futures_futs_table),
            variable_values={
                "exchange": exchange,
            },
        )


    def defi_zeta_orderbook(
        self
    ) -> Dict:
        """
        Why do traders like this endpoint?
        This endpoint is real-time and will return live prices when requested.
        This endpoint will return the option order-book, oracle prices, order depth and implied volatility.

        Calculation:
        Black-Scholes Implied Volatility assumptions: 0% interest rate, oracle price as underlying.

        Endpoint Output Details:
        Granularity: 1 minute
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year

        Args:
            {
            }
        Returns:
            {
            "instrumentName": "21iZtRQWqBCBmq5oSCScpgU9JNEFLyEfWxdvpJxZuA8N",
            "date": "1656418441215",
            "currency": "SOL",
            "expiration": "1656662400000",
            "strike": 36,
            "putcall": "C",
            "distinctBidWallets": 1,
            "bidDepth": "{$2.2800000000000002x182.793}",
            "bestAskAmount": null,
            "bestBidPrice": 2.2800000000000002,
            "bidIv": null,
            "markPrice": null,
            "markIv": null,
            "askIv": null,
            "bestAskPrice": null,
            "askDepth": null,
            "distinctAskWallets": null,
            "isATM": "false",
            "oraclePrice": 39.41
            }
        """
        return self._client.execute(
            gql(queries.defi_zeta_orderbook),

        )

    def defi_ribbon_trades(
        self
    ) -> Dict:
        """
        Why do traders like this endpoint?
        This endpoint returns the option contract specs and notional size for Ribbon DOV (DeFi Option Vault) auctions, along with the given blockchain.

        Endpoint Output Details:
        Granularity: Daily
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year

        Args:
            {
            }
        Returns:
            {
            "date": "1656151185000",
            "expiration": "1656662400000",
            "defi": "ribbon",
            "underlying": "APE",
            "strike": 90,
            "putCall": "C",
            "direction": "sell",
            "volume": 8686.88,
            "coinPremium": 0.86,
            "notional": 39586
            }
        """
        return self._client.execute(
            gql(queries.defi_ribbon_trades),

        )


    def options_fitted_curves(
        self,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
        Returns fitted implied volatility with spline for expiration/strike

        Args:
            {
            "symbol":"BTC"
            }
        Returns:
            {
            "expiration": "1656460800000",
            "strike": 20000,
            "markIv": 72.07,
            "putCall": "C"
            }
        """
        return self._client.execute(
            gql(queries.options_fitted_curves),
            variable_values={
                "symbol": symbol,
            },
        )

    
    def defi_dovs_table(
        self,
    ) -> Dict:
        """
        Returns dovs (defi options vaults) "table" information
        Args:
            {
            }
        Returns:
            {
            "defi": "thetanuts",
            "instrumentName": "NEAR-01JUL22-5-C",
            "currency": "NEAR",
            "expiration": "1656662400000",
            "strike": 5,
            "putCall": "C",
            "usdOptionPremium": 0,
            "auctionWindowAveragePrice": 3.3,
            "volume": 30836.65,
            "notional": 103611.14,
            "deposits": 30836.6,
            "coinPremium": 616.73313739748,
            "absReturn": 0.02,
            "apy": 67.3,
            "iv": null
            }
        """
        return self._client.execute(
            gql(queries.defi_dovs_table),
            variable_values={},
        )


    ##ADDED AGAIN ON CUSTOMER'S REQUESTS

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
            expiration: "2022-12-30"  (YYYY-MM-DD)
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
    

   ##ADDED AGAIN ON CUSTOMER'S REQUESTS --FIN--


    def options_gvol_direction(
        self, dateStart: types.String, dateEnd: types.String, symbol: types.BTCOrETHEnumType
    ) -> Dict:
        """This query will return the Deribit trades with useful information about the orderbook at the time of the trade with the
        gvol feature gvol_direction that asses the real initiator of the trade.
        

        Args:
            {
            "dateStart": "2022-07-26", 
            "dateEnd": "2022-07-27"
            "symbol": "BTC"
            }
            
        Returns:
            {
            "preTxObTs": "1652831827818",
            "txTs": "1652831832293",
            "postTxObTs": "1652831832485",
            "tradeSeq": 210,
            "tradeId": "214787006",
            "instrumentName": "BTC-3JUN22-45000-C",
            "currency": "BTC",
            "expiration": "1654243200000",
            "strike": 45000,
            "putcall": "C",
            "blockTradeId": null,
            "liquidation": null,
            "direction": "sell",
            "tickDirection": "ZeroMinus",
            "txAmount": 16.8,
            "txIv": 83.29,
            "price": 0.001,
            "priceUsd": 30.41,
            "indexPrice": 30417.44,
            "underlyingPrice": 30459.1475,
            "volume24h": 27.1,
            "high24h": 0.002,
            "low24h": 0.0015,
            "preTxBbSize": 86.5,
            "preTxBbPrice": 0.001,
            "preTxBbIv": 83.34,
            "preTxMidIv": 85.81,
            "preTxMidPrice": 0.00125,
            "preTxMarkIv": 85.71,
            "preTxMarkPrice": 0.0012,
            "preTxBaIv": 88.29,
            "preTxBaPrice": 0.0015,
            "preTxBaSize": 8.6,
            "postTxBbSize": 44.3,
            "postTxBbPrice": 0.001,
            "postTxBbIv": 83.29,
            "postTxMidIv": 85.76,
            "postTxMidPrice": 0.00125,
            "postTxMarkIv": 85.72,
            "postTxMarkPrice": 0.0012,
            "postTxBaIv": 88.23,
            "postTxBaPrice": 0.0015,
            "postTxBaSize": 8.6,
            "delta": 0.019,
            "gamma": 0.00001,
            "theta": -8,
            "vega": 3,
            "rho": 0.2,
            "preTxOi": 86.3,
            "postTxOi": 84.1,
            "oiChange": -2.2
            "deribitDirection": "sell",
            "gvolDirection": "buy"
            }
        """
        return self._client.execute(
            gql(queries.options_gvol_direction),
            variable_values={"dateStart":dateStart, "dateEnd":dateEnd, "symbol":symbol},
        )

    def options_gvol_gex(
        self, symbol: types.BTCOrETHEnumType, date: types.String
    ) -> Dict:
        """This endpoint returns the gamma levels (in nr of contracts for 1$ move in the underlying) of Market Makers according to a proprietary gvol algorithm.
        Inventory of dealers are estimated using the gvol_direction of each trade and analyzing the live orderbook
        at millisecond level. Data available as of 1st August 2022. "DealerTotInventory" as of 8th Novemnber 2022
        Args:
            {
             "symbol": "BTC", 
             "date": "2022-11-11 14:00"
            }
        Returns:
                "currency": "BTC",
                "date": "1668175200000",
                "expiration": "1680249600000",
                "strike": 26000,
                "gammaLevel": -0.04,
                "dealerTotInventory": -1193.3
        """
        return self._client.execute(
            gql(queries.options_gvol_gex),
            variable_values={"symbol": symbol, "date":date},
        )

    def futures_constant_basis(
        self, symbol: types.BTCOrETHEnumType, dateStart: types.String, dateEnd: types.String, 
    ) -> Dict:
        """This query will return the Deribit futures basis annualized constant maturity in days.

        Args:
            {
            "symbol": "BTC",
            "dateStart": "2023-01-01",
            "dateEnd": "2023-01-09"
            }
            
        Returns:
            {
            "ts": "1673218800000",
            "currency": "BTC",
            "indexPrice": 16965.67,
            "b30": 0.1,
            "b60": 0.1,
            "b90": 0.1,
            "b120": 0.1
            }
        """
        return self._client.execute(
            gql(queries.futures_constant_basis),
            variable_values={"symbol":symbol, "dateStart":dateStart, "dateEnd":dateEnd},
        )

    def options_atm_skew_spot(
        self, symbol: types.BTCOrETHEnumType, dateStart: types.String, dateEnd: types.String, 
    ) -> Dict:
        """This query will return hourly data of: atm constant maturities, skew constant maturities with each components (puts and calls details) and index price. 

        Args:
            {
            "symbol": "BTC",
            "dateStart": "2023-01-01",
            "dateEnd": "2023-01-09"
            }
            
        Returns:
            {
                "ts": "1673222400000",
                "currency": "BTC",
                "atm7": 33.46,
                "atm30": 37.25,
                "atm60": 43.97,
                "atm90": 48.26,
                "atm180": 53.03,
                "ThirtyFiveDelta7Put": 33.76,
                "ThirtyFiveDelta7Call": 33.95,
                "TwentyFiveDelta7Put": 34.57,
                "TwentyFiveDelta7Call": 35.49,
                "FifteenDelta7Put": 36.37,
                "FifteenDelta7Call": 38.44,
                "FiveDelta7Put": 43.77,
                "FiveDelta7Call": 45.46,
                "ThirtyFiveDelta30Put": 38.43,
                "ThirtyFiveDelta30Call": 36.66,
                "TwentyFiveDelta30Put": 40.55,
                "TwentyFiveDelta30Call": 37.16,
                "FifteenDelta30Put": 44.65,
                "FifteenDelta30Call": 39.23,
                "FiveDelta30Put": 56.14,
                "FiveDelta30Call": 47.39,
                "ThirtyFiveDelta60Put": 45.67,
                "ThirtyFiveDelta60Call": 42.82,
                "TwentyFiveDelta60Put": 48.22,
                "TwentyFiveDelta60Call": 43,
                "FifteenDelta60Put": 53.26,
                "FifteenDelta60Call": 44.87,
                "FiveDelta60Put": 66.84,
                "FiveDelta60Call": 54.38,
                "ThirtyFiveDelta90Put": 49.98,
                "ThirtyFiveDelta90Call": 47.19,
                "TwentyFiveDelta90Put": 52.47,
                "TwentyFiveDelta90Call": 47.45,
                "FifteenDelta90Put": 57.55,
                "FifteenDelta90Call": 49.44,
                "FiveDelta90Put": 72.25,
                "FiveDelta90Call": 61,
                "ThirtyFiveDelta180Put": 54.22,
                "ThirtyFiveDelta180Call": 51.96,
                "TwentyFiveDelta180Put": 56.48,
                "TwentyFiveDelta180Call": 52.56,
                "FifteenDelta180Put": 60.52,
                "FifteenDelta180Call": 55.08,
                "FiveDelta180Put": 73.02,
                "FiveDelta180Call": 66.21
            }
        """
        return self._client.execute(
            gql(queries.options_atm_skew_spot),
            variable_values={"symbol":symbol, "dateStart":dateStart, "dateEnd":dateEnd},
        )

    def options_deribit_volume_detailed_daily(
        self, exchange: types.ExchangeEnumType, dateStart: types.String, dateEnd: types.String, 
    ) -> Dict:
        """This query will return the Deribit daily volumes detailed and open interest with putcall ratio.

        Args:
            {
            "exchange": "deribit",
            "dateStart": "2016-01-01",
            "dateEnd": "2023-01-19"
            }
            
        Returns:
            {
            "date": "1673395200000",
            "year": "2023",
            "month": "1",
            "blockTrade": "Block",
            "currency": "BTC",
            "typeOfTrade": "trade",
            "putCall": "C",
            "volume": 8670,
            "premium": 223,
            "notional": 151547850,
            "premiumDollar": 3902913,
            "avgIv": 48.3,
            "avgIndexPrice": 17480.4,
            "countTrades": 117,
            "oiNotional": 3404269477,
            "oiPcRatio": 0.47
            }
        """
        return self._client.execute(
            gql(queries.options_deribit_volume_detailed_daily),
            variable_values={"exchange":exchange, "dateStart":dateStart, "dateEnd":dateEnd},
        )