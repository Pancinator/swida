import { useRuntimeConfig, defineNuxtPlugin } from '#app'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();
  // Set backend url -> SSR/Docker related
  nuxtApp.provide("backendURL", () => {
    if (import.meta.server) {
      return config.public.backendURLServer;
    } else {
      return config.public.backendURL;
    }
  });
});
