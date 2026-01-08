import { ref } from 'vue'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'

export const useSideCardFilter = () => {
  const cardStore = useCardStore()

  const filterValue = ref('')

  const handleFilterInput = (e: Event) => {
    const target = e.target as HTMLInputElement
    filterValue.value = target.value
    cardStore.updateFilter(filterValue.value)
  }

  const clearFilter = () => {
    filterValue.value = ''
    cardStore.updateFilter('')
  }

  return { filterValue, handleFilterInput, clearFilter }
}
