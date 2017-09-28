import urllib, os

class Deal:
    # 保存网络图片（URL链接）
    def saveImgByUrl(url, filename):
        urllib.urlretrieve(url, filename)

    # 打开文件夹
    def mkDir(self, path):
        path = path.strip()
        # dir_path = self.path + path
        dir_path = path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    # 保存网络图片（内容）
    def saveImg(self, content, path):
        f = open(path, 'wb+')
        f.write(content)
        f.close()

    # 保存TXT文件
    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "wb+")
        f.write(content.encode('utf-8'))

    # 获取URL文件的后缀名
    def getExtension(self, url):
        extension = url.split('.')[-1]
        extension = extension.split('?')[0]
        return extension

    # 获取当前时间戳（秒）
    def ts(self):
        import time
        ticks = time.time()
        return int(ticks)

    # base64加密编码
    def base64encode(self, str):
        # 编码
        import base64
        bytesString = str.encode(encoding="utf-8")
        encodestr = base64.b64encode(bytesString).decode()
        return encodestr

    # base64解密解码
    def base64decode(self, str):
        # 解码
        import base64
        bytesString = str.encode(encoding="utf-8")
        decodestr = base64.b64decode(bytesString)
        return decodestr.decode()

    # MD5加密
    def md5(str):
        import hashlib
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        return m.hexdigest()