<template>
  <!-- Full-page flex layout -->
  <div class="flex flex-col h-screen">
    <!-- Header -->
    <header class="bg-indigo-50 text-indigo-500 p-4 flex items-center">
      <!-- Car icon (SVG) -->
      <svg
        class="h-6 w-6 mr-2"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M5 13l1.5 3h11l1.5-3m-1.5-3l-1.5-3h-6l-1.5 3m-7.5 3h18"
        />
      </svg>
      <span class="font-bold text-sm sm:text-lg">
        Transport Order Management System
      </span>
    </header>

    <!-- Main content area, scrollable if content is large -->
    <main class="flex-1 overflow-auto w-full max-w-3xl mx-auto p-4 relative">
      <NuxtRouteAnnouncer />
      <NuxtPage />
    </main>

    <!-- Footer -->
    <footer class="bg-indigo-50 text-indigo-500 p-4 text-center">
      © 2023 Matej Pancak
    </footer>
  </div>
</template>

<script setup lang="ts">
// No additional logic needed for a global layout
</script>

<style>
/* No extra styles needed; using Tailwind classes */
</style>
