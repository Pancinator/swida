<template>
  <!-- Header + Search -->
  <div class="mb-4">
    <div class="flex flex-wrap justify-center sm:justify-between mb-4">
      <h1 class="text-lg w-full sm:w-auto text-center sm:text-3xl font-extrabold tracking-tight text-indigo-300">
        Transport Orders
      </h1>
      <NuxtLink
        to="/orders/create"
        class="inline-flex items-center bg-white border border-white text-indigo-600 px-4 py-2 rounded hover:border-indigo-600 transition"
      >
        Create order
        <svg
          class="h-4 w-4 ml-2"
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path
            fill-rule="evenodd"
            d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
            clip-rule="evenodd"
          />
        </svg>
      </NuxtLink>
    </div>
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
      <!-- Loader if pending -->
      <div v-if="state.status === 'pending'" class="text-center py-4">
        Loading...
      </div>
      <div v-else-if="state.error" class="text-red-500">
        {{ state.error }}
      </div>
      <div class="relative w-full flex flex-wrap justify-between">
        <input
          v-model="searchQuery"
          v-debounce:300ms="searchOrders"
          type="text"
          placeholder="Search by customer name.."
          class="mb-4 sm:mb-0 border border-gray-300 rounded-lg py-2 pl-10 pr-4 focus:outline-none focus:border-blue-500 w-full sm:w-64"
        />

        <client-only>
          <Datepicker
            v-model:value="selectedDate"
            placeholder="Search by date"
            value-type="format"
            format="YYYY-MM-DD"
            :input-class="'w-full sm:w-64 border border-gray-300 rounded-lg py-2 pl-4 pr-10 focus:outline-none focus:border-blue-500'"
          />
        </client-only>

        <svg
          class="w-5 h-5 text-gray-400 absolute left-3 top-2.5"
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path
            fill-rule="evenodd"
            d="M13.477 12.283a5.5 5.5 0 111.06-1.06l3.387 3.387a.75.75 0 11-1.06 1.06l-3.387-3.387zm-4.477 0a4 4 0 100-8 4 4 0 000 8z"
            clip-rule="evenodd"
          />
        </svg>
      </div>
    </div>
  </div>

  <div class="overflow-auto space-y-4 h-3/6 sm:h-4/6">
    <OrderDetail
      v-for="order in state.orders"
      :key="order.uuid"
      :order="order"
    />
  </div>

  <!-- Pagination -->
  <div class="flex justify-center items-center mt-4 space-x-2">
    <button
      class="bg-gray-200 px-3 py-1 rounded hover:bg-gray-300"
      :disabled="state.currentPage === 1"
      @click="goToPrevious"
    >
      Previous
    </button>
    <template v-for="page in pages" :key="page">
      <button
        @click="goToPage(page)"
        class="px-3 py-1 rounded transition"
        :class="state.currentPage === page ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'"
      >
        {{ page }}
      </button>
    </template>
    <button
      class="bg-gray-200 px-3 py-1 rounded hover:bg-gray-300"
      :disabled="state.currentPage === totalPages"
      @click="goToNext"
    >
      Next
    </button>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useTransportOrders } from '~/composables/useTransportOrders.js'
import Datepicker from 'vue3-datepicker-next'
import 'vue-datepicker-next/index.css'
import OrderDetail from '~/components/OrderDetail.vue'

// custom composable
const { state, loadOrders } = useTransportOrders()

// SSR
await loadOrders({ page: '1', date: '', customer_name: '' })

const searchQuery = ref('')
const selectedDate = ref('')
const totalPages = computed(() => {
  return state.totalCount ? Math.ceil(state.totalCount / state.pageSize) : 1
})

const pages = computed(() => {
  const arr: number[] = []
  for (let i = 1; i <= totalPages.value; i++) {
    arr.push(i)
  }
  return arr
})

const goToPage = (page: number) => {
  loadOrders({ page: page.toString(), date: '', customer_name: '' })
}

const goToNext = () => {
  if (state.nextUrl && state.currentPage < totalPages.value) {
    loadOrders({ page: (state.currentPage + 1).toString(), date: '', customer_name: '' })
  }
}

const goToPrevious = () => {
  if (state.previousUrl && state.currentPage > 1) {
    loadOrders({ page: (state.currentPage - 1).toString(), date: '', customer_name: '' })
  }
}

const searchOrders = () => {
  loadOrders({ page: state.currentPage.toString(), date: selectedDate.value, customer_name: searchQuery.value })
}

watch(selectedDate, (newDate, oldDate) => {
  if (newDate !== oldDate) {
    searchOrders()
  }
})
</script>

<script lang="ts">
import vueDebounce from 'vue-debounce'
export default {
  directives: {
    debounce: vueDebounce({ lock: true })
  }
}
</script>

<style>
/* Optional custom styles */
</style>
