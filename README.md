# Installation 


## Initialize App
```sh
django-admin startproject flowers
cd .\flowers\
django-admin startapp api
```

## Bootstrap DB
```sh
python .\manage.py makemigrations
python .\manage.py migrate
```

## Run server 
```sh
python .\manage.py runserver
```

## Initialize React
```sh
django-admin startapp frontend
```

Add src components static templates folders

```sh
cd frontend
django-admin startapp frontend
```
    3. Install webpack ? (bundle to one file js)
    ```bash
    npm i webpack webpack-cli --save-dev
    ```

    4. Install babel ?
    ```bash 
    npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
    ```

    5. Install react
    ```bash
    npm i react react-dom --save-dev
    ```

    6. Install material-ui
    ```bash
    npm install @material-ui/core
    ```

    7. Install babel plugin - proposal (async wait)
     ```bash
     npm install @babel/plugin-proposal-class-properties
     ```
    8. Install react router
    ```bash 
    npm install react-router-dom
    ```    

    9. Install icons
    ```bash
    npm install @material-ui/icons
    ```

# Run 
## Containers
```sh
docker-compose up --build
```

## JS
```sh
docker-compose exec web sh
npm run dev
```

