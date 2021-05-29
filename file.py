import csv

bank_id = []
name = []
row = []
dct = {}
# with open('bank.csv', 'w') as f:
#     with open('bank_branches.csv', 'r') as file:
#         writer = csv.writer(f)
#         writer.writerow(['bank_id', 'name'])
        
#         csv_file = csv.DictReader(file)
        
#         for row in csv_file:
#             d = dict(row)
#             # bank_id.append(d['bank_id'])
#             # name.append(d['name'])
#             if d['bank_id'] not in dct.keys():
#                 writer.writerow([d['bank_id'], d['name']])
#             dct[d['bank_id']]=1

with open('branches.csv', 'w') as f:
    with open('bank_branches.csv', 'r') as file:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state'])
        
        csv_file = csv.DictReader(file)
        
        for row in csv_file:
            d = dict(row)
            if d['bank_id'] not in dct.keys():
                writer.writerow([d['ifsc'], d['bank_id'], d['branch'], d['address'], d['city'], d['district'], d['state']])
            dct[d['bank_id']]=1
# print(bank_id[0])
