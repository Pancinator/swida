<template>
  <Suspense>
    <template #default>
      <ModalNotification
        v-model:visible="showModal"
        :message="modalMessage"
        :variant="modalVariant"
      />
    </template>
    <template #fallback>
    </template>
  </Suspense>

  <div class="flex flex-wrap justify-center sm:justify-between mb-4">
    <div class="flex items-center space-x-2">
      <!-- Back button with arrow icon -->
      <NuxtLink
        to="/orders"
        class="inline-flex items-center bg-white border border-white text-indigo-600 px-4 py-2 rounded hover:border-indigo-600 transition"
      >
        <!-- Left arrow icon -->
        <svg
          class="w-4 h-4 mr-2"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
        Back to order list
      </NuxtLink>
    </div>
    <!-- Page Title -->
    <h1 class="text-3xl font-extrabold tracking-tight text-indigo-300">
      Create new order
    </h1>
  </div>
  <form @submit.prevent="submitOrder" class="space-y-6">
    <!-- Order Number -->
    <div>
      <label for="order_number" class="block text-gray-700 font-medium mb-2">
        Order Number
      </label>
      <input
        id="order_number"
        type="text"
        v-model="order.order_number"
        placeholder="Enter order number"
        class="border border-gray-300 rounded-lg py-2 px-4 w-full focus:outline-none focus:border-blue-500"
      />
    </div>

    <!-- Customer Name -->
    <div>
      <label for="customer_name" class="block text-gray-700 font-medium mb-2">
        Customer Name
      </label>
      <input
        id="customer_name"
        type="text"
        v-model="order.customer_name"
        placeholder="Enter customer name"
        class="border border-gray-300 rounded-lg py-2 px-4 w-full focus:outline-none focus:border-blue-500"
      />
    </div>

    <!-- Date -->
    <client-only>
      <Datepicker v-model:value="order.date" value-type="format" format="YYYY-MM-DD" :input-class="'w-full sm:w-64 border border-gray-300 rounded-lg py-2 pl-4 pr-10 w-full focus:outline-none focus:border-blue-500'"/>
    </client-only>

    <!-- Waypoints -->
    <div>
      <label class="block text-gray-700 font-medium mb-2">Waypoints</label>
      <div
        v-for="(wp, index) in order.waypoints"
        :key="index"
        class="mb-4 p-4 border border-gray-200 rounded-lg"
      >
        <div class="flex flex-col sm:flex-row sm:space-x-4">
          <!-- Waypoint Type -->
          <div class="flex-1 mb-2 sm:mb-0">
            <label :for="`waypoint-type-${index}`" class="block text-gray-600 mb-1">
              Type
            </label>
            <select
              :id="`waypoint-type-${index}`"
              v-model="wp.waypoint_type"
              class="border border-gray-300 rounded-lg py-2 px-4 w-full focus:outline-none focus:border-blue-500"
            >
              <option value="" disabled>Select type</option>
              <option value="Pickup">Pickup</option>
              <option value="Delivery">Delivery</option>
            </select>
          </div>
          <!-- Location -->
          <div class="flex-1">
            <label :for="`waypoint-location-${index}`" class="block text-gray-600 mb-1">
              Location
            </label>
            <input
              :id="`waypoint-location-${index}`"
              type="text"
              v-model="wp.location"
              placeholder="Enter location"
              class="border border-gray-300 rounded-lg py-2 px-4 w-full focus:outline-none focus:border-blue-500"
            />
          </div>
        </div>
        <!-- Remove Waypoint Button -->
        <button
          type="button"
          @click="removeWaypoint(index)"
          class="mt-2 text-red-600 hover:underline text-sm"
        >
          Remove waypoint
        </button>
      </div>
      <!-- Add Waypoint Button -->
      <button
        type="button"
        @click="addWaypoint"
        class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition"
      >
        Add Waypoint
      </button>
    </div>

    <!-- Submit Button -->
    <div>
      <button
        type="submit"
        class="w-full px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
      >
        Create Order
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, defineAsyncComponent } from 'vue'
import { createApiServiceFactory } from '~/api/orders'
import type { TransportOrder } from '~/interfaces/TransportOrderTypes'
import Datepicker from 'vue3-datepicker-next'
import 'vue-datepicker-next/index.css';
const ModalNotification = defineAsyncComponent(() =>
  import('~/components/modal.vue')
)

const apiService = createApiServiceFactory()

const order = ref<TransportOrder>({
  order_number: '',
  customer_name: '',
  date: null,
  waypoints: []  // start with an empty array; you can push an initial waypoint if desired
})
const showModal = ref(false)
const modalMessage = ref("")
const modalVariant = ref<"success" | "error" | "info">("success")

function addWaypoint() {
  order.value.waypoints.push({ waypoint_type: 'Delivery', location: '' })
}

function removeWaypoint(index: number) {
  if (order.value.waypoints.length > 1) {
    order.value.waypoints.splice(index, 1)
  }
}

async function submitOrder() {
  try {
    console.log("Submitting order:", order.value)
    const newOrder: TransportOrder = await apiService.createOrder(order.value)
    if (newOrder) {
      showModal.value = true
      modalMessage.value = "Transport order created!"
      modalVariant.value = "success"
      order.value = {
        order_number: '',
        customer_name: '',
        date: null,
        waypoints: []
      }
    }
  } catch (error) {
    console.error("Error creating order:", error)
    // On error: show error modal.
    showModal.value = true
    modalMessage.value = "Error creating order. Please try again."
    modalVariant.value = "error"
  }
}
</script>

<style scoped>
/* Optionally add additional custom styles */
</style>
