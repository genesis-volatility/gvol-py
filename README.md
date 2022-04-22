# GVol

[![Latest Version](https://img.shields.io/pypi/v/gvol.svg)](https://pypi.org/project/gvol/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/gvol.svg)](https://pypi.org/project/gvol/)
[![Main Workflow](https://github.com/genesis-volatility/gvol-py/actions/workflows/main.yml/badge.svg)](https://github.com/genesis-volatility/gvol-py/actions/workflows/main.yml)
[![Documentation Status](https://readthedocs.org/projects/gvol/badge/?version=latest)](https://gvol.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

GVol is a Python library to access the [GVol API](https://docs.gvol.io/).

---

**Documentation**: [https://gvol.readthedocs.io/en/latest/index.html](https://gvol.readthedocs.io/en/latest/index.html)

---

## Install

```bash
pip install gvol
```

## Demo

```python
from gvol import GVol
#Valid Headers: "x-oracle", "gvol-lite", "gvol-lite-plus"
gvol_client = GVol(header="gvol-lite", gvol_api_key="ENTER YOUR API KEY HERE")

orderbook_skew_strike = gvol_client.CurrentOrderbookSkewStrike(
    symbol="BTC", exchange="deribit"
)

print(orderbook_skew_strike)
```
