export const useButtonAdd = (emit: (event: 'click') => void) => {

  const handleClick = () => {
    emit('click')
  }

  return {
    handleClick
  }
}
