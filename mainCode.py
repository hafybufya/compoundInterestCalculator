# ---------------------------------------------------------------------
# Defined prompts and variables at the beginning of the program
#  -> make the code flexible if prompts or values changed changed
# ---------------------------------------------------------------------

# Prompts for variables
initial_savings_prompt = "Enter your initial amount of savings (£): "
rate_prompt = "Enter the annual interest rate (decimal): "
time_prompt = "Enter the number of months you're saving for (whole numbers only): "

# Prompts for error handling
prompt_error_handling_negative = "Amount cannot be below 0 "
prompt_error_handling_non_numeric = "Amount must be a numerical value"
prompt_error_handling_integer = "Amount must be a whole positive number"

prompt_error_handling_dp = "Please enter a value with at most 2 decimal places."
prompt_error_handling_rate= "Rate falls between 0 and 1"

# Value for any of these variables must be > 0
min_number = 0

max_rate = 1 # Rate cannot go above 1 if decimal

# ---------------------------------------------------------------------
# FUNCTION: Get initial savings amount 
# ---------------------------------------------------------------------


def initial_savings_amount():
    while True:
        initial_savings_amount = input( initial_savings_prompt)
        try:
            initial_amount = float(initial_savings_amount) 

        # Users can't input strings
        except ValueError:
            raise ValueError(prompt_error_handling_non_numeric)

        # Users can't input values which are more than 2 decimal places
        if initial_amount * 100 != int(initial_amount * 100):
            raise ValueError(prompt_error_handling_dp)           
            
        # Users can input a value below min_number
        if min_number > initial_amount:               
             raise ValueError(prompt_error_handling_negative)
        
        # Returned to be passed into comp_in_calc()
        return initial_amount

# ---------------------------------------------------------------------
# FUNCTION: Get rate  
# ---------------------------------------------------------------------

def rate():
    while True:
        try:
            rate = float(input(rate_prompt)) 
    
        # Users can't input strings
        except ValueError:       
            raise ValueError(f"{prompt_error_handling_non_numeric}") 
        
        if rate < min_number or rate > max_rate: 

            raise ValueError(f"{prompt_error_handling_rate}")        
        
        # Returned to be passed into comp_in_calc()
        return rate

# ---------------------------------------------------------------------
# FUNCTION: Get time 
# ---------------------------------------------------------------------

def time():
    while True:
        try:
            time = int(input(time_prompt))

        # Users can't input non integers      
        except ValueError:
            raise ValueError(f"{prompt_error_handling_non_numeric}") 
        
        # Users can input a value below min_number    
        if min_number > time:
            raise ValueError(f"{prompt_error_handling_negative}")
        
        # Returned to be passed into comp_in_calc()
        return time

# ---------------------------------------------------------------------
# FUNCTION: Compound interest calculator
# ---------------------------------------------------------------------

def comp_in_calc(initial_savings_amount, rate, time):

    time = time/12 # Converting from months to years
    total_amount_saved = initial_savings_amount * (1 + rate) ** time
    return total_amount_saved


if __name__ == "__main__":
    initial_savings_amount = initial_savings_amount()

    rate = rate()

    time= time()

    total_amount_saved = comp_in_calc(initial_savings_amount, rate, time)
    print(f'£{total_amount_saved:.2f}')