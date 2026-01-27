# Extra Credit 1: Movie Ticket Software

'''
Overview:

Your task is to create a program for selling movie tickets! 
The program will only support a few select movies and times but will allow the 
user to select their movie, desired showtime, and number of tickets to purchase.
Each movie and its respective showtime is given in the table below. 
Note that the prices for each movie depend on the time of the movie and the type 
of ticket being purchased!
'''

'''
Input:

Movies Available today:
Display table of movies and showtimes

Movie Choice:
User will always enter a single letter, but it may not match an actual movie choice

Showtime:
User will always enter a positive, whole number, but it may not match a valid option

Adult Tickets:
User will always enter a positive whole number but only 30 total (kids + adult) tickets can be purchased at a time.

Kid Tickets:
User will always enter a positive whole number but only 30 total (kids + adult) tickets can be purchased at a time.
'''


print("Available movies today:\nA)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50\nB)Coco:        1)12:40 2)3:45\nC)The Post:    1)12:45 2)3:35 3)7:05 4)9:55")

valid_input = False # Only asks the user how many tickets they would like to purchase if and only if they had entered valid responses to all the previous inputs. So, whenever it is True for valid_input, it ask how many and will do the official calculation as well
error_message = "Invalid option; please restart app..." 
movie_choice = input("Movie choice: ")
if movie_choice in "ABC":
    showtime = input("Showtime: ")
else: 
    print(error_message)

if movie_choice == "A":
    if showtime in "1234":
        adult_price = 12.45
        kid_price = 9.68
        valid_input = True
    else:
        print(error_message)

elif movie_choice == "B":
    if showtime in "12":
        if showtime == "1":
            adult_price = 11.17
            kid_price = 8.00
        elif showtime == "2":
            adult_price = 12.45
            kid_price = 9.68
        valid_input = True
    else:
        print(error_message)

elif movie_choice == "C":
    if showtime in "1234":
        if showtime == "1":
            adult_price = 11.17
            kid_price = 8.00
        elif showtime in "234":
            adult_price = 12.45
            kid_price = 9.68
        valid_input = True
    else:
        print(error_message)

if valid_input == True:
    adult_tickets = int(input("Adult tickets: ")) # 30 total tickets max per payment 
    kid_tickets = int(input("Kid tickets: ")) # 30 total tickets max per payment
    if adult_tickets + kid_tickets > 30:
        print(error_message)
            
    elif 0 <= adult_tickets <= 30:
        total_price = (adult_tickets * adult_price) + (kid_tickets * kid_price)
        print(f"Total cost: ${total_price:.2f}") # round to 2 decimal places each time means not to use round() function since that function can sometimes round to 1 decimal place whenever possible
    else:
        print(error_message)
