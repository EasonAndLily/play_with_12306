# coding: utf-8

import base64
import cv2
import numpy as np
from keras import models, backend
from .utils import Utils


def load_images(img):
    interval = 5
    length = 67
    for x in range(40, img.shape[0] - length, interval + length):
        for y in range(interval, img.shape[1] - length, interval + length):
            yield img[x:x + length, y:y + length]


def load_text(img, offset=0):
    # 得到图像中的文本部分
    return img[3:22, 120 + offset:177 + offset]


def preprocess_input(x):
    x = x.astype('float32')
    # 我是用cv2来读取的图片，其已经是BGR格式了
    mean = [103.939, 116.779, 123.68]
    x -= mean
    return x


def get_text(img, offset=0):
    text = load_text(img, offset)
    text = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)
    text = text / 255.0
    h, w = text.shape
    text.shape = (1, h, w, 1)
    return text


def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.frombuffer(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)

    return img


def verify(base64_code):
    import os

    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    backend.clear_session()
    verify_titles = ['打字机', '调色板', '跑步机', '毛线', '老虎', '安全帽', '沙包', '盘子', '本子', '药片', '双面胶', '龙舟', '红酒', '拖把', '卷尺',
                     '海苔', '红豆', '黑板', '热水袋', '烛台', '钟表', '路灯', '沙拉', '海报', '公交卡', '樱桃', '创可贴', '牌坊', '苍蝇拍', '高压锅',
                     '电线', '网球拍', '海鸥', '风铃', '订书机', '冰箱', '话梅', '排风机', '锅铲', '绿豆', '航母', '电子秤', '红枣', '金字塔', '鞭炮',
                     '菠萝', '开瓶器', '电饭煲', '仪表盘', '棉棒', '篮球', '狮子', '蚂蚁', '蜡烛', '茶盅', '印章', '茶几', '啤酒', '档案袋', '挂钟', '刺绣',
                     '铃铛', '护腕', '手掌印', '锦旗', '文具盒', '辣椒酱', '耳塞', '中国结', '蜥蜴', '剪纸', '漏斗', '锣', '蒸笼', '珊瑚', '雨靴', '薯条',
                     '蜜蜂', '日历', '口哨']
    # 读取并预处理验证码
    captcha = base64_to_image(base64_code)
    text = get_text(captcha)

    captcha_item = np.array(list(load_images(captcha)))
    captcha_item = preprocess_input(captcha_item)

    text_list = []
    # 识别文字
    model = models.load_model(Utils.get_root_path() + os.path.sep + 'model' + os.path.sep + 'model.v2.0.h5',
                              compile=False)
    label = model.predict(text)
    label = label.argmax()
    text = verify_titles[label]
    text_list.append(text)
    # 获取下一个词
    # 根据第一个词的长度来定位第二个词的位置
    if len(text) == 1:
        offset = 27
    elif len(text) == 2:
        offset = 47
    else:
        offset = 60
    text = get_text(captcha, offset=offset)
    if text.mean() < 0.95:
        label = model.predict(text)
        label = label.argmax()
        text = verify_titles[label]
        text_list.append(text)
    print("题目为: {}".format(text_list))
    # 加载图片分类器
    model = models.load_model(Utils.get_root_path() + os.path.sep + 'model' + os.path.sep + '12306.image.model.h5',
                              compile=False)
    labels = model.predict(captcha_item)
    labels = labels.argmax(axis=1)
    results = []
    for pos, label in enumerate(labels):
        text = verify_titles[label]
        print('选项{}.{}'.format(pos + 1, text))
        if text in text_list:
            results.append(str(pos + 1))
    return results

# if __name__ == '__main__':
#     res = verify(
#         "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")
#     print(res)
