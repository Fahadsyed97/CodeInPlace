from PIL import Image
image_pfizer = Image.open('pfizer.png')
image_moderna = Image.open('moderna.jpg')
image_covishield = Image.open('covishield.jpg')
image_covaxin = Image.open('covaxin.jpg')
image_sinopharm = Image.open('sinopharm.jpg')
image_sputnikv = Image.open('sputnikv.jpg')
image_astrazeneca = Image.open('astrazeneca.jpg')
image_epivaccorona = Image.open('epivaccorona.jpg')
image_johnson = Image.open('johnson.jpg')
image_sinovac = Image.open('sinovac.jpg')
image_chart = Image.open('VaccineChart.jpg')
def main():
    intro()
    for i in range(1):
        country_name = input("Which country do you belong to? ")
        country(country_name)
        vaccine_name = vaccine()
        age(vaccine_name)

def intro():
    print("")
    print("This system will tell country wise details of every vaccine available.")
    print("You will be provided with the number of dosage, side effects and effectiveness of every vaccine based on what you select.")
    print("At the end your eligibility w.r.t your age will be checked for the selected vaccine.")
    print("Stay Safe and Healthy.")
    print("")
    print("For now countries included are: \nUSA \nIndia \nGermany \nRussia \nChina \nUK \nSaudiArabia \nQatar \nUAE \nPakistan \nBangladesh \nCanada \nFrance.")
    print("")

def country(country_name):
    USA = ["Johnson&Johnson", "Moderna", "Pfizer"]
    India = ["Covishield", "Covaxin", "Sputnik V"]
    Germany = ["Johnson&Johnson", "Moderna", "AstraZeneca", "Pfizer"]
    Russia = ["EpiVacCorona", "Sputnik V"]
    China = ["Sinopharm", "Sinovac"]
    UK = ["Moderna", "AstraZeneca", "Pfizer"]
    SaudiArabia = ["AstraZeneca", "Pfizer"]
    Qatar = ["Moderna", "Pfizer"]
    UAE = ["AstraZeneca", "Pfizer", "Sinopharm", "Sputnik V"]
    Pakistan = ["AstraZeneca", "Sinopharm", "Sputnik V"]
    Bangladesh = ["AstraZeneca"]
    Canada = ["Moderna", "AstraZeneca", "Pfizer"]
    France = ["Johnson&Johnson", "Moderna", "AstraZeneca", "Pfizer"]
    if country_name == "USA" or country_name == "America" or country_name == "usa" or country_name == "america":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in USA:
            print(VACCINE)
        print("")
    elif country_name == "India" or country_name == "india":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in India:
            print(VACCINE)
        print("")
    elif country_name == "Germany" or country_name == "germany":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Germany:
            print(VACCINE)
        print("")
    elif country_name == "Russia" or country_name == "russia":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Russia:
            print(VACCINE)
        print("")
    elif country_name == "China" or country_name == "china":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in China:
            print(VACCINE)
        print("")
    elif country_name == "UK" or country_name == "England" or country_name == "england" or country_name == "uk":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in UK:
            print(VACCINE)
        print("")
    elif country_name == "SaudiArabia" or country_name == "saudi" or country_name == "saudiarabia" or country_name == "saudi arabia" or country_name == "Saudi Arabia":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in SaudiArabia:
            print(VACCINE)
        print("")
    elif country_name == "Qatar" or country_name == "qatar":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Qatar:
            print(VACCINE)
        print("")
    elif country_name == "Dubai" or country_name == "UAE" or country_name == "uae" or country_name == "dubai":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in UAE:
            print(VACCINE)
        print("")
    elif country_name == "Pakistan" or country_name == "pakistan":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Pakistan:
            print(VACCINE)
        print("")
    elif country_name == "Bangladesh" or country_name == "bangladesh":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Bangladesh:
            print(VACCINE)
        print("")
    elif country_name == "Canada" or country_name == "canada":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in Canada:
            print(VACCINE)
        print("")
    elif country_name == "France" or country_name == "france":
        print("Below are the vaccines available in your country",str(country_name)+".")
        for VACCINE in France:
            print(VACCINE)
        print("")
    else:
        print("Please enter a proper country name as shown above.")
        print("Restart.")
        print("")
    return country_name


