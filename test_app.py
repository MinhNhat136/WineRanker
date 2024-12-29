from app import app 

def test_training(): 
    response = app.test_client().get('/train')
    assert response.status_code == 200
    assert response.data == b"Training Successful!"

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data

def test_predict(): 
    response = app.test_client().get('/predict')
    assert b"<!DOCTYPE html>" in response.data