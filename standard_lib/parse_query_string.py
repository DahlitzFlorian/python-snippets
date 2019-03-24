from urllib.parse import parse_qs


input_string = "host=171.25.2.7&port=8080&port=8081"
result = parse_qs(input_string)
print(result)
