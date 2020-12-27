# Online shoppers purchasing intention prediction

An analysis of a shoppers purchasing intention dataset. Contains a Python Notebook with visualizations, data pre-processing and machine/deep learning models for supervised learning. A model is then exported to a Django application to be used with a REST API. Requests can be made with cURL or every request senders to make predictions on a new observation.

## Dataset description

The dataset used is the "Online Shoppers Purchasing Intention Dataset". 

It's a dataset regrouping online sessions and for each one, whether or not it ended with shopping. Of the 12,330 sessions in the dataset, 84.5% (10,422) were negative class samples that did not end with shopping, and the rest (1908) were positive class samples ending with shopping.

The dataset consists of 10 numerical and 8 categorical attributes.
The 'Revenue' attribute is a boolean feature indicating if the session ended with shopping or not.

[Dataset Link](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset#)  

Citations: Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018)

## Data analysis

### Study objectives

Our objective is, for a given observation, to be able to predict whether or not the session will end with shopping. As the target is a boolean variable, it's a binary classification problem. Using the multiple features of a session, we will implement data-driven models to predict the shopper intention.


### Data-driven models

For this dataset, we used and studied multiple machine/deep learning models. We showed an evolution of our models, the advantages and disadvantages and we compared them.
The three models used are:
- a Decision Tree
- a Multi-layer Perceptron
- a Random Forest Classifier

## Django application and REST API

First, we have to start the Django Web application.

```sh
❯ cd /path/to/project/apirest
❯ python manage.py runserver
```

### REST endpoints

#### `GET /shoppers/`

Fetch the database population.

```sh
❯ curl localhost:8000/shoppers/
```
![movies](./img/get_shoppers.png)

#### `POST /shoppers/`

Save a new shopper in the database.

```sh
> curl -X POST -H "Content-Type: application/json" -d 
   "{\"Administrative\":0,
     \"Administrative_Duration\":0.0,
     \"Informational\":0,
     \"Informational_Duration\":0.0,
     \"ProductRelated\":1,
     \"ProductRelated_Duration\":0.0,
     \"BounceRates\":0.2,
     \"ExitRates\":0.2,
     \"PageValues\":0.0,
     \"SpecialDay\":0.0,
     \"Month\":\"Feb\",
     \"OperatingSystems\":1,
     \"Browser\":1,
     \"Region\":1,
     \"TrafficType\":1,
     \"VisitorType\":\"Returning_Visitor\",
     \"Weekend\":false,
     \"Revenue\":null}" localhost:8000/shoppers/
```

#### `GET /shopper/:id`

Fetch a specific shopper.

```sh
❯ curl -H "Accept: application/json" localhost:8000/shopper/1/
{
  "Administrative":0,
  "Administrative_Duration":0.0,
  "Informational":0,
  "Informational_Duration":0.0,
  "ProductRelated":1,
  "ProductRelated_Duration":0.0,
  "BounceRates":0.2,
  "ExitRates":0.2,
  "PageValues":0.0,
  "SpecialDay":0.0,
  "Month":"Feb",
  "OperatingSystems":1,
  "Browser":1,
  "Region":1,
  "TrafficType":1,
  "VisitorType":"Returning_Visitor",
  "Weekend":false,
  "Revenue":null
}
```
#### `PUT /shopper/:id`

Modify a specific shopper.

```sh
> curl -X PUT -H "Content-Type: application/json" -d 
   "{\"Administrative\":123456,
     \"Administrative_Duration\":0.0,
     \"Informational\":0,
     \"Informational_Duration\":0.0,
     \"ProductRelated\":1,
     \"ProductRelated_Duration\":0.0,
     \"BounceRates\":0.2,
     \"ExitRates\":0.2,
     \"PageValues\":0.0,
     \"SpecialDay\":0.0,
     \"Month\":\"Feb\",
     \"OperatingSystems\":1,
     \"Browser\":1,
     \"Region\":1,
     \"TrafficType\":1,
     \"VisitorType\":\"Returning_Visitor\",
     \"Weekend\":false,
     \"Revenue\":null}" localhost:8000/shopper/4/
```

#### `DELETE /shopper/:id`

Delete a specific shopper.

```sh
> curl -X DELETE localhost:8000/shopper/4/
```

[MIT](https://choosealicense.com/licenses/mit/)
