<template>
  <div class="continuous-stats">
    <div v-if="continuousHistory" class="stats-content">
      <h3 class="section-title">连续涨跌统计</h3>

      <!-- 最近涨跌流 -->
      <div class="latest-flows">
        <h4>最近涨跌流</h4>
        <div class="flows-container">
          <div
            v-for="(flow, index) in continuousHistory.latest_flows"
            :key="index"
            class="flow-item"
          >
            <div class="flow-date">{{ flow[0] }}</div>
            <div class="flow-days">{{ flow[1] }}天</div>
            <div class="flow-ratio" :class="{ up: flow[2] >= 0, down: flow[2] < 0 }">
              {{ flow[2] >= 0 ? '+' : '' }}{{ flow[2]?.toFixed(2) }}%
            </div>
          </div>
        </div>
      </div>

      <!-- 连续天数统计 -->
      <div class="days-stats">
        <h4>连续天数分布</h4>
        <div class="stats-table">
          <div class="table-row">
            <div class="row-label">累积天数</div>
            <div
              v-for="(days, index) in sortedDays"
              :key="`days-${index}`"
              class="table-cell"
            >
              {{ getDayLabel(index) }}
            </div>
          </div>
          <div class="table-row">
            <div class="row-label">买侧次数</div>
            <div
              v-for="(days, index) in sortedDays"
              :key="`buy-${index}`"
              class="table-cell"
            >
              {{ getBuyDayCount(index) }}
            </div>
          </div>
          <div class="table-row">
            <div class="row-label">卖侧次数</div>
            <div
              v-for="(days, index) in sortedDays"
              :key="`sell-${index}`"
              class="table-cell"
            >
              {{ getSellDayCount(index) }}
            </div>
          </div>
        </div>
      </div>

      <!-- 连续涨跌幅统计 -->
      <div class="grades-stats">
        <h4>连续涨跌幅分布</h4>
        <div class="stats-table">
          <div class="table-row">
            <div class="row-label">累积幅度</div>
            <div
              v-for="(grade, index) in sortedGrades"
              :key="`grade-${index}`"
              class="table-cell"
            >
              {{ getGradeLabel(index) }}%
            </div>
          </div>
          <div class="table-row">
            <div class="row-label">买侧次数</div>
            <div
              v-for="(grade, index) in sortedGrades"
              :key="`buy-grade-${index}`"
              class="table-cell"
            >
              {{ getBuyGradeCount(index) }}
            </div>
          </div>
          <div class="table-row">
            <div class="row-label">卖侧次数</div>
            <div
              v-for="(grade, index) in sortedGrades"
              :key="`sell-grade-${index}`"
              class="table-cell"
            >
              {{ getSellGradeCount(index) }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="empty-state">
      暂无数据
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  continuousHistory: {
    buy_side: Array<Array<number>>
    sell_side: Array<Array<number>>
    fund_days: number
    buy_side_grades: Array<number> | Array<Array<number>>
    sell_side_grades: Array<number> | Array<Array<number>>
    latest_flows: Array<[string, number, number]>
  } | null | undefined
}

const props = defineProps<Props>()

const sortedDays = computed(() => {
  if (!props.continuousHistory) return []
  // 根据文档，累积天数是 1, 2, 3, 4, 5, 6, 7, 8, 9, 10+
  return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

const getBuyDayCount = (index: number) => {
  if (!props.continuousHistory || !Array.isArray(props.continuousHistory.buy_side)) return 0
  // index 是 0-9 对应 buy_side[1]-buy_side[10]
  const dataIndex = index + 1
  const item = props.continuousHistory.buy_side[dataIndex]
  // 使用子数组的长度
  return Array.isArray(item) ? item.length : 0
}

const getSellDayCount = (index: number) => {
  if (!props.continuousHistory || !Array.isArray(props.continuousHistory.sell_side)) return 0
  const dataIndex = index + 1
  const item = props.continuousHistory.sell_side[dataIndex]
  return Array.isArray(item) ? item.length : 0
}

const getDayLabel = (index: number) => {
  // index 0-9 对应 1-10，最后一个显示 10+
  if (index === 9) {
    return '10+'
  }
  return (index + 1).toString()
}

const sortedGrades = computed(() => {
  if (!props.continuousHistory) return []
  // 根据文档，累积幅度是 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30+
  return [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
})

const getBuyGradeCount = (index: number) => {
  if (!props.continuousHistory || !Array.isArray(props.continuousHistory.buy_side_grades)) return 0
  const item = props.continuousHistory.buy_side_grades[index]
  return Array.isArray(item) ? item.length : (item ?? 0)
}

const getSellGradeCount = (index: number) => {
  if (!props.continuousHistory || !Array.isArray(props.continuousHistory.sell_side_grades)) return 0
  const item = props.continuousHistory.sell_side_grades[index]
  return Array.isArray(item) ? item.length : (item ?? 0)
}

const getGradeLabel = (index: number) => {
  // index 0-10，最后一个显示 30+
  if (index === 10) {
    return '30+'
  }
  return (index * 3).toString()
}
</script>

<style scoped lang="scss">
.continuous-stats {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

  .stats-content {
    .section-title {
      font-size: 18px;
      color: #333;
      margin: 0 0 20px 0;
    }

    .latest-flows {
      margin-bottom: 24px;

      h4 {
        font-size: 14px;
        color: #666;
        margin: 0 0 12px 0;
      }

      .flows-container {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;

        .flow-item {
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 12px 20px;
          background: #f5f5f5;
          border-radius: 8px;
          min-width: 100px;

          .flow-date {
            font-size: 12px;
            color: #999;
          }

          .flow-days {
            font-size: 16px;
            font-weight: 600;
            color: #333;
            margin: 4px 0;
          }

          .flow-ratio {
            font-size: 14px;
            font-weight: 600;

            &.up {
              color: #f44336;
            }

            &.down {
              color: #4caf50;
            }
          }
        }
      }
    }

    .days-stats,
    .grades-stats {
      margin-bottom: 24px;

      &:last-child {
        margin-bottom: 0;
      }

      h4 {
        font-size: 14px;
        color: #666;
        margin: 0 0 12px 0;
      }

      .stats-table {
        background: #f5f5f5;
        border-radius: 8px;
        overflow: hidden;

        .table-row {
          display: flex;
          border-bottom: 1px solid #e0e0e0;

          &:last-child {
            border-bottom: none;
          }

          .row-label {
            min-width: 100px;
            padding: 12px 16px;
            background: #e8e8e8;
            font-size: 13px;
            font-weight: 600;
            color: #333;
            flex-shrink: 0;
          }

          .table-cell {
            flex: 1;
            padding: 12px 8px;
            text-align: center;
            font-size: 14px;
            color: #333;
            min-width: 60px;
          }
        }
      }
    }
  }

  .empty-state {
    text-align: center;
    color: #999;
    padding: 40px;
  }
}
</style>
