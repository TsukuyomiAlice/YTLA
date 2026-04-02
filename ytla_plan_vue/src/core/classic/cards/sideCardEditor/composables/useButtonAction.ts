export const useButtonAction = (emit: (e: 'click') => void) => {
  const handleClick = () => {
    emit('click')
  }

  return { handleClick }
}
