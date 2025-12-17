<template>
  <SideCard
    :span-columns="2"
    :card-id="cardId"
    :name="name"
    :icon="iconPath"
    :background="background"
    :tags="tags"
    :description="description"
    :showIcon=false
    :showTitle=false
    :showTags=false
    :showSettings=true
    :showDeactivate=false
    :showClose=true
    @settings="handleEdit"
  >

    <template #top-left-actions></template>
    <template #top-actions></template>

    <template #card-content>

    </template>

    <template #left-actions-buttons>

    </template>

    <template #right-actions></template>

    <template #secondary-content>
      <div class="wordle-container">
        <!-- 游戏主界面 -->
        <div class="grid-container">
          <div
            v-for="(row, rowIndex) in guesses"
            :key="rowIndex"
            class="grid-row"
          >
            <div
              v-for="(letter, colIndex) in row"
              :key="colIndex"
              class="letter-tile"
              :class="getTileState(rowIndex, colIndex)"
            >
              {{ letter }}
            </div>
          </div>
        </div>

        <!-- 键盘区域 -->
        <div class="keyboard">
          <div class="keyboard-row" v-for="(row, index) in keyboardLayout" :key="index">
            <button
              v-for="key in row"
              :key="key"
              class="key"
              @click="handleKeyPress(key)"
              :disabled="gameOver"
            >
              {{ key }}
            </button>
          </div>
        </div>

        <!-- 游戏状态反馈 -->
        <div v-if="feedback" class="feedback" :class="feedbackType">
          {{ feedback }}
          <button v-if="gameOver" @click="resetGame" class="replay-btn">再玩一次</button>
        </div>
      </div>
    </template>

  </SideCard>
</template>
<script setup lang="ts">
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import type { WordleCardData } from '@/features/relax/cards/wordle/types/cardDataType.ts'

const props = defineProps({
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String
})

const handleEdit = () => {
  const { showEdit } = useSideCardEditor()
  showEdit({
    card_id: props.cardId,
    card_sub_type: 'wordle'
  } as WordleCardData)
}

import { ref, reactive, computed, onMounted } from 'vue'

// 游戏状态
const answer = ref('')
const guesses = reactive(Array(6).fill('').map(() => Array(5).fill('')))
const currentGuess = ref(0)
const feedback = ref('')
const feedbackType = ref('')
const gameOver = ref(false)

// 键盘布局
const keyboardLayout = [
  ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
  ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
  ['Enter', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '⌫']
]

