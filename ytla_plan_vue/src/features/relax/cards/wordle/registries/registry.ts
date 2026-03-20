import WordleCard from '../components/WordleCard.vue'

export default {
  subType: 'wordle',
  component: WordleCard,
  getSubTypeProps: (card: any) => {
    return card
  }
}
