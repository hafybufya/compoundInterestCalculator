# compound interest calculator that takes initial savings amount, months of saving, number of compounding periods and the annual interest rate.

#prompts variables
initial_savings_prompt = "Enter your initial amount of savings (£): "
time_prompt = "Enter the number of months you're saving for (whole numbers only): "
rate_prompt = "Enter the annual interest rate (decimal): "

#prompts error handling
prompt_error_handling_negative = "Amount cannot be below 0 "
prompt_error_handling_non_numeric = "Amount must be a numerical value"
prompt_error_handling_integer = "Amount must be a whole positive number"

prompt_error_handling_dp = "Please enter a value with at most 2 decimal places."
prompt_error_handling_rate= "Rate falls between 0 and 1"

#value for any of these variables > 0
min_number = 0
max_rate = 1

def initial_savings_amount():
    while True:
        initial_savings_amount = input( initial_savings_prompt)
        try:
            initial_amount = float(initial_savings_amount) 
        except ValueError:
            raise ValueError(prompt_error_handling_non_numeric)

            #restrict user input to 2 dp
        if initial_amount * 100 != int(initial_amount * 100):
            raise ValueError(prompt_error_handling_dp)           
            #user input > 0
        if min_number > initial_amount:               
             raise ValueError(prompt_error_handling_negative)
        
        return initial_amount


#future improvement: allowing users to enter either percentage or decimal
def rate():
    while True:
        try:
            rate = float(input(rate_prompt))            
            if min_number < rate <=max_rate:               
                return rate               
            else:
                print(f"{prompt_error_handling_rate}")        
        except ValueError:
            print(f"{prompt_error_handling_non_numeric}") #unhardcode numbers

# def rate():
#     while True:
#         try:
#             rate = float(input(rate_prompt))            
#             if min_number < rate <=max_rate:               
#                 return rate               
#             else:
#                 print(f"{prompt_error_handling_rate}")        
#         except ValueError:
#             print(f"{prompt_error_handling_non_numeric}") #unhardcode numbers



def time():
    while True:
        try:
            time = int(input(time_prompt))            
            if min_number < time:               
                return time #in months
            else:
                print(f"{prompt_error_handling_negative}")
        #users can't input non-integers        
        except ValueError:
            print(f"{prompt_error_handling_integer}") #unhardcode numbers


def comp_in_calc(initial_savings_amount, rate, time):
    time = time/12 #month/12 = year
    total_amount_saved = initial_savings_amount * (1 + rate) ** time
    return total_amount_saved






if __name__ == "__main__":
    initial_savings_amount = initial_savings_amount()

    rate = rate()

    time= time()

    total_amount_saved = comp_in_calc(initial_savings_amount, rate, time)
    print(f'£{total_amount_saved:.2f}')