old_des = ['nokia', 'micromax', 'samsung', 'lg', 'china']
dispose_des = []
while old_des:
    current_des = old_des.pop()
    print("These is old model of phone : "+current_des)
    dispose_des.append(current_des.title())
for updated in dispose_des:
    print(updated.title())
