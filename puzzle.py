# Morning warmup

# Bronze
# create two variables containing floats and print the result of floor division

num_1 = 25.7
num_2 = 17.8
float_division = num_1 // num_2
print(float_division)

# Silver & gold catering service
# Prompt user for an event type, and the number of guests attending
# If the event is a banquet the minimum number of attendees for the catering
# business to work is 30
# If the event is a wedding, the minimum number of attendees must be 25
# The catering business will not work with any other events at this time
# When the number of attendees is below min amount, display message that expresses
# there are too few atendees.

# event_type = input("What type of event? Banquet or Wedding? ")
# if event_type == "banquet" or event_type == "wedding":
#     guests = int(input("How many guests? "))
#     if event_type == True:
#         if guests >= 25 and event_type.lower() == 'wedding':
#             print("We can do a wedding")
#         elif guests >= 30 and event_type.lower() == 'banquet':
#             print("we can do a banquet")
#         else:
#             print("There are not enough")   

# How the group has done it
x = 25
y = 30
event = input("What is your event? >").lower()
people_attending = int(input("How many people are coming? >"))
'''
if event != "banquet" and event != "wedding":
    print("We don't have that service yet")
elif: event == "banquet" and people_attending < y:
    print("There are too few attendees for the banquet")
elif event == "wedding" and people_attending < x:
    print("There are too few attendees for the wedding")
else:
    print("There are too few attendees.")
'''


