from faker import Faker
import time
import re

# fake = Faker('en_US')

# content = ''

# for i in range(100):
#     content += fake.paragraph(2)
#     content += fake.email()
#     content += ' '
#     content += fake.paragraph()
#     content += fake.phone_number()
#     content += ' '
#     content += fake.paragraph()
#     content += '\n\n'
# print(content)

# with open('notes.txt', 'w+') as file:
#     file.write(content)
emailList = []
new_email_list = []

with open('assets/potential-contacts.txt', 'r') as fr, open ('raw/new_email.txt', 'w') as fw:
    for paragraph in fr:
        email_lst = re.findall('\S+@\S+', paragraph)
        phone_lst = re.findall('[0-9-+x.()]{7,}', paragraph)
        for email in email_lst:
            fw.write(email + '\n')

with open('raw/new_email.txt','r') as f:                                                                                                                                                                                                                                                 
    distinct_content=set(f.readlines())                                                                                                                                                                                                                                                   

to_file=""                                                                                                                                                                                                                                                                       
for element in distinct_content:                                                                                                                                                                                                                                                               
    to_file=to_file+element                                                                                                                                                                                                                                                           
with open('email.txt','w') as w:                                                                                                                                                                                                                                                  
    w.write(to_file) 

with open('assets/potential-contacts.txt', 'r') as fr, open ('raw/raw_phone_numbers.txt', 'w') as fw:
    for paragraph in fr:
        email_lst = re.findall('\S+@\S+', paragraph)
        phone_lst = re.findall('[0-9-+x.()]{7,}', paragraph)
        for phone in phone_lst:
            numbers = phone.replace(".", "").replace("-","").replace("(","").replace(")","")
            if len(numbers) == 10:
                format_num = numbers[:3] + '-' + numbers[3:6] + '-' + numbers[6:]
                fw.write(format_num + '\n')

with open('raw/raw_phone_numbers.txt','r') as f:                                                                                                                                                                                                                                                 
    distinct_content=set(f.readlines())                                                                                                                                                                                                                                                   

to_file=""                                                                                                                                                                                                                                                                       
for element in distinct_content:                                                                                                                                                                                                                                                               
    to_file=to_file+element                                                                                                                                                                                                                                                           
with open('phone_numbers.txt','w') as w:                                                                                                                                                                                                                                                  
    w.write(to_file) 
    
