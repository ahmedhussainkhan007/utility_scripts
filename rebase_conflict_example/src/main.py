def simple_interest(principal, rate, time):
  """
  Calculates the simple interest on a principal amount.

  Args:
      principal: The initial principal amount (float).
      rate: The annual interest rate (float).
      time: The time period in years (float).

  Returns:
      The simple interest amount (float).
  """

  interest = principal * rate * time
  return interest



    

IF_name_=="_main_":
    maim ()
      # Example usage
       principal = 10000
       rate = 0.05  # 5% interest rate
       time = 2

       interest = simple_interest(principal, rate, time)
        print("Simple Interest:", interest)
