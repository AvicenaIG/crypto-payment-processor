# crypto-payment-processor

![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Version](https://img.shields.io/badge/version-0.1.0-green?style=flat-square)
![Python](https://img.shields.io/badge/python-3-blue?style=flat-square)

A cryptocurrency payment processing and invoice settlement engine with exchange rate aggregation, payout workflows, and merchant notification tooling.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#license)
- [License](#license)

## Features

- **Aggregate exchange rates** across multiple providers — CoinGecko, Kraken, and fiat rate sources — via a pluggable exchange abstraction (`BaseExchange`, `CoingeckoExchange`, `Kraken`, `FiatExchange`).
- **Define custom FX rules** with the expression-based rate engine (`ExpressionParser`, `ExchangeTransformer`, `ExchangePair`) and validate computed rates with `is_valid_rate`.
- **Track invoice lifecycle states** for payment processing, including settlement and exception statuses (`InvoiceStatus`, `InvoiceExceptionStatus`, `convert_status`).
- **Manage payout statuses and auth scopes** through typed constants (`PayoutStatus`, `AuthScopes`).
- **Format money precisely** with half-up, up, and down rounding modes plus raw-unit conversion (`round_half_up`, `round_up`, `round_down`, `to_raw`, `format_raw`, `CurrencyTable`).
- **Export invoice data** to JSON and CSV for accounting and reconciliation workflows (`process_invoice`, `db_to_json`, `json_to_csv`).

## Installation

```bash
git clone https://github.com/AvicenaIG/crypto-payment-processor.git
cd crypto-payment-processor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

```python
from api.ext.moneyformat import CurrencyTable, round_half_up
from api.ext.exchanges.coingecko import CoingeckoExchange
from api.invoices import InvoiceStatus

# Format a settlement amount with banker-safe rounding
amount = round_half_up("0.15375", 8)

# Look up a currency's display metadata
currency = CurrencyTable.get("btc")

# Fetch a crypto/fiat rate from CoinGecko
exchange = CoingeckoExchange()
rate = exchange.get_rate("BTC", "USD")

# Inspect an invoice's lifecycle state
print(InvoiceStatus.PENDING)
```

## Usage

### Building an FX rate pipeline

Compose rate sources and validation rules for checkout pricing:

```python
from api.ext.fxrate import ExpressionParser, ExchangeTransformer, is_valid_rate
from api.ext.exchanges.kraken import Kraken, build_kraken_quotes

# Pull live quotes from Kraken
quotes = build_kraken_quotes()

# Parse a pricing rule expression and validate the resulting rate
parser = ExpressionParser("BTC/USD * 1.02")
transformer = ExchangeTransformer()
rate = parser.parse()
if is_valid_rate(rate):
    apply_rate_to_invoice(rate)
```

### Exporting invoices for reconciliation

```python
from api.ext.export import process_invoice, db_to_json, json_to_csv

# Convert stored invoice records into JSON, then CSV for the books
records = db_to_json([invoice_dict])
csv_output = json_to_csv(records)
```

## Configuration

| Option | Type | Default | Description |
| ------ | ---- | ------- | ----------- |
| `MAX_CONFIRMATION_WATCH` | `int` | via `get_max_confirmation_watch()` | Maximum number of confirmations watched before an invoice is considered settled. |

## Contributing

Contributions are welcome — please open an issue or pull request describing the change. Ensure new payment or rate-handling logic includes tests and follows the existing code style. See the repository for further guidelines.

## License

MIT © 2026 crypto-payment-processor contributors