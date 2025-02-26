import tailwindcss from "@tailwindcss/vite";
console.log('url: ', process.env.NUXT_ENV_API_URL)
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  runtimeConfig: {
    public: {
      backendURLServer: process.env.NUXT_ENV_API_URL || "http://web:8000/api", // SSR v Dockeri
      backendURL: "http://localhost:8000/api", // Prehliadač musí volať localhost
    }
  }

})
