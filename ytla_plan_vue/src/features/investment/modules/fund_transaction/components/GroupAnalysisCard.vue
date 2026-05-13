<template>
  <div class="group-analysis-card">
    <div class="card-header" @click="toggleExpand">
      <div class="header-left">
        <span class="expand-icon">{{ isExpanded ? '▼' : '▶' }}</span>
        <h4>交易分组 #{{ index + 1 }}</h4>
        <div class="group-status" :class="statusClass">
          {{ statusText }}
        </div>
        <span class="tx-type-label" :class="txTypeClass">
          {{ txTypeLabel }}
        </span>
      </div>
      <div class="header-right">
        <span class="tx-count">{{ group.length }} 笔交易</span>
      </div>
    </div>
    
    <div class="transactions-list">
      <table class="tx-table">
        <thead>
          <tr>
            <th>序号</th>
            <th>交易编号</th>
            <th>交易日期</th>
            <th>参照</th>
            <th>交易金额</th>
            <th>交易价格</th>
            <th>交易份额</th>
            <th>浮盈</th>
            <th>浮盈(%)</th>
          </tr>
        </thead>
        <tbody v-show="isExpanded">
          <template v-for="(tx, txIndex) in group" :key="txIndex">
            <tr class="tx-row" :class="{ 'latest-tx': txIndex === group.length - 1 }">
              <td>{{ txIndex + 1 }}</td>
              <td>{{ tx.transaction_id }}</td>
              <td>{{ tx.transaction_date }}</td>
              <td class="base-label">实际</td>
              <td>{{ tx.transaction_amount?.toFixed(2) }}</td>
              <td>{{ tx.transaction_price?.toFixed(4) }}</td>
              <td>{{ tx.transaction_share?.toFixed(4) }}</td>
              <td :class="{ profit: tx.transaction_profit > 0, loss: tx.transaction_profit < 0, zero: tx.transaction_profit === 0 }">
                {{ tx.transaction_profit > 0 ? '+' : '' }}{{ tx.transaction_profit?.toFixed(4) }}
              </td>
              <td :class="{ profit: tx.transaction_profit_pct > 0, loss: tx.transaction_profit_pct < 0, zero: tx.transaction_profit_pct === 0 }">
                {{ tx.transaction_profit_pct > 0 ? '+' : '' }}{{ tx.transaction_profit_pct?.toFixed(2) }}%
              </td>
            </tr>
            <tr v-if="tx.transaction_base_amount" class="base-row">
              <td colspan="3"></td>
              <td class="base-label">基准</td>
              <td>{{ tx.transaction_base_amount?.toFixed(2) }}</td>
              <td>{{ tx.transaction_base_price?.toFixed(4) }}</td>
              <td>{{ tx.transaction_base_share?.toFixed(4) }}</td>
              <td :class="{ profit: tx.transaction_profit_to_base > 0, loss: tx.transaction_profit_to_base < 0, zero: tx.transaction_profit_to_base === 0 }">
                {{ tx.transaction_profit_to_base > 0 ? '+' : '' }}{{ tx.transaction_profit_to_base?.toFixed(4) }}
              </td>
              <td :class="{ profit: tx.transaction_profit_pct_to_base > 0, loss: tx.transaction_profit_pct_to_base < 0, zero: tx.transaction_profit_pct_to_base === 0 }">
                {{ tx.transaction_profit_pct_to_base > 0 ? '+' : '' }}{{ tx.transaction_profit_pct_to_base?.toFixed(2) }}%
              </td>
            </tr>
            <tr v-if="tx.analyze_transaction_stage" class="summary-row">
              <td colspan="9">
                <div class="summary-content">
                  <span class="profit-summary">
                    收益 {{ tx.analyze_transaction_profit?.toFixed(4) }} 收益(%) {{ tx.analyze_transaction_profit_pct?.toFixed(2) }}% 
                    合计盈利金额 {{ tx.analyze_group_profit_amount?.toFixed(2) }} 
                    合计盈利份额 {{ tx.analyze_group_profit_share?.toFixed(4) }}
                  </span>
                </div>
              </td>
            </tr>
            <tr v-if="tx.memo" class="summary-row">
              <td colspan="9">
                <div class="summary-content">
                  <span class="memo-text">
                    备注 {{ tx.memo }}
                  </span>
                </div>
              </td>
            </tr>
          </template>
        </tbody>
        <tbody v-show="!isExpanded && lastAnalyzedTx">
          <tr class="tx-row latest-tx">
            <td>{{ lastAnalyzedTxIndex + 1 }}</td>
            <td>{{ lastAnalyzedTx?.transaction_id }}</td>
            <td>{{ lastAnalyzedTx?.transaction_date }}</td>
            <td class="base-label">实际</td>
            <td>{{ lastAnalyzedTx?.transaction_amount?.toFixed(2) }}</td>
            <td>{{ lastAnalyzedTx?.transaction_price?.toFixed(4) }}</td>
            <td>{{ lastAnalyzedTx?.transaction_share?.toFixed(4) }}</td>
            <td :class="{ profit: (lastAnalyzedTx?.transaction_profit || 0) > 0, loss: (lastAnalyzedTx?.transaction_profit || 0) < 0, zero: (lastAnalyzedTx?.transaction_profit || 0) === 0 }">
              {{ (lastAnalyzedTx?.transaction_profit || 0) > 0 ? '+' : '' }}{{ lastAnalyzedTx?.transaction_profit?.toFixed(4) }}
            </td>
            <td :class="{ profit: (lastAnalyzedTx?.transaction_profit_pct || 0) > 0, loss: (lastAnalyzedTx?.transaction_profit_pct || 0) < 0, zero: (lastAnalyzedTx?.transaction_profit_pct || 0) === 0 }">
              {{ (lastAnalyzedTx?.transaction_profit_pct || 0) > 0 ? '+' : '' }}{{ lastAnalyzedTx?.transaction_profit_pct?.toFixed(2) }}%
            </td>
          </tr>
          <tr v-if="lastAnalyzedTx?.transaction_base_amount" class="base-row">
            <td colspan="3"></td>
            <td class="base-label">基准</td>
            <td>{{ lastAnalyzedTx?.transaction_base_amount?.toFixed(2) }}</td>
            <td>{{ lastAnalyzedTx?.transaction_base_price?.toFixed(4) }}</td>
            <td>{{ lastAnalyzedTx?.transaction_base_share?.toFixed(4) }}</td>
            <td :class="{ profit: (lastAnalyzedTx?.transaction_profit_to_base || 0) > 0, loss: (lastAnalyzedTx?.transaction_profit_to_base || 0) < 0, zero: (lastAnalyzedTx?.transaction_profit_to_base || 0) === 0 }">
              {{ (lastAnalyzedTx?.transaction_profit_to_base || 0) > 0 ? '+' : '' }}{{ lastAnalyzedTx?.transaction_profit_to_base?.toFixed(4) }}
            </td>
            <td :class="{ profit: (lastAnalyzedTx?.transaction_profit_pct_to_base || 0) > 0, loss: (lastAnalyzedTx?.transaction_profit_pct_to_base || 0) < 0, zero: (lastAnalyzedTx?.transaction_profit_pct_to_base || 0) === 0 }">
              {{ (lastAnalyzedTx?.transaction_profit_pct_to_base || 0) > 0 ? '+' : '' }}{{ lastAnalyzedTx?.transaction_profit_pct_to_base?.toFixed(2) }}%
            </td>
          </tr>
          <tr v-if="lastAnalyzedTx?.analyze_transaction_stage" class="summary-row">
            <td colspan="9">
              <div class="summary-content">
                <span class="profit-summary">
                  收益 {{ lastAnalyzedTx?.analyze_transaction_profit?.toFixed(4) }} 收益(%) {{ lastAnalyzedTx?.analyze_transaction_profit_pct?.toFixed(2) }}% 
                  合计盈利金额 {{ lastAnalyzedTx?.analyze_group_profit_amount?.toFixed(2) }} 
                  合计盈利份额 {{ lastAnalyzedTx?.analyze_group_profit_share?.toFixed(4) }}
                </span>
              </div>
            </td>
          </tr>
          <tr v-if="lastAnalyzedTx?.memo" class="summary-row">
            <td colspan="9">
              <div class="summary-content">
                <span class="memo-text">
                  备注 {{ lastAnalyzedTx?.memo }}
                </span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

