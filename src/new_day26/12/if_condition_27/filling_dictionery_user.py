response = {}
poll_act = True
while poll_act:
    name = input("\n what is your name :")
    mout = input("\n which mountain you want ot go :")
    response[name] = mout
    repeat = input("\n would you like to go with another person (yes/no)? :")
    if repeat == 'no':
        poll_act = False

print("\n----poll results----")
for name,mout in response.items():
    print(name+" would you like climb:"+mout+"!")