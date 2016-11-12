'''
    Created by pqh on 2016/8/27.
'''


from zhclient import ZHclient



s = '/r/roundtables?offset=42'

print(s.find('offset='))
print(s[s.find('offset=')+len('offset='):])

