# dog
12306抢票软件学习

2018-06-29 第一次提交0.1版本,实现了自动登陆功能,不过验证码识别率不高,后续将重点放在解决验证码识别率上,由于是第一次使用python,并不明白python的依赖库怎么上传,所以将依赖都写在lib.txt文件中

2018-11-06 第二次提交,整套还未完成
    因为百度识图每天只有500次调用机会,我一个人的力量有限,希望能大家一起来
    在百度云注册账号,里面有人工智能服务中图片识别服务,申请后会得到appkey之类的资料
    然后在ClassifyApi.py 和 OcrApi.py 的构造函数中替换掉我的账号资料
    注意 这里面是有两个账号的,ocr 是图片识别文字  classify 是图片识别场景
    我看了 百度,阿里,腾讯,目前对外开放的免费图片识别,百度是最强大的,所以这里选择百度当作图片识别的基础,每次识别验证码验证成功后会把图片md5值保存自己的阿里云数据库,请大家不要恶意去破坏数据里的数据。
    另外很多人会说可以基于谷歌的 Tesseract ocr图片识别文字,这不是立即就可以使用的,像简单无干扰的是能识别,总之还需要使用jTessBoxEditor等工具去训练它的识别正确率,大致意思是如果它识别错误了。
    需要人工去纠正,它自己会保存本次的纠正,但是这只是最简单,如果碰到了干扰特别强的图片则需要先处理图片的干扰,比如去底噪,去干扰线,高亮等,这一切的目的是让Tesseract的识别正确率提高,这才是简单的图片识别文字。
    这可以运用到12306图片验证码上的中文提问,最难的是下面的图片回答,需要识别图片中的场景叫什么中文,纵观各大公司,目前只有百度提供这样的服务并且对外开放,这是我半年前关注的,后面有没有新出我不知道,所以我选择直接用百度接口。
    这个程序不能作为优秀的抢票程序,众所周知抢票讲究的是正确,以及快速,从语言执行速度,以及宽带,机器,验证码识别速度,显然是达不到黄牛或一流公司所提供的抢票服务那种能力,图片识别率,则需要大量的数据来支撑,这不是我一个人能解决的。
    但是本源码应该还是能为大家解答抢票程序是如何制作的，这才是目的。
    如果大家愿意为图片识别数据提供积累,则可以按照上面的方法去百度云申请账号,修改掉对应位置后
    解开App.py 中的注释
    # 用于采集数据的
    #collect = CollectData()
    #collect.go(config)
    并且给下面的代码添加注释,因为用不着下面的代码,另外
    config = { # 固定格式
    "username":"",
    "password":"",
    "http": None # 这个session对象需要全程用来访问请求,因为验证通过是与session绑定的,再每次提交验证失败后会重新创建session为了防止出现复杂验证码
    }
    在采集数据的时候 不需要填这个12306的账号密码,所以不必担心被添加到黑名单等意外问题
    在 Config.py 中修改localimgpath 参数的地址,它可以是你电脑的磁盘任何位置。

    碰到的问题
        1。我在执行登陆,查票,选票后,再次验证是否登陆的时候 竟然是 false,这个有点不解，我并没有更换session对象,这一块需要再看一下。