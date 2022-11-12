# m1=int input("marks")
# m2=int input("marks")
# m3=int input("marks")

# accept 3 marks from the user and print the average of best 2 marks
marks1 = int(input("enter the first mark:"))
marks2 = int(input("enter the second mark:"))
marks3 = int(input("enter the third mark"))
if marks1 < marks2 and marks1 < marks3:
    print("average of best two marks:", (marks2 + marks3)/2)
elif marks2 < marks3 and marks2<marks1:
    print("äverage of best two marks:", (marks1 + marks3)/2)
else:
    print("average of best two marks:", (marks1+marks2)/2)