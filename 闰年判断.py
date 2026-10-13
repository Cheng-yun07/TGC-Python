year = int(input("请输入年份："))
month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    days = 29
                else:
                    days = 28
            else:
                days = 29
        else:
            days = 28
    else:
        if month in [1,3,5,7,8,10,12]:
            days = 31
        else:
            days = 30
    print(f"{year}年 {month}月,共有{days}天")
else:
    print("输入有误，月份必须在1-12之间")