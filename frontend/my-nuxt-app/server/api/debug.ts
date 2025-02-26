export default defineEventHandler((event) => {
  const config = useRuntimeConfig();
  return { apiBase: config.public.apiBase };
});