# Author: Klaus
# Date: 2022/9/27 16:28
import requests, re, execjs, datetime, os
from urllib import parse

if __name__ == "__main__":
    uname = os.environ["USERNAME"]
    pw = os.environ["PASSWORD"]
    telephone = os.environ["TELEPHONE"]
    ## 登录部分
    urlBegin = 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/'
    login_url = 'https://login.bit.edu.cn/authserver/login'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        "uer-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        'Referer': 'https://login.bit.edu.cn/authserver/login',

    }
    session = requests.session()
    get_login = session.get(login_url)
    get_login.encoding = 'utf-8'
    salt = re.search('id="pwdEncryptSalt" value="(.*?)"', get_login.text).group(1)
    execution = re.search('name="execution" value="(.*?)"', get_login.text).group(1)
    # print(salt)
    # print(execution)


    f = open("./encrypt.js", 'r', encoding='UTF-8')
    line = f.readline()
    js = ''
    while line:
        js = js + line
        line = f.readline()
    ctx = execjs.compile(js)
    password = ctx.call('encryptPassword', pw, salt)
    # print(password)

    personal_info = {'username': uname,
                     'password': password,
                     '_eventId': 'submit',
                     'cllt': 'userNameLogin',
                     'dllt': 'generalLogin',
                     'lt': None,
                     # 'captcha': None,
                     'execution': execution,
                     }

    res = session.post(url=login_url, headers=headers, data=personal_info)
    res.encoding = 'utf-8'
    if re.search("姓名", res.text):
        print('登陆成功')
    else:
        print('登录失败')


    ## 获取cookie
    cookie_url = 'http://stu.bit.edu.cn/xsfw/sys/swpubapp/indexmenu/getAppConfig.do?appId=4810794463325921&appName=xsqjapp'
    get_cookie = session.get(cookie_url)
    cookie = requests.utils.dict_from_cookiejar(session.cookies)
    c = ""
    for (key, value) in cookie.items():
        c += key + "=" + value + "; "

    header = {'Referer': 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/*default/index.do',
                   'Cookie': c}
    print(c)

    ## 销假
    get_xj_url = 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/modules/wdqj/wdqjbg.do'
    get_xj_info = {
        'XSBH': str(uname),
        'pageSize': '10',
        'pageNumber': '1',
    }
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     # 'Content-Length': '40',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'Host': 'stu.bit.edu.cn',
    #     'Origin': 'http://stu.bit.edu.cn',
    #     "uer-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    #     'Referer': 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/*default/index.do',
    #     'X-Requested-With': 'XMLHttpRequest',
    #
    # }
    qj_text = session.post(get_xj_url, get_xj_info, headers=header).text
    print(qj_text)
    ex = '"SQBH":"(.*?)".*?"XJZT":"0"'
    xj_list = re.findall(ex, qj_text,re.S)
    print(xj_list)
    if len(xj_list) > 0 :
        print('存在未销假记录：' + xj_list[0])
        xj_url = 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/modules/leaveAudit/removeLeaveInfo.do'
        xjrq = str(datetime.datetime.now()).split(' ')[0]
        xj_data = {"XJRQ":xjrq,"XJSM":"返校","SQBH":xj_list[0]}
        xj_data_formdata = parse.urlencode({'data': xj_data})
        header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
        try:
            xj_res = session.post(xj_url, data=xj_data_formdata, headers=header)
        except:
            print("销假超时!")

        if "成功" in xj_res.text:
            print('销假成功!')
        else:
            print("销假失败!")
            print(xj_res.text)

    ## 请假
    qj_url = 'http://stu.bit.edu.cn/xsfw/sys/xsqjapp/modules/leaveApply/addLeaveApply.do'
    qj_data = {"QJXZ_DISPLAY":"因公请假","QJXZ":"2","QJLX_DISPLAY":"2022秋季学期进出校","QJLX":"ba4a95d3aaa6497f9d042ff7ef0989b2","SQSM":"","QJKSRQ":"","QJJSRQ":"","QJTS":1,"YL1_DISPLAY":"科研需求","YL1":"2dafc849555e4de7913b674279633df0","YL2":"","YL3":"国防科技园","YL4_DISPLAY":"单车/摩托车","YL4":"2","YL5":"2022-09-29 06:00:00","YL6":"2022-09-29 23:00:00","YL7_DISPLAY":"否","YL7":"0","YL8":"","QJSY":"前往国防科技园","ZMCL":"","SJH":str(telephone),"SQBH":"","XSBH":"","QJRQ":"2022-09-29","BEGINDATE":"2022-09-29"}
    now_time = datetime.datetime.now()
    qj_data["YL5"] = (now_time + datetime.timedelta(days=+1)).strftime("%Y-%m-%d 06:00:00")
    qj_data["YL6"] = (now_time + datetime.timedelta(days=+1)).strftime("%Y-%m-%d 23:30:00")
    qj_data["QJRQ"] = str((now_time + datetime.timedelta(days=+1))).split(' ')[0]
    qj_data["BEGINDATE"] = qj_data["QJRQ"]
    print(qj_data)
    header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    FormData = {'data': qj_data}
    data = parse.urlencode(FormData)
    try:
        qj_res = session.post(qj_url, data=data, headers=header)
    except:
        print("上报超时!")

    if "成功" in qj_res.text:
        print('请假成功!')
    else:
        print("请假失败!")
        print(qj_res.text)
