from sys import flags

from django.shortcuts import render, HttpResponse, redirect
import json
from datetime import datetime
from django.http import JsonResponse
from django.db import connection

# Create your views here.
mycursor = connection.cursor()  # 获取游标对象


def index(request):
    pageNum = request.GET['page']
    return HttpResponse(f"页码：{pageNum}<br/><a href='https:www.bilibili.com' target='_blank'>bilibili</a>")


def getNews(request):
    list1 = [{'title': "那里的人为什么这么帅？", "date": "2022-10-11 10:23:22"},
             {'title': "广州官宣9月30日起全面取消楼市限购，会带来哪些影响？", "date": "2024-9-29 05:33:12"}]
    # 或者这种方式
    # str1js = json.dumps(list1)
    # return HttpResponse(str1js)
    return JsonResponse(list1, safe=False)


# 首页
def myhome(request):
    blog_name = "hello,testblog"
    L = [666, 777, 888]
    articleList = [{'title': "那里的包子大帝为什么这么帅？", "author": "唐超",
                    "date": datetime.strptime("2022-10-11 10:23:22", "%Y-%m-%d %H:%M:%S")},
                   {'title': "广州官宣9月30日起全面取消楼市限购，会带来哪些影响？", "author": "张三",
                    "date": datetime.strptime("2022-10-12 08:53:22", "%Y-%m-%d %H:%M:%S")},
                   {'title': "qwertyuiop？", "author": "李四",
                    "date": datetime.strptime("2022-10-13 04:13:22", "%Y-%m-%d %H:%M:%S")}]
    return render(request, 'index.html', {"blog_name": blog_name, "articleList": articleList, "L": L})


# 关于我
def aboutme(request):
    return render(request, 'aboutme.html')


# 注册页面
def register(request):
    return render(request, 'register.html')


# 注册功能
def regadd(request):
    userid = request.POST['userid']
    password = request.POST['password']
    username = request.POST['username']
    truename = request.POST['truename']
    sex = request.POST['sex']
    age = request.POST['age']
    print(userid, username, password, truename, sex, age)

    mycursor.execute('insert into userinfo(userID,username,password,truename,sex,age) values(%s,%s,%s,%s,%s,%s)',
                     (userid, username, password, truename, sex, age))
    return redirect('/userlist/')


# 用户列表
def userlist(request, curpage):
    pagesize = 2 if request.GET.get('pagesize') is None else int(request.GET.get('pagesize'))
    mypagestart = (int(curpage) - 1) * pagesize
    mycursor.execute('select * from userinfo limit %s,%s', (mypagestart, pagesize))
    myusers = mycursor.fetchall()
    myheads = [head[0] for head in mycursor.description]
    myusers2 = []
    for user in myusers:
        uo = zip(myheads, user)
        myusers2.append(dict(uo))
    myprev = 0
    if int(curpage) == 1:
        myprev = 1
    else:
        myprev = int(curpage) - 1

    # 获取总用户数
    mycursor.execute('SELECT COUNT(*) FROM userinfo')
    total_users = mycursor.fetchone()[0]
    # 计算总页数
    total_pages = (total_users + pagesize - 1) // pagesize
    mynext = int(curpage) + 1 if int(curpage) < total_pages else total_pages

    mypage = {'prev': myprev, 'next': mynext, 'last':total_pages,'pagesize': pagesize}
    return render(request, 'userlist.html', {'myusers2': myusers2, 'myheads': myheads, 'mypage': mypage})


def useredit(request):
    userid = request.GET['userid']
    print(userid)
    mycursor.execute('select * from userinfo where userid=%s', (userid,))
    curuser = mycursor.fetchone()
    print(curuser)
    return render(request, 'useredit.html', {"curuser": curuser})


def useredit_action(request):
    userid = request.POST['userid']
    password = request.POST['password']
    username = request.POST['username']
    truename = request.POST['truename']
    sex = request.POST['sex']
    age = request.POST['age']
    print(userid, username, password, truename, sex, age)
    mycursor.execute('update userinfo set username=%s,password=%s,truename=%s,sex=%s,age=%s where userid=%s',
                     (username, password, truename, sex, age, userid))
    return redirect('/userlist/')


def userdel_action(request, userid):
    mycursor.execute('delete from userinfo where userid=%s', (userid,))
    return redirect('/userlist/')
