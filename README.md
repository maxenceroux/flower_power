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
Install webpack ? (bundle to one file js)
```bash
npm i webpack webpack-cli --save-dev
```

Install babel ?
```bash 
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
```

Install react
```bash
npm i react react-dom --save-dev
```

Install material-ui
```bash
npm install @material-ui/core
```

Install babel plugin - proposal (async wait)
```bash
npm install @babel/plugin-proposal-class-properties
```
Install react router
```bash 
npm install react-router-dom
```    
Install icons
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

