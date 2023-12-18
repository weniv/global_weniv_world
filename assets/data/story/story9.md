# Let’s Automate!

## Let’s Automate! `Function`

Licat's fish company has become the fastest-growing distribution company in the entire Weniv World. However, employees became tired of simple and repetitive work.

"Can't we guarantee autonomy and creative thinking, personal growth, and clear purpose and motivation for each task?"

Licat analyzed each employee's work to see which tasks they spent the most time on. It was fishing, packaging, and delivery which are the simplest and most repetitive tasks.

The next day, Licat said at the meeting:

> "Let's adopt robots to replace repetitive tasks! Then we can focus more on creative work, meow!"

However, employees who were already filled with discontent were skeptical about this idea.

> "So who's going to make it!? Is CEO?!"

> "I already made it! So let's take this robot and install it, meow!"


## Mission

Create a function that automatically catches fish and delivers them. You need to fill in the `pass` part in the basic code below.

The function should perform the following: pick up the fish, go up to the top, and say in the form of `Completed delivery: 3` for each column.

Please refer to the image below.

![Mission image](./story9-3.png)

### Basic Code
```python
def delivery():
    pass
repeat(4, delivery)
```

## Hints
Complete the mission by combining the codes below.
```python
mission_start()
mission_end()
move()
turn_left()
on_item()
repeat(2, move)
pick()
put('fish-1')
print('hello world!')
front_is_clear()
left_is_clear()
right_is_clear()
```
