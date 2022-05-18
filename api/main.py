
from fastapi import FastAPI
from constants import target_names
from pydantic import BaseModel
import joblib
import os
 
# Creating FastAPI instance
app = FastAPI()
 
# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
 
# Loading model
clf = joblib.load(
    os.environ.get('MODEL_PATH')
)

# Creating an endpoint to receive the data
# to make prediction on.
@app.post('/predict')
def predict(data : request_body):
    # Making the data in a form suitable for prediction
    test_data = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
    ]]
     
    # Predicting the class
    class_idx = clf.predict(test_data)[0]
     
    # Return the result
    return { 'class' : target_names[class_idx]}