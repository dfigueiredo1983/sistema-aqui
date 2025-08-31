FROM nginx:alpine

# Remove o arquivo index.html padrão do Nginx para evitar conflitos
RUN rm /usr/share/nginx/html/index.html

# Copia configuração nginx
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# Copia Vue
COPY ./frontend/dist /usr/share/nginx/html/frontend

# Copia React
COPY ./gestao/dist /usr/share/nginx/html/gestao

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
