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

At this point application must be running already. Access:
http://localhost:8000/admin

Now we need to migrate the database schema:
```shell
docker-compose exec backend python manage.py migrate --noinput
```

In case you want to login to admin you'll need a superuser. Run:
```shell
docker-compose exec backend python manage.py createsuperuser
```
It will ask you for username, email and password.

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
```
mutation {
  partner(
    input: {
      tradingName: "Foo2",
      ownerName: "Bar2",
      document: "SP100700TO",
      coverageArea: {type: "MultiPolygon", coordinates: [[[[30, 20], [45, 40], [10, 40], [30, 20]]],[[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]]},
      address: {type: "Point", coordinates: [-46.57421, -21.785741]}
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
  partner (location: {lat: 9.055862678251549, long: 7.493147848993504}) {
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
In case you want to search all partners.
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
