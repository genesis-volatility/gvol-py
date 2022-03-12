CurrentOrderbookSkewStrike = """
    query OrderbookSkew($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      genericOrderbookSkew(symbol: $symbol, exchange: $exchange) {
        ts
        instrumentName
        strike
        expiration
        bidIv
        markIv
        askIv
        delta
      }
    }
"""

Shadow25Skews = """
    query TwentyThirtySkewShadow($dateTime: String, $symbol: SymbolEnumType) {
      TwentyThirtySkewShadow(dateTime: $dateTime, symbol: $symbol) {
        date
        twentyThirtyCallIvMinusPutIv
        daysUntilExpiration
      }
    }
"""

CurrentOrderbookSkewDeltaBucket = """
    query OrderbookSkewDelta($expiration: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderbookSkewDelta: genericOrderBookSkewDelta(symbol: $symbol, expiration: $expiration, exchange: $exchange) {
        expiration
        n00
        n01
        n02
        n03
        atm
        p03
        p02
        p01
        p00
      }
    }
"""

CurrentOrderbookTermStructure = """
    query OrderbookForwardImpliedVolatilityCurve1($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderbookForwardImpliedVolatilityCurve: genericOrderbookTermStructure(symbol: $symbol, exchange: $exchange) {
        expiration
        markIv
        forwardVolatility
      }
    }
"""

CurrentOrderbook1hr3020Skew = """
    query Orderbook1hr3020Skew($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      Orderbook1hr3020Skew: genericOrderbook1hr3020Skew(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        date
        callIvMinusPutIv
      }
    }
"""

CurrentOrderbook1HrATMVol = """
    query OrderBook1HrAtmVol($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      Orderbook1HrAtmVol: genericOrderbook1HrAtmVol(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        date
        avgMarkIv
      }
    }
"""

ConstantMaturityATMIV = """
    query ConstantMaturityAtmIv($symbol: SymbolEnumType) {
      HistoricalConstantMaturityVariousAtmIv(symbol: $symbol) {
        date
        seven
        thirty
        sixty
        ninty
        onehundredeighty
      }
    }
"""

ConstantMaturity30to20DeltaSkew = """
    query ConstantMaturity2030($symbol: SymbolEnumType) {
      HistoricalConstantMaturityVariousSkews(symbol: $symbol) {
        date
        seven
        thirty
        sixty
        ninty
        onehundredeighty
      }
    }
"""

ShadowTermStructure = """
    query OrderbookShadowTermStructure($dateTime: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderbookShadowTermStructure: genericShadowTermStructure(symbol: $symbol, dateTime: $dateTime, exchange: $exchange) {
        sequenceDays2Exp
        tsHourShadow
        tsHourCurrent
        daysUntilExpiration
        markIvCurrent
        markIvShadow
      }
    }
"""

ShadowTermStructureComparison = """
    query OrderbookShadowTermStuctureCompare($dateTimeOne: String, $dateTimeTwo: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderbookShadowTermStuctureCompare: genericShadowTermStructureCompare(symbol: $symbol, dateTimeOne: $dateTimeOne, dateTimeTwo: $dateTimeTwo, exchange: $exchange) {
        sequenceDays2Exp
        tsHourShadow
        tsHourCurrent
        daysUntilExpiration
        markIvCurrent
        markIvShadow
      }
    }
"""

HistoricalSkew = """
    query HistoricalSkewExpirations($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalSkew: genericHistoricalSkew(symbol: $symbol, date: $date, exchange: $exchange) {
        expirationDate
        weightedIv
        strike
        premiumValue
      }
    }
"""

HistoricalTermStructure = """
    query HistoricalATMDeltasTermStructure($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalATMDeltasTermStructure: genericHistoricalAtmDeltasTermStructure(symbol: $symbol, date: $date, exchange: $exchange) {
        expirationDate
        weightedIv
        fwdIv
        totalUsdTraded
      }
    }
"""

HistoricalConstantSkew = """
    query HistoricalConstantSkew($exchange: ExchangeEnumType, $days: Float) {
      HistoricalConstantSkew: genericHistoricalConstantSkew(exchange: $exchange, days: $days) {
        date
        btcSkewShort
        btcSkewMed
        btcSkewLong
        ethSkewShort
        ethSkewMed
        ethSkewLong
      }
    }
"""

