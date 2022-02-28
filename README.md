# Car Follower

## Synopsis

An Ev3Dev program that allows the Ev3 to acccurately follow another RC car infront of it using proportionality.

## Tutorial

Clone the repository.

Build your robot. Make sure that the robot includes two large motors, an ultrasound sensor, and a touch sensor . 

In lines 47, remove the negative sign in `left_motor.duty_cycle_sp= int(-(power + correction))`, right before the word `power`. Do the same for line 48. I have the negative sign because my robot's motors are reversed. 

Run the program! Change the [constant of proportionality] (https://tutorme.com/blog/post/constant-of-proportionality/), power, and target distance by changing the variables `kp`, `power`, and `target` in line 21.

## More Info

To see an in-depth breakdown, check out the blog post I wrote on it here: (unfinished)

To see more examples of using proportionality with the Ev3, see my other program, [LineFollower] (https://github.com/rtenacity/LineFollower).
