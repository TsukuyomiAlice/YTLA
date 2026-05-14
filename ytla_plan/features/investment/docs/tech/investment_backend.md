# Investment - Backend Technical Document

### Frank Wang

File update date: 2026-05-14

## Module Overview

The investment module is a domestic fund transaction analysis system backend, providing fund information query, historical net value display, transaction group matching analysis, position statistics, and continuous rise/fall analysis functions for investment decision-making reference.

### Main Features
- Fund basic information query
- Fund historical net value data retrieval
- Transaction history matching and grouping analysis
- Position statistics and profit calculation
- Continuous rise/fall trend analysis

### Design Goals
- Modular architecture with clear separation of concerns
- High maintainability and extensibility
- Efficient data processing for transaction matching
- Clear API interface for frontend consumption

### Position in System
This module is part of the YTLA investment features, working in conjunction with the frontend Vue.js application to provide a complete fund analysis experience.

## File Structure

### Core Directories
```
investment/modules/
├── fund_info/          # Fund information and historical net value module
│   ├── dao/           # Database access layer
│   ├── process/       # Business logic layer
│   ├── routes/        # API routing layer
│   └── utils/         # Utility functions
└── fund_transaction/  # Transaction analysis module
    ├── dao/           # Database access layer
    ├── process/       # Business logic layer
    ├── routes/        # API routing layer
    └── utils/         # Utility functions
```

### Key Files

#### fund_info Module
- [processModuleFundInfo.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info\process\processModuleFundInfo.py) - Fund info API business logic
- [routeModuleFundInfo.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info\routes\routeModuleFundInfo.py) - Fund info API routes
- [daoFundInfo.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info\dao\daoFundInfo.py) - Fund info database access
- [daoFundHistory.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info\dao\daoFundHistory.py) - Fund history database access

#### fund_transaction Module
- [processModuleFundTransaction.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\process\processModuleFundTransaction.py) - Transaction analysis API business logic
- [routeModuleFundTransaction.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\routes\routeModuleFundTransaction.py) - Transaction analysis API routes
- [processTransactionMatchGroup.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\process\processTransactionMatchGroup.py) - Core transaction matching algorithm
- [daoTransactionHistory.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\dao\daoTransactionHistory.py) - Transaction history database access

## Core Components

### Fund Info Module ([fund_info](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info))

#### Component Responsibilities
- Retrieve fund basic information (name, code, type, etc.)
- Fetch historical net value data
- Calculate and return latest net value
- Provide consistent data format for frontend consumption

#### API Endpoints

##### GET /fund_info/get
Get fund basic information by fund code.

**Request Parameters:**
- `code`: Fund code (string, required)

**Response Format:**
```json
{
  "success": true,
  "data": {
    "code": "161725",
    "name": "招商中证白酒指数(LOF)A",
    "fund_type": "stock",
    "ratio": 1.0,
    "share_accuracy": 4,
    "fee_free_limit": 7,
    "latest_price": 1.2345
  }
}
```

##### GET /fund_info/history
Get fund historical net value data.

**Request Parameters:**
- `code`: Fund code (string, required)

**Response Format:**
```json
{
  "success": true,
  "data": [
    {
      "transaction_date": "2026-05-13",
      "current_price": 1.2345,
      "origin_price": 1.2200,
      "fluctuation": 0.0145,
      "share_change_ratio": 1.0,
      "share_change_note": ""
    }
  ]
}
```

##### GET /fund_info/latest_price
Get fund latest net value.

**Request Parameters:**
- `code`: Fund code (string, required)

**Response Format:**
```json
{
  "success": true,
  "data": {
    "latest_price": 1.2345,
    "origin_price": 1.2200
  }
}
```

### Transaction Analysis Module ([fund_transaction](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction))

#### Component Responsibilities
- Match and group transactions by trading logic
- Calculate profit and loss for each group
- Generate position statistics summary
- Analyze continuous rise/fall patterns

#### Core Algorithm - Transaction Matching ([processTransactionMatchGroup.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\process\processTransactionMatchGroup.py))

The transaction matching algorithm processes transaction history and groups them by:

1. **Transaction Type Identification**
   - BUY vs SELL transactions
   - Real vs Benchmark price calculations

2. **Transaction Stages**
   - Stage 1: Create new group
   - Stage 2/2a: Rolling transactions
   - Stage 3: Open position
   - Stage 4: Closed position (profit)
   - Stage 5: Closed position (loss)

3. **Dual Price System**
   - Real transaction price from actual records
   - Benchmark price for theoretical calculations
   - Profit comparison between both approaches

#### API Endpoints

##### GET /fund_transaction/analysis
Get comprehensive transaction analysis for a fund.

**Request Parameters:**
- `code`: Fund code (string, required)

