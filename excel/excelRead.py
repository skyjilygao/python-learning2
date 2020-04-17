import pandas as pds
import json
import excel.account_info as aa

data = pds.read_excel("files/temp/account-info.xlsx")
# print(data[1:3])
# line = len(data.values)
# print(data[line-3:line])
df = pds.DataFrame(data)
print('columns=',df.columns.array)
print('line nums=', len(df))
n = 0
act_info_arr = []
print(data)
for i in range(len(df)):
    n += 1
    print('i=',i,' data=',end='')
    ld = data.loc[i]
    info = aa.account_info(ld['ID'], ld['人员'], ld['部门'], ld['公司'], ld['申请备足'])
    info2 = info.__dict__
    print(info2)
    act_info_arr.append(info2)
    if n == 3:
        break

print(json.dumps(act_info_arr))
