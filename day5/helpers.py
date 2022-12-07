def move_cargo(list_of_orders, cargo_stacks_list):
    """
    Takes a list of movement orders and applys it to a list of cargo stacks, which are 
    all LIFO queues

    Args:
        list_of_orders (list): what moves to make
        cargo_stacks_list (list): what cargo stacks list
    """

    for line in list_of_orders:
        # get orders by spliting up the line and if it numeric, creating the integer
        # [number to move, stack from, stack to]
        orders = [int(x) for x in line.split() if x.isnumeric()]

        # number of crates to move, add 1 for range()
        crates_to_move = orders[0]+1

        # cargo stack to take from (index)
        cargo_stack_from_index = orders[1] - 1
        cargo_stack_from = cargo_stacks_list[cargo_stack_from_index]

        # cargo stack to place cargo (index)
        cargo_stack_to_index = orders[2] - 1
        cargo_stack_to = cargo_stacks_list[cargo_stack_to_index]


        for _ in range(1, crates_to_move):
            moving_crate = cargo_stack_from.get()
            cargo_stack_to.put(moving_crate)
        
        # print("Moving crates in this area. Please standby.")