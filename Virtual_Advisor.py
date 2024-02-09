
"""
Name: Abdul Rauf
Roll No: 93597
Email Address: raufakram91@gmail.com
Project Name: Virtual Advisor
Project Description:
It will take User's Name and Age as input and give Advices on Love, Life & Career according to User's Age as Output.
......................................................................................................................

First We'll Take User's Name and Age as Input by Making Variables
"""
Name= str(input("Enter Your Name"))
Age= int(input("Enter Your Age "))
"""
Implementing data as advices according to different age groups by applying if and elif.
"""
if 1 <= Age <= 15:

  print("Hi!",Name)
  print("Love: Focus on developing strong friendships and understanding healthy relationships.")
  print("Life: Explore your interests, discover your values, and build self-confidence.")
  print("Career: Start thinking about your passions and potential future paths. ") 
elif 15 <= Age <= 30:
 print("Hi!",Name)
 print("Love: Experiment with relationships, learn about communication and boundaries, and discover what qualities you value in a partner.")
 print("Life: Pursue your education or career goals, travel, step outside your comfort zone, and embrace self-discovery.")
 print("Career: Gain experience through internships, volunteering, or entry-level jobs, explore different fields, and develop your skills. ")
elif 31 <= Age <=50 :
    print("Hi!",Name)
    print("Love: Build a strong foundation in your existing relationship or seek fulfilling partnerships if single. Prioritize communication and intimacy.")
    print("Life: Focus on family, your career, personal growth, and achieving your goals. Maintain a healthy work-life balance.")
    print("Career: Advance your career, develop leadership skills, consider career changes if desired, and find work-life balance. ") 
elif 50 <= Age <=70:
 print("Hi!",Name)
 print("Love: Cherish your partner, nurture deep connections, and explore new adventures together.")
 print("Life: Pursue passions, contribute to the community, spend time with loved ones, and prioritize your well-being.")
 print("Career:  Transition to retirement smoothly, explore new challenges, or continue working if desired. Focus on personal fulfillment.") 
elif 70< Age< 100:
  print("Hi!",Name)
  print("Love: Continue nurturing relationships with loved ones, embrace new friendships, and appreciate the richness of your life.")
  print("Life: Prioritize your health, enjoy relaxation and leisure activities, share your wisdom, and leave a positive legacy.")
  print("Career: Enjoy retirement, volunteer, pursue hobbies, and focus on personal fulfillment. ")  



  """
  The End
  """
