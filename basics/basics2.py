# string=input("enter the string: ")
# string_clean=string.strip()
# if string_clean == "":
#     print("operation aborted: you didn't typed anthing")
# elif string_clean.isdigit():
#     string_integer=int(string_clean)
#     print("string in integer form is: ", string_integer)
# elif string_clean.count('.')==1 and string_clean.replace('.','',1).isdigit():
#     string_decimal=float(string_clean)
#     print("string in decimal form: ", string_decimal)
# else:
#     print(string, "is not of numeric type")

# string=input("enter the string: ")
# string_clean=string.strip()
# try:
#     if string_clean=="":
#         raise ValueError("blank input")
#     elif string_clean.isdigit():
#         parsed_result=int(string_clean)
#         detected_type="integer"
#     else:
#         parsed_result=float(string_clean)
#         detected_type="decimal"
# except ValueError:
#     if string_clean == "":
#         print("string can't be blank")
#     else:
#         print("string is not numeric type")
# else:
#     print(f"{string} is of {detected_type} datatype")
# finally:
#     print("parsing execution round finished")