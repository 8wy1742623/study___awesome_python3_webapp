#! python3
# -*- coding: utf-8 -*-
import os, sqlite3

# 练习
# 在 sqlite 中根据分数段查找指定名字：

db_file = os.path.join(os.path.dirname(__file__), "test.db")
# if os.path.isfile(db_file):
#     os.remove(db_file)

# # 初始数据
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE user(id varchar(20) primary key,\
#     name varchar(20), score int)")
# cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
# cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
# cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
# cursor.close()
# conn.commit()
# conn.close()


def select_from_table(low, high):
    connect = sqlite3.connect(db_file)
    cursor = connect.cursor()
    cursor.execute(
        "SELECT score, name FROM user where score >= ? AND score <= ?",
         (low, high))
    select_l =  cursor.fetchall()
    cursor.close()
    connect.commit()
    connect.close()
    return select_l


def sort_list(l):
    """
    [(95, u'Adam'), (62, u'Bart'), (78, u'Lisa')]
    -> [(62, u'Bart'), (78, u'Lisa'), (95, u'Adam')].
    """
    j = 1
    while j < len(l):
        for i in range(len(l) - j):
            if l[i][0] > l[i + 1][0]:
                l[i], l[i + 1] = l[i + 1], l[i]
        j += 1
    return l


def format_to_name_list(s_l):
    """
    [(95, u'Adam'), (62, u'Bart'), (78, u'Lisa')]
    -> ['Adam', 'Bart', 'Lisa'].
    """
    result_list = []
    for tuple_ele in s_l:
        result_list.append(tuple_ele[1].encode('utf-8'))
    return result_list



def get_score_in(low, high):
    " 返回指定分数区间的名字，按分数从低到高排序。 "
    select_list = select_from_table(low, high)
    result_list = format_to_name_list(sort_list(select_list))
    return result_list


# 测试：
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
