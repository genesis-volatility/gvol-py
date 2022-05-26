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

LiveOiGlobalApi = """
    query LiveOiGlobalApi($symbol: BTCOrETHEnumType) {
      LiveOiGlobalApi: LiveOiGlobalApi(symbol: $symbol) {
        currency
        putCall
        openInterest1xMult
        notionalOpenInterest
        expiration
        exchange
        strike
      }
    }
"""

LiveOiByPutCallApi = """
query LiveOiByPutCallApi($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
		LiveOiByPutCallApi: LiveOiGlobalApi(symbol: $symbol, exchange: $exchange) {
      currency
      putCall
      openInterest1xMult
      notionalOpenInterest
    }
}
"""

LiveOiByStrikeApi = """
query LiveOiByStrikeApi($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
		LiveOiByStrikeApi: LiveOiByStrikeApi(symbol: $symbol, exchange: $exchange) {
      currency
      putCall
      openInterest1xMult
      notionalOpenInterest
      strike		
    }
}
"""

LiveOiByExpirationApi = """
query LiveOiByExpirationApi($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
		LiveOiByExpirationApi: LiveOiByExpirationApi(symbol: $symbol, exchange: $exchange) {
      currency
      putCall
      openInterest1xMult
      notionalOpenInterest
      expiration
		}
	}
"""

TableTurnoverLite = """
query TableTurnoverLite($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
	    TableTurnoverLite: TableTurnoverLite(symbol: $symbol, exchange: $exchange) {
			  date
        instrumentName
        currency
        expiration
        putCall
        strike
        openInterest
        volume
        notional
        turnover
		}
	}
"""

TableTurnoverCurrencyWithPc7DayLite = """
query TableTurnoverCurrencyWithPc7DayLite( $symbol: SymbolEnumType, $exchange: ExchangeEnumType ) {
	    TableTurnoverCurrencyWithPc7DayLite: TableTurnoverCurrencyWithPc7DayLite(symbol: $symbol, exchange: $exchange) {
        currency
        putCall
        openInterest
        openInterest7DayAverage
        oiRatio
        volume24h
        volumeRatio
        volume7DayAverage
        notionalRatio 
        notional7DayAverage
        notional24h
        turnover
        turnover7DayAverage
		}
	}
"""


ChangeOiPutCallAggApi = """
query ChangeOiPutCallAggApi($symbol: SymbolEnumType, $startDate: String, $endDate: String, $exchange: ExchangeEnumType){
      ChangeOiPutCallAggApi: ChangeOiPutCallAggApi(symbol:$symbol, startDate:$startDate, endDate:$endDate, exchange: $exchange){
        endDate
        putCall
        startOpenInterest
        endOpenInterest
        openInterestChange
        expired
        totalGrowth
  }
}
"""

ChangeOiStrikeAggApi = """
query ChangeOiStrikeAggApi($symbol: SymbolEnumType, $startDate: String, $endDate: String, $exchange: ExchangeEnumType){
      ChangeOiStrikeAggApi: ChangeOiStrikeAggApi(symbol:$symbol, startDate:$startDate, endDate:$endDate, exchange: $exchange){
        endDate
        putCall
        strike
        startOpenInterest
        endOpenInterest
        openInterestChange
        expired
        totalGrowth
  }
}
"""

ChangeOiStrikePricePcExpApi = """
query ChangeOiStrikePricePcExpApi($symbol: SymbolEnumType, $startDate: String, $endDate: String, $exchange: ExchangeEnumType){
      ChangeOiStrikePricePcExpApi: ChangeOiStrikePricePcExpApi(symbol:$symbol, startDate:$startDate, endDate:$endDate, exchange: $exchange){
        endDate
        putCall
        strike
        startOpenInterest
        endOpenInterest
        openInterestChange
        expiration
  }
}
"""

TurnoverTimeSeriesLite = """
query TurnoverTimeSeriesLite($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String ) {
	    TurnoverTimeSeriesLite: TurnoverTimeSeriesLite(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
        date
			  currency
        putCall
        openInterest
        volume24h
        notional24h
        turnover
        indexPrice
		}
	}
"""


