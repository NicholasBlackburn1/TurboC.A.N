# Suberu Impresa 2010 Canbus Ids


*Reverse Engineering can bus ids to understand what id's do what in my car to improve car's functionalities*

**P.s higher the C.A.N Id the More Critical the Device is**

**UnKnown Kan ids  1398, 1536, 1057,1058 of Interest**

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
| 0x1040  | 00-ef   | 00-ef  | 00-ff  | 13-14 | 00   | 00-ff   | 00-0b   | c0-00   | Gas pos i think)|


    
## Might be brake peddle/ Detects If in gear
### B1 is break pressed or not Relay Click

ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1300 | 00-08   | 00 |  fe-76 | 00  | 0c-08   | 80   | e0-ff   | 00-ff   | Something)|


 
## Might be Engin rpm
#### B4 seems to be Throttle body pos general
#### B5 seems to be Throttle body pos finer or User added pos
### B6, B7, B8 seem to be Filler Bytes`

ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1537 | 08   | d3    |  00 | 13-ff  | 00-ff   | 00   | 00   | 00   | engine throttle flap pos)|


## Unknown Because when parked shows no data
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1299 | 00   |00    |  00 | 00  | 00   | 00   | 00   | 00   | Unknown)|


## Break / Something Is Unknown
#### B5 seems to Detect only if the break is pressed 
#### B6 seems to be a countor 
#### B7 seems to be a cointor to
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1298 | 00   |00    |  00 | 00  | 80-90   | 00-ff   | 00-ff   | 00-ff   | Unknown)|


## Ok Actually Break Pos or Pressure
#### B5 seems to Detect only if the break pressure/pos
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1297 | ff   |ff    |  00 | 00  | 00-80   | ff   | 00   |00   | Break Pressure /Pos)|



## Something
#### B6 seems is incrementing
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1281 | 00   |00    |  00 | ff  | 00   | 00-99   | 00   |00   | Something)|



## Detects If Car is in Park or In of Gear
#### B3 Byte that shows if Car is in park or not
ID      | B1   | B2   | B3   | B4   | B5   | B6   | B7   | B8   | Comments      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------- |
| 0x1568 | 00   |00    |  05-01 | 00  | 00   | 00   | 00   |00   |  Check if car is in Park or not)|


