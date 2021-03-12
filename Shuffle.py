# Made by Snehashish Laskar
# Email id : snehashish.laskar@gmail.com
# Made on 09-03-2021

import random
members = int(input("enter the number of students in each group: "))
participants = ['armaan', 'Uday','Ruhan', 'Vidushi', 'Aashi','Ruhani',
' Siddharth', 'Sohamm',  'Ananya J', 'shaurya',
 'Ishan', 'Anindita', 'Niloufer', 'Ovee', 'Amrita', 
 'Kailash', 'Vashist', 'Prakriti', 'hia', 'Anadya', 
 'Anavi', 'Ahona',
  'Sreehita', 'Reyansh', 'Ruchira', 'Kabir', 'Namit',
   'Nitin', 'Shiv', 'Indira', 'Raju', 'Aadil', 'Ananya S', 'Pratham', 
  'rishabh', 'Aadhira', 'Yajnesh', "Snehashish" ]


random.shuffle(participants)

for i in range(len(participants) // members + 1):
    print('Group {} consists of:'.format(i + 1))
    group = participants[i*members:i*members + members]
    for participant in group:
        print(participant)