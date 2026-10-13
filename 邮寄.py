length = float(input("请输入长（米）:"))
width = float(input("请输入宽（米）:"))
height = float(input("请输入高（米）:"))
weight = float(input("请输入重量（千克）:"))
if length > 1 or width > 1 or height > 1 or weight > 40:
    print("超出限制，不予邮寄（长、宽、高任意尺寸超过1米或重量超过40千克)")
elif weight < 10:
    print(f"总费用:{5 + 1.5}元（手续费5元+邮资1.5元）")
elif weight < 30:
    print(f"总费用:{5 + 2.0}元（手续费5元+邮资2.0元）")
elif weight <= 40:
    print(f"总费用:{5 + 2.5}元（手续费5元+邮资2.5元）")