HistoricalConstantATM = """
    query HistoricalConstantAtm($exchange: ExchangeEnumType, $days: Float) {
      HistoricalConstantAtm: genericHistoricalConstantsAtm(exchange: $exchange, days: $days) {
        date
        btcAtmShort
        btcAtmMed
        btcAtmLong
        ethAtmShort
        ethAtmMed
        ethAtmLong
      }
    }
"""

HistoricalConstantWings = """
    query HistoricalConstantWingsAtm($exchange: ExchangeEnumType, $days: Float) {
      HistoricalConstantWingsAtm: genericHistoricalConstantWingsAtm(exchange: $exchange, days: $days) {
        date
        btcShort
        btcMed
        btcLong
        ethShort
        ethMed
        ethLong
      }
    }
"""

DVolIndex = """
    query dVol($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $interval: String, $dateStart: String, $dateEnd: String) {
      dVol: genericDvol(symbol: $symbol, exchange: $exchange, interval: $interval, dateStart: $dateStart, dateEnd: $dateEnd) {
        timerange
        instrument
        open
        high
        low
        close
      }
    }
"""

OrderbookATMDepthPriceandSize = """
    query OrderbookAtmDepthPxSize($date: String, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OrderbookAtmDepthPxSize: genericOrderbookAtmDepthPxSize(symbol: $symbol, date: $date, exchange: $exchange) {
        date
        instrumentName
        baseCurrency
        expiration
        bidSize5LevelsDeep
        avgBidPrice5LevelsDeep
        askSize5LevelsDeep
        avgAskPrice5LevelsDeep
      }
    }
"""

OpenInterestByStrike = """
    query OrderBookOpenInterestByStrike($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderBookOpenInterestByStrike: genericOrderBookOpenInterestByStrike(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        strike
        openInterest
        notionalOpenInterest
        coinPremium
        dollarPremium
        netDeltaExposure
        coinOi
      }
    }
"""

OpenInterestByPutCall = """
    query OrderBookOpenInterestByPutCall($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OrderBookOpenInterestByPutCall: genericOrderBookOpenInterestByPutCall(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        putCall
        openInterest
        notionalOpenInterest
        coinPremium
        dollarPremium
        netDeltaExposure
        coinOi
      }
    }
"""

OpenInterestByExpiration = """
    query OrderBookOpenInterestByExpiration($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OrderBookOpenInterestByExpiration: genericOrderBookOpenInterestByExpiration(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        expiration
        openInterest
        notionalOpenInterest
        coinPremium
        dollarPremium
        netDeltaExposure
        coinOi
      }
    }
"""

GlobalOpenInterestByStrikeExpirationPutCall = """
    query GlobalExchangeStrikeExpirationOi($symbol: SymbolEnumType) {
      GlobalExchangeStrikeExpirationOi(symbol: $symbol) {
        strike
        putCall
        expiration
        deribitContractOi
        deribitNotionalOi
        bitcomContractOi
        bitcomNotionalOi
        okexContractOi
        okexNotionalOi
        ledgerXContractOi
        ledgerXNotionalOi
      }
    }
"""

CurrentOiChangeByStrikeandExpiration = """
    query CurrentOiChangeByStrikeExpirationDetailed($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOiChangeByStrikeExpirationDetailed: genericCurrentOiChangeByStrikeExpirationDetailed(symbol: $symbol, exchange: $exchange) {
        expiration
        strike
        oiChange
      }
    }
"""

CurrentVolumebyExpiration = """
    query CurrentVolumeByExpiration($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumeByExpiration: genericCurrentVolumeByExpiration(symbol: $symbol, exchange: $exchange) {
        date
        expiration
        contractsTraded
        coin1Volume
        premiumTraded
      }
    }
"""

CurrentVolumebyStrike = """
    query CurrentVolumeByStrike($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumeByStrike: genericCurrentVolumeByStrike(symbol: $symbol, exchange: $exchange) {
        date
        strike
        contractsTraded
        premiumTraded
        coin1Volume
      }
    }
"""

CurrentVolumebyPutCall = """
    query CurrentVolumeByPutCall($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumeByPutCall: genericCurrentVolumeByPutCall(symbol: $symbol, exchange: $exchange) {
        contractVolume
        putContractVolume
        putContractVolume1Btc
        putPremiumTraded
        callContractVolume
        callContractVolume1Btc
        callPremiumTraded
      }
    }
"""

