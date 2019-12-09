Welcome to Wazimap Data Manager's documentation!
================================================

Wazimap Data Manager is a django application to upload datasets to `Wazimap <http://wazimap.co.za>`_.

This application was built to allow users to easily upload datasets via a ui or an api.


Formatting of Data
====================


Data Manager UI
================
The UI is a simple django admin page which contains 2 form fields

* Table Name - This is the name of the field table.
* Dataset - File to be uploaded.



Data Manager API
====================
The api provides a programatic way to upload datasets.

There are two api urls that are needed to upload a new dataset.

* api/1.0/table

Quick Note: This api endpoint is avaliable in wazimap  
This lists all the avaliable tables and their ids  in wazimap
   
* /api/1.0/data/upload
  
This endpoint allows for the uploading of the dataset to a specific Fieldtable id. 




