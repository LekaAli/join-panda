**Join Panda**

 *How to*:
- Setup: run *make install*
- Apply Migrations: run *make makemigrations*
- Create User: run *make createsuperuser*
- Running the app: run *make run*

 *Endpoint*
    Retrieve Rows(GET): 

    - endpoint: http://localhost:8000/api/endpoints/retrieve-rows/
    - query parameter names: date, country
    - example: ?date=2022-08-26&country=Italy
 
    Upload File(POST): 

    - endpoint: http://localhost:8000/api/endpoints/upload-file/
    
    - parameter names: uploaded_csv_file
    - example: {'uploaded_csv_file': <csv-file>}
    



 
