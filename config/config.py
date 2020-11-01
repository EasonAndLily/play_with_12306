# coding:utf-8
# 识别验证码方式: [1: 手动, 0: 自动]
CAPTCHA_IDENTIFY = 1

# 12306登陆用户名
USERNAME = "test"

# 12306登陆用户的密码
PASSWORD = "test"

# 出发车站
FROM_STATION = "北京"

# 到达车站
END_STATION = "上海"

# 出发日期
TRAIN_DATA = "2020-10-31"

# 列车号
TRAIN_NUMBER = "G111"

# 乘车人 例如：["张三","李四"]
PASSENGERS = ["张三"]

# 座位类型[二等座:"O", 一等座:"M", 商务座:"9", 硬卧："3", 硬座:"1", 软卧:"4"]
SEAT_TYPE = "O"

# 选择的座位编号[A:靠窗, B:中间, C:过道, D:过道, F:靠窗]
# 编号前面的数字代表第几个乘车人，比如给张三和李四定过道和靠窗的票，则为[1D2F]
CHOOSE_SEATS = "1A"