# Goal:
# print a countdown before something " exciting " happens (like " launching
# Happy New Year! ").

import time

count= int(input("Enter the counter num: "))

print("\n countdown starts now: ")
for i in range(count,0,-1):
    print(count)
    time.sleep(1)

print("\n WOHOOO! Haappy New Year")