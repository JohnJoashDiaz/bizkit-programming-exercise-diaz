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
                return False
   

    
