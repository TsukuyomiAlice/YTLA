export const useButtonScale = (emit: (e: 'click') => void) => {
  const handleClick = () => {
    emit('click')
  }

  return { handleClick }
}
