import datetime
Donor_database = {
"Ashwin" : {
    "_id" : "1",
    "Blood_type" : "O+ve",
    "Priority" : 3,
    "Last_donation": datetime.datetime(2021,5,12),
    "Layer" : 1},
#each of 5 k radius
"Gokul" : {
    "_id" : "2",
    "Blood_type" : "O+ve",
    "Priority" : 2,
    "Last_donation": datetime.datetime(2021,5,12),
    "Layer" : 1},
"Ilamvazhuthi" : {
    "_id" : "1",
    "Blood_type" : "A1B+ve",
    "Priority" : 1,
    "Last_donation": datetime.datetime(2021,5,12),
    "Layer" : 1},
"Raam" : {
    "_id" : "1",
    "Blood_type" : "A1B+ve",
    "Priority" : 2,
    "Last_donation": datetime.datetime(2021,10,12),
    "Layer" : 6},
"Jeff" : {
    "_id" : "1",
    "Blood_type" : "A1B+ve",
    "Priority" : 1,
    "Last_donation": datetime.datetime(2021,5,12),
    "Layer" : 3},
"Sid" :  {
    "_id" : "1",
    "Blood_type" : "O-ve",
    "Priority" : 1,
    "Last_donation": datetime.datetime(2021,10,12),
    "Layer" : 4}
    
}
filtered={}
Requested_Blood_type = input("Enter the Blood Type: ")
count = 0
Case= int(input("Enter your display filter priority \n1.Show all the donors matching the blood group\n2.Show the donors matching the blood group and in the same location\n3.Show all the universal donors: "))
if Case == 1:
    for i in Donor_database:
        if Donor_database[i]["Blood_type"] == Requested_Blood_type :
            Duration =  datetime.datetime.now() - Donor_database[i]["Last_donation"]
            if Duration.days > 112:
                filtered[i] = Donor_database[i]
        
    res = sorted(filtered.items(), key = lambda x: x[1]['Layer'])
    print(res)
elif Case == 2:
    for i in Donor_database:
        if Donor_database[i]["Blood_type"] == Requested_Blood_type :
            Duration =  datetime.datetime.now() - Donor_database[i]["Last_donation"]
            if Duration.days > 112:
                if Donor_database[i]["Layer"] == 1:
                    print(i)
elif Case == 3:
    for i in Donor_database:
        if Donor_database[i]["Blood_type"] == "O+ve" :
            Duration =  datetime.datetime.now() - Donor_database[i]["Last_donation"]
            if Duration.days > 112:
               filtered[i] = Donor_database[i]
    res = sorted(filtered.items(), key = lambda x: x[1]['Layer'])
    print(res)
                