const validWords = [
  'APPLE', 'BEACH', 'BRAIN', 'BREAD', 'CHAIR', 'CLOUD', 'DREAM', 'EARTH', 'FAITH', 'FRUIT',
  'GRAPE', 'HAPPY', 'HEART', 'HOTEL', 'HOUSE', 'JUICE', 'LIGHT', 'MONEY', 'MUSIC', 'NIGHT',
  'OCEAN', 'PARTY', 'PIANO', 'POWER', 'QUEEN', 'RIVER', 'SMILE', 'SUGAR', 'TABLE', 'TRAIN',
  'UNITY', 'VITAL', 'WATER', 'WHALE', 'YOUTH',
  'ABOUT', 'ACTOR', 'ADAPT', 'ADOBE', 'ADOPT', 'ADORE', 'AGENT', 'ALARM', 'ALBUM', 'ALERT',
  'ALIEN', 'ALIKE', 'ALIVE', 'ALLOW', 'ALOHA', 'ALPHA', 'AMBER', 'ANGEL', 'ANGER', 'ANGRY',
  'ANIME', 'APART', 'ARISE', 'ARROW', 'AUDIO', 'AWAKE', 'AWARD', 'AWARE', 'BACON', 'BASIC',
  'BEACH', 'BEARD', 'BEAST', 'BEGIN', 'BERRY', 'BIRTH', 'BLACK', 'BLADE', 'BLAST', 'BLEND',
  'BLINK', 'BLOCK', 'BLOOM', 'BLUFF', 'BLUSH', 'BOOST', 'BRAVE', 'BREAD', 'BREAK', 'BRICK',
  'BRIDE', 'BROWN', 'BUDDY', 'BUILD', 'BUNNY', 'CABIN', 'CANDY', 'CARGO', 'CHARM', 'CHASE',
  'CHEAT', 'CHESS', 'CHILL', 'CHIME', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK',
  'CLIFF', 'CLIMB', 'CLOCK', 'CLOUD', 'COAST', 'COMET', 'COMFY', 'COMIC', 'CRASH', 'CRISP',
  'CROWN', 'CURVE', 'DAISY', 'DANCE', 'DELAY', 'DIARY', 'DIGIT', 'DITTO', 'DIZZY', 'DONOR',
  'DOUBT', 'DRAFT', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'DUTCH', 'EAGLE', 'EARLY', 'EBONY',
  'EJECT', 'ELBOW', 'ELDER', 'ELITE', 'EMPTY', 'ENJOY', 'ENTRY', 'EQUAL', 'ERROR', 'ESSAY',
  'EVENT', 'EVERY', 'EXACT', 'EXCEL', 'EXIST', 'EXTRA', 'FABLE', 'FANCY', 'FAULT', 'FERRY',
  'FIBER', 'FIELD', 'FIFTH', 'FINAL', 'FLAIR', 'FLAME', 'FLASH', 'FLICK', 'FLING', 'FLOOD',
  'FLOOR', 'FLUFF', 'FOCUS', 'FORCE', 'FRAME', 'FRESH', 'FRONT', 'FROST', 'FUNNY', 'GHOST',
  'GIANT', 'GLASS', 'GLOBE', 'GLOVE', 'GRAIN', 'GRAND', 'GRASS', 'GREAT', 'GREEN', 'GROUP',
  'GUARD', 'GUEST', 'GUIDE', 'HABIT', 'HAPPY', 'HEAVY', 'HELIX', 'HONEY', 'HORSE', 'HUMAN',
  'HUMOR', 'HURRY', 'HYPER', 'IDEAL', 'IGLOO', 'IMAGE', 'IVORY', 'JELLY', 'JEWEL', 'JOINT',
  'JOKER', 'JUDGE', 'JUICE', 'KARMA', 'KAYAK', 'KEBAB', 'KINKY', 'KIOSK', 'KITTY', 'KNOCK',
  'LABEL', 'LARGE', 'LAUGH', 'LEARN', 'LEMON', 'LEVEL', 'LIGHT', 'LUCKY', 'LUNAR', 'MAGIC',
  'MAJOR', 'MANGO', 'MAPLE', 'MARCH', 'MEDAL', 'MERCY', 'MERGE', 'METAL', 'METER', 'MIDST',
  'MIXER', 'MODEL', 'MOIST', 'MONEY', 'MONTH', 'MOSSY', 'MOTOR', 'MOUNT', 'MOUSE', 'MOVIE',
  'MUSIC', 'NASTY', 'NIGHT', 'NOBLE', 'NOISE', 'NOVEL', 'NURSE', 'OCEAN', 'OLIVE', 'OPERA',
  'ORBIT', 'ORDER', 'OTHER', 'OUTDO', 'PAGER', 'PANDA', 'PANEL', 'PEACH', 'PEARL', 'PHASE',
  'PHONE', 'PHOTO', 'PIANO', 'PILOT', 'PIXEL', 'PIZZA', 'PLANE', 'PLANT', 'PLATE', 'PLAZA',
  'PLUCK', 'POINT', 'POKER', 'POLAR', 'POUND', 'POWER', 'PRIME', 'PROUD', 'PUPPY',
  'PURSE', 'QUACK', 'QUARK', 'QUEEN', 'QUICK', 'QUIET', 'RADAR', 'RADIO', 'RAINY', 'RALLY',
  'RAPID', 'REACH', 'REACT', 'REALM', 'REBEL', 'RHYME', 'RIVER', 'ROBOT', 'ROYAL', 'RUMOR',
  'SALAD', 'SAUCE', 'SCALE', 'SCARF', 'SCOUT', 'SERVE', 'SHADE', 'SHAKE', 'SHAPE', 'SHARK',
  'SHEEP', 'SHEET', 'SHELF', 'SHELL', 'SHINE', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SIGHT',
  'SILLY', 'SINCE', 'SKILL', 'SLEEP', 'SLICE', 'SLIDE', 'SMART', 'SMILE', 'SMOKE', 'SNAKE',
  'SNOWY', 'SOFTY', 'SOLAR', 'SOLID', 'SOUND', 'SPACE', 'SPARK', 'SPEED', 'SPICE', 'SPIKE',
  'SPOON', 'SPORT', 'SQUAD', 'STACK', 'STAFF', 'STAGE', 'STAND', 'STARK', 'START', 'STATE',
  'STEAM', 'STEEL', 'STICK', 'STONE', 'STOOL', 'STORY', 'STUDY', 'SUGAR', 'SUPER', 'SWEET',
  'SWIFT', 'SWING', 'TABLE', 'TASTE', 'TEACH', 'TENTH', 'THEME', 'THERE', 'THICK',
  'THINK', 'THIRD', 'THORN', 'TIGER', 'TODAY', 'TOKEN', 'TOOTH', 'TOUCH', 'TOWER', 'TRAIN',
  'TREND', 'TRIBE', 'TRICK', 'TROUT', 'TRUCK', 'TRUST', 'TRUTH', 'TULIP', 'TWICE', 'UNCLE',
  'UNDER', 'UNITY', 'URBAN', 'USAGE', 'USHER', 'VALID', 'VALUE', 'VAPOR', 'VENOM', 'VIDEO',
  'VILLA', 'VINYL', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'VOTER', 'WACKY', 'WAIST',
  'WASTE', 'WATCH', 'WATER', 'WEARY', 'WHALE', 'WHEAT', 'WHEEL', 'WHERE', 'WHITE', 'WHOLE',
  'WINDY', 'WOMAN', 'WORLD', 'WORRY', 'YACHT', 'YEARN', 'YOUTH', 'ZEBRA'
]

