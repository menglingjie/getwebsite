#gethttp

这是一个下载网站的小脚本

## 用法

### 下载网站
````bash
python get_web_site.py get http:// 网站host /网页路径 匹配模式
````
例子
````bash
python get_web_site.py get http:// www.runoob.com /git/git-tutorial.html ^/git
````
下载网站`www.runoob.com`下`/git/git-tutorial.html`网页，同时通过该网页的`ref`信息爬取所有能连接到的网页（限定在该网站内），网页的网址必须符合`^/git`模式。

### 转换本地下载网页

下载到的网页中的`ref`大部分是绝对路径，在本地使用浏览器查看的时候无法正常跳转，可以使用下面的命令进行转换。
````bash
python get_web_site.py trans 网页所在根目录
````
例子
````bash
python get_web_site.py trans www.runoob.com
````

## TODO

1. 能够下载图片等资源文件
2. 增加配置文件，能够配置下载文件的类型