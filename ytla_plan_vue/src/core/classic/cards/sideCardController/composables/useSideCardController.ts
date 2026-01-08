import { useSideCardFilter } from '@/core/classic/cards/sideCardFilter/composables/useSideCardFilter.ts'

export const useSideCardController = () => {

  const { filterValue, handleFilterInput, clearFilter } = useSideCardFilter()

  return { filterValue, handleFilterInput, clearFilter }
}
