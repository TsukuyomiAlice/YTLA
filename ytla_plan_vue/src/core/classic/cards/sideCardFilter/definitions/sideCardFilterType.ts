export interface SideCardFilterProps {
  filterValue: string
  handleFilterInput: (e: Event) => void
  clearFilter: () => void
}

export interface SideCardFilterInputProps {
  value: string
  handleInput: (e: Event) => void
}

export interface SideCardFilterClearButtonProps {
  handleClear: () => void
}
