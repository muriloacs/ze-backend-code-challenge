# Backend Challenge

## 1. Stack

This project was built on top of the following stack:
- **Programming language:** Python (3.8.3)
- **Framework:** Django (3.0.8)
- **API:** GraphQL
- **Database:** Postgres/Postgis
- **Container:** Docker/Compose

## 2. Installation

In order to make this project cross-platform it was built on top of docker containers. 
So please, install it if you don't have it yet.

Docker: https://docs.docker.com/get-docker/

Docker Compose: https://docs.docker.com/compose/install/

Go to project root:
```shell
cd ze-backend-code-challenge
```

Before starting make sure to stop running containers:
```shell
docker stop $(docker ps -a -q)
```

Now build the application:
```shell
docker-compose up -d --build
```

Once it's done, you can check logs by running:
```shell
docker-compose logs -f
```
Wait until server is up and running. You will see this message:
```
ze_backend | Django version 3.0.8, using settings 'ze.config.settings'
ze_backend | Starting development server at http://0.0.0.0:8000/
ze_backend | Quit the server with CONTROL-C.
```

At this point application must be running already. CTRL+C to quit the logs.

Now we need to migrate the database schema:
```shell
docker-compose exec backend python manage.py migrate --noinput
```

In case you want to login to admin you'll need a superuser. Run:
```shell
docker-compose exec backend python manage.py createsuperuser
```
It will ask you for username, email and password.
You can access admin: http://localhost:8000/admin

Running all unit and API tests:
```shell
docker-compose exec backend python manage.py test --keepdb
```

## 3. Challenge resolution
Before talking about code I'd like to clarify the development process that I used throughout the project.

First of all, I did the analyses, created tasks and put them on a Kanban Board: https://github.com/muriloacs/ze-backend-code-challenge/projects/1

After that I started creating dedicated branches on Git for each one of those tasks. Each one of them led to a PR: https://github.com/muriloacs/ze-backend-code-challenge/pulls?q=is%3Apr+

I set the Github project to only allow "Squash and Merge" on PRs so the Git history looks crystal clear.

This application is able to create partners and search for them through either an ID or by location.
The location search ensures to seek the nearest partner which the coverage area includes the location.
APIs are exposed through the GraphQL endpoint: http://localhost:8000/graphql.

Database table is properly indexed in order to make search faster.

I tried to keep the project clean and the code readable to humans as I always do :)

Now let's play around with the API: http://localhost:8000/graphql

### 3.1. Create a partner:
Create a partner and copy the returned id so you can use it in the next Query.

ps: You may try to create partners with same document. It must return an error since it's unique.
```
mutation {
  partner(
    input: {
      tradingName: "Foo",
      ownerName: "Bar",
      document: "SP100700TO",
      coverageArea: {type: "MultiPolygon", coordinates: [[[[-46.65285,-23.62214],[-46.66087,-23.6175],[-46.66919,-23.61431],[-46.67681,-23.60916],[-46.68238,-23.61879],[-46.69753,-23.61244],[-46.70271,-23.62229],[-46.70967,-23.62544],[-46.72057,-23.63543],[-46.72585,-23.64278],[-46.72505,-23.65023],[-46.72014,-23.65516],[-46.72703,-23.67252],[-46.72053,-23.6773],[-46.71904,-23.68142],[-46.71394,-23.68979],[-46.70936,-23.69737],[-46.70341,-23.69991],[-46.69105,-23.70101],[-46.68075,-23.70266],[-46.67217,-23.69696],[-46.66204,-23.69677],[-46.65157,-23.69543],[-46.63441,-23.69048],[-46.62797,-23.68686],[-46.6229,-23.67696],[-46.62727,-23.67526],[-46.63078,-23.6723],[-46.63372,-23.65602],[-46.63314,-23.65139],[-46.63118,-23.64707],[-46.62985,-23.63813],[-46.62967,-23.6336],[-46.62958,-23.62914],[-46.63482,-23.62981],[-46.64152,-23.6293],[-46.64392,-23.63054],[-46.64598,-23.63088],[-46.64736,-23.62903],[-46.64847,-23.62658],[-46.6498,-23.62405],[-46.65285,-23.62214]]]]},
      address: {type: "Point", coordinates: [-46.66771, -23.659363]}
    },
  )
{
    partner {
      id
      tradingName
      ownerName
      document
      coverageArea {
        type
        coordinates
      }
      address {
        type
        coordinates
      }
    }
  }
}
```

### 3.2. Load partner by id:
Use here the partner id that was returned in the Mutation.
```
query {
  partner (id: "UGFydG5lclR5cGU6MQ==") {
    id
    tradingName
    ownerName
    document
    coverageArea {
      type
      coordinates
    }
    address {
      type
      coordinates
    }
  }
}
```

### 3.3. Search partner by location:
After saving some partners you can query by location (lat/long).

The search ensures to find the nearest partner which the coverage area includes the location.
```
query {
  partner (location: {lat: -46.66700, long: -23.659300}) {
    id
    tradingName
    ownerName
    document
    coverageArea {
      type
      coordinates
    }
    address {
      type
      coordinates
    }
  }
}
```

### 3.4. Search all partners:
Just in case you want to search all partners.
```
query {
  allPartners {
    edges {
      node {
        id
        tradingName
        ownerName
        document
        coverageArea {
          type
          coordinates
        }
        address {
          type
          coordinates
        }
      }
    }
  }
}
```
