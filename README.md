# GPT Address API (GPTAAPI) for Naruno
GPTAAPI is a decentralized API for OpenAI GPT. It allows you to use GPT without exposing your API key to the public. It is based on the [Naruno](https://naruno.org/) blockchain and uses the [Naruno API](https://naruno.org/api/) to communicate with the blockchain. GPTAAPI is written in Python and uses the [OpenAI GPT-3 API](https://openai.com/blog/openai-api/) to communicate with GPT.

## Features
- Decentralized system
- Secure communication between nodes
- Fast and easy to use
- Secure point for GPT API's
- Uses encryption to protect sensitive information


## Installation
You can install GPTAAPI by pip3:

```console
pip3 install gpt_address_api
```

## Usage

*If you want to use gpt_address_api you must to use Naruno. For now please checkout the [Baklava Testnet](https://naruno.org/baklava-testnet/).

Getting address of client and server:
```console
narunocli -pw
```

### Server
For accessing your gpt api on blockchain you should create a gpt_address_api, giving trusted user addresses and api_key.

```python
from gpt_address_api import gptaapi

my_gptaapi_server = gptaapi("MyNarunoPass")

my_gptaapi_server.set_encrypt_key("mystrongencrypt_key")

my_gptaapi_server.set_api_key("my_open_ai_api_key")

my_gptaapi_server.add_user("client_address")

my_gptaapi_server.run()
```

also you can use in command line:
```console	
gptaapi --password MyNarunoPass --encrypt_key "mystrongencrypt_key" --trusted_users ["client_address"] --api_key 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 run
```

### Client
To use gptaapi, you can call the gptaapi.ask function with your blockchain address, message and encryption key as the parameter:

```python
from gpt_address_api import gptaapi

my_gptaapi_client = gptaapi("MyNarunoPass")

response = my_gptaapi_client.ask("server_address", "Hello gpt, how are you", "mystrongencrypt_key")

print(response)

my_gptaapi_client.close()
```

also you can use in command line:
```console	
gptaapi --password "MyNarunoPass" ask "server_address" "Hello gpt, how are you" "mystrongencrypt_key"
```


This will return the response of gpt result.

## Contributing
Contributions to gptaapi are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
gptaapi is released under the MPL-2.0 License.
