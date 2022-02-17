#!/usr/bin/env sh

python /opt/textmatch/manage.py collectstatic --no-input
python /opt/textmatch/manage.py migrate

hypercorn -b 0.0.0.0:${PORT} asgi:application
