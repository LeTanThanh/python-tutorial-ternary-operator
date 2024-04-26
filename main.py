if __name__ == "__main__":
  # Introduction to Python Ternary Operator

  age = int(input("Enter your age: "))
  # if age >= 18:
  #   ticket_price = 20
  # else:
  #   ticket_price = 5

  """
  value_if_true if condition else value_if_false
  """

  ticket_price = 20 if age >= 18 else 5

  print(f"The ticket price is {ticket_price}")
