import jwt

payload_data = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dies ist ein Kommentar


token1 = jwt.encode (
   payload = payload_data,
    key ='superkey'
)
print(token1)

tokendecode = jwt.decode (token1,"superkey",algorithms=['HS256'])
print(tokendecode)