HistoricalPutCallRatio = """
    query HistoricalPutCallRatio($date1: String, $date2: String, $rangeStart: Float, $rangeEnd: Float, $direction1: String, $direction2: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalPutCallRatio: genericHistoricalPutCallRatio(symbol: $symbol, beginDate: $date1, endDate: $date2, rangeStart: $rangeStart, rangeEnd: $rangeEnd, direction1: $direction1, direction2: $direction2, exchange: $exchange) {
        date
        callContracts
        putContracts
        callPremium
        putPremium
        callsBlockTraded
        putsBlocktraded
        callPremiumBlockTraded
        putPremiumBlockTraded
      }
    }
"""

HistoricalVolume = """
    query HistoricalContractsTradedAndPremiumVolume($date1: String, $date2: String, $rangeStart: Float, $rangeEnd: Float, $direction1: String, $direction2: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalContractsTradedAndPremiumVolume: genericHistoricalContractsTradedAndPremiumDollarVolume(symbol: $symbol, beginDate: $date1, endDate: $date2, rangeStart: $rangeStart, rangeEnd: $rangeEnd, direction1: $direction1, direction2: $direction2, exchange: $exchange) {
        date
        contractsTraded
        contractsBlockTraded
        premiumValue
        premiumBlockTraded
      }
    }
"""

HistoricalChangeinOIbyExpiration = """
    query HistoricalOiChangeByPutCallExpiration($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalOiChangeByPutCallExpiration: genericHistoricalOiChangeByPutCallExpiration(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol, exchange: $exchange) {
        expiration
        callOiChange
        putOiChange
        totalOiChange
      }
    }
"""

HistoricalChangeinOIbyStrike = """
    query HistoricalOiChangeByStrike($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalOiChangeByStrike: genericHistoricalOiChangeByStrike(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol, exchange: $exchange) {
        strike
        totalOiChange
        callOiChange
        putOiChange
      }
    }
"""

ParadigmBlockSnifferCallSpreadsasPercentageofTradeCount = """
    query ParadigmCallSpreadPercentage($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
      ParadigmCallSpreadPercentage(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        percentageOfTrades
      }
    }
"""

ParadigmBlockSnifferPutSpreadsasPercentageofTradeCount = """
    query ParadigmPutSpreadPercentage($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
      ParadigmPutSpreadPercentage(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        percentageOfTrades
      }
    }
"""

ParadigmBlockSnifferSingleLegBlockTrades = """
    query ParadigmSingleTrades($date: String, $symbol: SymbolEnumType) {
      ParadigmSingleTrades(symbol: $symbol, date: $date) {
        date
        indexPrice
        direction
        amount
        price
        instrumentName
        priceUsd
        sizeUsd
        iv
        blockTradeId
        count
      }
    }
"""

ParadgimBlockSnifferTradesTiedUpMultiLegTrades = """
    query OrderbookTiedUpInBlocks($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OrderbookTiedUpInBlocks: genericTiedUpBlockTrades(symbol: $symbol, date: $date, exchange: $exchange) {
        ts
        indexPrice
        direction
        amount
        instrumentName
        sizeUsd
        priceUsd
        iv
        blockTradeId
        count
      }
    }
"""

ParadgimBlockSnifferDetailedVolumeBreakdown = """
    query ParadigmVolume($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
      ParadigmVolume(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        expiration
        strike
        putCall
        contractVolume
        premiumVolume
      }
    }
"""

TimesandSales = """
    query TimesAndSales($date: String, $exchange: ExchangeEnumType) {
      TimesAndSales(date: $date, exchange: $exchange) {
        exchange
        date
        instrumentName
        baseCurrency
        expiration
        strike
        putCall
        direction
        blockTrade
        liquidation
        amount
        price
        priceUsd
        iv
      }
    }
"""

VolatilityCone = """
    query RealizedVolVolatilityConesQuery($symbol: SymbolEnumType, $date1: String, $date2: String) {
      RealizedVolVolatilityCones(symbol: $symbol, beginDate: $date1, endDate: $date2) {
        max365
        current365
        min365
        p75365
        p50365
        p25365
        max180
        current180
        min180
        p75180
        p50180
        p25180
        max90
        current90
        min90
        p7590
        p5090
        p2590
        max30
        current30
        min30
        p7530
        p5030
        p2530
        max14
        current14
        min14
        p7514
        p5014
        p2514
        max7
        current7
        min7
        p757
        p507
        p257
        max0
        current0
        min0
        p750
        p500
        p250
      }
    }
"""

