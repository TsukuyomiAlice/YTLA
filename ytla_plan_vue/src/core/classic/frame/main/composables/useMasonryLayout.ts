import { onMounted, onUnmounted } from 'vue'

const debounce = (fn: (...args: unknown[]) => void, delay: number) => {
  let timeoutId: number
  return (...args: unknown[]) => {
    clearTimeout(timeoutId)
    timeoutId = setTimeout(() => fn(...args), delay)
  }
}

export const useMasonryLayout = () => {
  const updateColumns = () => {
    const container = document.querySelector('.masonry-container')
    if (!container) return

    const width = container.clientWidth
    let columns = 1
    if (width >= 661) columns = 3
    else if (width >= 441) columns = 2

    document.documentElement.style.setProperty('--columns', columns.toString())
  }

  const debouncedUpdate = debounce(updateColumns, 200)

  onMounted(() => {
    updateColumns()
    window.addEventListener('resize', debouncedUpdate)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', debouncedUpdate)
  })

  return { debouncedUpdate }
}
