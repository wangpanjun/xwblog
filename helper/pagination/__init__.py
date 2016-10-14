# coding=utf-8

import math

import re


class Pager:
    __totalRec = 0  # 总记录数
    __pageSize = 10  # 每页记录数
    __page = 1  # 当前页码
    __startNo = 0  # 开始记录号
    __endNo = 0  # 结束记录号
    __url = ''  # URL
    __pageCount = 1  # 总页数

    def __init__(self, total=0, page=1, pagesize=20, url=''):
        """
        @param total: 总记录数
        @param page: 当前页码
        @param pagesize: 每页记录数
        @param url: 当前请求URL
        """
        self.set_page(total, page, pagesize)
        self.__url = url

    def set_page(self, total, page, pagesize):

        """
        @param total: 总记录数
        @param page: 当前页码
        @param pagesize: 每页记录数
        """
        self.__totalRec = total
        self.__page = page
        self.__pageSize = pagesize
        self.__startNo = page * pagesize + 1
        self.__endNo = (page + 1) * pagesize
        self.__pageCount = int(math.ceil(self.__totalRec * 1.0 / self.__pageSize))

    def a(self, rec=5):
        if self.__page > 2:
            start = 1












    def start_no(self):
        """
        返回开始记录号
        """
        return self.__startNo

    def end_no(self):
        '''
        返回结束记录号
        '''
        return self.__endNo

    @property
    def page_count(self):
        return self.__pageCount

    def render_page_tag(self):

        '''
        生成页面分页标签
        '''
        # if not self.__totalRec or len(self.__url) < 1: return '';  # 没有总数或总数为0且不总输出，不输出
        if not self.__totalRec: return '';  # 没有总数或总数为0且不总输出，不输出
        page_num = self.__page
        page_size = self.__pageSize

        state = 1

        pagecount = self.page_count
        page = min(pagecount, self.__page)
        prepg = page - 1
        nextpg = 0

        page_html = ['<ul class="pagination">', '<li><a href="#"><<</a></li>']

        page_html.append('<li class="active"><a>' + str(page_num) + '</a>')

        if pagecount < 1: return ''
        pagenav = u"总数：<b>%s</b>&nbsp;" % self.__totalRec

        if prepg:
            pagenav += u"&nbsp;&nbsp;<a onclick='app_search(1,%(page_size)s,%(state)s)' href='#'>第一页</a>&nbsp;&nbsp;<a onclick='app_search(%(page_num)s,%(page_size)s,%(state)s)' href='#'>上一页</a>" % {
                'page_num': int(page_num) - 1, 'page_size': page_size, 'state': state}
        else:
            pagenav += u"&nbsp;&nbsp;<a href=\"#\">第一页</a>&nbsp;&nbsp;<a href=\"#\">上一页</a>"
        if int(page_num) < pagecount:
            param = {'page_num': int(page_num) + 1, 'page_size': page_size, 'state': state, 'pagecount': pagecount}
            pagenav += u"&nbsp;&nbsp;<a href='#' onclick='app_search(%(page_num)d, %(page_size)s, %(state)s)'>下一页</a>&nbsp;&nbsp;<a onclick='app_search(%(pagecount)d, %(page_size)s, %(state)s)' href='#'>尾页</a>" % param
        else:
            pagenav += u"&nbsp;&nbsp;<a href=\"#\">下一页</a>&nbsp;&nbsp;<a href=\"#\">尾页</a>&nbsp;"
        pagenav += u"&nbsp;&nbsp;页码：<b><font color=red>%(page)s</font>/%(pagecount)s</b>&nbsp;&nbsp;" % {
            'page': int(page_num),
            'pagecount': pagecount}

        page_html.append('</ul>')
        print "".join(page_html)
        return "".join(page_html)
