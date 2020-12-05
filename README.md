# Busscheduler
A program that helps you keep track of available busses at your local busstation

Purpose of this program is to make it easier to keep track of the available busses from your local busstation.
The idea here is that you at any point in time will be able to see how much time you have left before the next
scheduled bus arrives at your selected busstation. But not just that, this program will also calculate the distance
to your local busstation which is also included in calculating the amount of time left before the next bus leaves.

The schedule is stored in a dictionary in the format: 'letter': [integer(hour), integer(minutes)].

There is also a "normalize" function that adds 24 hours or 60 minutes should the result of subtracting the
current hour from the hour in the schedule result in a negative value.

To-Do list:
1. Add a self-updating clock that refreshes on its own every minute.
2. Find a way to display the most current next two busses with expected arrival.

Problems:
The program is not very user-friendly since there is no real way of loading schedules from sources into the program.
In order to get a good estimate of the distance between the users home and his chosen busstation, he'll have to measure
the distance by himself, either through the use of a surveyor's wheel or through redrawing the path on google Maps.
At the moment I don't have a more comfortable way of providing that information to the program. 
