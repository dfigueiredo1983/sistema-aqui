# Build
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Serve with Nginx
FROM nginx:alpine

# Criar diretório gestao
RUN mkdir -p /usr/share/nginx/html/gestao

# Copiar build para o diretório do Nginx
COPY --from=build /app/dist /usr/share/nginx/html/gestao

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
