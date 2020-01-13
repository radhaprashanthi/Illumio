# Goal
    Implement an interface or an application through which we can validate the network packets based on given set of rules.

# Requirements
    1. Python 3.6
    2. VirtualEnv - `virtualenv -p python3.6 illumio36`

# Execution Guidelines
    ```
    python main.py --> this will run the main function which reads the network pakcets read from file

    python -m unittest firewall_test.py --> running test cases
    ```

# Optimization:




# Questions

1. Do we have to return true if atleast one of the rule is satisfied?
    ```
    example: inbound, tcp, 4567892, 1.1.1.1
    the above example validates direction and protocol. but fails for port and ipaddress. SO Should we return TRUE or FALSE?
```

2. For ranges of ports or IP adress - 
    ```
    example: inbound, tcp, 10-754673, 1.1.1.1 
    we have ports that are valid from 10 to 65535.
    Should our function be returning true for those and false for out of range
    OR SHOULD we considering this as one input and return FALSE as outerbound is 
    out of range.
    ```

3. Should we consider our input from csv file as Strings and then convert them into INT while passing them to accpet_packet function?


