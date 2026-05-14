# Investment - Frontend Technical Document

### Frank Wang

File update date: 2026-05-14

## Module Overview

The investment frontend module provides a user interface for the domestic fund transaction analysis system, enabling users to query fund information, view historical net value charts, analyze transaction groups, and examine position statistics.

### Main Features
- Fund code input and search functionality
- Fund basic information display card
- Interactive historical net value chart with ECharts
- Position statistics and profit/loss summary
- Transaction group analysis with collapsible cards
- Continuous rise/fall trend analysis display
- Two main entry points: fund_info and fund_transaction

### Design Goals
- Clean and intuitive user interface
- Responsive layout with modern design
- Smooth data loading and error handling
- Modular component architecture
- Reusable business components
- Following YTLA framework conventions

### Position in System
This module is the frontend companion to the investment backend module, consuming REST APIs to provide a complete user experience.

## File Structure

### Core Directories
```
investment/modules/
├── fund_info/                  # Fund information module
│   ├── components/             # Vue components
│   │   ├── Fund_infoMain.vue   # Flow navigator wrapper
│   │   ├── Fund_infoMain_00.vue # Main content component
│   │   ├── FundInfoCard.vue    # Fund info card
│   │   └── FundPriceChart.vue  # Net value chart
│   ├── services/               # API service layer
│   ├── stores/                 # Pinia state management
│   ├── flows/                  # Flow management
│   └── registries/             # Module registration
└── fund_transaction/           # Transaction analysis module
    ├── components/             # Vue components
    │   ├── Fund_transactionMain.vue
    │   ├── Fund_transactionMain_00.vue
    │   ├── HoldingStats.vue    # Position statistics
    │   ├── ContinuousStats.vue # Continuous rise/fall
    │   └── GroupAnalysisCard.vue # Transaction groups
    ├── services/
    ├── stores/
    ├── flows/
    └── registries/
```

### Key Files

#### fund_info Module
- [Fund_infoMain_00.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\components\Fund_infoMain_00.vue) - Fund info entry point with search
- [FundInfoCard.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\components\FundInfoCard.vue) - Fund basic information display
- [FundPriceChart.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\components\FundPriceChart.vue) - ECharts net value visualization
- [fundInfoStore.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\stores\fundInfoStore.ts) - State management
- [fundInfoService.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\services\fundInfoService.ts) - API calls

#### fund_transaction Module
- [Fund_transactionMain_00.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\components\Fund_transactionMain_00.vue) - Transaction analysis entry with left-right layout
- [HoldingStats.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\components\HoldingStats.vue) - Position statistics display
- [GroupAnalysisCard.vue](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\components\GroupAnalysisCard.vue) - Collapsible transaction group card
- [fundTransactionStore.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\stores\fundTransactionStore.ts) - State management
- [fundTransactionService.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\services\fundTransactionService.ts) - API calls

## Core Components

### Fund Info Module ([fund_info](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info))

#### Fund_infoMain_00 - Main Entry Component

**Responsibilities:**
- Fund code input and search
- Loading state management
- Error display
- Rendering fund info card and chart

**Key Features:**
- Input field with enter key support
- Search button with loading state
- Data validation for fund code

**Usage:**
```vue
<template>
  <Fund_infoMain_00 />
</template>
```

#### FundInfoCard - Fund Information Display

**Props:**
- `fundInfo`: Fund information object (optional)

**Displayed Information:**
- Fund code and name
- Fund type
- Latest net value
- Share accuracy
- Fee-free days

**Styling:**
- White card with shadow
- Clean grid layout
- Consistent typography

#### FundPriceChart - Net Value Visualization

**Props:**
- `history`: Array of historical net value data

**Features:**
- Uses ECharts for visualization
- Smooth line chart with gradient fill
- Data zoom (slider + inside)
- Shows last 250 days by default
- Tooltip with detailed information
- Responsive to container size

