CurrentOrderbookSkewStrike = """
    query CurrentOrderbookSkewStrike($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbookSkewStrike: genericOrderbookSkew(symbol: $symbol, exchange: $exchange) {
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

CurrentOrderbookSkewDeltaBucket = """
    query CurrentOrderbookSkewDeltaBucket($expiration: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbookSkewDeltaBucket: genericOrderBookSkewDelta(symbol: $symbol, expiration: $expiration, exchange: $exchange) {
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
    query CurrentOrderbookTermStructure($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbookTermStructure: genericOrderbookTermStructure(symbol: $symbol, exchange: $exchange) {
        expiration
        markIv
        forwardVolatility
      }
    }
"""

CurrentOrderbook1hr3020Skew = """
    query CurrentOrderbook1hr3020Skew($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbook1hr3020Skew: genericOrderbook1hr3020Skew(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        date
        callIvMinusPutIv
      }
    }
"""

CurrentOrderbook1HrATMVol = """
    query CurrentOrderbook1HrATMVol($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbook1HrATMVol: genericOrderbook1HrAtmVol(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
        date
        avgMarkIv
      }
    }
"""

ConstantMaturityATMIV = """
    query ConstantMaturityATMIV($symbol: SymbolEnumType) {
      ConstantMaturityATMIV: HistoricalConstantMaturityVariousAtmIv(symbol: $symbol) {
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
    query ConstantMaturity30to20DeltaSkew($symbol: SymbolEnumType) {
      ConstantMaturity30to20DeltaSkew: HistoricalConstantMaturityVariousSkews(symbol: $symbol) {
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
    query ShadowTermStructure($dateTime: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      ShadowTermStructure: genericShadowTermStructure(symbol: $symbol, dateTime: $dateTime, exchange: $exchange) {
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
    query ShadowTermStructureComparison($dateTimeOne: String, $dateTimeTwo: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      ShadowTermStructureComparison: genericShadowTermStructureCompare(symbol: $symbol, dateTimeOne: $dateTimeOne, dateTimeTwo: $dateTimeTwo, exchange: $exchange) {
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
    query HistoricalSkew($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalSkew: genericHistoricalSkew(symbol: $symbol, date: $date, exchange: $exchange) {
        expirationDate
        weightedIv
        strike
        premiumValue
      }
    }
"""

HistoricalTermStructure = """
    query HistoricalTermStructure($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalTermStructure: genericHistoricalAtmDeltasTermStructure(symbol: $symbol, date: $date, exchange: $exchange) {
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
    query HistoricalConstantATM($exchange: ExchangeEnumType, $days: Float) {
      HistoricalConstantATM: genericHistoricalConstantsAtm(exchange: $exchange, days: $days) {
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
    query HistoricalConstantWings($exchange: ExchangeEnumType, $days: Float) {
      HistoricalConstantWings: genericHistoricalConstantWingsAtm(exchange: $exchange, days: $days) {
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
    query DVolIndex($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $interval: String, $dateStart: String, $dateEnd: String) {
      DVolIndex: genericDvol(symbol: $symbol, exchange: $exchange, interval: $interval, dateStart: $dateStart, dateEnd: $dateEnd) {
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
    query OrderbookATMDepthPriceandSize($date: String, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OrderbookATMDepthPriceandSize: genericOrderbookAtmDepthPxSize(symbol: $symbol, date: $date, exchange: $exchange) {
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
    query OpenInterestByStrike($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      OpenInterestByStrike: genericOrderBookOpenInterestByStrike(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
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
    query OpenInterestByPutCall($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OpenInterestByPutCall: genericOrderBookOpenInterestByPutCall(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
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
    query OpenInterestByExpiration($rangeStart: Float, $rangeEnd: Float, $symbol: SymbolEnumType!, $exchange: ExchangeEnumType) {
      OpenInterestByExpiration: genericOrderBookOpenInterestByExpiration(symbol: $symbol, rangeStart: $rangeStart, rangeEnd: $rangeEnd, exchange: $exchange) {
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
    query GlobalOpenInterestByStrikeExpirationPutCall($symbol: SymbolEnumType) {
      GlobalOpenInterestByStrikeExpirationPutCall(symbol: $symbol) {
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
    query CurrentOiChangeByStrikeandExpiration($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOiChangeByStrikeandExpiration: genericCurrentOiChangeByStrikeExpirationDetailed(symbol: $symbol, exchange: $exchange) {
        expiration
        strike
        oiChange
      }
    }
"""

CurrentVolumebyExpiration = """
    query CurrentVolumebyExpiration($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumebyExpiration: genericCurrentVolumeByExpiration(symbol: $symbol, exchange: $exchange) {
        date
        expiration
        contractsTraded
        coin1Volume
        premiumTraded
      }
    }
"""

CurrentVolumebyStrike = """
    query CurrentVolumebyStrike($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumebyStrike: genericCurrentVolumeByStrike(symbol: $symbol, exchange: $exchange) {
        date
        strike
        contractsTraded
        premiumTraded
        coin1Volume
      }
    }
"""

CurrentVolumebyPutCall = """
    query CurrentVolumebyPutCall($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentVolumebyPutCall: genericCurrentVolumeByPutCall(symbol: $symbol, exchange: $exchange) {
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
    query HistoricalVolume($date1: String, $date2: String, $rangeStart: Float, $rangeEnd: Float, $direction1: String, $direction2: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalVolume: genericHistoricalContractsTradedAndPremiumDollarVolume(symbol: $symbol, beginDate: $date1, endDate: $date2, rangeStart: $rangeStart, rangeEnd: $rangeEnd, direction1: $direction1, direction2: $direction2, exchange: $exchange) {
        date
        contractsTraded
        contractsBlockTraded
        premiumValue
        premiumBlockTraded
      }
    }
"""

HistoricalChangeinOIbyExpiration = """
    query HistoricalChangeinOIbyExpiration($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalChangeinOIbyExpiration: genericHistoricalOiChangeByPutCallExpiration(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol, exchange: $exchange) {
        expiration
        callOiChange
        putOiChange
        totalOiChange
      }
    }
"""

HistoricalChangeinOIbyStrike = """
    query HistoricalChangeinOIbyStrike($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      HistoricalChangeinOIbyStrike: genericHistoricalOiChangeByStrike(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol, exchange: $exchange) {
        strike
        totalOiChange
        callOiChange
        putOiChange
      }
    }
"""

ParadigmBlockSnifferCallSpreadsasPercentageofTradeCount = """
    query ParadigmCallSpreadPercentage($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
      ParadigmCallSpreadPercentage: ParadigmCallSpreadPercentage(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        percentageOfTrades
      }
    }
"""

ParadigmBlockSnifferPutSpreadsasPercentageofTradeCount = """
    query ParadigmPutSpreadPercentage($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
      ParadigmPutSpreadPercentage: ParadigmPutSpreadPercentage(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        percentageOfTrades
      }
    }
"""

ParadigmBlockSnifferSingleLegBlockTrades = """
    query ParadigmSingleTrades($date: String, $symbol: SymbolEnumType) {
      ParadigmSingleTrades: ParadigmSingleTrades(symbol: $symbol, date: $date) {
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
    query ParadigmTiedTrades($date: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      ParadigmTiedTrades: genericTiedUpBlockTrades(symbol: $symbol, date: $date, exchange: $exchange) {
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
      ParadigmVolume: ParadigmVolume(symbol: $symbol, dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd) {
        expiration
        strike
        putCall
        contractVolume
        premiumVolume
      }
    }
"""

TimesandSales = """
    query TimesandSales($date: String, $exchange: ExchangeEnumType) {
      TimesandSales: TimesandSales(date: $date, exchange: $exchange) {
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
        indexPrice
        iv
      }
    }
"""

VolatilityCone = """
    query VolatilityCone($symbol: SymbolEnumType, $date1: String, $date2: String) {
      VolatilityCone: RealizedVolVolatilityCones(symbol: $symbol, beginDate: $date1, endDate: $date2) {
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
    query RealizedVolvsTradeWeightedIV($date1: String, $date2: String, $timeWindow: Float, $beginDate: String, $endDate: String, $rangeStart: Float, $rangeEnd: Float, $deltaRangeStart: Float, $deltaRangeEnd: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      RealizedVolvsTradeWeightedIV: RealizedVolParkinsonCalc(symbol: $symbol, beginDate: $date1, endDate: $date2, timeWindow: $timeWindow) {
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
    query RealizedVolDayofWeek($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      RealizedVolDayofWeek: OrderbookDayOfWeekRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        dowUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

RealizedVolHourofDay = """
    query RealizedVolHourofDay($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      RealizedVolHourofDay: OrderbookHourOfDayRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        hourUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

RealizedVolHourofDayandDayofWeek = """
    query RealizedVolHourofDayandDayofWeek($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType) {
      RealizedVolHourofDayandDayofWeek: OrderbookHourAndDayRv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        dowVal
        dow
        hourUtc
        parkinsonHvPerp
        parkinsonHvIndex
      }
    }
"""

IntradayRealizedVolatility = """
    query IntradayRealizedVolatility($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String, $range1: Float, $range2: Float) {
      IntradayRealizedVolatility: OrderbookIntradayParkinsonHv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, range1: $range1, range2: $range2) {
        ts
        parkinsonHvPerp
        parkisonHvIndex
      }
    }
"""

ClosetoCloseHistoricalVol = """
    query ClosetoCloseHistoricalVol($symbol: String, $dateStart: String, $dateEnd: String) {
      ClosetoCloseHistoricalVol: CloseToCloseHv(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        date
        currency
        close
        yesterdayClose
        vol
      }
    }
"""

RealizedVolParkinson = """
    query RealizedVolParkinson($symbol: String, $dateStart: String, $dateEnd: String, $parkinsonRange: Float) {
      RealizedVolParkinson: RvParkinson(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, parkinsonRange: $parkinsonRange) {
        date
        parkinsonHV
      }
    }
"""

OHLC = """
    query OHLC($symbol: String, $dateStart: String, $dateEnd: String) {
      OHLC: RvOhlc(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
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
    query CoveredCall($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CoveredCall: genericCoveredCall(symbol: $symbol, exchange: $exchange) {
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
    query CashSecuredPuts($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CashSecuredPuts: genericCashSecuredPuts(symbol: $symbol, exchange: $exchange) {
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
    query StraddleRun($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      StraddleRun: genericStraddleRun(symbol: $symbol, exchange: $exchange) {
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
    query GlobalAllOrderBooksOptionPricing {
      GlobalAllOrderBooksOptionPricing: currentOrderbookPricing {
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
    query VolatilitySurfaceDelta($symbol: BTCOrETHEnumType, $date: String) {
      VolatilitySurfaceDelta: HifiVolSurface1DayOf1Min(symbol: $symbol, date: $date) {
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
    query ShadowTermStructureand25Skew($date: String, $symbol: SymbolEnumType) {
      ShadowTermStructureand25Skew: ShadowTimeSkew(date: $date, symbol: $symbol) {
        dateAndHour
        daysUntilExpiration
        atmIv
        twentyThirtyCallIvMinusPutIv
      }
    }
"""

HourlyInstrumentImpliedVolandOI = """
    query HourlyInstrumentImpliedVolandOI($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $strike: String, $putCall: PutCallEnumType, $expiration: String) {
      HourlyInstrumentImpliedVolandOI: InstrumentOiIv1Hr(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, strike: $strike, putCall: $putCall, expiration: $expiration) {
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
    query SpotPrices($symbol: String, $dateStart: String, $dateEnd: String) {
      SpotPrices: SpotPrices(dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol) {
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
    query ConstantMaturitySkew1minutegranularity($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $interval: String) {
      ConstantMaturitySkew1minutegranularity: ConstantMaturitySkew1Min(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, interval: $interval) {
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
    query ConstantMaturityATM1minutegranularity($symbol: BTCOrETHEnumType, $dateStart: String, $dateEnd: String, $interval: String) {
      ConstantMaturityATM1minutegranularity: ConstantMaturityAtm1Min(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd, interval: $interval) {
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
    query CustomMaturityDeltaSurface($symbol: BTCOrETHEnumType, $date: String, $days: Float) {
      CustomMaturityDeltaSurface: CustomMaturityAtmDelta(symbol: $symbol, date: $date, days: $days) {
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
    query Orderbook30dayHourlyBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String) {
      Orderbook30dayHourlyBasis: FuturesCurrentOb30dayHourlyBasisandSpot: genericCurrentOb30dayHourlyBasisandSpot(exchange: $exchange, symbol: $symbol, expiration: $expiration) {
        date
        midPrice
        basis
      }
    }
"""

OrderbookBasisVolumeandOpenInterest = """
    query OrderbookBasisVolumeandOpenInterest($exchange: ExchangeEnumType, $symbol: SymbolEnumType) {
      OrderbookBasisVolumeandOpenInterest: CurrentObBasisVolumeOpenInterests: genericCurrentObBasisVolumeOpenInterest(exchange: $exchange, symbol: $symbol) {
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
    query OrderbookPast1HrBasisandSpot($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String) {
      OrderbookPast1HrBasisandSpot: futuresCurrentObPastBasisAndSpot: genericCurrentObPast1HrBasisAndSpot(exchange: $exchange, symbol: $symbol, expiration: $expiration) {
        date
        price
        expiration
        amount
        annualizedPercentSpread
      }
    }
"""

Orderbook30DayTradeWeightedBasis = """
    query Orderbook30DayTradeWeightedBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $excludeExpiration: Boolean) {
      Orderbook30DayTradeWeightedBasis: Historical30dayTradeWeightedBasis: genericHistorical30DayTradeWeightedBasis(exchange: $exchange, symbol: $symbol, excludeExpiration: $excludeExpiration) {
        date
        instrumentName
        vwapBasis
      }
    }
"""

HistoricalIntradayTradedWeightedBasis = """
    query HistoricalIntradayTradedWeightedBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String, $dateStart: String, $dateEnd: String) {
      HistoricalIntradayTradedWeightedBasis: HistoricalIntraDayTradedBasis: genericHistoricalIntraDayTradedBasis(exchange: $exchange, symbol: $symbol, expiration: $expiration, dateStart: $dateStart, dateEnd: $dateEnd) {
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
    query Basis24HR($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String, $dateStart: String, $dateEnd: String) {
      Basis24HR: genericCurrentOb24HrBasisHistogram(exchange: $exchange, symbol: $symbol, expiration: $expiration, dateStart: $dateStart, dateEnd: $dateEnd) {
        annualizedPercentSpread
        dollarVolume
      }
    }
"""

HifiStrikesVolSurface = """
    query HifiStrikesVolSurface($symbol: BTCOrETHEnumType, $date: String, $interval: String, $exchange: ExchangeEnumType) {
      HifiStrikesVolSurface: HifiStrikesVolSurface(symbol: $symbol, date: $date, interval: $interval, exchange: $exchange) {
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
query HifiVolSurfaceStrikesGreeksMinute($symbol: BTCOrETHEnumType, $dateTime: String,$exchange: ExchangeEnumType){
  HifiVolSurfaceStrikesGreeksMinute: HifiVolSurfaceStrikesGreeksMinute(symbol: $symbol, dateTime: $dateTime, exchange:$exchange) {
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
query HifiVolSurfaceStrikesGreeksHourly($symbol: BTCOrETHEnumType, $date: String, $interval:String, $exchange: ExchangeEnumType){
  HifiVolSurfaceStrikesGreeksHourly: HifiVolSurfaceStrikesGreeksHourly(symbol: $symbol, date: $date, interval: $interval, exchange:$exchange) {
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
query dvolVariancePremium($symbol: SymbolEnumType) {
		dvolVariancePremium: dvolVariancePremium(symbol: $symbol) {
			dvolImpliedRvDate
			instrument
			dvolOpen30Days
			parkinsonHv
			variancePremium
		}
	}
"""


UtilityRealtimeOptionbook = """	
query UtilityRealtimeOptionbook($exchange: ExchangeEnumType) {
		UtilityRealtimeOptionbook: genericUtilityRealtimeOptionbook(exchange: $exchange) {
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

# Starting here.
SpotPricesLite = """
query SpotPricesLite( $symbol:SymbolEnumType){
  SpotPricesLite: SpotPricesLite(symbol: $symbol) {
    date
    currency
    open
    high
    low
    close
  } 
}
"""

FixedMaturityAtm = """
query FixedMaturityAtm($exchange: ExchangeEnumType, $symbol:BTCOrETHEnumType){
  FixedMaturityAtm: FixedMaturityAtm(exchange:$exchange, symbol: $symbol) {
    date
    atm7
    atm30
    atm60
    atm90
    atm180
    currency
  }
}
"""


FixedMaturitySkewLite = """
query FixedMaturitySkewLite($exchange: ExchangeEnumType, $symbol:BTCOrETHEnumType){
  FixedMaturitySkewLite: FixedMaturitySkewLite(exchange:$exchange, symbol: $symbol) {
    date
    currency
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

TwentyFourHourTradesLite = """
query TwentyFourHourTradesLite($exchange: ExchangeEnumType, $symbol: SymbolEnumType) {
		TwentyFourHourTradesLite: TwentyFourHourTradesLite(exchange: $exchange, symbol: $symbol) {
		date
    exchange
    tradeId
    blockId
    block
    amount
    optionCoinPrice
    optionUsdPrice
    indexPrice
    instrumentName
    baseCurrency
    expiratioin
    putcall
    notional
    liquidation
		}
	}
"""

ParkinsonComboVolatilityLite = """
query ParkinsonComboVolatilityLite( $symbol:SymbolEnumType){
  ParkinsonComboVolatilityLite: ParkinsonComboVolatilityLite(symbol: $symbol) {
    date
    parkinsonHV10
    parkinsonHV30
    parkinsonHV90
    parkinsonHV190
    parkinsonHV365
  } 
}
"""

RealizedVolConeLite = """
query RealizedVolConeLite( $symbol:SymbolEnumType){
  RealizedVolConeLite: RealizedVolConeLite(symbol: $symbol) {
    measurement
    current
    max
    p75
    p50
    p25
    min
  } 
}
"""

UtilityRealtimeFuturesPrices = """
query UtilityRealtimeFuturesPrices($exchange: ExchangeEnumType){
	UtilityRealtimeFuturesPrices: UtilityRealtimeFuturesPrices(exchange: $exchange) {
    date
    instrumentName
    expiration
    openInterest
    volume24Hr
    bestBidAmount
    bestBidPrice
    markPrice
    indexPrice
    bestAskPrice
    bestAskAmount
    currentFunding
  }
}

"""

BasisTradedLite = """
query BasisTradedLite($exchange: ExchangeEnumType, $symbol: BTCOrETHEnumType){
	BasisTradedLite: BasisTradedLite(exchange: $exchange, symbol: $symbol) {
    date
    tradeSequence
    instrumentName
    baseCurrency
    expiration
    timeleft
    amount
    indexPrice
    price
    basis
  }
}
"""


CurrentObBasisVolumeOpenInterests = """
	query CurrentObBasisVolumeOpenInterests($exchange: ExchangeEnumType, $symbol: SymbolEnumType) {
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

DeribitFunding = """
	query DeribitFunding{
	  DeribitFunding: DeribitFunding{
                date
                instrumentName
                markPrice
                indexPrice
                currentFunding
                funding8h
            }
	}
"""

ConstantBasisSevenDayOneHour = """
query ConstantBasisSevenDayOneHour($exchange: ExchangeEnumType, $symbol:BTCOrETHEnumType){
  ConstantBasisSevenDayOneHour: ConstantBasisSevenDayOneHour(exchange:$exchange, symbol: $symbol) {
    date
    y30
    y60
    y90
    currency
  }
}
"""

DydxFunding = """
query DydxFunding{
	  DydxFunding: DydxFunding{
            date
            market
            id
            rate
            price
            effectiveAt
            }
	}
"""

ZetaOrderbookLite = """
query ZetaOrderbookLite{
	ZetaOrderbookLite: ZetaOrderbookLite {
    instrumentName
    date
    currency
    expiration
    strike
    putcall
    distinctBidWallets
    bidDepth
    bestAskAmount
    bestBidPrice
    bidIv
    markPrice
    markIv
    askIv
    bestAskPrice
    askDepth
    distinctAskWallets
    isATM
    oraclePrice
  }
	}
"""

RibbonTimeAndSales = """
	query RibbonTimeAndSales {
		RibbonTimeAndSales: RibbonTimeAndSales {
		    date
            expiration
            defi
            underlying
            strike
            putCall
            direction
            volume
            coinPremium
            notional
		}
	}
"""
