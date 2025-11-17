# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字

reserved_words = set(keyword.kwlist)

def is_keyword(s: str) -> bool:
    """判断一个字符串是否是 Python 关键字"""
    return s in reserved_words


if __name__ == "__main__":
    test_cases = ["if", "for", "hello", "def", "123"]
    for case in test_cases:
        print(f"'{case}' is a Python keyword: {is_keyword(case)}")
