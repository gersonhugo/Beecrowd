n = int(input())
m = [(1,'January'),
     (2,'February'),
     (3,'March'),
     (4,'April'),
     (5,'May'),
     (6,'June'),
     (7,'July'),
     (8,'August'),
     (9,'September'),
     (10,'October'),
     (11,'November'),
     (12,'December')
    ]
for i in range(len(m)):
    if n == m[i][0]:
        print(m[i][1])
        break