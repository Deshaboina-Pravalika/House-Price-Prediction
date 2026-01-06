import pickle
import xgboost as xgb

with open("hyd_house_xgb.pkl", "rb") as f:
    model = pickle.load(f)
 
model.save_model("hyd_house_xgb_revised.json")

print("Model successfully converted to hyd_house_xgb_revised.json")
