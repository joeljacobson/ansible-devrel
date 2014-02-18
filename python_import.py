import csv
import json
import riak


 
client = riak.RiakClient(pb_port=10017, protocol='pbc')
bucket = client.bucket('customers')
 
f = open("data/customer_data.csv", "r")
for row in csv.DictReader(f):
    key = row['id']
    item = bucket.new(row['id'], data=row)
    item.add_index('id_bin', row['id'])
    item.add_index('title_bin', row['title'])
    item.add_index('first_name_bin', row['first_name'])
    item.add_index('last_name_bin', row['last_name'])
    item.add_index('street_bin', row['street_number'])
    item.add_index('state_bin', row['state'])
    item.add_index('gender_bin', row['gender'])
    item.add_index('cc_type_bin', row['cc_type'])
    
    item.store()
    print('.'),
f.close()