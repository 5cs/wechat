import requests
import json

def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    appid = ''
    secret = ''

    payload = {'grant_type': 'client_credential', 'appid': appid, 'secret': secret}
    r = requests.get(url, params=payload, verify=False)
    # print r.url
    # print r.text
    return json.loads(r.text)


def get_user_info(openid, access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/user/info'
    lang = 'zh_CN'
    
    payload = {'access_token': access_token, 'openid': openid, 'lang': lang}
    r = requests.get(url, params=payload, verify=False)
    print r.text

def set_industry(access_token):
     url = 'https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=' + access_token
     payload = {"industry_id1": "1", "industry_id2": "4"} 
     r = requests.post(url, json=payload, verify=False)
     print r.text

def get_industry(access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/template/get_industry?access_token=' + access_token
    r = requests.get(url, verify=False)
    print r.text

def get_template_id(access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=' + access_token
    payload = {'template_id_short': 'TM00001'}
    r = requests.post(url, json=payload, verify=False)
    print r.text

    url = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=' + access_token
    r = requests.get(url, verify=False)
    print r.text

def get_auto_reply_ways(access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/get_current_autoreply_info?access_token=' + access_token
    r = requests.get(url, verify=False)
    print r.text

def main():
    # openid = 'onjmIw5U9DChPXofpK8ZsylR-z38'
    openid = 'oVMbfvg0Jj_9Du8AkENGsvcbHKuU'
    response = get_access_token()
    access_token = response['access_token'].encode('ascii')
    print access_token
    print '-'*63
    get_user_info(openid, access_token)
    # print '-'*63  # one time each month
    # set_industry(access_token)
    print '-'*63
    get_industry(access_token)
    print '-'*63
    get_template_id(access_token)
    print '-'*63
    get_auto_reply_ways(access_token)


if __name__ == '__main__':
    main()
