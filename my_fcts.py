#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
=== structur ===
unique key is uuid for each entry/report in dictionary 

values are
request
    uuid":uuid,
    "userid", integer value 
    either
    "latitude":value,
    "longitude":value,
    or
    "streetname", string value, 
optional    
    "public", boolean value: default False
    "deth",float value,
    "long",float value,
    "wide",float value,
    "holeScale1to10", int value
    
    
_> to create a new item in dictionary 
values must have ("latitude", "longitude",) or "streetname"
dictionary = {uuid,{"uuid":uuid,"userid",value, \
    "latitude":value,"longitude":value,"streetname", value, \
    "deth",value,"long",value}}

    
=== idea ==
or organize as class

    
=== ToDo ===
-> count entries with same location/gps( "latitude","longitude") or streetname
and plot
_> test valid gps format or street name

_> add user_id

_> add distanze function and plot hist plot

_> write in file
'''
import uuid
import random 


#%%
def create_unique_uuid(my_dict):
    my_new_uuid = create_uuid()
    while my_new_uuid  in my_dict.keys():
        my_new_uuid = create_uuid()    
    return my_new_uuid 

def create_uuid():
    # create uui 
    return str(uuid.uuid4())

def is_uuid_in_dict(my_dict,my_uuid):
    # Test is uui in dictionary
    if my_uuid in my_dict:
        return True
    else:
        return False
    
#%%
def create_unique_userid(my_dict):
    my_new_userid = create_userid()        
    while is_userid_in_dict(my_dict,my_new_userid):
        my_new_userid = create_userid()                
    return my_new_userid  

def create_userid():
    # create uui 
    return random.randint(1,10000)

def is_userid_in_dict(my_dict,my_userid):
    # Test is userid in dictionary    
    for key, sub_dict in my_dict.items():        
        if my_userid == sub_dict["userid"]:
            return True
    else:
        return False
    
#%%
def add_new_item_in_dict(my_dict,my_userid, arg_dict):
    # add new item entry in dictonary, each entry has a unit uuid
    check_gps = ("longitude" in arg_dict.keys() ) & ("latitude" in arg_dict.keys())
    check_street = ("streetname" in arg_dict.keys())
    my_new_uuid = create_unique_uuid(my_dict)    
    if check_gps  | check_street:
        # create item
        my_dict.update({my_new_uuid:{"uuid":my_new_uuid,"userid":my_userid}})
        # add properties
        my_dict = add_new_entries_in_dict(my_dict,my_new_uuid,arg_dict)
                   
    return my_dict                    


#%%
def add_new_entry_in_dict(my_dict,my_uuid,my_property_key,my_property_value):
    if is_uuid_in_dict(my_dict,my_uuid) == True:
        sub_dict = my_dict[my_uuid]
        sub_dict.update({my_property_key: my_property_value})
        #my_dict[my_property_key]=sub_dict
        my_dict.update({my_uuid:sub_dict})
        return my_dict
    else:
        print('uuid is not in the dictionary')
        return my_dict        


def add_new_entries_in_dict(my_dict,my_uuid,arg_dict):
    for sub_key, sub_value in arg_dict.items():
        my_property_key = sub_key
        my_property_value = sub_value
        my_dict = add_new_entry_in_dict(my_dict,my_uuid,my_property_key,my_property_value)
    return my_dict 

#%%
def get_entry(my_dict, my_uuid, my_property):    
    # my_property "uuid"   
    if is_uuid_in_dict(my_dict,my_uuid) == True:
        sub_dict = my_dict[my_uuid]
        if my_property in sub_dict.keys():
            return sub_dict[my_property ]
        else:
            print('in get fct uuid or proberty not in dictornary')

#%%
def del_item(my_dict, my_uuid):
    if is_uuid_in_dict(my_dict,my_uuid) == True:
        del my_dict[my_uuid]
        return my_dict
       
    else:
        print('in del item fct: uuid not in dictornary')

def del_entry(my_dict, my_uuid,my_property):
    if is_uuid_in_dict(my_dict,my_uuid) == True:
        sub_dict = my_dict[my_uuid]        
        if my_property in sub_dict.keys():
            del sub_dict[my_property]
    else:
        print('in del_entry uuid or proberty not in dictornary')
        
    return my_dict
#%%
def num_in_range(lower_bound,upper_bound,num):
    return (num<=upper_bound) & (num>=lower_bound)