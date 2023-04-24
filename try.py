food = {
   "indian" : ["fish","chicken"],
   "western" : ["hambuger","taco"]
}

print(food.get("indian"))

class avaFood(str,Enum):
   indian  = "indian"
   Western = "western" 
food = {
   "indian" : ["fish","chicken"],
   "western" : ["hambuger","taco"]
}
@app.get("/food/{fod}")
async def root(fod: avaFood):
   return food.get(fod)