**Response Format:**
```json
{
  "success": true,
  "data": {
    "brief": {
      "code": "161725",
      "fund_name": "招商中证白酒指数(LOF)A",
      "last_transaction_date": "2026-05-13",
      "latest_price": 1.2345,
      "holding_amount": 1234.56,
      "holding_share": 1000.0000,
      "profit_in_amount": 234.56,
      "profit_in_share": 100.0000,
      "long_position_amount": 1000.00,
      "long_position_share": 810.0000,
      "short_position_share": 0.0000,
      "short_position_amount": 0.00
    },
    "match_list": [
      [
        {
          "transaction_id": 1,
          "code": "161725",
          "transaction_date": "2026-01-01",
          "transaction_type": "BUY",
          "transaction_price": 1.0000,
          "transaction_amount": 1000.00,
          "transaction_share": 1000.0000,
          "transaction_profit": 0.0000,
          "transaction_profit_pct": 0.00,
          "analyze_transaction_stage": "3",
          "analyze_group_profit_amount": 0.00,
          "analyze_group_profit_share": 0.0000
        }
      ]
    ],
    "continuous_history": {
      "buy_side": [],
      "sell_side": [],
      "fund_days": 100,
      "buy_side_grades": [],
      "sell_side_grades": [],
      "latest_flows": []
    }
  }
}
```

## Data Flow

### Fund Info Query Flow
```
Frontend Request
    ↓
routeModuleFundInfo.py (Router)
    ↓
processModuleFundInfo.py (Business Logic)
    ↓
daoFundInfo.py / daoFundHistory.py (Data Access)
    ↓
SQLite Database (fund.db)
    ↓
Return response to frontend
```

### Transaction Analysis Flow
```
Frontend Request
    ↓
routeModuleFundTransaction.py (Router)
    ↓
processModuleFundTransaction.py (Business Logic)
    ├─→ processTransactionMatchGroup.analyze_transaction_match_group()
    │   ├─→ daoTransactionHistory (Fetch transaction history)
    │   ├─→ daoFundHistory (Fetch price history)
    │   ├─→ Match and group transactions
    │   ├─→ Calculate position statistics
    │   └─→ Generate brief summary
    └─→ processTransactionMatchGroup.analyze_continuous_history()
        └─→ Analyze continuous rise/fall patterns
    ↓
Return structured JSON response
```

## Data Model

### Database Configuration

#### Fund Database ([config_database_sqlite.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_info\utils\config_database_sqlite.py))
```python
db_files = {
    "fund": "fund.db"
}
```

**Tables:**
- `FUND_INFO`: Fund basic information
- `FUND_HISTORY`: Historical net value data

#### Transaction Database ([config_database_sqlite.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\utils\config_database_sqlite.py))
```python
db_files = {
    "Transaction": "transaction.db"
}
```

**Tables:**
- `TRANSACTION_HISTORY`: Transaction records

### Key Data Structures

#### Instance (Transaction)
Represents a single transaction with analysis fields.

**Key Fields:**
- `transaction_id`: Unique transaction identifier
- `transaction_date`: Transaction date
- `transaction_type`: BUY/SELL
- `transaction_price`: Actual transaction price
- `transaction_share`: Transaction share amount
- `analyze_transaction_stage`: Analysis stage (1-5)
- `analyze_group_profit_amount`: Group profit amount
- `analyze_group_profit_share`: Group profit share

#### InstanceForBrief (Position Summary)
Represents overall position statistics.

**Key Fields:**
- `holding_amount`: Current holding value
- `holding_share`: Current holding shares
- `profit_in_amount`: Profit in currency
- `profit_in_share`: Profit in shares
- `long_position_*`: Long position details
- `short_position_*`: Short position details

## Important Implementation Details

### Database Access Pattern

All DAO functions use dictionary key access instead of index access:

**Before (Deprecated):**
```python
result = daoFundHistory.fund_history_select_latest_price(code)
price = result[0][0]  # Index access
```

**After (Current):**
```python
result = daoFundHistory.fund_history_select_latest_price(code)
price = result[0]["CURRENT_PRICE"]  # Key access
```

### Precision Handling

- **Amount precision**: 2 decimal places (0.01 yuan)
- **Share precision**: Configurable per fund (0.01 or 0.0001 shares)
- **Price precision**: 4 decimal places

### Transaction Matching Logic

The algorithm follows a priority-based matching:
1. Match with current transaction price
2. Fallback to benchmark price if needed
3. Create new group when no match found
4. Support rolling positions (adding to existing groups)

## Configuration & Deployment

### Environment Requirements
- Python 3.7+
- Flask framework
- SQLite 3+

### Database Setup
1. Ensure fund.db exists in YTLA_DATA directory
2. Ensure transaction.db exists in YTLA_DATA directory
3. Verify directory permissions for read/write

### Integration Points
- Frontend Vue.js application consumes API endpoints
- Database paths configured via `config_database_sqlite.py`
- API routes auto-registered by YTLA framework

## Extension Development

### Adding New API Endpoint
1. Create new function in respective `processModule*.py`
2. Add route in `routeModule*.py`
3. Add necessary DAO functions if database access needed
4. Return structured Response object

### Modifying Transaction Matching Algorithm
1. Edit [processTransactionMatchGroup.py](file:///d:\YTLA\ytla_plan\features\investment\modules\fund_transaction\process\processTransactionMatchGroup.py)
2. Test with existing transaction data
3. Verify `to_dict()` methods still work correctly
4. Update related components if data structure changes

### Adding New Analysis Module
1. Follow existing module structure (dao/process/routes)
2. Update parent module registries if needed
3. Create corresponding frontend components
4. Update documentation

## Notes

- All database results use dictionary key access, not index access
- Transaction analysis can process large datasets, consider performance
- The module is designed for Chinese domestic fund market conventions
- Author: Frank Wang
