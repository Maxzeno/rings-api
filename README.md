# Lord of the rings sdk

SDK for Lord of the rings api
## Setup

Install

```bash
  pip install lord-of-the-rings-sdk
```


## API Reference

#### Imports

```python
  from lord_of_the_rings_sdk import LordOfTheRings
```
```python
  # The first argument is the token
  api = LordOfTheRings(base_url='url to api', token='your token')
```

#### Get items example movie

```python
  # Returns requests.models.Response object
  resp = api.movie()

  # Returns json object
  resp.json()

```

#### Get single item example quote

```python
  # if the_id is specified it returns item with specified id
  resp = api.quote(the_id="id of the item")

  # Returns json object
  resp.json()

```

#### Get single movie with quate

```python
  # if the_id is specified it returns item with specified id
  resp = api.quote(the_id="id of the item", extra_path='quote')

  # Returns json object
  resp.json()

```

#### Tests
- Clone the repo

- run 'test/name of test'

