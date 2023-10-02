from Crypto.Hash import SHA256, SHA512 , RIPEMD 
from collections import Counter

#generate 1000 length input as string as all 1's
inputData="1"
for i in range(999):
    inputData = inputData + "1"

'''-----------------PART ONE------------------'''
#SHA 256 
hash256=int(SHA256.new(inputData.encode()).hexdigest(),base=16)
sumSHA256 = 0
for i in range(1000):
    #changing one bit 
    stringWithOneBitChange = inputData[:i] + '0' + inputData[i+1:]
    #hashing
    ihash256 =  int(SHA256.new(stringWithOneBitChange.encode()).hexdigest(),base=16)
    sumSHA256+=Counter(bin(hash256^int(ihash256)))['1']
avg_change=sumSHA256/(256*1000)
print('Average change in output of SHA256 for one bit change in input=',round(avg_change*100,2),'%')    



#SHA 512
hash512=int(SHA512.new(inputData.encode()).hexdigest(),base=16)
sumSHA512 = 0
for i in range(1000):
    #changing one bit 
    stringWithOneBitChange = inputData[:i] + '0' + inputData[i+1:]
    #hashing
    ihash512 =  int(SHA512.new(stringWithOneBitChange.encode()).hexdigest(),base=16)
    sumSHA512+=Counter(bin(hash512^int(ihash512)))['1']
avg_change=sumSHA512/(512*1000)
print('Average change in output of SHA512 for one bit change in input=',round(avg_change*100,2),'%') 


#RIPEMD
hashRIPEMD=int(RIPEMD.new(inputData.encode()).hexdigest(),base=16)
sumRIPEMD = 0
for i in range(1000):
    #changing one bit 
    stringWithOneBitChangeRIPEMD = inputData[:i] + '0' + inputData[i+1:]
    #hashing
    ihashRIPEMD =  int(RIPEMD.new(stringWithOneBitChangeRIPEMD.encode()).hexdigest(),base=16)
    sumRIPEMD+=Counter(bin(hashRIPEMD^int(ihashRIPEMD)))['1']
avg_change=sumRIPEMD/(160*1000)
print('Average change in output of RIPEMD for one bit change in input=',round(avg_change*100,2),'%') 

'''-----------------PART TWO------------------'''
hash256=int(SHA256.new(inputData.encode()).hexdigest(),base=16)
hashRIPEMDandSHA256=int(RIPEMD.new(str(hash256).encode()).hexdigest(),base=16)
sumRIPEMDandSHA256=Counter(bin(hashRIPEMD^int(hashRIPEMDandSHA256)))['1']
avg_change=sumRIPEMDandSHA256/(160)
print('Average change in output of SHA 256 followed by RIPEMD change =',round(avg_change*100,2),'%') 





