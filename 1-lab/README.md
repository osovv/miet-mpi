## Task

Implement a "counter" process that starts with an initial value of `0` and

1. If a message `-1` is received, it outputs the current counter value and terminates;
2. If any other message is received, the counter value is incremented by `1`.

## Run

`./run.sh 4`, where `4` is number of available nodes

## Example output

```
$ ./run.sh 4
Slave #1 stopped.
Slave #3 stopped.
Slave #2 stopped.
Master stopped. Counter: 2938.
```
