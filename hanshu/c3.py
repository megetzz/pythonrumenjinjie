'''
函数返回形式 
重点 多结果函数返回的写法
'''
# 函数返回两个值



def damage(skill_1,skill_2):
    # damage_1,damage_2
    damage_1 = skill_1 * 3
    damage_2 = skill_2 * 2 + 10
    return damage_1,damage_2

# 用两个变量 接收 函数的两个返回结果
skill_1_damage,skill_2_damage = damage(9,12)
# 序列解包 
# 有意义的变量名称  接受元组的值
print(skill_1_damage,skill_2_damage)

# damages = damage(1,2)
# print(damages)
# print(type(damages))

# 用一个变量接受到元组后,如何启用这个结果
#不算好的形式
# print(damages[0],damages[1])