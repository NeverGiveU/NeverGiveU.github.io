# -*- coding:utf-8 -*-


"""

@author: Chopin
@file: index.py
@time: 2018/7/21 8:51
"""

from flask import Flask, make_response, render_template, request, send_file

import uuid
import datetime
import simplejson

class G:
    succeeded_total_num = 0
    failed_total_num = 0
    signal = 3

app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello(name=None):
    response = make_response(render_template('index.html', name=name))
    if request.cookies.get('id') is None:
        outdate = datetime.datetime.today() + datetime.timedelta(days=30)
        response.set_cookie('id', str(uuid.uuid4()), expire=outdate)
    else:
        pass
    return response
@app.route('/login', methods=['POST', 'GET'])
@app.route('/hello/login', methods=['POST', 'GET'])
def goto_login():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录小黑の空间</title>
    <link rel="icon" href="../static/src/favicon.ico" type="image/x-icon" />
    <link rel="shortcut icon" href="../static/src/favicon.ico" type="image/x-icon"/>
    
    <script src="http://libs.baidu.com/jquery/1.8.3/jquery.min.js"></script>
    <link href="../static/css/index.css" rel="stylesheet" type="text/css"/>
    <link href="../static/css/login.css" rel="stylesheet" type="text/css"/>
</head>
<body background="../static/images/bg.jpg">
    <div class="snow">
        <div id='password'>
            <p id="code" ><b>幸运代码</b></p>
            <p id="verbar">|</p>
            <input type='password' id='coding' style='padding-left: 5%'>
            <a id='cod_ent' style='text-decoration:none'>Submit</a>
        </div>
        <a id='enter' href='main3'><img src='../static/src/Bcat_smile.png' id='enterimg'></img></a>
        
    </div>
	<script src="../static/js/login.js"></script>
</body>
</html>
    """
@app.route("/daily", methods=['POST', 'GET'])
@app.route("/hello/daily", methods=['POST', 'GET'])
def daily():
    sig = request.args.get('signal')
    if sig == '752025':
        return simplejson.dumps({
            'permission': 1
        })
    elif sig == 'chopin':
        return simplejson.dumps({
            'permission': 0
        })
    else:
        return simplejson.dumps({
            'permission': -1
        })

@app.route('/fish', methods=['POST', 'GET'])
def fish():
    sig = request.args.get('signal')
    G.signal = int(sig)
    return 'SUCCESS'

@app.route(('/main3'))
@app.route(('/hello/main3'))
def main3():
    return render_template('daily.html')

@app.route('/chopin/')
@app.route('/hello/chopin')
def chopin():
    return render_template('chopin-answer-platform.html')

@app.route('/fresh', methods=['POST', 'GET'])
@app.route('/hello/fresh', methods=['POST', 'GET'])
def refresh():
    command = request.args.get('require')
    if command == 'refresh':
        daily_history = []
        #item = {'time':"", 'user':"", 'content':""}
        with open('static/images/forusers/752025/daily.txt', 'r', encoding='UTF-8') as f:
            line = f.readline()

            while line:
                if line is not "\n":
                    arr = line.split("@")
                    time = arr[0]
                    user = arr[1]
                    arr = arr[2:]
                    content = ""
                    if len(arr) >= 2:
                        for i in range(len(arr-1)):
                            content = content + arr[i] + "@"
                        content += arr[len(arr)-1]
                    else:
                        content += arr[len(arr)-1]
                    '''
                    item['time'] = time
                    item['user'] = name
                    item['content'] = content
                    '''
                    item = {'time': time, 'user': user, 'content': content}
                    daily_history.append(item)

                line = f.readline()
        f.close()
        # print(daily_history)
        return simplejson.dumps({
            'history': daily_history
        })
    elif command == "add":
        user = request.args.get('user')
        content = request.args.get('content')
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
        val = nowTime + '@' + user + '@' + content + '\n';
        # print(val)

        item = {'time': nowTime, 'user': user, 'content': content}
        f = open('static/images/forusers/752025/daily.txt', 'a', encoding='UTF-8')
        f.write(val)
        f.close()
        return simplejson.dumps({
            'item': item
        })
    #print(command)
    return "Wrong"

if __name__ == '__main__':
    app.run(debug=True)