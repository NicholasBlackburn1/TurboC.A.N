# Suberu Impresa 2010 Canbus Ids


*Reverse Engineering can bus ids to understand what id's do what in my car to improve car's functionalities*

**P.s higher the C.A.N Id the More Critical the Device is**

**UnKnown Kan ids 1537, 1056. 1300, 1058, 1537, 1281 and  of Interest**

<li> 1041 seems to be linked to accelerator to but need to look into it more 


## Um Unknown(counts in hexadecimal changes b2 (pos))
#### B1 seems static so i does not seem to change when car is running
#### B2 seems to Stay static to maby a buffer bit before real data
#### B3 seems to be I dont know what yet
#### B4 Pos of Peddle Pressed

 ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1041   | 04   | ff   | 3f-fb  | 00-fc   | 00   | 00   | 00   | C0   | Unknown|



## Stearing turning ( counts in hexaDesimal)
#### Units of turning counts B1 up but B2 increments 1 per 9 of B1
#### still Dont know what B3 is i assume thats is and finer incremented
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x02   | 0e-fe   | 00-f1   | 00-ee  | 00   | 00   | 00   | 00   | 01   | Wheel getting turned)|


## GasPeddle I think ( counts in hexaDesimal)
#### B1 Maby small rpm count
#### B2 Is Peddle Pos Count General
#### B3 Is Peddle Pos Count Finer
#### B4 Buffer Mabey but it witches between 13-14
#### B5 Buffer bit i think
#### B6 Maby the actual rpm but changes really fast and not steady
#### B7 Seems to Hopefully a small incremets of rotations 
#### B8 Seems to See if Peddle is Gas Pressed or released
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1040  | 00-ef   | 00-ef  | 00-ff  | 13-14 | 00   | 00-ff   | 00-0b   | c0-00   | Enging data for rpm i think)|


    
## Might be brake peddle
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1300 | 00   | 00    |  00 | 00  | 00   | 00   | 00   | 00   | Braking / abs)|

