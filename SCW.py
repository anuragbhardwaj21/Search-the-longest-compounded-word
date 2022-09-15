import time
begin = time.time()

def isbuildingword(s, originalword, mp):

 if s in mp and mp[s] == 0:
  return False

 if s in mp and mp[s] == 1 and originalword == 0:
  return True

 for i in range(1, len(s)):
  l = s[:i]
  r = s[i:]
  if l in mp and mp[l] == 1 and isbuildingword(r, 0, mp):
   return True
 mp[s] = 0
 return False


def returnlongestword(listofwords):
 mp = dict()
 for i in listofwords:
  mp[i] = 1
 listofwords.sort(key=lambda x: len(x), reverse=True)

 for i in listofwords:
  if isbuildingword(i, 1, mp):
   return i
 return "-1"


if __name__ == "__main__":
 my_file = open("Input_02.txt", "r")
 data = my_file.read()
 listofwords = data.split("\n")
 longword=returnlongestword(listofwords)
 while(longword in listofwords):
    listofwords.remove(longword)
 secondlongword=returnlongestword(listofwords)
 print("Longest Compound Word: " + longword)
 print("Second Longest Compound Word: " + secondlongword)
 time.sleep(1)
 end = time.time()
 print(f"Time Taken: {end - begin}")