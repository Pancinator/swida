FROM node:20.18-alpine as builder
WORKDIR /app

COPY my-nuxt-app/package*.json ./
RUN npm install

COPY my-nuxt-app/ ./
RUN npm run build

FROM node:20.18-alpine
WORKDIR /app
COPY --from=builder /app ./
EXPOSE 3000
CMD ["npm", "start"]
