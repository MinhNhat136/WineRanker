from app import app 

def test_training(): 
    response = app.test_client().get('/train')
    assert response.status_code == 200
    assert response.data == b"Training Successful!"

