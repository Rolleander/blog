FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY rol-ost.de_ssl_certificate.cer /etc/nginx/cert.cer
COPY _.rol-ost.de_private_key.key /etc/nginx/key.key