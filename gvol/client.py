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
        """The volatility skew, also known as the smile, represents an option’s implied volatility given different strike prices or delta.

        The Black-Scholes model assumes a constant volatility throughout the life of the option, yet, the underlying may behave differently depending on where it’s trading.

        Hence, if crypto were to drop 50% tomorrow (or double in value), the volatility would probably increase, therefore, out-of-money strikes and deltas are typically priced with richer volatilities.

        A good way of measuring skew is by calculating the ratio of an out-of-money option versus an at-the-money option. This relationship typically changes in low volatility environments versus high volatility environments.

        Example Response: ``{"ts": "1637677441586", "instrumentName": "BTC-24NOV21-59000-C", "strike": 59000, "expiration": "1637712000000", "bidIv": 59.4, "markIv": 66.33, "askIv": 71.68, "delta": 0.10811}``
        Args:
            symbol: BTC / ETH / SOL (deribit) / BCH (bitcom)
            exchange: deribit / bitcom / okex / ledgerx

        Returns:
            dict

        """
        return self._client.execute(
            gql(queries.options_orderbook),
            variable_values={"symbol": symbol, "exchange": exchange},
        )

    
    def options_termstructure(
        self, symbol: types.SymbolEnumType, exchange: types.ExchangeEnumType
    ) -> Dict:
        """The volatility term structure represents the implied volatility given different expiration dates.

        Example Response: ``{"expiration": "1637740800000", "markIv": 72.305, "forwardVolatility": 72.3 }``

        Args:
            symbol: BTC / ETH / SOL (deribit) / BCH (bitcom)
            exchange: deribit / bitcom / okex / ledgerx

        Returns:
            dict
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

        Example Response: ``{"sequenceDays2Exp": 0, "tsHourShadow": "1609502400000", "tsHourCurrent": null, "daysUntilExpiration": "0", "markIvCurrent": 73.02, "markIvShadow": 66.9 }``

        Args:
            dateTime: (types.String)
            symbol: (types.SymbolEnumType)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
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
        """DVolIndex query

        Example Response: ``{"timerange": "1635084000000", "instrument": "BTC", "open": 88.33, "high": 88.6, "low": 88.07, "close": 88.54}``

        Args:
            "exchange": "deribit", 
            "symbol":  "BTC", 
            "interval": "1 minute",
            "dateStart": "2022-04-11", 
            "dateEnd": "2022-04-12"

        Returns:
            dict
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

        Example Response: ``{"exchange": "deribit", "date": "1631750359238", "instrumentName": "ETH-17SEP21-3900-C", "baseCurrency": "ETH", "expiration": "ETH", "strike": 3900, "putCall": "C", "direction": "buy", "blockTrade": "no", "liquidation": "no", "amount": 7, "price": 0.002, "priceUsd": 7.22, "iv": "89.79"}``

        Args:
            date: (types.String)
            exchange: (types.ExchangeEnumType)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.options_trades),
            variable_values={"date": date, "exchange": exchange},
        )

    def options_trades_orderbook_details(
        self, exchange: types.ExchangeEnumType, symbol: types.SymbolEnumType, dateStart: types.String, dateEnd: types.String 
    ) -> Dict:
        """This query will return the trades with useful information about the orderbook at the time of the trade.

        Example Response: ``{"exchange": "deribit", "date": "1631750359238", "instrumentName": "ETH-17SEP21-3900-C", "baseCurrency": "ETH", "expiration": "ETH", "strike": 3900, "putCall": "C", "direction": "buy", "blockTrade": "no", "liquidation": "no", "amount": 7, "price": 0.002, "priceUsd": 7.22, "iv": "89.79"}``

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: BTC/ETH/SOL
            dateStart: '2022-12-31'
            dateEnd: '2022-12-31'
            

        Returns:
            dict
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

        Example Response: ``{"date": "1630454400000", "timeLeft": "08:00:00", "currency": "ETH", "expiration": "1630483200000", "underlyingPrice": 3431.38, "spot": 3431.24, "putD05": 104.11, "putD15": 100.33, "putD25": 94.6, "putD35": 90.61, "callD05": 86.85, "callD15": 85.78, "callD25": 84.85, "callD35": 83.97, "atmMarkIV": 86.75, "atmMidIV": 89.23, "atmBidIV": 84.86, "atmAskIV": 93.6}``

        Args:
            symbol: (types.BTCOrETHEnumType)
            date: (types.String)

        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.options_volatility_surface),
            variable_values={"symbol": symbol, "date": date},
        )

    
    def spot_prices(
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
        """HistoricalIntradayTradedWeightedBasis query

        Args:
            exchange: (types.ExchangeEnumType)
            symbol: (types.SymbolEnumType)
            expiration:  "2022-12-30 08:00:00"  (YYYY-MM-DD hh:mm:ss)
            dateStart: (types.String)
            dateEnd: (types.String)

        Returns:
            dict
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
             exchange: (types.ExchangeEnumType)
        Returns:
            dict
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
            portfolio: [{ "instrument": "BTC-30DEC22-40000-C", "size": 15 }, { "instrument": "BTC-30DEC22-55000-C", "size": -15}],
            deltaFutures: deltas to add/remove to portfolio
            ivShift: 0 (simulation of a shift in vol termstructure)
            symbol: BTC
      Returns:
            dict
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
             exchange: (types.ExchangeEnumType),
             symbol: (types.SymbolEnumType),
             date: (types.String)
        Returns:
            dict
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
             exchange: (types.ExchangeEnumType),
             symbol: (types.SymbolEnumType),
             dateTime: (types.String)
        Returns:
            dict
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
             symbol: (types.SymbolEnumType),

        Returns:
            dict
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
             exchange: (types.ExchangeEnumType)
             symbol: (types.SymbolEnumType),

        Returns:
            dict
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
             exchange: (types.ExchangeEnumType)
             symbol: (types.SymbolEnumType),

        Returns:
            dict
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
             symbol: (types.SymbolEnumType),

        Returns:
            dict
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
        Granularity: 100ms

        Dataset: Returns the perpetual prices, index price, current funding and funding 8h.
        Date: Unix Format
        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year
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
        Granularity: 100ms

        Dataset: Returns the perpetual prices, index price, current funding and funding 8h.
        Date: Unix Format
        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year
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
      Explanation:
        Inputs: None

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


        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.defi_zeta_orderbook),

        )

    def defi_ribbon_trades(
        self
    ) -> Dict:
        """
      Explanation:
        Inputs: None

        Why do traders like this endpoint?
        This endpoint returns the option contract specs and notional size for Ribbon DOV (DeFi Option Vault) auctions, along with the given blockchain.

        Endpoint Output Details:
        Granularity: Daily
        Date: Unix Format

        Need More? info@genesisvolatility.io
        API LITE Plus: Rate limit increase (10 per SECOND) $178/mo
        GVol API Pro: 30/SEC rate, fitted + model-free surfaces, intraday granularity extended histories $11,000/year
        GVol Enterprise API: GVol API Pro + Daily Raw data S3 bucket downloads $14,999/year


        Returns:
            dict
        """
        return self._client.execute(
            gql(queries.defi_ribbon_trades),

        )


    def options_fitted_curves(
        self,
        symbol: types.SymbolEnumType,
    ) -> Dict:
        """
        Parameters:
            "symbol":"BTC"
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
        Parameters:
        """
        return self._client.execute(
            gql(queries.defi_dovs_table),
            variable_values={},
        )