VolumesIntradayPutCallQuery = """
query VolumesIntradayPutCallQuery($dateStart: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType, $granularity: String) {
		  VolumesIntradayPutCall: VolumesIntradayPutCall(dateStart: $dateStart, symbol: $symbol, exchange: $exchange, granularity: $granularity ) {
        date
        putCall
        exchange
        notional
        indexAvg
        }
	}
"""

VolumesIntradayStrikePutCallQuery = """
query VolumesIntradayStrikePutCallQuery($dateStart: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType, $granularity: String) {
		  VolumesIntradayStrikePutCall: VolumesIntradayStrikePutCall(dateStart: $dateStart, symbol: $symbol, exchange: $exchange, granularity: $granularity ) {
        date
        strike
        putCall
        exchange
        notional
        indexAvg
      }
	}
"""

VolumesIntradayExpirationPutCallQuery = """
query VolumesIntradayExpirationPutCallQuery($dateStart: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType, $granularity: String) {
		  VolumesIntradayExpirationPutCall: VolumesIntradayExpirationPutCall(dateStart: $dateStart, symbol: $symbol, exchange: $exchange, granularity: $granularity ) {
          date
          expiration
          putCall
          exchange
          notional
          indexAvg
        }
	}
"""

VolumesMonthlyQuery = """
query VolumesMonthlyQuery($dateStart: String, $dateEnd: String, $symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
		  VolumesMonthlyQuery: VolumesMonthly( dateStart: $dateStart, dateEnd: $dateEnd, symbol: $symbol, exchange: $exchange) {
        date
        putCall
        exchange
        expiration
        strike
        notional
        indexAvg
   }  
	}
"""

TurnoverBtcEthComparisonLite = """
query TurnoverBtcEthComparisonLite( $dateStart: String, $dateEnd: String ) {
	    TurnoverBtcEthComparisonLite: TurnoverBtcEthComparisonLite(dateStart: $dateStart, dateEnd: $dateEnd) {
			    date
          ratioOpenInterest
          btcNotionalOpenInterest
          ethNotionalOpenInterest
          btcNotional24h
          ethNotional24h
          btcIndexPrice
          ethIndexPrice
          ratioNotional24h
		}
	}
"""

HistoricalContractsTradedAndPremiumVolume = """
query HistoricalContractsTradedAndPremiumVolume(
				$date1: String
				$date2: String
				$rangeStart: Float
				$rangeEnd: Float
				$direction1: String
				$direction2: String
				$symbol: SymbolEnumType
				$exchange: ExchangeEnumType
			) {
				HistoricalContractsTradedAndPremiumVolume: genericHistoricalContractsTradedAndPremiumDollarVolume(
					symbol: $symbol
					beginDate: $date1
					endDate: $date2
					rangeStart: $rangeStart
					rangeEnd: $rangeEnd
					direction1: $direction1
					direction2: $direction2
					exchange: $exchange
				) {
					date
					contractsTraded
					contractsBlockTraded
					premiumValue
					premiumBlockTraded
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

dvolSpotVolData = """
query dvolSpotVolData($symbol: SymbolEnumType, $days: DaysBackEnumType) {
		dvolSpotVolData: dvolSpotVolData(symbol: $symbol, days: $days) {
			date
			coin_close
			dvol_open
			dvol_high
			dvol_low
			dvol_close
		}
	}
"""

dVolVolOfVol = """
query dVolVolOfVol($symbol: SymbolEnumType, $days: DaysBackEnumType) {
	  	dVolVolOfVol: dvolVolOfVolData(symbol: $symbol, days: $days) {
        date
        volOfVol
        open
        high
        low
        close
		}
	}
