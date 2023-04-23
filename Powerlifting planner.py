#def all the functions needed to create a workout planner.
#import the libraries needed
#import the data needed
#create a function to create a workout plan
#make a program that when you input your excercises, rpe, weight, and reps it will save it.
#button for create workout plan
#it should auto save the workout plan
#button for add excercise
  #when adding new exercise the format will be set-rpe-weight-reps-RIR
  #option to add notes
  #option to add video
  #option to swap excercise
  #option to add aditional excercise
    #option to delete excercise
    #option to add extra set
    #option to switch between kilo and pounds
        #we could make a default setting for the user if they want kilo or pounds
  #button for converting input weight into kg or vice versa
    #output will be in the number from the weight selection so 60kg will be 132lbs but since we only have 135 for pounds
    #it will round up to 135lbs so it will display bar + 45 +45.
  #option for auto rest timer between sets
  #finish button will save the workout for the day and will be saved in the history
    #button for cancel workout
  #button for create new account
  #button for login page
    #button for logout
    #button for delete account
    #button for change password
    #button for change email
    #button for change username
    #button for change name

#search button
#category button
#profile button
#history button for previous workout plan: it should be in a list format. 
  #the profile will nest the history for that profile( each profile is basic a new user)

"""
1) Create a function that will adjust the workout weight base on progressive periodization principles. 

2) The program will have a function to "suggest" base on keywords store in user input as notes.
        Example if week 1 bench press was 135 for 5 reps at 6 rpe and on the notes it say "easy", "no pain" "can do more" 
        then suggestion will be to increase the number base on either % or weight.

3) The program will have a function to show previous numbers in the input box of that rpe and exercises. 
        Example if last week i bench 135 for rpe 5, on the input box of week 2 it will show 135 in a grey translucid 
        number suggesting that is what i did last week or highest attempt for that rpe *this feature need more testing and feedback
        #if the user select the suggest feature it will auto fill the input box with the suggested weight base on the formula.
4) The program will have a function store data history of each lift including date and if possible video. 
        This way if i click on my bench press history it will show me all the data i have for that lift. this include notes and videos if possible.
          Add option to edit the data and media files.

5) The program need a way to store all the data in a file that can be accessed by the program and the user. 
        This way the user can access the data and edit it if needed. 

6) The program will is design to be use by powerlifter but can be use by any one that want to track their progress.
        
7) We need to create a function that will calculate the 1rm base on the rpe and weight input.

8) We need a library of exercises that can be added to the program. Including custom exercises.

9) add option to save and load workout plans for that day and at the end of the training week consolidate all the data in a file for access.
    *this is for future development:
        -add option to push data to google sheets or excel file. 
        -add option to push data to other user via email. Give them option to push the data of the day or push the entire week.
        -for media maybe only give them option to upload via their phone or computer. this way it only store what most important 
            even in the event they change phone.

10) we need to find a library of workout plans for powerlifting and powerbuilding to let user select them if they want to.

11) export option and data analysis:
    -a format that is easy to read and edit. Data after export can be edited and import back to the program. so try to keep the same
      format as the original file.
    -when in the app user can have a paid options for analyze the data: 
        -graph of the data that show the progress of the user. Their peek and their average base on the training block and cycles. 
        -give them the total volume for the weight they lift for that week/day
    -give user the PR for each lift and the date they got it. and includes previous PR and date and how many weeks/months ago they got it.

12) Suggestions: options
    -allow option to add reminder for options like:
        -every 4 weeks need a deload week.
        -every 12 weeks is a peaking week. Such as remind them that they are about to do a peaking week.( give them suggestion box)
        -customization reminder for the user:
            -timer for rest and between sets.

13) "ai suggestion" features (paid features):
    -collect data from the user and give them suggestion base on their data:
        -suggest a deload week if they are not making progress. This is base on certain conditions and only if they click on the suggestion feature(paid)
        -collect data on injury and give them suggestion on how to avoid it. (this might be too complicated for now)
        -if the program see that user had been making the choices that are in the same pattern for weeks without making progress then suggest a deload week
         or change exercise or change rep scheme. This is prompt user to ask them for what they feel is the problem. This will generate a list 
            of exercises
         that will work on the weak point. Then have them test this after a certain amount of time. 
        -suggest workout plan base on user experiences(future development)
        -optimize the workout plan base on user data(future development):
            if it beginner or intermediate or advanced:
                -adjust the workout plan base on the user data. This include keywords from their notes, rpe, weight, and reps.
                -adjust the workout plan for when they have a certain restriction such as injury or equipment.
                -adjust the workout plan for when they have a certain goal such as strength, hypertrophy, or power.
    -suggestion options can be for individual exercises or for the whole workout plan.(pref only for the exercises base on the user data from notes.)

14) "notes" feature:
    -add option to add notes to each exercise. this will be use to give suggestion to the user. This will be used to give suggestion to the user.
    -keywords base on user input will be use to give suggestion to the user.
    
        """
