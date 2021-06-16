#coding:utf-8
from urllib.error import URLError
from urllib.request import urlopen

import re
import ssl


def decode_page(page_bytes, charsets=('utf-8',)):
    """通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)"""
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    """获取页面的HTML代码(通过递归实现指定次数的重试操作)"""
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    """从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)"""
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    url_list = [seed_url]
    # 通过下面的字典避免重复抓取并控制抓取深度
    visited_url_list = {seed_url: 0}
    while url_list:
        current_url = url_list.pop(0)
        depth = visited_url_list[current_url]
        if depth != max_depth:
            # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
            page_html = get_page_html(
                current_url, charsets=('utf-8', 'gbk', 'gb2312'))
            links_list = get_matched_parts(page_html, match_pattern)
            # print(links_list)
            # print(page_html)
            param_list = []
            for link in links_list:
                if link not in visited_url_list:
                    if not link.startswith('http'):
                        link = "http:"+link
                    visited_url_list[link] = depth + 1
                    page_html = get_page_html(
                        link, charsets=('utf-8', 'gbk', 'gb2312'))
                    headings = get_matched_parts(
                        page_html, r'<title>(.*)')
                    if headings:
                        param_list.append((headings[0], link))
    return param_list


def main():
    """主函数"""
    ssl._create_default_https_context = ssl._create_unverified_context
    param_list = start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]*href=["\'](.*?)["\']',
                max_depth=2)
    for num in range(len(param_list)):
        print(param_list[num])


if __name__ == '__main__':
    main()