def vaccine():
    vaccine_name = str(input("Select and type the vaccine to get details: "))
    if vaccine_name == "Pfizer" or vaccine_name == "pfizer":
        with open('pfizer.txt', mode='r') as pfizer:
            print(pfizer.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n95%")
            image_chart.show()
            image_pfizer.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Johnson&Johnson" or vaccine_name == "johnson&johnson" or vaccine_name == "johnson":
        with open('johnson.txt', mode='r') as johnson:
            print(johnson.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n72%")
            image_chart.show()
            image_johnson.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Covishield" or vaccine_name == "covishield":
        with open('covishield.txt', mode='r') as covishield:
            print(covishield.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n70.42%")
            image_chart.show()
            image_covishield.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Moderna" or vaccine_name == "moderna":
        with open('moderna.txt', mode='r') as moderna:
            print(moderna.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n94.5%")
            image_chart.show()
            image_moderna.show()
            print("")
        else:
            print("")
    elif vaccine_name == "AstraZeneca" or vaccine_name == "astrazeneca" or vaccine_name == "Astrazeneca":
        with open('astrazeneca.txt', mode='r') as astrazeneca:
            print(astrazeneca.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n82.4%")
            image_chart.show()
            image_astrazeneca.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Covaxin" or vaccine_name == "covaxin":
        with open('covaxin.txt', mode='r') as covaxin:
            print(covaxin.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n80.6%")
            image_chart.show()
            image_covaxin.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Sinopharm" or vaccine_name == "sinopharm":
        with open('sinopharm.txt', mode='r') as sinopharm:
            print(sinopharm.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n70-90%")
            image_chart.show()
            image_sinopharm.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Sputnik V" or vaccine_name == "sputnikv" or vaccine_name == "sputnik v" or vaccine_name == "sputnik V":
        with open('sputnikv.txt', mode='r') as sputnikv:
            print(sputnikv.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n91.6%")
            image_chart.show()
            image_sputnikv.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Epivaccorona" or vaccine_name == "epivaccorona" or vaccine_name == "EpiVacCorona":
        with open('epivaccorona.txt', mode='r') as epivaccorona:
            print(epivaccorona.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n95-100%")
            image_chart.show()
            image_epivaccorona.show()
            print("")
        else:
            print("")
    elif vaccine_name == "Sinovac" or vaccine_name == "sinovac":
        with open('sinovac.txt', mode='r') as sinovac:
            print(sinovac.read())
        print("")
        user = str(input("Want to get more details? Type Yes or No: "))
        print("")
        if user == "yes" or user == "Yes":
            print("How Effective? \n50%")
            image_chart.show()
            image_sinovac.show()
            print("")
        else:
            print("")
    else:
        print("Enter the vaccine name as shown above.")
        print("Restart.")
        print("")
    return vaccine_name

def age(vaccine_name):
    person_age = int(input("Please enter your age? "))
    if vaccine_name == "Pfizer" or vaccine_name == "pfizer" or vaccine_name == "covaxin" or vaccine_name == "Covaxin":
        if person_age >=12:
            print("Great you are eligible to get vaccinated. 😃")
            print("")
        else:
            print("Sorry, you are not eligible for",str(vaccine_name),"vaccine. ☹")
            print("")
    elif person_age >=18:
        print("Great you are eligible to get vaccinated. 😃")
        print("")
    else:
        print("Since your age is",str(person_age),"you are not eligible for",str(vaccine_name),"vaccine. ☹")
        print("")


if __name__ == '__main__':
    main()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
