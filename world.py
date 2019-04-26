from utils import get_time

def compare(db_time, now_time):
    if now_time - db_time > 300:
        print("请重新登录")
        return 1
    else:
        return 0

if __name__ == "__main__":
    db_time_ = 1506268498
    now_time_ = get_time()
    val = compare(db_time_, now_time_)
    print(val)
