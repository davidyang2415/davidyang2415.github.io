是什么？
文本转换引擎，将文档(如Markdown/Textile)转换为静态网站的转换器。

1.本地安装Jekyll
本地安装jekyll配置：Ruby, RubyGems, NodeJs, Python
用 RubyGems 安装 Jekyll

2.使用Jekyll命令
比如 jekyll build, jekyll serve

3.目录结构
.
├── _config.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.textile
|   └── on-simplicity-in-technology.markdown
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
|   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _site
├── .jekyll-metadata
└── index.html

_config.yml，配置数据
_drafts，草稿
_posts，文章，文件格式 YEAR-MONTH-DAY-title.MARKUP
_includes，引用数据 {% include file.ext %}
_layouts，包裹再文章外部的模板，{{ content }}
_data，格式化号的网站数据放在这里，加载目录下的所有yaml文件，通过 site.data 访问
_site，转换后的页面
.jekyll-metadata，jekyll项目数据
index.html and other HTML/Markdown/Textile files，
Other Files/Folders

4.YAML头信息
任何包含YAML头信息的问题件在Jekyll中都被当做一个特殊的文件处理。
YAML头信息格式，写在两个三虚线之间，示例：

---
layout: post
title: Blogging Like a Hacker
---

包括：预定义变量，自定义变量

4.1.全局变量
layout，指定使用该模板文件(不需要文件扩展名)
permalink，发布博客的URL地址
published，是否发布博文

4.2.自定义变量
比如 title 变量，模板中使用 {{ page.title }}

4.3.预定义的变量
date，日期会覆盖文章名字中的日期，保障文章排序，格式 YYYY-MM-DD HH:MM:SS +/-TTTT (时分秒和时区可选)
category/categories，除了 文件夹 归类，用这个字段也归类
tags，标签

5.撰写博客
5.1.文章文件夹(_posts)，文件名 年-月-日-标题.MARKUP
5.2.内容格式，YAML头信息
5.3.引用图片和其他资源，图片和资源文件放在指定文件夹下面，引用 ![图片]({{ site.url }}/assets/screenshot.jpg)
    站点只在域名的根 URL 下展示，可以不使用 {{ site.url }} 变量，如 /path/file.jpg 即可。
5.4.文章目录，不主动提供目录展示不会被看到。
创建文章列表，比如：
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
5.5.文章摘要，从开头到第一次出现 excerpt_separator 的地方作为摘要
    使用摘要 post.excerpt 变量
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
    摘要中包含 p 标签，移除 {{ post.excerpt | remove: '<p>' | remove: '</p>' }}
    手动摘要覆盖
---
excerpt_separator: <!--more-->
---

Excerpt
<!--more-->
Out-of-excerpt
    在 _config.yaml 全局声明 excerpt_separator
5.6.高亮代码片段，使用 Pygments 或 Rouge 两种工具
{% highlight ruby %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}

6.使用草稿
_drafts文件夹下，没有日期的文章。


7.创建页面
作为写文章的补充，可以创建静态页面。
主页，按约定在站点的根目录下 index.html 文件。
  任何 HTML 文件，包括主页，可使用 layout 和 include 中内容。
其他页面，1.HTML或Markdown文档，2.每个页面创建一个文件夹并在其中放置HTML或Markdown文件--命名 index.html 文件。
  以上两种方法可以混用。
  区别是访问的URL样式不同：1.文件 url/abount.html，2.文件夹 url/about/
    第2中方法中，Markdown文件使用 头信息变量 permalink 实现，如 permalink: /about 可使用 url/about


8.静态文件
不包含任何 YAML 头信息，通过 site.static_files 访问，元数据：
  file.path, file.modified_time, file.name, file.basename, file.extname


9.常用变量
  任何有 YAML头信息 的文件都是要处理的对象，生成数据。
9.1.全局变量 Global
  size(_config.yml)，page(页面所属信息+YAML头文件信息)，layout，content，paginator
9.2.全站变量 site
  site.time, site.pages, site.posts, site.related_posts, 
  site.static_files, site.html_pages, site.html_files,
  site.collections, site.data, site.documents,
  site.categories.CATEGORY, site.tags.TAG,
  site.[CONFIGURATION_DATA]
9.3.页面变量 page
  page.content, page.title, page.excerpt(摘要), page.url, page.date, page.id,
  page.categories(post目录或YAML头文件信息设置), page.tags, page.path,
  page.next, page.previous
  自定义的头文件信息都会在 page 中可用。
9.4.分页器 Paginator
  paginator.per_page, paginator.posts,paginator.total_posts, paginator.total_pages, paginator.page,
  paginator.previous_page,paginator.previous_page_path, paginator.next_page,paginator.next_page_path
  仅在 首页文件 中可用，也会存在于 子目录 中。

10.集合 Collections
  非文章或页面

11.数据文件
  从 _data 目录下的 YAML/JSON/CSV 载入数据，CSV文件必须包含表头行。
  通过 site.data 访问，包括 文件和文件夹。

12.资源
  对 Sass 的内建支持

13.博客迁移
  Jekyll 导入器

14.模板
  过滤器，如 {{ site.time | date_to_xmlschema }}
  标签，引用、代码高亮、行号、链接、博文链接、Gist

15.永久链接
  通过 Configuration 或 YAML头信息 设置 永久链接，格式默认 date /:categories/:year/:month/:day/:title.html
    pretty /:categories/:year/:month/:day/:title/
    ordinal /:categories/:year/:y_day/:title.html
    none /:categories/:title.html

16.分页功能 paginate
  与 permalink 冲突，缺省即可。

17.插件
  github不支持插件

18.主题

19.附加功能
  数字支持，使用其他Markdown解析器

20.发布：GitHub Pages
21.发布：部署发放
22.发布：持续集成