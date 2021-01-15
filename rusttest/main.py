from xpinyin import Pinyin

import pypinyin


if __name__ == '__main__':
    for i in pypinyin.pinyin("python 真方便"):
        print(i)