RealizedVolvsTradeWeightedIV = """
    query RealizedVolParkinsonCalc($date1: String, $date2: String, $timeWindow: Float, $beginDate: String, $endDate: String, $rangeStart: Float, $rangeEnd: Float, $deltaRangeStart: Float, $deltaRangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      RealizedVolParkinsonCalc(symbol: $symbol, beginDate: $date1, endDate: $date2, timeWindow: $timeWindow) {
        date
        parkinsonHv
      }
      HistoricalTradeWeightedIV: genericHistoricalTradeWeightedIV(symbol: $symbol, beginDate: $beginDate, endDate: $endDate, rangeStart: $rangeStart, rangeEnd: $rangeEnd, deltaRangeStart: $deltaRangeStart, deltaRangeEnd: $deltaRangeEnd, exchange: $exchange) {
        date
        weightedIv
      }
    }
"""

RealizedVolDayofWeek = """
    query OrderbookDayOfWeekRv($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      OrderbookDayOfWeekRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        dowUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

RealizedVolHourofDay = """
    query OrderbookHourOfDayRv($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      OrderbookHourOfDayRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        hourUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

RealizedVolHourofDayandDayofWeek = """
    query OrderbookHourAndDayRv($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      OrderbookHourAndDayRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        dowVal
        dow
        hourUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

IntradayRealizedVolatility = """
    query OrderbookIntradayParkinsonHv($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String, $range1: Float, $range2: Float) {
      OrderbookIntradayParkinsonHv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, range1: $range1, range2: $range2) {
        ts
        parkinsonHvPerp
        parkisonHvIndex
      }
    }
"""

ClosetoCloseHistoricalVol = """
    query currentOrderbookPricing($symbol: String, $dateStart: String, $dateEnd: String) {
      CloseToCloseHv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        date
        currency
        close
        yesterdayClose
        vol
      }
    }
"""

RealizedVolParkinson = """
    query currentOrderbookPricing($symbol: String, $dateStart: String, $dateEnd: String, $parkinsonRange: Float) {
      RvParkinson(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, parkinsonRange: $parkinsonRange) {
        date
        parkinsonHV
      }
    }
"""

OHLC = """
    query OHLC($symbol: String, $dateStart: String, $dateEnd: String) {
      RvOhlc(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        date
        currency
        open
        high
        low
        close
      }
    }
"""

CoveredCall = """
    query coveredCall($symbol: SymbolEnumType) {
      deribit: genericCoveredCall(exchange: deribit, symbol: $symbol) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        calledOutAnnualized
        calledOutAbsolute
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        annualBidYieldNet
        annualAskYieldNet
        annualMarkYieldNet
        absoluteMarkYieldCalledOut
        absoluteAskYieldCalledOut
        absoluteBidYieldCalledOut
        annualizedBidYieldCalledOut
        annualizedMarkYieldCalledOut
        annualizedAskYieldCalledOut
      }
      bitcom: genericCoveredCall(exchange: bitcom, symbol: $symbol) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        calledOutAnnualized
        calledOutAbsolute
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        annualBidYieldNet
        annualAskYieldNet
        annualMarkYieldNet
        absoluteMarkYieldCalledOut
        absoluteAskYieldCalledOut
        absoluteBidYieldCalledOut
        annualizedBidYieldCalledOut
        annualizedMarkYieldCalledOut
        annualizedAskYieldCalledOut
      }
      ledgerx: genericCoveredCall(exchange: ledgerx, symbol: $symbol) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        calledOutAnnualized
        calledOutAbsolute
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        annualBidYieldNet
        annualAskYieldNet
        annualMarkYieldNet
        absoluteMarkYieldCalledOut
        absoluteAskYieldCalledOut
        absoluteBidYieldCalledOut
        annualizedBidYieldCalledOut
        annualizedMarkYieldCalledOut
        annualizedAskYieldCalledOut
      }
      okex: genericCoveredCall(exchange: okex, symbol: $symbol) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        calledOutAnnualized
        calledOutAbsolute
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        annualBidYieldNet
        annualAskYieldNet
        annualMarkYieldNet
        absoluteMarkYieldCalledOut
        absoluteAskYieldCalledOut
        absoluteBidYieldCalledOut
        annualizedBidYieldCalledOut
        annualizedMarkYieldCalledOut
        annualizedAskYieldCalledOut
      }
      binance: genericCoveredCall(exchange: binance, symbol: $symbol) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        calledOutAnnualized
        calledOutAbsolute
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        annualBidYieldNet
        annualAskYieldNet
        annualMarkYieldNet
        absoluteMarkYieldCalledOut
        absoluteAskYieldCalledOut
        absoluteBidYieldCalledOut
        annualizedBidYieldCalledOut
        annualizedMarkYieldCalledOut
        annualizedAskYieldCalledOut
      }
    }
