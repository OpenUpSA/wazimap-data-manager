Welcome to Wazimap Data Manager's documentation!
================================================

Wazimap Data Manager is a django application to upload datasets to `Wazimap <http://wazimap.co.za>`_.

This application has 2 goals

* Upload formatted datasets via django admin.
  
* Programatically upload datasets via an api.


Formatting of Data
====================

Data manager expects the data to be formatted in such a way that it can be directly inserted into the database.
An Example:

This table represents a csv file containing data related to population group.
Notice that the csv file must match the database structure of the FieldTable


.. csv-table:: Example csv file
    :header: "geo_level", "geo_code", "geo_version", "population group", "total"

    "ward", "12345678", "2011", "Black", "1234"     
    "ward", "12345678", "2011", "White", "5678"
    "ward", "12345678", "2011", "Coloured", "5232"
    "ward", "12345678", "2011", "Indian", "2346"


Behind the scenes data manager uses the postgres copy command, so the headers of the csv must be removed before the dataset gets uploaded.



Data Manager UI
================

The UI is a simple django admin page which contains 2 form fields

* Table Name - This is the name of the field table.
* Dataset - File to be uploaded in csv format.



Data Manager API
====================
The api provides a programatic way to upload datasets.

There are two api urls that are needed to upload a new dataset.

* api/1.0/table

Quick Note: This api endpoint is avaliable in wazimap.  
This lists all the avaliable tables and their ids in wazimap
   
* /api/1.0/data/upload
  
This endpoint allows for the uploading of the dataset to a specific Fieldtable id. 




