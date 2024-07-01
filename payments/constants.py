CONTRACT_ABI = """
[
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "senderAddress",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "recieverAddress",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "PaymentAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "senderAddress",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "recieverAddress",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "PaymentCompleted",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        },
        {
          "internalType": "address",
          "name": "recieverAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "addPayment",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        }
      ],
      "name": "completePayment",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        }
      ],
      "name": "getPayment",
      "outputs": [
        {
          "components": [
            {
              "internalType": "string",
              "name": "paymentId",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            },
            {
              "internalType": "enum LetapayV2.Status",
              "name": "status",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "senderAddress",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "recieverAddress",
              "type": "address"
            }
          ],
          "internalType": "struct LetapayV2.Payment",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "name": "payments",
      "outputs": [
        {
          "internalType": "string",
          "name": "paymentId",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "enum LetapayV2.Status",
          "name": "status",
          "type": "uint8"
        },
        {
          "internalType": "address",
          "name": "senderAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "recieverAddress",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]
"""

CONTRACT_ADDRESS = "0x4C849A3736694567cbd304fd8526339ed29b23AB"

alfajores_url = "https://alfajores-forno.celo-testnet.org"

NETWORK_URL = alfajores_url