"""

CashSecuredPuts = """
    query cashSecuredPuts($symbol: SymbolEnumType) {
      deribit: genericCashSecuredPuts(symbol: $symbol, exchange: deribit) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        bidYieldNetAnnual
        markYieldNetAnnual
        askYieldNetAnnual
      }
      bitcom: genericCashSecuredPuts(symbol: $symbol, exchange: bitcom) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        bidYieldNetAnnual
        markYieldNetAnnual
        askYieldNetAnnual
      }
      ledgerx: genericCashSecuredPuts(symbol: $symbol, exchange: ledgerx) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        bidYieldNetAnnual
        markYieldNetAnnual
        askYieldNetAnnual
      }
      okex: genericCashSecuredPuts(symbol: $symbol, exchange: okex) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        bidYieldNetAnnual
        markYieldNetAnnual
        askYieldNetAnnual
      }
      binance: genericCashSecuredPuts(symbol: $symbol, exchange: binance) {
        date
        instrumentName
        expiration
        strike
        putCall
        bidUsd
        markUsd
        askUsd
        absoluteBidYieldNet
        absoluteMarkYieldNet
        absoluteAskYieldNet
        bidYieldNetAnnual
        markYieldNetAnnual
        askYieldNetAnnual
      }
    }
"""

StraddleRun = """
    query straddleRun($symbol: SymbolEnumType) {
      deribit: genericStraddleRun(symbol: $symbol, exchange: deribit) {
        expiration
        strike
        bidUsd
        markUsd
        askUsd
        bidSpotPercentage
        markSpotPercentage
        askSpotPercentage
        theta
        vega
        underlyingPrice
      }
      bitcom: genericStraddleRun(symbol: $symbol, exchange: bitcom) {
        expiration
        strike
        bidUsd
        markUsd
        askUsd
        bidSpotPercentage
        markSpotPercentage
        askSpotPercentage
        theta
        vega
        underlyingPrice
      }
      ledgerx: genericStraddleRun(symbol: $symbol, exchange: ledgerx) {
        expiration
        strike
        bidUsd
        markUsd
        askUsd
        bidSpotPercentage
        markSpotPercentage
        askSpotPercentage
        theta
        vega
        underlyingPrice
      }
      okex: genericStraddleRun(symbol: $symbol, exchange: okex) {
        expiration
        strike
        bidUsd
        markUsd
        askUsd
        bidSpotPercentage
        markSpotPercentage
        askSpotPercentage
        theta
        vega
        underlyingPrice
      }
      binance: genericStraddleRun(symbol: $symbol, exchange: binance) {
        expiration
        strike
        bidUsd
        markUsd
        askUsd
        bidSpotPercentage
        markSpotPercentage
        askSpotPercentage
        theta
        vega
        underlyingPrice
      }
    }
"""

GlobalAllOrderBooksOptionPricing = """
    query currentOrderbookPricing {
      currentOrderbookPricing {
        date
        instrumentName
        currency
        expiration
        strike
        putCall
        bestBidPrice
        bestAskPrice
        markIv
        bidIv
        askIv
        exchange
      }
    }
"""

VolatilitySurfaceStrikes = """
    {
      HifiStrikesVolSurface(symbol: BTC, date: "2021-12-13", interval: "1 hour", exchange: deribit) {
        date
        currency
        expiration
        strike
        putCall
        spot
        underlyingPrice
        bidIv
        markIv
        askIv
        bestBidAmount
        bestBidPrice
        markPrice
        bestAskPrice
        bestAskAmount
      }
    }
