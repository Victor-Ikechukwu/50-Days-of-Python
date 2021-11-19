Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tax = 18/100
price =  500
qty =  5
Amount = price * qty + tax
amount
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    amount
NameError: name 'amount' is not defined. Did you mean: 'Amount'?
Amount
2500.18
round(_,2)
2500.18
round(_, 1)
2500.2
round(1)
1
round(,1)
SyntaxError: invalid syntax
round(Amount,1)
2500.2