"""

TimesAndSales = """
query TimesAndSales($exchange: ExchangeEnumType $date: String) {
		TimesAndSales: TimesAndSales( exchange: $exchange date: $date) {
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

ParadigmApiTradeTypeDistribution = """
query ParadigmApiTradeTypeDistribution($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType) {
		ParadigmApiTradeTypeDistribution: ParadigmApiTradeTypeDistribution(
			symbol: $symbol
			dateRangeStart: $dateRangeStart
			dateRangeEnd: $dateRangeEnd
		) {
			description
			tradeCount
			venue
		}
	}
"""

ParadigmApiTradeTimeSeries = """
query ParadigmApiTradeTimeSeries($dateRangeStart: String, $dateRangeEnd: String, $symbol: SymbolEnumType){
      ParadigmApiTradeTimeSeries: ParadigmApiTradeTimeSeries(dateRangeStart: $dateRangeStart, dateRangeEnd: $dateRangeEnd, symbol: $symbol){
        date
        description
        blockTradeId
        instrumentName
        direction
        indexPrice
        volume
        iv
        optionPrice
  }
}
"""


MarketCaps = """
query MarketCaps {
		MarketCaps: MarketCaps {
			currency
      price
      marketCapMillions
		}
	}
"""

RealizedC2cAltcoin5Day = """
query RealizedC2cAltcoin5Day($symbol: SymbolEnumType) {
		RealizedC2cAltcoin5Day: RealizedC2cAltcoin5Day(symbol: $symbol) {
		    date
        currency
        close
        annualizedRv
		}
	}
"""

RealizedC2cAltcoin10Day = """
query RealizedC2cAltcoin10Day($symbol: SymbolEnumType) {
		RealizedC2cAltcoin10Day: RealizedC2cAltcoin10Day(symbol: $symbol) {
		    date
        currency
        close
        annualizedRv
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

CobIvRvComparison = """
query CobIvRvComparison($symbol: BTCOrETHEnumType, $interval: Float, $rangeStart: String, $rangeEnd: String){
  CobIvRvComparison: CobIvRvComparison(symbol: $symbol, interval: $interval, rangeStart: $rangeStart, rangeEnd: $rangeEnd){
   date
   parkinsonRvIndex
   atm7
   atm30
   atm60
   atm90
   atm180
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

PortfolioAnalyzer = """
  query PortfolioAnalyzer($portfolio: [CreatePortfolioInput], $deltaFutures: Float, $numberOfDays:Float, $ivShift:Float, $symbol:BTCOrETHEnumType){
    PortfolioAnalyzer: PortfolioAnalyzer(portfolio:$portfolio, deltaFutures:$deltaFutures,numberOfDays:$numberOfDays, ivShift:$ivShift, symbol:$symbol){
      PnL
      PnLUSD
      deltaBSM
      deltaCash
      deltaSkew
      gamma
      vega
      vegaNorm30
      theta
      index
      equity
      equityUSD
      days
    }
  }
"""

FittedCurves = """
query FittedCurves($symbol: BTCOrETHEnumType){
  FittedCurves: FittedCurves(symbol:$symbol) {
    expiration
    strike
    markIv
    putCall
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

GlobalQuery = """
query GlobalQuery($symbol: BTCOrETHEnumType, $date: String) {
		GlobalQuery: GlobalSpotPutCallOi(symbol: $symbol, date: $date) {
			date
			open
			high
			closed
			low
			deribitContracts
			bitcomContracts
			okexContracts
			ledgerxContracts
			deribitNotional
			bitcomNotional
			okexNotional
			ledgerxNotional
			deribitPutCallRatio
			bitcomPutCallRatio
			okexPutCallRatio
			ledgerxPutCallRatio
			globalPutCallRatio
		}
	}
"""

DovsCharts = """
query DovsCharts {
		DovsCharts: DovsCharts {
			defi
      currency
      putCall
      strikeMoneyness
      price
      notionalSold
		}
	}
"""

Dovs = """
query Dovs {
      Dovs: Dovs {
              defi
              instrumentName
              currency
              expiration
              strike
              putCall
              usdOptionPremium
              auctionWindowAveragePrice
              volume
              notional
              deposits
              coinPremium
              absReturn
              apy
              iv
              deposits
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

TablePerpsLive = """
query TablePerpsLive($exchange: ExchangeEnumType) {
		TablePerpsLive: TablePerpsLive(exchange: $exchange) {
			    date
          instrumentName
          margin
          indexPrice
          markPrice
          percentChange24h
          apyChange24h
          funding8h
          apy
          nextFunding
          volume24h
          volumeChange24h
          usdOi
          usdOi24hChange
          oiPercentChange24h
          turnover
		}
	}
"""

TableClickForDetailsDydx = """
query TableClickForDetailsDydx(
		$instrumentName: String, $rangeStart: String, $rangeEnd: String) {
		TableClickForDetailsDydx: TableClickForDetailsDydx(instrumentName: $instrumentName, rangeStart: $rangeStart, rangeEnd: $rangeEnd) {
			    date
          openInterest
          volume24h
          markPrice
          indexPrice
          turnover
          apy
          funding8h
          nextFunding
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

DailyBasisVwap = """
	query DailyBasisVwap($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String) {
        DailyBasisVwap: DailyBasisVwap(symbol: $symbol, dateRangeStart: $dateStart,	dateRangeEnd: $dateEnd) {
          date
          vwapBasis
          instrumentName
          baseCurrency
          expiration
		}
	}
"""

TradesWithBasis = """
query TradesWithBasis($symbol: SymbolEnumType, $date: String) {
		TradesWithBasis: TradesWithBasis(symbol: $symbol,	date: $date) {
			date
      amount
      indexPrice
      price
      basis
      instrumentName
      baseCurrency
      expiration
		}
	}
"""

DeribitFundingPerp = """
query DeribitFundingPerp($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String) {
		DeribitFundingPerp: DeribitFundingPerp(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
			date
			indexPrice
			currentFundingPercent
			tradableBboPremiumDiscount
		}
	}
"""

PremiaCumulativeVolumeByNetwork = """
query PremiaCumulativeVolumeByNetwork($dateStart: String, $dateEnd: String) {
			PremiaCumulativeVolumeByNetwork: PremiaCumulativeVolumeByNetwork(dateStart: $dateStart, dateEnd:$dateEnd) {
          date
          network
          cumulativeNotional
				}
			}
"""

PremiaCumulativeVolumeByNetwork = """
	query PremiaCumulativeVolumeByNetwork($dateStart: String, $dateEnd: String) {
				PremiaCumulativeVolumeByNetwork: PremiaCumulativeVolumeByNetwork(dateStart: $dateStart, dateEnd:$dateEnd) {
            date
            network
            cumulativeNotional
				}
			}
"""

PremiaCumulativeVolumeByPutCall = """
	query PremiaCumulativeVolumeByPutCall($dateStart: String, $dateEnd: String) {
				PremiaCumulativeVolumeByPutCall: PremiaCumulativeVolumeByPutCall(dateStart: $dateStart, dateEnd:$dateEnd) {
            date
            putcall
            cumulativeNotional
				}
			}
"""

PremiaTotalDailyVolumeAndCumulative = """
	query PremiaTotalDailyVolumeAndCumulative($dateStart: String, $dateEnd: String) {
				PremiaTotalDailyVolumeAndCumulative: PremiaTotalDailyVolumeAndCumulative(dateStart: $dateStart, dateEnd:$dateEnd) {
            date
            dailyNotionalVolume
            cumulativeNotional
				}
			}
"""

PremiaCumulativeVolumeByPool = """
query PremiaCumulativeVolumeByPool($dateStart: String, $dateEnd: String, $currency: String, $network: String, $putCall: PutCallEnumType) {
				PremiaCumulativeVolumeByPool: PremiaCumulativeVolumeByPool(dateStart: $dateStart, dateEnd:$dateEnd, currency: $currency,network: $network, putCall: $putCall) {
            date
            cumulativeNotional
				}
			}
"""

PremiaTotalValueLockedNetwork = """
	query PremiaTotalValueLockedNetwork($dateStart: String, $dateEnd: String) {
				PremiaTotalValueLockedNetwork: PremiaTotalValueLockedNetwork(dateStart: $dateStart, dateEnd:$dateEnd) {
            date
            network
            tvlUsd
				}
			}
"""

PremiaTotalValueLockedPool = """
query PremiaTotalValueLockedPool($dateStart: String, $dateEnd: String, $currency: String, $network: String, $putCall: PutCallEnumType) {
				PremiaTotalValueLockedPool: PremiaTotalValueLockedPool(dateStart: $dateStart, dateEnd:$dateEnd, currency: $currency,network: $network, putCall: $putCall) {
          date
          network
          tvlUsd
				}
			}
"""

PremiaLiveOptionTvl = """
	query PremiaLiveOptionTvl{
				PremiaLiveOptionTvl: PremiaLiveOptionTvl{
           tvlUsd
			}
    }
"""

PremiaTransactionsByPool = """
query PremiaTransactionsByPool($dateStart: String, $dateEnd: String, $currency: String, $network: String,$putCall: PutCallEnumType) {
			PremiaTransactionsByPool: PremiaTransactionsByPool(dateStart: $dateStart, dateEnd:$dateEnd, currency: $currency,network: $network, putCall: $putCall) {
          date
          instrument
          activity
          amount
          notional
          initiatingWallet
				}
			}
"""

PremiaLiveOiAllOptionsWithGreeks = """
query PremiaLiveOiAllOptionsWithGreeks($currency: String, $network: String, $putCall: PutCallEnumType) {
			PremiaLiveOiAllOptionsWithGreeks: PremiaLiveOiAllOptionsWithGreeks( currency: $currency,network: $network, putCall: $putCall) {
          instrument
          oi
          iv
          delta
          theta
          gamma
          vega
          totalHolders
          priceUsd
          priceUsd24hrAgo
          percentage24hrChange
				}
			}
"""

PremiaLiveOptionOiCurrency = """
	query PremiaLiveOptionOiCurrency{
				PremiaLiveOptionOiCurrency: PremiaLiveOptionOiCurrency{
              currency
              notionalOiInMillions
				}
			}
"""

PremiaLiveOptionOiExpiration = """
	query PremiaLiveOptionOiExpiration{
				PremiaLiveOptionOiExpiration: PremiaLiveOptionOiExpiration{
              expiration
              notionalOiInMillions
				}
			}
"""

PremiaLiveOptionOiNetwork = """
	query PremiaLiveOptionOiNetwork{
				PremiaLiveOptionOiNetwork: PremiaLiveOptionOiNetwork{
          network
          notionalOiInMillions
				}
			}
"""

PremiaLiveOptionOiPutCall = """
	query PremiaLiveOptionOiPutCall{
				PremiaLiveOptionOiPutCall: PremiaLiveOptionOiPutCall{
          putcall
          notionalOiInMillions
				}
			}
"""

PremiaLiveOptionOiStrikePutCall = """
	query PremiaLiveOptionOiStrikePutCall($symbol: String){
				PremiaLiveOptionOiStrikePutCall: PremiaLiveOptionOiStrikePutCall(symbol: $symbol){
          putcall
          strike
          notionalOiInMillions
				}
			}
"""

GreeksPricingTable = """
query GreeksPricingTable {
				GreeksPricingTable: GreeksPricingTable {
					instrumentName
					contractType
					expiration
					last
					change1h
					change24h
					volume
					iv
					markPrice
					openInterest
					indexPrice
					strikePrice
					delta
					gamma
					theta
					vega
				}
			}
"""

TimeSeriesOfGreeks = """
query TimeSeriesOfGreeks($instrumentName: String) {
				TimeSeriesOfGreeks: TimeSeriesOfGreeks(instrumentName: $instrumentName) {
					date
					iv
					markPrice
					delta
					gamma
					theta
					vega
				}
			}
"""

LiveSqueethStats = """
query LiveSqueethStats {
				LiveSqueethStats: LiveSqueethStats {
					date
          iv
          markPrice
          delta
          gamma
          theta
          vega
          eth2Index
          ethUsd
          nextFunding
          normFactor
          nextNormFactor
          oSqueeth
          oSqueethOi
          volumeUsd
          volume
				}
			}
"""

HistoricalOsqthIvFundingIndexMark = """
query HistoricalOsqthIvFundingIndexMark($dateStart: String, $dateEnd: String) {
				HistoricalOsqthIvFundingIndexMark: HistoricalOsqthIvFundingIndexMark(dateStart: $dateStart, dateEnd: $dateEnd) {
					date
					iv
					markPrice
					eth2Index
					ethUsd
					oSqueeth
					dailyFunding
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

# API LITE SPECIFIC APIs

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


# END
# #END


# OLD QUERIES/APIs

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
