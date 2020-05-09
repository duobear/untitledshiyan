# coding=utf-8
import time
from splinter import Browser


def login_mail(url):
    browser = Browser()
    # login 163 email websize
    browser.visit(url)
    # wait web element loading
    # fill in account and password
    browser.find_by_id('username').fill('shshgogo')
    browser.find_by_id('password').fill('zxcv1234')
    # click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(5)
    # close the window of brower
    browser.quit()


if __name__ == '__main__':
    mail_addr = 'https://mail.163.com/'
    login_mail(mail_addr)