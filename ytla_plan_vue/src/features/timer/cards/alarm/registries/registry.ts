import AlarmCard from '../components/AlarmCard.vue'
import type { AlarmCardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'alarm',
  component: AlarmCard,
  getSubTypeProps: (card: any) => {
    const alarmCard = card as AlarmCardData
    return {
      alarmTime: alarmCard.alarm_time,
      alarmDays: alarmCard.alarm_days,
      startTime: alarmCard.start_time
    }
  }
}
