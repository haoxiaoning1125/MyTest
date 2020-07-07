# coding=utf-8

dau = dict()  # uid: [system, sdk, payment_count]
result = [dict(), dict()]  # system_sdk: [user_count, payment_count]

with open('newbingo.client_login/newbingo.client_login-2020-06-27_00000') as f:
    for line in f:
        fs = line.split('\t')
        try:
            d = eval(fs[5])
            uid = fs[2]
            model = d['model'] == 'ios'
            sdk = '.'.join(d['sysinfo']['SDK'].split('.')[:2])
            dau[uid] = [model, sdk, 0]
        except Exception as e:
            print line, e

with open('newbingo_payment/newbingo_payment-2020-06-27_00000') as f:
    for line in f:
        fs = line.split('\t')
        try:
            uid = fs[0]
            payment_add = float(fs[3])
            if uid in dau:
                dau[uid][2] += payment_add
        except Exception as e:
            print line, e

for uid, data in dau.items():
    model, key = data[0], data[1]
    if key in result[model]:
        result[model][key][0] += 1
        result[model][key][1] += data[2]
    else:
        result[model][key] = [1, data[2]]

print('android-------------')
for k, v in sorted(result[0].items(), key=lambda x: x[1][0], reverse=1):
    print '{}, user_count: {}, payment_count: {}'.format(k, v[0], v[1])
print('\n')
print('ios-------------------')
for k, v in sorted(result[1].items(), key=lambda x: x[1][0], reverse=1):
    print '{}, user_count: {}, payment_count: {}'.format(k, v[0], v[1])
