# Backend Challenge

## 1. Stack

**cross-platform**
**docker**

This project was built on top of the following stack:
- **Programming language:** Python (v3.8.3)
- **Framework:** Django (v3.0.8)
- **API:** GraphQL through Graphene
- **Database:** Postgres

## 2. Installation

cd ze-backend-code-challenge

docker stop $(docker ps -a -q)
docker-compose up -d --build
docker-compose logs -f

http://localhost:8000/admin

docker-compose exec backend python manage.py migrate --noinput
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py test --keepdb

## 3. Challenge resolution
...

### 3.1. Create a partner:
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
    success
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

### 3.2. Load partner by id:
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

### 3.3. Search partner by location:
query {
  partner (lat: 9.055862678251549, long: 7.493147848993504) {
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

### 3.4. Search all partners:
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
