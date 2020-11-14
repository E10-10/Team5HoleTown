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
    "depth",float value,
    "long",float value,
    "wide",float value,
    "holeScale1to10", int value
    
    
_> to create a new item in dictionary 
values must have ("latitude", "longitude",) or "streetname"


    
=== idea ==
or organize as class

    
=== ToDo ===
-> count entries with same location/gps( "latitude","longitude") or streetname
and plot
_> test valid gps format or street name

_> add distanze function and plot hist plot

_> write and read in file
'''
from my_fcts import  *

#%%
# set up inint case
main_dict = {}
for i in range(4):
    #my_uuid = create_uuid()
    my_uuid     = create_unique_uuid(main_dict)
    my_userid   = create_unique_userid(main_dict)
    main_dict.update({my_uuid:{"uuid":my_uuid,"userid":my_userid,\
                               "latitude":random.randint(1,10000),"longitude":random.randint(1,10000)}})


print(main_dict )
print(len(main_dict ))
  
#%%
print('\n== test add new item for given user id==')
my_test_dict = {}
arg_dict = args={"latitude":4,"longitude":5,"streetname":"abdcefStreet"}
my_new_userid   = create_unique_userid(my_test_dict)
my_test_dict  = add_new_item_in_dict(my_test_dict,my_new_userid,arg_dict)
print(my_test_dict  )

#%%
print('\n== test is userid in dictrionary ==')
main_dict = {}
for i in range(4):
    my_uuid     = create_unique_uuid(main_dict)
    my_userid   = create_unique_userid(main_dict)
    if i>2:
        my_userid = 2
        main_dict.update({my_uuid:{"uuid":my_uuid,"userid":my_userid,\
                                   "latitude":random.randint(1,10000),"longitude":random.randint(1,10000)}})
    else:
        main_dict.update({my_uuid:{"uuid":my_uuid,"userid":my_userid,\
                                   "latitude":random.randint(1,10000),"longitude":random.randint(1,10000)}})

my_userid = 2
print(is_userid_in_dict(main_dict,my_userid))


#%%
print('\n== test get fct==')
my_property = "uuid"
my_return_value = get_entry(main_dict,my_uuid, my_property)    
print(my_property + " = " + str(my_return_value ))
my_property = "userid"
my_return_value = get_entry(main_dict,my_uuid, my_property)    
print(my_property + " = " + str(my_return_value ))

#%%
print('\n== Test set entry ==')
print('one')
# just one entry
print('before')
my_test_dict = main_dict
print(my_test_dict[my_uuid])
my_test_dict = add_new_entry_in_dict(main_dict,my_uuid,"latitude",50)
print('\n after ')
print(my_test_dict[my_uuid].items())
print('before')# more than one entry
args={"latitude":40,"longitude":55,"depth":500,"long":1000}
my_test_dict = add_new_entries_in_dict(main_dict,my_uuid,args)
print('\nmore than one')
print(my_test_dict[my_uuid].items())
print('\n')
#for i in my_test_dict.keys():
#    print("key= "+str(i) + " value[i] = " + str(my_test_dict[i]))
    
#%%
print('\n== Test del entry ==')
try:
    my_property = 'long'
    print('before')
    print(my_test_dict[my_uuid])
    my_test_dict_return = del_entry(my_test_dict, my_uuid,my_property)
    print('\n after ')

    print(my_test_dict_return[my_uuid])
    my_test_dict_return = del_item(my_test_dict, my_uuid)
    print()
    print('exist = ' + str((my_uuid in my_test_dict_return.keys() )))
except:
    print('empty item')    
#del_item(my_dict, my_uuid)



  
#%%
print('\n== Test bound fct ==')
print(num_in_range(1,8,2))
print(num_in_range(1,8,999))