1. create virtual environment 
```python -m venv venv```
2. activate virtual environment 
PowerShell:
```\venv\Scripts\activate.ps1``` 
or 
bash:
```source /venv/bin/activate```
`
3. run
```python -m pip install -r requirements.txt```
4. Create a copy of `.env.example` named `.env`
5. Enter Credentials into `.env`
6. Run `python atlassian-api-tester.py

    - If anything besides 'Successful connection' prints, the connection to the api failed!