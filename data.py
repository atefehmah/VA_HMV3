import csv

data = []
with open("data/losses2015_transformed.csv") as csvFile:
    csvReader =  csv.DictReader(csvFile)
    for line in csvReader:
        data.append(line)

print(data[0])

dataSum = {}

# for d in data:
#     if d["State_Code"] in dataSum:
#         dataSum[d["State_Code"]] += int(d["Amount"])
#     else:
#         dataSum[d["State_Code"]] = int(d["Amount"])

# with open("dataSum.csv","w") as csvFile:
#     csvWriter = csv.writer(csvFile)
#     csvWriter.writerow(["id","amount"])
#     for d in dataSum:
#         csvWriter.writerow([d,dataSum[d]])

for d in data:
    if d["Damage_Descp"] in dataSum:
        dataSum[d["Damage_Descp"]] += int(d["Amount"])
    else:
        dataSum[d["Damage_Descp"]] = int(d["Amount"])
print(dataSum)

sortedData = sorted([i for i in dataSum.items()],key=lambda x:x[1])

with open("descSum.csv","w") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["desc","amount"])
    for d in sortedData:
        csvWriter.writerow([d[0],d[1]])

