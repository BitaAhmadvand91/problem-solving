n = input()
planets ={'mercury':'-','venus':'--','earth':'---','mars':'----','jupiter':'-------------','saturn':'-------------------------','uranus':'------------------------------------------------','neptune':'--------------------------------------------------------------------------','pluto':'--------------------------------------------------------------------------------------------------'}
if n in planets:
    print(f'sun {planets[n]} {n}')
else:
    print(f'there is no panet with {n} name. try again.') 
       