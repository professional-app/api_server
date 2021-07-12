FROM httpd:2.4.48-alpine

COPY ./api_project /var/www/html/api_project
ADD ./docker/httpd.conf /usr/local/apache2/conf/httpd.conf
ADD ./docker/entrypoint.sh /entrypoint.sh
ADD ./requirements.txt /tmp/requirements.txt
RUN chmod +x /entrypoint.sh

RUN apk update \
    && apk add --no-cache python3-dev==3.9.5-r1 py3-pip postgresql-dev \
    && apk add --no-cache --virtual build-deps gcc musl-dev apache2-mod-wsgi \
    && pip3 install --no-cache-dir -r /tmp/requirements.txt \
    && cp /usr/lib/apache2/mod_wsgi.so /usr/local/apache2/modules/ \
    && apk del --purge build-deps

EXPOSE 80

CMD ["httpd-foreground"]
ENTRYPOINT ["/entrypoint.sh"]