interface Transaction {
  transaction_id: number
  code: string
  fund_name: string
  transaction_date: string
  transaction_type: string
  transaction_price: number
  transaction_amount: number
  transaction_share: number
  transaction_profit: number
  transaction_profit_pct: number
  transaction_base_price: number
  transaction_base_amount: number
  transaction_base_share: number
  transaction_profit_to_base: number
  transaction_profit_pct_to_base: number
  order_id: number
  memo: string
  analyze_transaction_profit: number
  transaction_profit_amount: number
  transaction_profit_share: number
  analyze_transaction_profit_pct: number
  analyze_transaction_type: string
  analyze_transaction_stage: string
  analyze_group_profit_amount: number
  analyze_group_profit_share: number
}

interface Props {
  group: Transaction[]
  index: number
}

const props = defineProps<Props>()

const isExpanded = ref(false)

const lastTx = computed(() => props.group[props.group.length - 1])

const lastAnalyzedTx = computed(() => {
  return props.group.slice().reverse().find(tx => tx.analyze_transaction_stage) || lastTx.value
})

const lastAnalyzedTxIndex = computed(() => {
  const idx = props.group.findIndex(tx => tx === lastAnalyzedTx.value)
  return idx !== -1 ? idx : props.group.length - 1
})

const txTypeClass = computed(() => {
  if (!lastTx.value) return ''
  return lastTx.value.analyze_transaction_type === 'BUY' ? 'long' : 'short'
})

