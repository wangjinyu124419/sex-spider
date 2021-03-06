# 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import hashlib
import http.client
import json
import random
import urllib

from config import appid, secretKey

appid = appid  # 填写你的appid
secretKey = secretKey  # 填写你的密钥
myurl = '/api/trans/vip/translate'
fromLang = 'auto'  # 原文语种
toLang = 'zh'  # 译文语种
salt = random.randint(32768, 65536)


def baidu_tranlate(q):
    httpClient = None
    try:
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        translateurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', translateurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        dst = result['trans_result'][0]['dst']
        print(result)
        return dst
    except Exception as e:
        print(e)
        return ''
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    res = baidu_tranlate('test')
    print(res)
