# Letapay backend

## sample post request
```
curl --location 'http://127.0.0.1:8000/payments' \
--header 'Content-Type: application/json' \
--data '{
    "sender_address": "0x141adc0e0158B4c6886534701412da2E2b0d7fF1",
    "receiver_address": "0x31B2821B611b8e07d88c9AFcb494de8E36b09537",
    "amount": 0.6,
    "payment_datetime": "2023-06-29T12:34:56Z",
    "status": "INPROGRESS",
    "payment_type": "SCHEDULED"
}'
```

## sample get request
```
curl --location --request GET 'http://127.0.0.1:8000/payments' \
--header 'Content-Type: application/json' \
--data '{
    "sender_address": "0x141adc0e0158B4c6886534701412da2E2b0d7fF1",
    "receiver_address": "0x31B2821B611b8e07d88c9AFcb494de8E36b09537",
    "amount": 0.6,
    "payment_datetime": "2023-06-29T12:34:56Z",
    "status": "INPROGRESS",
    "payment_type": "SCHEDULED"
}'
```

```

```