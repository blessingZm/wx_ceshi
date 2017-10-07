# -*- coding: utf-8 -*-
from demo_dialog_reply.reply_event import replyWelcome
from demo_dialog_reply.reply_function import replyFunction
from demo_dialog_reply.reply_forecast import replyForecast
from demo_dialog_reply.reply_rain import replyRain
from demo_dialog_reply.reply_tulin import replyTulin
from demo_dialog_reply.reply_imginfo import replyImginfo


# REDIS 配置，请自行替换
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = 'foobared'
REDIS_DB = 0
# REDIS KEY的格式，会接收用户的open_id作为变量
REDIS_KEY = 'wechat-dialog:demo:%(open_id)s'

# 初始配置，根据用户信息分配对应的会话处理器
# 格式为(<匹配模式>, <处理函数>), 匹配模式为正则表达式
# 通过is_replay避免重复执行某段代码
# 通过raise UnexpectAnswer将某个不合法输入当做下一个输入的入口
ROUTER = {
    'text': [
        ('0', 'replyFunction'),
        ('1', 'replyForecast'),
        ('2', 'replyRain'),
        ('3', 'replyTulin'),
        ('.*', 'replyFunction')
    ],
    'event': [
        ('subscribe', 'replyWelcome'),
        ('.*', 'replyFunction')
    ],
    'image': [
        ('.*', 'replyImginfo')
    ],
}
