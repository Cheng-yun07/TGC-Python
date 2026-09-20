threshold = 60000.0  # 年个税起征点 5000元*12
special_ratio = 0.24  # 专项扣除比例
per_baby_deduction = 2000  # 每个三岁以下婴幼儿扣除2000元
per_oldman_deduction = 3000  # 每个60岁以上老人扣除3000元
per_chile_deduction = 2000  # 每个子女教育扣除2000元
# 输入信息
income = float(input("请输入税前年总收入:"))
# 判断年收入不能为负数
if income < 0:
    print("年收入不能小于0!")
    input("\n...请按回车键退出...")  # 控制台防税闪退
    exit()
baby_num = int(input('请问您家中有几个3岁以下的婴幼儿？'))
oldmen_num = int(input('请问您家中有几位60岁以上的老人？'))
child_num = int(input('请问您家中有几个受教育的子女？'))
special_deduction = income * special_ratio  # 计算专项扣除
baby_deduction = baby_num * per_baby_deduction  # 计算抚养幼儿扣除
oldman_deduction = oldmen_num * per_oldman_deduction  # 计算赡养老人扣除
chile_deduction = child_num * per_chile_deduction  # 计算子女教育扣除
# 计算专项附加扣除综合
expense_deduction = baby_deduction + oldman_deduction + chile_deduction
# 计算全年应纳税所得额
tax_income = income - threshold - special_deduction - expense_deduction
if tax_income < 0:
    tax = 0
else:
    if tax_income <= 36000.0:
        tax = tax_income * 0.03 - 0
    elif tax_income <= 144000.0:
        tax = tax_income * 0.1 - 2520
    elif tax_income <= 300000.0:
        tax = tax_income * 0.2 - 16920
    elif tax_income <= 420000.0:
        tax = tax_income * 0.25 - 31920
    elif tax_income <= 660000.0:
        tax = tax_income * 0.3 - 52920
    elif tax_income <= 960000.0:
        tax = tax_income * 0.35 - 85920
    else:
        tax = tax_income * 0.45 - 181920
# 计算税后收入
real_income = income - special_deduction - tax
# 答应结果 保留两位小数
print("需缴纳个税:", round(tax, 2), "元")
print("专项扣除:", round(special_deduction, 2), "元")
print("抚养幼儿扣除:", round(baby_deduction, 2), "元")
print("赡养老人扣除:", round(oldman_deduction, 2), "元")
print("子女教育扣除:", round(chile_deduction, 2), "元")
print("税后总收入", round(real_income, 2), "元")
input("\n请按回车键退出...")  # 控制台打开防闪退