**ECharts Configuration:**
- Canvas renderer for performance
- Legend and grid components
- Date-axis with auto-rotation
- Scale-based y-axis

### Transaction Analysis Module ([fund_transaction](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction))

#### Fund_transactionMain_00 - Transaction Analysis Entry

**Responsibilities:**
- Fund code search
- Left-right split layout
- Combine fund info and transaction analysis
- Loading and error states

**Layout Structure:**
```
┌─────────────────────────────────────────┐
│          Fund Code Input                │
├──────────────┬──────────────────────────┤
│   Fund Info  │  Transaction Groups      │
│   & Chart    │  (scrollable)            │
│   & Stats    │                          │
│ (scrollable) │                          │
└──────────────┴──────────────────────────┘
```

**Left Panel:**
- FundInfoCard
- FundPriceChart
- HoldingStats
- ContinuousStats

**Right Panel:**
- List of GroupAnalysisCard components
- Scrollable container

#### HoldingStats - Position Statistics

**Props:**
- `brief`: Position summary object
- `history`: Historical data array

**Statistics Display:**
- Latest price
- Holding amount and share
- Displayed amount and share
- Long position details
- Short position details
- Profit in amount and share (with color coding)

**Profit Color Coding:**
- Positive profit: Red (#f44336)
- Negative profit: Green (#4caf50)
- Zero profit: Default color

#### GroupAnalysisCard - Transaction Group Display

**Props:**
- `group`: Array of transactions in this group
- `index`: Group index for display

**Features:**
- Collapsible/expandable card
- Group status badge (open/closed/rolling)
- Transaction type badge (long/short)
- Transaction count display
- Table showing all transactions
- Last transaction highlighted

**Transaction Table Columns:**
- Index
- Transaction ID
- Date
- Reference (Actual/Benchmark)
- Amount
- Price
- Share
- Profit
- Profit %

**Status Badge Types:**
- `closed-profit`: Closed with profit (green)
- `closed-loss`: Closed with loss (red)
- `open`: Currently open (orange)
- `rolling`: Rolling position (blue)
- `new`: New group (gray)

**Card Interaction:**
- Click header to toggle expand/collapse
- Chevron icon indicates state
- Default collapsed, shows only last analyzed transaction
- Expanded shows full transaction history

## State Management

### fundInfoStore ([fundInfoStore.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info\stores\fundInfoStore.ts))

**State:**
- `fundInfo`: Fund basic information object
- `fundHistory`: Array of historical data
- `isLoading`: Loading boolean
- `error`: Error message string

**Actions:**
- `loadAllData(code)`: Load both info and history
- `loadFundInfo(code)`: Load fund info only
- `loadFundHistory(code)`: Load history only
- `clearData()`: Reset state

### fundTransactionStore ([fundTransactionStore.ts](file:///d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_transaction\stores\fundTransactionStore.ts))

**State:**
- `transactionData`: Complete analysis data
- `isLoading`: Loading boolean
- `error`: Error message string

**Actions:**
- `fetchTransactionAnalysis(code)`: Load transaction analysis
- `clearData()`: Reset state

## Services & API Integration

### API Services Pattern

All services follow the same pattern:
1. Import YTLA HTTP client
2. Define API endpoints
3. Wrap with try-catch for error handling
4. Return response data

### fundInfoService

**Endpoints:**
- `getFundInfo(code)`: GET /fund_info/get
- `getFundHistory(code)`: GET /fund_info/history
- `getFundLatestPrice(code)`: GET /fund_info/latest_price

### fundTransactionService

**Endpoints:**
- `getTransactionAnalysis(code)`: GET /fund_transaction/analysis

## YTLA Framework Integration

### Module Flow Navigator Pattern

The frontend follows YTLA's flow-based architecture:

**Main File (Fund_infoMain.vue):**
```vue
<template>
  <ModuleFlowNavigator
    ref="flowNavigator"
    module-type="fund_info"
    flow-name="fund_info-main-steps"
    frame-type="main"
  />
</template>
```

**Flow Manager:**
- Located in `flows/` directory
- Manages step navigation
- Integrates with YTLA module system

### Module Registration

Each module has:
- `registries/` directory
- Module config file
- Auto-registered by YTLA framework

## Data Flow

### Fund Info Query Flow
```
User Input (Fund Code)
    ↓
handleSearch() called
    ↓
fundInfoStore.loadAllData(code)
    ↓
fundInfoService calls API endpoints
    ├─→ getFundInfo()
    └─→ getFundHistory()
    ↓
Store updates state
    ↓
Components reactively re-render
    ↓
Display fund info and chart
```

### Transaction Analysis Flow
```
User Input (Fund Code)
    ↓
handleSearch() in Fund_transactionMain_00
    ↓
Promise.all([
  fundInfoStore.loadAllData(),
  fundTransactionStore.fetchTransactionAnalysis()
])
    ↓
Both stores updated
    ↓
All components update with new data
    ↓
Left: Info, Chart, Stats
Right: Transaction groups
```

## Styling & Design System

### SCSS Structure
All components use scoped SCSS:
```vue
<style scoped lang="scss">
.component {
  // Styles here
}
</style>
```

### Design Principles
- Card-based UI with shadows
- Consistent spacing (8px grid)
- Clear visual hierarchy
- Color coding for status
- Responsive containers

### Color Palette
- Primary: #1976d2 (Blue)
- Success/Profit: #4caf50 (Green)
- Loss: #f44336 (Red)
- Warning/Open: #ff9800 (Orange)
- Neutral: #f5f5f5 (Light Gray)

## Component Development Guidelines

### Creating New Components
1. Follow PascalCase naming convention
2. Place in `components/` directory
3. Use `<script setup lang="ts">` syntax
4. Define clear prop interfaces
5. Use scoped styling
6. Update related documents

### Adding New Features
1. Update store state/actions if needed
2. Add service layer API calls
3. Create/modify components
4. Update flow manager if needed
5. Test integration
6. Update documentation

## Important Implementation Details

### Component Architecture
- **Container/Presentational pattern**: Main components manage state, child components are dumb
- **Props down, Events up**: Data flows through props, actions emit events
- **Reactive data**: Uses Vue Composition API with ref/computed

### Error Handling
- All API calls wrapped in try-catch
- Error state stored in Pinia
- Friendly error messages displayed to users
- Loading states prevent duplicate requests

### Performance Considerations
- ECharts uses Canvas renderer
- Virtual scrolling not needed for typical transaction count
- Chart data zoom limits initial render
- Collapsed cards reduce DOM complexity

### Precision Display
- Amount: 2 decimal places
- Price: 4 decimal places
- Share: 4 decimal places
- Percentage: 2 decimal places

## Configuration & Dependencies

### Required Dependencies
- `vue`: ^3.x
- `pinia`: State management
- `echarts`: Charting library
- `vue-echarts`: Vue wrapper for ECharts
- YTLA core framework

### Browser Support
- Modern browsers with ES6+ support
- Canvas support for ECharts

## Extension Development

### Adding New Stats Component
1. Create new `.vue` component in `components/`
2. Define props interface
3. Implement display logic
4. Add styling
5. Import and use in main component
6. Update tech documentation

### Adding New Chart Type
1. Create new chart component
2. Configure ECharts options
3. Accept data via props
4. Handle empty/loading states
5. Add to appropriate location

### Modifying GroupAnalysisCard
1. Edit existing component file
2. Update template structure as needed
3. Maintain collapsible functionality
4. Update styling while keeping consistency
5. Test with real transaction data

## Notes

- The frontend is designed for Chinese domestic fund market conventions
- Author: Frank Wang
- Always keep readme and tech documentation in sync with code changes
- Follow YTLA framework patterns for new features
- Use TypeScript for all new code
- Consider accessibility when adding interactive elements
