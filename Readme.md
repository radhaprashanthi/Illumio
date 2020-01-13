# Goal

Implement an interface or an application through which we can validate the network packets based on given set of rules.

# Requirements
    1. Python 3.6
    2. VirtualEnv - `virtualenv -p python3.6 illumio36`

# Execution Guidelines
1. How to run the main function?
    `python main.py`
    - which will result in output from input file,
    - and couple of examples executing `accept_packet` method

2. How to run tests?
    `python -m unittest firewall_test.py`

# Optimization:
1. Time Complexity:
    - Already implemented a better way of identifying ports and IP addresses ranges.
    - I am reading the data and validating them in O(n) time which is linear.

2. Space Complexity:
    - I am using a dictionary to store the results of newtwork packet whether it is valid or not, this can be improved to store it in a file or disk instead of storing it in memory.
    - For given rules, currently there are 4, so I used them directly. But if there are many rules, we can keep a look up data structure or table through which we can save in-memory space for rules.

3. Distributed Computing:
    - If its a huge file containing millions of records, we can use hadoop or Spark to divide the file into data chunks and process the file parallely.


# Questions

1. Do we have to return true if atleast one of the rule is satisfied?
    ```
    example: inbound, tcp, 4567892, 1.1.1.1the above example has valid direction and protocol but fails for port and ip address. SO, Should we return TRUE or FALSE?

    Assumption: True is returned if and only if all the 4 parameters are valid.
    ```

2. For ranges of ports or IP adress - 
    ```
    example: inbound, tcp, 10-754673, 1.1.1.1 we have ports that are valid from 10 to 65535.Should our function be returning true for the valid range and false for out of rangeOR SHOULD we be considering this as one input and return FALSE as upper bound is out of range.

    Assumption: Returning True if and only if both lower and upper bounds are valid for port and IP address ranges and not comparing individual port and IP addresses withing the range.
    ```
