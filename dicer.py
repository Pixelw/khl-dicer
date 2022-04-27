import random


def judge1(dice, v_max):
    if dice == 100:
        return '大失败'
    elif dice >= 96:
        if v_max >= 50:
            return '大失败'
        else:
            return '失败'
    elif dice > v_max:
        return '失败'
    elif dice > v_max / 2:
        return '成功'
    elif dice > v_max / 5:
        return '困难成功'
    else:
        return '极难成功'


def ra(sender: str, skill: str, v_max: int) -> str:
    if v_max > 100 or v_max < 0:
        return ""
    dice = random.randint(1, 100)
    result = judge1(dice, v_max)
    return f'结果：1d100={dice}/{v_max} {result}'


def r(sender: str, count: int, dice: int) -> str:
    result = []
    _sum = 0
    for d in range(0, count):
        s = random.randint(1, dice)
        result.append(s)
        _sum += s
    return f'r{count}d{dice}: {result.__str__()}={_sum}'


# test
if __name__ == '__main__':
    print(judge1(45, 45))
    for i in range(1, 10):
        print(ra('pixelw', 'photo', 45))
        print(r("pxxx", 3, 6))
