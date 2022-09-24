from difflib import Match
import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404
    
    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match", 
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    fave_numbers_1.sort()
    low = 0
    high = len(fave_numbers_1)-1 
    foundstatus = False
    index = 0
    while (low <= high):
        mid = (low+high)//2
        if (fave_numbers_1[mid]>fave_numbers_2[index]):
            high= mid-1
        elif (fave_numbers_1[mid]<fave_numbers_2[index]):
            low=mid+1
        else:
            print("favenum1", fave_numbers_1[mid],"=", fave_numbers_2[index])
            print("element found at ",mid)
            low = high +1 
            foundstatus= True
            if (foundstatus== True):
                index = index+1
                low = 0
                high = len(fave_numbers_1)-1 
                foundstatus = False
                if (index > len(fave_numbers_2)-1):
                    return True 
            else:
                print ("Element", fave_numbers_2[index], " Cannot Be found") 
                return False
                    #print ("value at fave_num 2 is ", str(fave_numbers_2[index_2]))
                    #print("Number Found at index: " + str(mid))
                    #print ("number found at index no. ", str(fave_numbers_1[mid]))  
                



    
    
    
    
    
    #print ("last is ", last)
    #index = -1
    #index_2 = 0
    #while (first <= last) and (index == -1):
    #    mid = (first + last) //2
    #    print (mid)
    #    if fave_numbers_1[mid] == fave_numbers_2[index_2]:
    #        index = mid 
    #    else:
    #        if fave_numbers_2[index_2] < fave_numbers_1[mid]:
    #            last = mid - 1 
    #        else:
    #            first= mid +1
    #    index_2 = index_2 + 1
    #return True
    
    #linear search algo
    #for number in fave_numbers_2:
    #    if number not in fave_numbers_1:
    #        return False



   

    
