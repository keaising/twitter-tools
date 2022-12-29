#!/usr/bin/env python3

import xlsxwriter
import common

api = common.api()

friends_cursor = -1
friends = []

print('Getting following list...')
while friends_cursor != 0:
    friends_cursor, _, ids = api.GetFriendsPaged(cursor=friends_cursor)
    friends += ids
print('You have %d followings' % len(friends))


workbook = xlsxwriter.Workbook('Following.xlsx')
worksheet = workbook.add_worksheet("Following")

for i, user in enumerate(friends):
    row = [user.id, '@%s' % user.screen_name, user.name, 'https://twitter.com/%s' % user.screen_name]
    for j, item in enumerate(row):
        worksheet.write(i, j, item)

workbook.close()
