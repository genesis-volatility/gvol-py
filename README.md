# GVol

[![Main workflow](https://github.com/genesis-volatility-public/gvol/actions/workflows/main.yml/badge.svg)](https://github.com/genesis-volatility-public/gvol/actions/workflows/main.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Install

```bash
pip install git+ssh://git@github.com/genesis-volatility-public/gvol@main
```

## Demo
```python
from gvol import GVol

gvol_client = GVol("gvol_api_key")

orderbook_skew_strike = gvol_client.CurrentOrderbookSkewStrike(
    symbol="BTC", exchange="deribit"
)

print(orderbook_skew_strike)
```