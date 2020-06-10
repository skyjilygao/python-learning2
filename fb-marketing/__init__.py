import sys
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser


def fun1():
    print('ssssss')

my_app_id = 'xx'
my_app_secret = 'xx'
my_access_token = 'xx'
FacebookAdsApi.init(my_app_id,my_app_secret,my_access_token)

# act = AdAccount("act_599679690213860")
# campaigns = act.get_campaigns()
# print(campaigns)

me = AdUser(fbid='me')
my_accounts = me.get_ad_accounts(params={'limit':10})
# print(my_accounts)
allAct = []
page = 1
print(type(my_accounts))
print('page=',page)
for act in my_accounts:
    print(type(act))
    page += 1
    print('page=', page,'========')
    print(act[AdAccount.Field.id])


# while my_accounts.g:
#     allAct.append(my_accounts)
#     print('page=', times, ', size=', len(my_accounts))
#     times += 1
#     my_accounts = my_accounts.next

# print(len(allAct))
# print(type(my_accounts[0]))

