import { reactive } from 'vue'
// @ts-ignore
import { useRuntimeConfig } from '#app'
import type { TransportOrder, PaginatedResponse } from 'interfaces/TransportOrderTypes.js'
import { useFetch, useNuxtApp } from 'nuxt/app'

export function useTransportOrders() {
  const { $backendURL } = useNuxtApp()

  const state = reactive({
    orders: [] as TransportOrder[],
    totalCount: 0,
    nextUrl: null as string | null,
    previousUrl: null as string | null,
    currentPage: 1,
    pageSize: 10,
    status: '',
    error: ''
  })

  async function loadOrders(queryParams: Record<string, string> = { page: "1", date: "", customer_name: "" }) {
    try {
      console.log('query params: ', queryParams)
      const { data, status: fetchStatus, error: fetchError } = await useFetch<PaginatedResponse<TransportOrder>>(
        `/orders/`,
        // @ts-ignore
        { key: `orders-${queryParams.page}`, immediate: true, baseURL: $backendURL(), query: queryParams }
      )

      if (data.value) {
        state.orders = data.value.results
        state.totalCount = data.value.count
        state.nextUrl = data.value.next
        state.previousUrl = data.value.previous
        state.currentPage = parseInt(queryParams.page, 10)
      }

      // Convert fetchStatus and fetchError to strings
      state.status = fetchStatus.value
      state.error = fetchError.value?.message || ''
    } catch (err) {
      console.error('Error loading orders:', err)
    }
  }

  return {
    state,
    loadOrders
  }
}
