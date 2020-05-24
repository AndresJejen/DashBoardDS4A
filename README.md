# DashBoard DS4A Dashboard - Bogota Team 7

Frontend for Final project DS4A Latam.
Data Source: provided by company

## General Description

Our data comes from a big E-commerce with operations in Brazil, this company sells mobile cellphones
that have been used and still work for a second customer.

This Dashboard shows in two different sections a general overview about data and in a third one a dinamic
implementation of a trained model that helps us to understand and give son valuable insights
about conversion.

## Technology

This part of the project is build in two parts `Backend` and `Frontend`.

### Backend

The Backend is build with python using Flask as server and Docker as process runner in second plane, 
also the data that this dashboard uses provides from a database in `Elastic Search`, where all the data provided
by the company stay safe and is easy to query from authorized users.

### Frontend

The frontend is implemented with `Dash`, a powerful toll for building interactive plots with `Plotly`.

## Data Flow

For this application the data was indexed on a cluster of `Elastic Search` via Python SDK, every Row of the CSV provided by the company 
is a Document. We use the power of `DSL` of `Elasticsearch` to query specific data between (~8.7 Millons of Rows) via Python SDK.
Our Python Backend convert this query into Pandas dataframe and provide some transformations if it is needed, next
we plot data.

## Model Implementation
Our Model was packed using pickle format. This file was loaded on Python backend, with schema and weights. On Model Tab,
we provide some inputs (numeric and Select) where the user can fill it and the model is feeded with this data.

## Developers
- Germán Andrés Jején cortés
- Fancisco Paz
- Victor Saenz Bonilla