const lastAnalyzedTxTypeClass = computed(() => {
  if (!lastAnalyzedTx.value) return ''
  return lastAnalyzedTx.value.analyze_transaction_type === 'BUY' ? 'long' : 'short'
})

const txTypeLabel = computed(() => {
  if (!lastTx.value) return ''
  return lastTx.value.analyze_transaction_type === 'BUY' ? '做多' : '做空'
})

const lastAnalyzedTxTypeLabel = computed(() => {
  if (!lastAnalyzedTx.value) return ''
  return lastAnalyzedTx.value.analyze_transaction_type === 'BUY' ? '做多' : '做空'
})

const statusClass = computed(() => {
  if (!lastTx.value) return ''
  const stage = lastTx.value.analyze_transaction_stage
  if (stage === '4') return 'closed-profit'
  if (stage === '5') return 'closed-loss'
  if (stage === '3') return 'open'
  if (stage === '2' || stage === '2a') return 'looping'
  return 'new'
})

const statusText = computed(() => {
  if (!lastTx.value) return ''
  const stage = lastTx.value.analyze_transaction_stage
  if (stage === '5' || stage === '4') return '平仓'
  if (stage === '3') return '开仓'
  if (stage === '2' || stage === '2a') return '滚动'
  return '开仓'
})

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}
</script>

<style scoped lang="scss">
.group-analysis-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow-x: auto;

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid #f0f0f0;
    cursor: pointer;
    user-select: none;

    &:hover {
      background: #f9f9f9;
      border-radius: 4px;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;

      h4 {
        margin: 0;
        font-size: 16px;
        color: #333;
      }

      .expand-icon {
        font-size: 12px;
        color: #999;
        width: 16px;
        text-align: center;
      }

      .group-status {
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;

        &.closed-profit {
          background: #e8f5e9;
          color: #4caf50;
        }

        &.closed-loss {
          background: #ffebee;
          color: #f44336;
        }

        &.open {
          background: #fff3e0;
          color: #ff9800;
        }

        &.looping {
          background: #e3f2fd;
          color: #2196f3;
        }

        &.new {
          background: #f5f5f5;
          color: #999;
        }
      }

      .tx-type-label {
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;

        &.long {
          background: #fff3e0;
          color: #ff9800;
        }

        &.short {
          background: #e3f2fd;
          color: #2196f3;
        }
      }
    }

    .header-right {
      .tx-count {
        font-size: 13px;
        color: #999;
      }
    }
  }

  .transactions-list {
    .tx-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;

      thead {
        th {
          background: #f5f5f5;
          padding: 10px 8px;
          text-align: left;
          font-weight: 600;
          color: #666;
          border-bottom: 2px solid #e0e0e0;
        }
      }

      tbody {
        .tx-row {
          border-bottom: 1px solid #f0f0f0;

          &.latest-tx {
            background: #fff9e6;
          }

          td {
            padding: 8px;
            border-bottom: 1px solid #f0f0f0;
            text-align: left;

            &.profit {
              color: #f44336;
              font-weight: 600;
            }

            &.loss {
              color: #4caf50;
              font-weight: 600;
            }
            
            &.zero {
              color: #333;
              font-weight: 600;
            }
          }
        }

        .base-row {
          background: #f9f9f9;

          td {
            padding: 6px 8px;
            font-size: 12px;
            color: #666;
            text-align: left;

            .base-label {
              font-weight: 600;
            }

            &.profit {
              color: #f44336;
              font-weight: 600;
            }

            &.loss {
              color: #4caf50;
              font-weight: 600;
            }
            
            &.zero {
              color: #333;
              font-weight: 600;
            }
          }
        }

        .summary-row {
          td {
            padding: 8px;
            font-size: 12px;
            background: #fafafa;

            .summary-content {
              display: flex;
              flex-wrap: wrap;
              gap: 16px;

              .profit-summary {
                color: #333;
              }

              .memo-text {
                color: #f44336;
                font-style: italic;
              }
            }
          }
        }
      }
    }
  }
}
</style>
