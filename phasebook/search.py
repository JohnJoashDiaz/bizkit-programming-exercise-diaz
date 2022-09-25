from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    args = request.args
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')
    result = []

    if request.args == {}:
        result = USERS
    if 'id' in request.args:
        index = 0
        for i in USERS:
            if id in USERS[index]['id']:
                result.append(USERS[index])
                index+=1
            else:
                index+=1
    if 'name' in request.args:
        index = 0
        for i in USERS:
            if name in USERS[index]['name'] or name.capitalize() in USERS[index]['name']:
                result.append(USERS[index])
                index+=1
            else:
                index+=1
    if 'age' in request.args:
        index = 0
        age_mid = int(age)
        age_low = age_mid -1
        age_high = age_mid +1
        for i in USERS:
            if age_low == USERS[index]['age']:
                result.append(USERS[index])
                index+=1 
            elif age_mid == USERS[index]['age']:
                result.append(USERS[index])
                index+=1 
            elif age_high == USERS[index]['age']:
                result.append(USERS[index])
                index+=1
            else:
                index+=1     
    if 'occupation' in request.args:
        index = 0
        for i in USERS:
            if occupation in USERS[index]['occupation'] or occupation.capitalize() in USERS[index]['occupation']:
                result.append(USERS[index])
                index+=1
            else:
                index+=1
    result = [i for n, i in enumerate(result) if i not in result[:n]] 
    return result
    
    
    

