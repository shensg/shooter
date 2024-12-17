# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

import requests
from config import CLOUDFLARE_TOKEN

# Zi-_vrNlld2lTNWu9UgYoH4F90lf1J375YXBMVTG
# hadestestg.com
# 区域ID：52bd583cff1d67ac479f169a777d3fac
# aalive.io
# 区域ID：cfebaf6fa3b331608aecee1da4f4d962
# curl -X GET "https://api.cloudflare.com/client/v4/user/tokens/verify" \
#      -H "Authorization: Bearer Zi-_vrNlld2lTNWu9UgYoH4F90lf1J375YXBMVTG" \
#      -H "Content-Type:application/json"

# curl -X POST "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/purge_cache" \
#      -H "Authorization: Bearer <API_TOKEN>" \
#      -H "Content-Type: application/json" \
#      --data '{"files":["https://example.com/file1.jpg", "https://example.com/file2.css"]}'

# 清掉整个域名的缓存
# curl -X POST "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/purge_cache" \
#      -H "Authorization: Bearer <API_TOKEN>" \
#      -H "Content-Type: application/json" \
#      --data '{"purge_everything":true}'

# curl --request POST \
#   --url https://api.cloudflare.com/client/v4/zones/zone_id/purge_cache \
#   --header 'Content-Type: application/json' \
#   --header 'X-Auth-Email: ' \
#   --data '{
#   "hosts": [
#     "www.example.com",
#     "images.example.com"
#   ]
# }'
# curl -X POST "https://api.cloudflare.com/client/v4/zones/52bd583cff1d67ac479f169a777d3fac/purge_cache" \
#      -H "Authorization: Bearer Zi-_vrNlld2lTNWu9UgYoH4F90lf1J375YXBMVTG" \
#      -H "Content-Type: application/json" \
#      --data '{"files":["https://h5.hadestestg.com/"]}'
# curl --request POST \
#   --url https://api.cloudflare.com/client/v4/zones/52bd583cff1d67ac479f169a777d3fac/purge_cache \
#   --header 'Content-Type: application/json' \
#   --header "Authorization: Bearer Zi-_vrNlld2lTNWu9UgYoH4F90lf1J375YXBMVTG" \
#   --data '{
#   "hosts": [
#     "h5.hadestestg.com"
#   ]
# }'

# curl -X POST "https://api.cloudflare.com/client/v4/zones/cfebaf6fa3b331608aecee1da4f4d962/purge_cache" -H "Authorization: Bearer Zi-_vrNlld2lTNWu9UgYoH4F90lf1J375YXBMVTG" -H "Content-Type: application/json" --data \'{"files":["https://h5.aalive.io/"]}\'

class Sample(object):
    def __int__(self):
        pass

    def refresh(self):
        pass









