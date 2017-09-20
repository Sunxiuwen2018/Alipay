#! /usr/bin/env python
# -*- coding: utf-8 -*-


class AlipayConfig(object):
    # app_id
    app_id = "2016081500252288"

    # 商户私钥
    merchant_private_key = ""

    # 支付宝公钥
    alipay_public_key = ""

    # 服务器异步通知页面路径 需http: // 格式的完整路径，不能加?id = 123 这类自定义参数，必须外网可以正常访问
    notify_url = "http://项目公网访问地址/alipay.trade.page.pay-JAVA-UTF-8/notify_url.jsp"

    # 页面跳转同步通知页面路径 需http: // 格式的完整路径，不能加?id = 123 这类自定义参数，必须外网可以正常访问
    return_url = "http://项目公网访问地址/alipay.trade.page.pay-JAVA-UTF-8/return_url.jsp"

    # 签名方式(当前只支持RSA和RSA2)
    sign_type = "RSA2"

    # 字符编码格式
    charset = "utf-8"

    # 支付宝网关(如果是线上环境的话, dev 这三个字去掉即可)
    gateway_url = "https://openapi.alipaydev.com/gateway.do"