// 判断格子状态
const getTileState = (row: number, col: number) => {
  if (row >= currentGuess.value) return ''
  const guessLetter = guesses[row][col]
  const answerLetter = answer.value[col]

  if (guessLetter === answerLetter) return 'correct'
  if (answer.value.includes(guessLetter)) return 'present'
  return 'absent'
}

// 处理按键
const handleKeyPress = (key: string) => {
  if (gameOver.value) return

  if (key === '⌫') {
    deleteLetter()
  } else if (key === 'Enter') {
    submitGuess()
  } else if (/^[A-Z]$/.test(key)) {
    addLetter(key)
  }
}

// 添加字母
const addLetter = (letter: string) => {
  const currentRow = guesses[currentGuess.value]
  const firstEmptyIndex = currentRow.findIndex(cell => cell === '')
  if (firstEmptyIndex !== -1) {
    currentRow[firstEmptyIndex] = letter
  }
}

// 删除字母
const deleteLetter = () => {
  const currentRow = guesses[currentGuess.value]
  let lastFilledIndex = -1
  for (let i = currentRow.length - 1; i >= 0; i--) {
    if (currentRow[i] !== '') {
      lastFilledIndex = i
      break
    }
  }
  if (lastFilledIndex !== -1) {
    currentRow[lastFilledIndex] = ''
  }
}

// 提交猜测
const submitGuess = () => {
  const guess = guesses[currentGuess.value].join('')
  if (guess.length < 5) {
    showFeedback('单词长度不够', 'error')
    return
  }

  // 这里可以添加真实的单词校验（需要API）
  currentGuess.value++

  if (guess === answer.value) {
    showFeedback('恭喜你猜对了！🎉', 'success')
    gameOver.value = true
  } else if (currentGuess.value === 6) {
    showFeedback(`游戏结束，正确答案是：${answer.value}`, 'error')
    gameOver.value = true
  }
}

// 显示反馈
const showFeedback = (message: string, type: string) => {
  feedback.value = message
  feedbackType.value = type
}

// 初始化游戏
onMounted(() => {
  initAnswer()
})

// 随机选择答案
const initAnswer = () => {
  answer.value = validWords[Math.floor(Math.random() * validWords.length)]
}


// 重置游戏
const resetGame = () => {
  guesses.splice(0, guesses.length, ...Array(6).fill('').map(() => Array(5).fill('')))
  currentGuess.value = 0
  feedback.value = ''
  gameOver.value = false
  initAnswer() // 添加重新初始化的调用
}
</script>

<style scoped lang="scss">

.wordle-container {
  padding: 1rem;
  max-width: 500px;
  margin: 0 auto;
}

.grid-container {
  display: grid;
  gap: 5px;
  margin-bottom: 1.5rem;
}

.grid-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 5px;
}

.letter-tile {
  aspect-ratio: 1;
  border: 2px solid #d3d6da;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  text-transform: uppercase;

  &.correct {
    background: #6aaa64;
    border-color: #6aaa64;
    color: white;
  }

  &.present {
    background: #c9b458;
    border-color: #c9b458;
    color: white;
  }

  &.absent {
    background: #787c7e;
    border-color: #787c7e;
    color: white;
  }
}

.keyboard {
  display: grid;
  gap: 5px;
  margin-top: 20px;
}

.keyboard-row {
  display: flex;
  justify-content: center;
  gap: 5px;
}

.key {
  padding: 0.8rem;
  border: none;
  border-radius: 4px;
  background: #d3d6da;
  cursor: pointer;
  font-weight: bold;
  text-transform: uppercase;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  &:active:not(:disabled) {
    transform: scale(0.95);
  }
}

.feedback {
  margin-top: 1rem;
  padding: 1rem;
  border-radius: 4px;
  text-align: center;

  &.success {
    background: #6aaa64;
    color: white;
  }

  &.error {
    background: #ff6961;
    color: white;
  }
}

.replay-btn {
  margin-left: 1rem;
  padding: 0.5rem 1rem;
  background: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
