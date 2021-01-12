"""
def clothing_companies(*clothing_companies):
    print("the last companies is : "+clothing_companies[-1])



clothing_companies("Nike","addidas","H&M")
"""





def my_function(**company_info):
    print("his last name is "+company_info["model"])

my_function(brand="apple",model="iphone-x")