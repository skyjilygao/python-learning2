import pandas as pds
import json
import excel.account_info as aa

data = pds.read_excel("E:\\!work\\FB开户信息\\account-info.xlsx")
# print(data[1:3])
# line = len(data.values)
# print(data[line-3:line])
df = pds.DataFrame(data)
print('columns=',df.columns)
print('line nums=', len(df))
n = 0
act_info_arr = []
for i in range(len(df)):
    n += 1
    print('i=',i,' data=',end='')
    ld = data.loc[i]
    info = aa.account_info(ld['ID'], ld['负责人'], ld['部门'], ld['归属公司'], ld['申请信息'])
    info2 = info.__dict__
    print(info2)
    act_info_arr.append(info2)
    if n == 3:
        break

print(json.dumps(act_info_arr))
# print(df.keys)
# len = print(len(df))
# for i in range(len):
#     line_data = df.keys()
# print(df.tail(-3))
# print('==========================')
# print(df.tail(-2))

# print(df.tail(-3))
# print(len(data.values))
# print(data[0:3])
# print(data.values)
# print(data[1].data)
# for i in data:
#     print(i)

