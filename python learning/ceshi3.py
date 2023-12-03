member = ['z','x','c','v']
member.insert(0,'x')
member.extend(member)
member.append(1)
print(member)
member2 = member
print(member2)
member2 = 'member'
print(member2)
n = len(member) - 1
print(n)
print(member.index('z',0,n))