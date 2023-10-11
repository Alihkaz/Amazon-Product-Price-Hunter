#
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib



# extracting the price:

my_email="Your Email"
passwordd="Your Password"

link="https://www.amazon.com/dp/B075CYMYK6ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(
  
                        url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers={ 'User-Agent':'find them in the properties of your browser settings',
                                 'Accept-Language':'find them in the properties of your browser settings ',
                                 'Accept':'find them in the properties of your browser settings',
                                 'Accept-Encoding':'find them in the properties of your browser settings'}
                     )


soup = BeautifulSoup(response.content, "lxml")

price=soup.find(name="span",class_="a-offscreen")

name=soup.find(name="span",id="productTitle")

# sprice=price.split("$")[1]

print(price.text)

print(name.text)



#**********************sending email***********************#


if float(price.text)<100:
   with smtplib.SMTP("smtp.gmail.com") as connection :

    connection.starttls()
    connection.login(user=my_email,password=passwordd)
    connection.sendmail(from_addr=my_email,to_addrs="Address to send",msg= f"subject:Amazon Price Alert! \n\n {name} is now ${price.text}\n visit {link} for more info !")
    connection.close()



