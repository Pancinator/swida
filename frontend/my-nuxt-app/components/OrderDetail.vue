<!-- components/OrderDetail.vue -->
<template>
  <div class="bg-white shadow-sm rounded-lg border border-gray-200 p-4 transition hover:shadow-md">
    <h2 class="text-lg sm:text-xl font-semibold mb-1 text-gray-800">
      {{ order.order_number }}
    </h2>
    <p class="text-gray-600 mb-1">Customer: {{ order.customer_name }}</p>
    <p class="text-gray-500 mb-2">Date: {{ order.date }}</p>
    <div>
      <h3 class="font-medium mb-1 text-gray-700">Waypoints:</h3>
      <ul class="list-disc list-inside text-gray-700">
        <li v-for="(wp, index) in order.waypoints" :key="index">
          {{ wp.waypoint_type }} – {{ wp.location }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
import type { TransportOrder } from '~/interfaces/TransportOrderTypes'

const props = defineProps<{
  order: TransportOrder
}>()
</script>
