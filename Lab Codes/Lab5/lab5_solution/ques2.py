def isPerfect(max_range):  
    perfect_list = []
    deficient_count = 0
    abundant_count = 0

    #for each number
    for number_int in range (2,max_range+1):
        factor_list = []
        # check the factors from 1 to that number and collect them
        for factor in range (1,number_int):
            if number_int % factor == 0:
                factor_list.append(factor)
        # sum up the factors
        sum_int = sum(factor_list)

        #classify
        if sum_int == number_int:
            print(number_int," is a perfect number with factors: ",factor_list)
            perfect_list.append(number_int)
        elif sum_int > number_int:
            abundant_count += 1
        else:
            deficient_count += 1

    print()
    print("Summary")
    print("In the range of 2 to ",max_range," there are")
    print(len(perfect_list)," perfect numbers: ",perfect_list)
    print(abundant_count," abundant numbers")
    print(deficient_count, "deficient numbers")

# get the top of the range
max_range = int(input("Give me the top range to check: "))
isPerfect(max_range)
