import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()

@app.get('/') # principal route
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact', response_class=HTMLResponse) # contact route
def get_list():
    return '''
        <h1> Contact </h1>
        <p> This is a contact page </p>
    '''




def run():
    store.get_categories()



if __name__ == '__main__':
    run()