"""

VolatilitySurfaceDelta = """
    query HifiVolSurface1DayOf1Min($symbol: BTCOrETHEnumType, $date: String) {
      HifiVolSurface1DayOf1Min(symbol: $symbol, date: $date) {
        date
        timeLeft
        currency
        expiration
        underlyingPrice
        spot
        putD05
        putD15
        putD25
        putD35
        callD05
        callD15
        callD25
        callD35
        atmMarkIV
        atmMidIV
        atmBidIV
        atmAskIV
      }
    }
"""

ShadowTermStructureand25Skew = """
    query ShadowTimeSkew($date: String, $symbol: SymbolEnumType) {
      ShadowTimeSkew(date: $date, symbol: $symbol) {
        dateAndHour
        daysUntilExpiration
        atmIv
        twentyThirtyCallIvMinusPutIv
      }
    }
"""

HourlyInstrumentImpliedVolandOI = """
    query InstrumentOiIv1Hr($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $strike: String, $putCall: PutCallEnumType, $expiration: String) {
      InstrumentOiIv1Hr(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, strike: $strike, putCall: $putCall, expiration: $expiration) {
        date
        instrumentName
        oi
        bidIV
        markIV
        askIV
      }
    }
"""

SpotPrices = """
    query spotPrice($symbol: String, $dateStart: String, $dateEnd: String) {
      SpotPrices(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol) {
        date
        currency
        open
        high
        low
        close
      }
    }
"""

ConstantMaturitySkew1minutegranularity = """
    query ConstantMaturitySkew1Min($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $interval: String) {
      ConstantMaturitySkew1Min(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, interval: $interval) {
        date
        thirtyFiveDelta7DayExp
        twentyFiveDelta7DayExp
        fifteenDelta7DayExp
        fiveDelta7DayExp
        thirtyFiveDelta30DayExp
        twentyFiveDelta30DayExp
        fifteenDelta30DayExp
        fiveDelta30DayExp
        thirtyFiveDelta60DayExp
        twentyFiveDelta60DayExp
        fifteenDelta60DayExp
        fiveDelta60DayExp
        thirtyFiveDelta90DayExp
        twentyFiveDelta90DayExp
        fifteenDelta90DayExp
        fiveDelta90DayExp
        thirtyFiveDelta180DayExp
        twentyFiveDelta180DayExp
        fifteenDelta180DayExp
        fiveDelta180DayExp
      }
    }
"""

ConstantMaturityATM1minutegranularity = """
    query ConstantMaturityAtm1Min($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $interval: String) {
      ConstantMaturityAtm1Min(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, interval: $interval) {
        date
        atm7
        atm30
        atm60
        atm90
        atm180
      }
    }
"""

CustomMaturityDeltaSurface = """
    query CustomMaturityAtmDelta($symbol: BTCOrETHEnumType, $date: String, $days: Float) {
      CustomMaturityAtmDelta(symbol: $symbol, date: $date, days: $days) {
        date
        p05
        p15
        p25
        p35
        atm
        c05
        c15
        c25
        c35
      }
    }
"""

Orderbook30dayHourlyBasis = """
    query FuturesCurrentOb30dayHourlyBasisandSpot($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String) {
      FuturesCurrentOb30dayHourlyBasisandSpot: genericCurrentOb30dayHourlyBasisandSpot(exchange: $exchange, symbol: $symbol, expiration: $expiration) {
        date
        midPrice
        basis
      }
    }
"""

OrderbookBasisVolumeandOpenInterest = """
    query CurrentObBasisVolumeOpenInterest($exchange: ExchangeEnumType, $symbol: SymbolEnumType) {
      CurrentObBasisVolumeOpenInterests: genericCurrentObBasisVolumeOpenInterest(exchange: $exchange, symbol: $symbol) {
        date
        instrument
        indexPrice
        markPrice
        midPrice
        expirationn
        timeleft
        dollarSpread
        annualizedPercentSpread
        coinVolume
        openInterestCoin
      }
    }
"""

OrderbookPast1HrBasisandSpot = """
    query futuresCurrentObPast1HrBasisAndSpot($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String) {
      futuresCurrentObPastBasisAndSpot: genericCurrentObPast1HrBasisAndSpot(exchange: $exchange, symbol: $symbol, expiration: $expiration) {
        date
        price
        expiration
        amount
        annualizedPercentSpread
      }
    }
