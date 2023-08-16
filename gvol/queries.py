options_orderbook = """
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

options_termstructure = """
    query CurrentOrderbookTermStructure($symbol: SymbolEnumType, $exchange: ExchangeEnumType) {
      CurrentOrderbookTermStructure: genericOrderbookTermStructure(symbol: $symbol, exchange: $exchange) {
        expiration
        markIv
        forwardVolatility
      }
    }
"""

options_termstructure_hist = """
    query TermStructureShadowQuery($symbol: SymbolEnumType, $dateTime: String, $exchange: ExchangeEnumType) {
          genericShadowTermStructureV2(exchange: $exchange, symbol: $symbol, dateTime: $dateTime) {
          currency
          date
          expiration
          dte
          markIv
        } 
    }
"""

options_termstructure_comparison = """
    query TermStructureShadowQuery($symbol: SymbolEnumType, $dateTimeOne: String, $dateTimeTwo: String, $exchange: ExchangeEnumType) {
          genericShadowTermStructureCompareV2(exchange: $exchange, symbol: $symbol, dateTimeOne: $dateTimeOne, dateTimeTwo: $dateTimeTwo) {
          days1
          date1
          expiration1
          markIv1
          days2
          date2
          expiration2
          markIv2
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
  query TurnoverBtcEthComparisonLite( $dateStart: String, $dateEnd: String ){
        TurnoverBtcEthComparisonLite: TurnoverBtcEthComparisonLite(dateStart: $dateStart, dateEnd: $dateEnd){
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

options_dvol_index = """
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

options_trades = """
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

options_trades_orderbook_details = """
  query TimesAndSalesWithOrderbookDetails($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $dateStart: String, $dateEnd: String){
    TimesAndSalesWithOrderbookDetails :genericTimesAndSalesWithOrderbookDetails(exchange:$exchange, symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd) {
      preTxObTs
      txTs
      postTxObTs
      tradeSeq
      tradeId
      instrumentName
      currency
      expiration
      strike
      putcall
      blockTradeId
      liquidation
      direction
      tickDirection
      txAmount
      txIv
      price
      priceUsd
      indexPrice
      underlyingPrice
      volume24h
      high24h
      low24h
      preTxBbSize
      preTxBbPrice
      preTxBbIv
      preTxMidIv
      preTxMidPrice
      preTxMarkIv
      preTxMarkPrice
      preTxBaIv
      preTxBaPrice
      preTxBaSize
      postTxBbSize
      postTxBbPrice
      postTxBbIv
      postTxMidIv
      postTxMidPrice
      postTxMarkIv
      postTxMarkPrice
      postTxBaIv
      postTxBaPrice
      postTxBaSize
      delta
      gamma
      theta
      vega
      rho
      preTxOi
      postTxOi
      oiChange
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

options_orderbook_details = """	
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


portfolio_analyzer = """
  query PortfolioAnalyzer($portfolio: [CreatePortfolioInput], $deltaFutures: Float,	$ivShift:Float,	$symbol:BTCOrETHEnumType){
    PortfolioAnalyzer: PortfolioAnalyzer(portfolio:$portfolio, deltaFutures:$deltaFutures,ivShift:$ivShift, symbol:$symbol){
          indexChange
          PnL
          PnLUSD
          deltaBSM
          deltaCash
          deltaSkew
          gamma
          vega
          wVega
          theta
          index
          equity
          equityUSD
          days
    }
  }
"""

options_fitted_curves = """
  query FittedCurves($symbol: BTCOrETHEnumType){
    FittedCurves: FittedCurves(symbol:$symbol) {
      expiration
      strike
      markIv
      putCall
    }
  }
"""

options_greeks_hour = """
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

options_volatility_surface = """
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

options_greeks_minute = """
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

spot_prices = """
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

options_skew_constant = """
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

options_atm_constant = """
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

defi_dovs_table = """
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

futures_basis_hist = """
    query HistoricalIntradayTradedWeightedBasis($exchange: ExchangeEnumType, $symbol: SymbolEnumType, $expiration: String, $dateStart: String, $dateEnd: String) {
      HistoricalIntradayTradedWeightedBasis: genericHistoricalIntraDayTradedBasis(exchange: $exchange, symbol: $symbol, expiration: $expiration, dateStart: $dateStart, dateEnd: $dateEnd) {
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

futures_perps_table = """
  query TablePerps($exchange:ExchangeEnumType){
    TablePerps:genericLiveTablePerps(exchange:$exchange) {
      mcapMils
      instrumentName
      currency
      margin
      expiration
      price
      indexPrice
      priceChange24
      apy
      funding
      oiUsdMillions
      volume24UsdMillions
      volumer2Oi
      lsRatio
      hv5
      hv10
      hv14
      hv30
      hv60
      hv90
      hv180
    }
  }
"""

futures_futs_table = """
  query TableFutures($exchange:ExchangeEnumType){
    TableFutures:genericLiveTableFutures(exchange:$exchange) {
      mcapMils
      instrumentName
      currency
      margin
      expiration
      price
      indexPrice
      priceChange24
      apy
      funding
      oiUsdMillions
      volume24UsdMillions
      volumer2Oi
      lsRatio
      hv5
      hv10
      hv14
      hv30
      hv60
      hv90
      hv180
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

defi_ribbon_trades = """
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

spot_prices_lite = """
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

options_atm_constant_lite = """
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

options_skew_constant_lite = """
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

futures_orderbook = """
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


defi_zeta_orderbook = """
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

options_gvol_direction = """
  query GvolDirection($dateStart: String, $dateEnd:String, $symbol:SymbolEnumType){
        GvolDirection: GvolDirection(dateStart:$dateStart, dateEnd: $dateEnd, symbol: $symbol) {
          preTxOrderbookTimestamp
          txTimestamp
          postTxOrderbookTimestamp
          tradeSeq
          tradeId
          instrumentName
          currency
          expiration
          strike
          putCall
          blockTradeId
          nrLegs
          liquidation
          tickDirection
          txAmount
          txIv
          price
          priceUsd
          indexPrice
          underlyingPrice
          volume24h
          high24h
          low24h
          preTxBbSize
          preTxBbIv
          preTxMidIv
          preTxMidPrice
          preTxMarkIv
          preTxMarkPrice
          preTxBaIv
          preTxBaPrice
          preTxBaSize
          postTxBbSize
          postTxBbPrice
          postTxBbIv
          postTxMidIv
          postTxMidPrice
          postTxMarkIv
          postTxMarkPrice
          postTxBaIv
          postTxBaPrice
          postTxBaSize
          delta
          gamma
          theta
          vega
          rho
          preTxOi
          postTxOi
          oiChange
          deribitDirection
          gvolDirection
        }
}
"""

options_gvol_gex = """
  query GammaLevelsExpiration($symbol:BTCOrETHEnumType, $date:String){
        GammaLevelsExpiration: GammaLevelsExpiration(symbol:$symbol, date:$date) {
          currency
          date
          expiration
          strike
          gammaLevel
          dealerTotInventory
          dealerNetInventory
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

futures_constant_basis = """
	query BasisFixedRevised($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String, $exchange: ExchangeEnumType) {  
    BasisFixedRevised: BasisFixedRevised(symbol: $symbol, dateStart:$dateStart,dateEnd:$dateEnd, exchange: $exchange) {
      ts
      currency
      indexPrice
      b30
      b60
      b90
      b120        
    }
  }
  """


options_atm_skew_spot = """
  query HourlyFixedDeltaSurface($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String) {  
    HourlyFixedDeltaSurface: HourlyFixedDeltaSurface(symbol: $symbol, dateStart:$dateStart,dateEnd:$dateEnd) {
      ts
      currency
      indexPrice
      atm7
      atm30
      atm60
      atm90
      atm180
      ThirtyFiveDelta7Put
      ThirtyFiveDelta7Call
      TwentyFiveDelta7Put
      TwentyFiveDelta7Call
      FifteenDelta7Put
      FifteenDelta7Call
      FiveDelta7Put
      FiveDelta7Call
      ThirtyFiveDelta30Put
      ThirtyFiveDelta30Call
      TwentyFiveDelta30Put
      TwentyFiveDelta30Call
      FifteenDelta30Put
      FifteenDelta30Call
      FiveDelta30Put
      FiveDelta30Call
      ThirtyFiveDelta60Put
      ThirtyFiveDelta60Call
      TwentyFiveDelta60Put
      TwentyFiveDelta60Call
      FifteenDelta60Put
      FifteenDelta60Call
      FiveDelta60Put
      FiveDelta60Call
      ThirtyFiveDelta90Put
      ThirtyFiveDelta90Call
      TwentyFiveDelta90Put
      TwentyFiveDelta90Call
      FifteenDelta90Put
      FifteenDelta90Call
      FiveDelta90Put
      FiveDelta90Call
      ThirtyFiveDelta180Put
      ThirtyFiveDelta180Call
      TwentyFiveDelta180Put
      TwentyFiveDelta180Call
      FifteenDelta180Put
      FifteenDelta180Call
      FiveDelta180Put
      FiveDelta180Call
    }
  }
"""


options_deribit_volume_detailed_daily = """
  query DeribitDetailedDaily($exchange: ExchangeEnumType, $dateStart: String,$dateEnd: String) {  
    DeribitDetailedDaily: DeribitDetailedDaily(exchange: $exchange, dateStart: $dateStart, dateEnd: $dateEnd) {
      date
      year
      month
      blockTrade
      currency
      typeOfTrade
      putCall
      volume
      premium
      notional
      premiumDollar
      avgIv
      avgIndexPrice
      countTrades
      oiNotional
      oiPcRatio
    }
  }
"""

options_cumulative_net_volumes = """
query NetVolumeGvolDirection($tradeType: TradeEnumType, $days: Float, $symbol: SymbolEnumType, $exchange: ExchangeEnumType, $showActiveExpirations: Boolean)
{genericNetVolumeGvolDirection(symbol: $symbol, tradeType: $tradeType, days: $days, exchange: $exchange, showActiveExpirations: $showActiveExpirations) 
{date strike cumulative indexPrice}}
"""

options_cumulative_net_volumes_hist = """
query HistoricalNetVolumeApi($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String $exchange: ExchangeEnumType, $tradeType: TradeEnumType, $showActiveExpirations: Boolean)
{ HistoricalNetVolumeApi(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd exchange: $exchange, tradeType: $tradeType, showActiveExpirations: $showActiveExpirations)
{date strike cumulative cumulativeGamma cumulativeVega cumulativeDelta indexPrice } }
"""

options_cumulative_net_positioning = """
query NetPositioning( $symbol: SymbolEnumType, $exchange: ExchangeEnumType, $dateStart: String) 
{genericNetPositioningGvolDirection(symbol: $symbol, exchange: $exchange, dateStart: $dateStart) 
{ date
   strike
   netInv
   indexPrice}}
"""

options_cumulative_net_positioning_hist = """
query HistoricalNetPositioningApi($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String $exchange: ExchangeEnumType)
{HistoricalNetPositioningApi(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd exchange: $exchange) 
{date strike netInv indexPrice } }
"""

options_iv_rv_comparison = """
query IvRvComparison($symbol: SymbolEnumType, $exchange: ExchangeEnumType, $dateStart: String, $dateEnd: String) 
{IvRvComparison(symbol: $symbol, exchange: $exchange dateStart: $dateStart dateEnd: $dateEnd) 
{ date parkinsonRvIndex atm7 atm30 atm60 atm90 atm180 } }
"""

options_butterfly_constant_maturities = """
query HistoricalConstantMaturitiesApi($symbol: SymbolEnumType, $dateStart: String, $dateEnd: String $exchange: ExchangeEnumType){ HistoricalConstantMaturitiesApi(symbol: $symbol, dateStart: $dateStart, dateEnd: $dateEnd exchange: $exchange) {  
        date
        fly05D7Day
        fly05D30Day
        fly05D60Day
        fly05D90Day
        fly05D180Day
        fly15D7Day
        fly15D30Day
        fly15D60Day
        fly15D90Day
        fly15D180Day
        fly25D7Day
        fly25D30Day
        fly25D60Day
        fly25D90Day
        fly25D180Day
        fly35D7Day
        fly35D30Day
        fly35D60Day
        fly35D90Day
        fly35D180Day
 } }
"""

options_term_structure_richness = """
query genericTermStructureRichness($symbol: SymbolEnumType, $exchange: ExchangeEnumType, $dateStart: String, $dateEnd: String) {
  genericTermStructureRichness: genericTermStructureRichness(symbol: $symbol, exchange: $exchange, dateStart: $dateStart, dateEnd: $dateEnd) {
    timeBucket
    atm7
    atm30
    atm60
    atm90
    atm180
    ratio
    counter
    termStructureRichness
  }
}
"""
