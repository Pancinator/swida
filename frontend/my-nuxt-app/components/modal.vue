<template>
  <transition name="fade">
    <div
      v-if="visible"
      class="fixed inset-0 flex items-center justify-center z-50 bg-transparent backdrop-blur-sm"
      @click.self="closeModal"
    >
      <div
        :class="modalClasses"
        class="px-10 py-6 rounded-lg shadow-xl transition-all duration-500"
      >
        <p class="text-center text-lg font-semibold">
          {{ message }}
        </p>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  variant: {
    type: String as () => 'success' | 'error' | 'info',
    default: 'success'
  },
  visible: {
    type: Boolean,
    default: false
  }
})

// Emit an update event for the visible prop so that the parent can change it (v-model)
const emit = defineEmits(['update:visible'])

function closeModal() {
  emit('update:visible', false)
}

const modalClasses = computed(() => {
  switch (props.variant) {
    case 'error':
      return 'bg-red-100 border border-red-400 text-red-700'
    case 'info':
      return 'bg-blue-100 border border-blue-400 text-blue-700'
    case 'success':
    default:
      return 'bg-green-100 border border-green-400 text-green-700'
  }
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
