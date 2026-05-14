<template>
  <div class="fund-info-card">
    <div v-if="fundInfo" class="card-content">
      <h2 class="fund-name">{{ fundInfo.name }}</h2>
      <div class="fund-code">{{ fundInfo.code }}</div>

      <div class="info-grid">
        <div class="info-item">
          <span class="label">最新净值</span>
          <span class="value">{{ fundInfo.latest_price?.toFixed(4) || '--' }}</span>
        </div>
        <div class="info-item">
          <span class="label">基金类型</span>
          <span class="value">{{ fundInfo.fund_type || '--' }}</span>
        </div>
        <div class="info-item">
          <span class="label">份额精度</span>
          <span class="value">{{ fundInfo.share_accuracy }}位</span>
        </div>
        <div class="info-item">
          <span class="label">0手续费天数</span>
          <span class="value">{{ fundInfo.fee_free_limit || '--' }}天</span>
        </div>
      </div>
    </div>
    <div v-else class="loading-state">
      暂无数据
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  fundInfo: {
    code: string
    name: string
    fund_type: string
    ratio: number
    share_accuracy: number
    fee_free_limit: number
    latest_price: number
  } | null
}

defineProps<Props>()
</script>

<style scoped lang="scss">
.fund-info-card {
  background: white;
  border-radius: 12px;
  padding: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

  .card-content {
    .fund-name {
      font-size: 24px;
      color: #333;
      margin: 0 0 8px 0;
    }

    .fund-code {
      font-size: 16px;
      color: #666;
      margin-bottom: 24px;
    }

    .info-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
      gap: 6px;

      .info-item {
        display: flex;
        flex-direction: column;
        gap: 6px;

        .label {
          font-size: 14px;
          color: #999;
        }

        .value {
          font-size: 20px;
          font-weight: 600;
          color: #333;
        }
      }
    }
  }

  .loading-state {
    text-align: center;
    color: #999;
    padding: 40px;
  }
}
</style>
