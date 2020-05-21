import sys, os, re, time
import urllib.request as req
import urllib.parse as parse
import json

PHOTOZOU_API = "https://api.photozou.jp/rest/serch_public.json"
CACHE_DIR = "./image/cache"

#　フォト蔵のAPIを利用して画像を検索する
def serch_photo(keyword, offset=0, limit=100):
    # APIのクエリを組み立てる
    keyword_enc = parse.quote_plus(keyword)
    q = "keyword={0}&offset={1}&limit={2}".format(
        keyword_enc, offset, limit)
    url = PHOTOZOU_API