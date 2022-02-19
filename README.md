# Python Text Match APP
Fuzzy text match app that finds similar strings in csv file and get matching percentage. 

The app contains two simple web views one contains a form with a dropdown that lists all the available lookup keys and a search button. Once you select a key and press enter you will be redirected to a second view which displays a table containing the key and all similar values to its value with the matching percentage for each one.

## Requirements
* Python >= 3.8
* Django >= 3.2


## Included Features
- Key lookup in a csv file using Pandas.
- Text matching rate using fuzzywuzzy.
- Code documentation using Sphinx.
- Request rate limiting 5/min.
- 100% Test coverage.
- The app is dockerized.


## Installation
1. Clone the project.
```bash
git clone https://github.com/mustafa-kamel/pytextmatch.git
```
2. Change the active directory to the project directory.
```bash
cd pytextmatch
```
3. Create a virtual environment.
```bash
python3 -m venv venv
```
4. Activate the virtual environment.
```bash
source venv/bin/activate
```
5. Install the app requirements by running.
```bash
pip install -r requirements.txt
```
6. Run the migrations.
```bash
./manage.py runserver
```
7. Run the local server.
```bash
./manage.py runserver
```
8. Now visit the [http://localhost:8000](http://localhost:8000/) to view the app.



## Testing
The project contains test coverage for all urls and views that covers all possible scenarios.

To test the app is working properly run the following command:
```bash
./manage.py test
```



## License
This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.