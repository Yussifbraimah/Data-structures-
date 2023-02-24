#Script for car prices
#prices of cars are in US dollars
carPrices= {'bentleyBacalar':4500,
'hennessey':750000,
'audi':320000,
'zenvoTsrs':3000000,
'ferrariMonza':20000000,
'mcLarenElva':818000,
'czinger21C':111000,
'deTomasoP72':32500,
'kia':801000,
'bugatti250P':55500,
'benz150Kp':91000,
'cadillac':43000,
'subaru':41200,
'luxus':21500,
'hyundai':86100,
'volvo':22200,
'landRover':53200,
'mitsubishi':72200,
'buick':34440,
'porche':83500,
'volkswagen':13000,
'chevrolet':56000,
'rangeRover':2000,
'bugatti250Gp':39000,
'mercedesBenz':9000,
'ferrari':89000,
'lamborghini':890000,
'pagani':4710000,
'astonMartin':633000,
'mazda':'298600',
'benleyMulsanne':'9710000',
'honda':3420000,
'rimacNevera':175000
}
carBrand = input('enter carBrand: ')
if carBrand in carPrices:
    print(f'the price of {carBrand} is ${carPrices[carBrand]:,}')
else:
    print(f'sorry {carBrand} is not available')
    
    
    #https://github.com/Yussifbraimah/Data-structures-






