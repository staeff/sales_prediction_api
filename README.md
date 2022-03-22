# Deploy a ML model using Flask

Based on: [https://github.com/abhinavsagar/machine-learning-deployment](https://github.com/abhinavsagar/machine-learning-deployment)

The app deploys a simple machine learning model to predict sales in the third month based on the sales in the first two months.

## Run the app and make a query

### With Docker

Run

```sh
$ docker run -dp 8080:8080 staeff/salespredictionapi
```

open [http://localhost:8080/](http://localhost:8080/) in a browser or make a curl request:

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"rate":5, "sales_in_first_month":200,"sales_in_second_month":400}' http://localhost:8080/results
```

### Without Docker

```sh
$ python3 -m venv .venv; source ./.venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ python app.py
# in another terminal window
(.venv) $ python request.py
523.8530977224776
```

When the flask process is running you can also open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and enter data into the website.

or use `curl`:

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"rate":5, "sales_in_first_month":200,"sales_in_second_month":400}' http://localhost:5000/results
```

## Repo contents

* `app.py` — a Flask app that receives inputs through website or API call, computes the predicted value based on our model and returns it.

* `HTML/CSS` — frontend code for the flask app

* `request.py` — makes an example API call

* `model.py` — computes a linear regression model to predict sales in the third month based on the sales in the first two months. No need to run this. The model is already stored in the repo.
