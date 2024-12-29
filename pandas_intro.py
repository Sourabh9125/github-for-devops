#DataFrame
import pandas as pd
cal={"Meals":[40,60,80],
     "calories":[420,380,390],
     "Divided":[2,1,3]}
calNew = pd.DataFrame(cal)
print(calNew) 


#Series
# import pandas as pd
# cal={"day1":420, "day2":380,"day3":390}
# calNew = pd.Series(cal)
# print(calNew["day2"])



# import pandas as pd
# num =[4,56,4,6,8,7,5,5]
# numNew = pd.Series(num,index=[5,6,7,8,9,10,11,12])
# print(numNew[8])