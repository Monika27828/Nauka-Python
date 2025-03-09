marketing = ['loyality program', 'client promotion', 'market research']
marketing.append('public relations')
print(marketing[2])
marketing.insert(1,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
x = tuple(emailMarketing)
print(x)