"""

Orderbook30DayTradeWeightedBasis = """
    query Historical30dayTradeWeightedBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $excludeExpiration: Boolean) {
      Historical30dayTradeWeightedBasis: genericHistorical30DayTradeWeightedBasis(exchange: $exchange, symbol: $symbol, excludeExpiration: $excludeExpiration) {
        date
        instrumentName
        vwapBasis
      }
    }
"""

HistoricalIntradayTradedWeightedBasis = """
    query HistoricalIntraDayTradedBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String, $dateStart: String, $dateEnd: String) {
      HistoricalIntraDayTradedBasis: genericHistoricalIntraDayTradedBasis(exchange: $exchange, symbol: $symbol, expiration: $expiration, dateStart: $dateStart, dateEnd: $dateEnd) {
        date
        expiration
        amount
        basis
        open
        high
        low
        close
      }
    }
"""

Basis24HR = """
    query CurrentObPast24HrBasisHistogram($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String, $dateStart: String, $dateEnd: String) {
      CurrentObPastBasisHistogram: genericCurrentOb24HrBasisHistogram(exchange: $exchange, symbol: $symbol, expiration: $expiration, dateStart: $dateStart, dateEnd: $dateEnd) {
        annualizedPercentSpread
        dollarVolume
      }
    }
"""

HifiStrikesVolSurface = """
    query HifiStrikesVolSurface($symbol: BTCOrETHEnumType, $date: String, $interval: String, $exchange: ExchangeEnumType) {
      HifiStrikesVolSurface(symbol: $symbol, date: $date, interval: $interval, exchange: $exchange) {
        date
        currency
        expiration
        strike
        putCall
        spot
        underlyingPrice
        bidIv
        markIv
        askIv
        bestBidAmount
        bestBidPrice
        markPrice
        bestAskPrice
        bestAskAmount
      }
    }
"""


HifiVolSurfaceStrikesGreeksMinute = """
query HifiVolSurfaceStrikesGreeksMinute(
  $symbol: BTCOrETHEnumType, 
  $dateTime: String, 
  $exchange: ExchangeEnumType
   ){
  HifiVolSurfaceStrikesGreeksMinute(
    symbol: $symbol, 
    dateTime: $dateTime, 
    exchange:$exchange,
    ) {
    date
    currency
    expiration
    strike
    putCall
    spot
    underlyingPrice
    bidIv
    markIv
    askIv
    bestBidAmount
    bestBidPrice
    markPrice
    bestAskPrice
    bestAskAmount
    delta
    gamma
    vega
    theta
  } 
}
"""

HifiVolSurfaceStrikesGreeksHourly = """
query HifiVolSurfaceStrikesGreeksHourly(
  $symbol: BTCOrETHEnumType, 
  $date: String, 
 $interval:String,
$exchange: ExchangeEnumType ){
  HifiVolSurfaceStrikesGreeksHourly(
    symbol: $symbol, 
    date: $date, 
    interval: $interval, 
    exchange:$exchange) {
    date
    currency
    expiration
    strike
    putCall
    spot
    underlyingPrice
    bidIv
    markIv
    askIv
    bestBidAmount
    bestBidPrice
    markPrice
    bestAskPrice
    bestAskAmount
    delta
    gamma
    vega
    theta
  } 
}
"""


dvolVariancePremium = """
query DVolVariancePremium($symbol: SymbolEnumType) {
		dvolVariancePremium(symbol: $symbol) {
			dvolImpliedRvDate
			instrument
			dvolOpen30Days
			parkinsonHv
			variancePremium
		}
	}
"""


UtilityRealtimeOptionbook = """	
query UtilityRealtimeOptionbook(
		$exchange: ExchangeEnumType
	) {
		UtilityRealtimeOptionbook: genericUtilityRealtimeOptionbook(
			exchange: $exchange	
		) {
			      date
            instrumentName
            currency
            expiration
            strike
            putCall
            isAtm
            oi
            bestBidPrice
            bestAskPrice
            usdBid
            usdAsk
            bidIV
            markIv
            askIv
            indexPrice
            underlyingPrice
		}
	}
  """
