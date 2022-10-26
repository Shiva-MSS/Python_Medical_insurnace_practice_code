Python Syntax: Medical Insurance Project:

Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. 
Using a formula that estimates a person’s yearly insurance costs, 
you will investigate how different factors such as age, sex, BMI, etc. 
affect the prediction
# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 1

# Add insurance estimate formula below
insurance_cost = 250 * age - (128 * sex) + (370*bmi)+(425*num_of_children)+(24000*smoker-12500)

print("This person's insurance cost is " + str(insurance_cost)+ " dollars.")
# Age Factor
age += 32
new_insurance_cost = 250 * age - (128 * sex) + (370*bmi)+(425*num_of_children)+(24000*smoker-12500)
print (new_insurance_cost)
change_in_insurance_cost  = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")
age += 28
# BMI Factor
bmi += 29.3
new_insurance_cost1 =  250 * age - (128 * sex) + (370*bmi)+(425*num_of_children)+(24000*smoker-12500)
change_in_insurance_cost_1 = new_insurance_cost1 - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost_1) + " dollars.")
# Male vs. Female Factor
bmi += 26.2
sex += 1
new_insurance_cost2 = (250 * age) - (128 * sex) + (370*bmi)+(425*num_of_children)+(24000*smoker - 12500)
print(new_insurance_cost2)
change_in_insurance_cost2 = new_insurance_cost2 - insurance_cost
print("The change in estimated cost for being male instead of female is "+ str(new_insurance_cost2)+ "dollars.")

Python Control Flow: Medical Insurance Project
In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.


#### Estimatiion of costs for 2nd project:

You will apply your knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.
# Add your code here
def analyze_smoker(smoker_status):
   if smoker_status == 1:
     print("To lower your cost, you should consider quitting smoking.")
   else:
     print("Smoking is not an issue for you.")
def analyze_bmi(bmi):
  if bmi > 30:
    print("“Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI to a value in between 18.5 and 25.”")
  elif bmi >= 25 and bmi <= 30 :
    print("“Your BMI is in the overweight range. To lower your cost, you should lower your BMI to a value in between 18.5 and 25.")
  elif bmi >= 18.5 and bmi < 25:
    print("Your BMI is in a healthy range")
  else:
    print("“Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.”")


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

Shiva_ins_cost = estimate_insurance_cost("Shiva", 22, 1, 18, 0, 0)

### python Loops:
Python Loops: Medical Insurance Estimates vs. Costs Project

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

total_cost  = 0
index = 0
while index < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[index]
  index += 1
average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: "+ str(average_cost) + " $$ dollars.")

for index in range(0,len (names)):
  name = names[index]
  insurance_cost = actual_insurance_costs[index]
  print("The insurance cost for "+ name +"is "+str(insurance_cost)+" $$ dollars.")
  Average_comparator = average_cost - actual_insurance_costs[index]
  if insurance_cost > average_cost:
    print("The insurance cost for "+name+" is above average by "+ (str(Average_comparator)).strip("-") + " $$ dollars")
  elif insurance_cost < average_cost:
    print("The insurance cost for "+name+" is below average by "+str(Average_comparator) + " $$ dollars")
  else :
    print("The insurance cost for "+name+" is equal to average ")

updated_estimated_costs = [estimated_cost * 11/10 for estimated_cost in estimated_insurance_costs]
print (updated_estimated_costs)


### Working with Python Lists: Medical Insurance Costs Project
You are a doctor sorting through medical insurance cost data for some patients.

Using your knowledge of Python lists,
you will store medical data and see what valuable insights 
you can gain from that data.

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("priscilla")
insurance_costs.append(8320.0)
medical_records  = zip(insurance_costs, names)
medical_records1 = list(medical_records)
print(medical_records1)
num_medical_records = len(medical_records1)
print(num_medical_records)
first_medical_record = medical_records1[0]
print("Here is the first medical record: "+ str(first_medical_record))
medical_records1.sort()
print('Here are the medical records sorted by insurance cost: '+ str(medical_records1))
cheapest_three = medical_records1[:3]
print(cheapest_three)
priciest_three = medical_records1[:-3]
print(priciest_three)

occurrences_paul = names.count("Paul")
print(occurrences_paul)

middle_five_records = medical_records1[3:7]
print(middle_five_records)
