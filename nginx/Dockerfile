FROM nginx:alpine

# Copia Vue
COPY ./frontend/dist /usr/share/nginx/html/frontend

# Copia React
COPY ./gestao/dist /usr/share/nginx/html/gestao

# Copia configuração nginx
# COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
# COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
