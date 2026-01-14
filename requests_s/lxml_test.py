from lxml import etree

text='<div class="item-top__1Z3Zo"><div class="position__21iOS"><span style=""><div class="position__21iOS"><div class="p-top__1F7CL"><a id="openWinPostion" class="">C++资深开发工程师[北京·海淀区]</a></div><div class="p-bom__JlNur"><span class="money__3Lkgq">30k-60k</span>经验5-10年 / 本科</div></div></span></div><div class="company__2EsC8"><div class="company-name__2-SjF"><a class="">搜狐集团</a></div><div class="industry__1HBkr">内容资讯,游戏,音频｜视频媒体 / 上市公司 / 2000人以上</div></div><div class="com-logo__1QOwC"><img src="https://www.lgstatic.com/thumbnail_120x120/i/image3/M00/15/40/Cgq2xlpxrIKAPFRwAAAzLesdOpI884.png" alt="搜狐集团"></div></div>'

html=etree.HTML(text)

print(html.xpath('//a/@id'))