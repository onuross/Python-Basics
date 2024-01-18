student_id= input("Enter Your Student ID:")
name_surname= input("Enter Your Name and Surname:")
theo_hour_first=float(input("Enter Weekly Theoretical Course Hours of First Course:"))
theo_hour_second=float(input("Enter Weekly Theoretical Course Hours of Second Course:"))
pract_hour_first=float(input("Enter Weekly Practical Course Hours of First Course:"))
pract_hour_second=float(input("Enter Weekly Practical Course Hours of Second Course:"))
ects_credit_first=float(input("Enter ECTS Credits of First Course:"))
ects_credits_second=float(input("Enter ECTS Credits of Second Course:"))
term_first=float(input("Enter Term Grade of First Course:"))
term_second=float(input("Enter Term Grade of Second Course:"))
total_local_credit=theo_hour_first+theo_hour_second+(pract_hour_first+pract_hour_second)/2
total_ects_credit=ects_credit_first+ects_credits_second
wgpa_local=term_first*(theo_hour_first+pract_hour_first/2)/total_local_credit+term_second*(theo_hour_second+pract_hour_second/2)/total_local_credit
wgpa_ects=term_first*ects_credit_first/total_ects_credit+term_second*ects_credits_second/total_ects_credit

print(f"Dear {student_id} numbered student {name_surname}"
      f"\nTotal amount of local credits taken this semester is {total_local_credit}"
      f"\nTotal amount of ECTS credits taken this semester is {total_ects_credit}"
      f"\nWGPA based on local credit at the end of this semester is {wgpa_local:.2f}"
      f"\nWGPA based on ECTS at the end of this semester is {wgpa_ects:.2f}")
