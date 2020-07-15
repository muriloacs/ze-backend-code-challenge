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
      coverageArea: {type: "MultiPolygon", coordinates: [[[[8.988174792345296, 7.305908202108059], [9.297306855044836, 7.673950194244314], [8.966471297361368, 7.855224608281604], [8.906780006290315, 7.399291991157497], [8.97732320720076, 7.316894530231506], [8.982749040383606, 7.322387694293275], [8.988174792345296, 7.305908202108059]]]]},
      address: {type: "Point", coordinates: [6.740986207824642, 6.225814818469395]}
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

### 3.3. Search partner:
...


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
