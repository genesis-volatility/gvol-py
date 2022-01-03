import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

BTCOrETHEnumType = Literal["BCH", "BTC", "ETH"]
BlockEnumType = Literal["any", "block", "nonBlock"]
Boolean = bool
DaysBackEnumType = Literal["NINETY", "ONE_EIGHTY", "ONE_YEAR", "SIXTY", "THIRTY"]
ExchangeEnumType = Literal[
    "binance", "bitcom", "cme", "delta", "deribit", "ftx", "ledgerx", "okex"
]
Float = float
Int = int
LiquidationEnumType = Literal["any", "liquidation", "nonLiquidation"]
PutCallEnumType = Literal["C", "P"]
String = str
SymbolEnumType = Literal[
    "AAVE",
    "ADA",
    "ALGO",
    "ANKR",
    "AR",
    "ATOM",
    "AVAX",
    "BAT",
    "BCH",
    "BNB",
    "BNT",
    "BSV",
    "BTC",
    "BTCB",
    "BTMX",
    "BTT",
    "CAKE",
    "CEL",
    "CELO",
    "CHSB",
    "CHZ",
    "CKB",
    "COMP",
    "CRO",
    "DASH",
    "DCR",
    "DENT",
    "DGB",
    "DOGE",
    "DOT",
    "EGLD",
    "ENJ",
    "EOS",
    "ETC",
    "ETH",
    "FIL",
    "FLOW",
    "FTM",
    "FTT",
    "GRT",
    "HBAR",
    "HNT",
    "HOT",
    "HT",
    "ICX",
    "IOST",
    "KLAY",
    "KSM",
    "LEO",
    "LINK",
    "LTC",
    "LUNA",
    "MANA",
    "MATIC",
    "MIOTA",
    "MKR",
    "NEAR",
    "NEO",
    "NEXO",
    "NPXS",
    "OMG",
    "ONE",
    "ONT",
    "QTUM",
    "REN",
    "RSR",
    "RUNE",
    "RVN",
    "SC",
    "SNX",
    "SOL",
    "STX",
    "SUSHI",
    "TFUEL",
    "THETA",
    "UMA",
    "UNI",
    "VET",
    "VGX",
    "WAVES",
    "WRX",
    "XEM",
    "XLM",
    "XMR",
    "XRP",
    "XTZ",
    "YFI",
    "ZEC",
    "ZIL",
    "ZRX",
]
YesNoAllType = Literal["all", "no", "yes"]
