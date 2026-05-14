<template>
  <div class="fund-price-chart">
    <v-chart
      v-if="chartOption"
      :option="chartOption"
      class="chart"
      autoresize
    />
    <div v-else class="empty-state">
      暂无数据
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import VChart from 'vue-echarts'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent
} from 'echarts/components'

use([
  CanvasRenderer,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent
])

interface Props {
  history: Array<{
    transaction_date: string
    current_price: number
    origin_price: number
    fluctuation: number
    share_change_ratio: number
    share_change_note: string
  }>
}

const props = defineProps<Props>()

const chartOption = computed(() => {
  if (!props.history || props.history.length === 0) return null

  const dates = props.history.map(item => item.transaction_date)
  const prices = props.history.map(item => item.current_price)

  // 计算显示范围，默认显示最近250天
  const totalDays = dates.length
  const displayDays = Math.min(totalDays, 250)
  const startIdx = totalDays - displayDays

  return {
    tooltip: {
      trigger: 'axis',
      formatter: (params: any) => {
        const data = params[0]
        return `${data.axisValue}<br/>净值: ${data.value.toFixed(4)}`
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: dates,
      axisLabel: {
        rotate: 45,
        interval: Math.floor(dates.length / 10)
      }
    },
    yAxis: {
      type: 'value',
      scale: true
    },
    dataZoom: [
      {
        type: 'inside',
        startValue: startIdx,
        endValue: totalDays - 1
      },
      {
        type: 'slider',
        startValue: startIdx,
        endValue: totalDays - 1,
        height: 25,
        bottom: 5
      }
    ],
    series: [
      {
        name: '净值',
        type: 'line',
        smooth: true,
        data: prices,
        itemStyle: {
          color: '#1976d2'
        },
        areaStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              { offset: 0, color: 'rgba(25, 118, 210, 0.3)' },
              { offset: 1, color: 'rgba(25, 118, 210, 0.05)' }
            ]
          }
        }
      }
    ]
  }
})
</script>

<style scoped lang="scss">
.fund-price-chart {
  background: white;
  border-radius: 8px;
  padding: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;

  .chart {
    height: 420px;
    width: 100%;
  }

  .empty-state {
    text-align: center;
    color: #999;
    padding: 80px;
  }
}
</style>
