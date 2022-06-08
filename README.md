
<!-- Find and Replace All [repo_name] -->
<!-- Replace [product-screenshot] [product-url] -->
<!-- Other Badgets https://naereen.github.io/badges/ -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


![image](https://user-images.githubusercontent.com/96163075/171256156-cd9562d6-07f9-405f-ae11-482c17c2633f.png)



# Rewards R' Tokens
Note: Please refer to smart contract files for complete source code.

Credit card companies are facing considerable decline with respect to customer retention.

This application contains features which are aimed at the that specific statistic.  This targeted feature requires the customer to be engaged with the credit card company and expect the customers to activate such cash back bonus when they use their credit card and recieve rewards.  

This project is a centralized platform where customers can link all their credit cards to an account.  The banks themselves define rewards tokens in the form of NFTs - which are activated via achieving a spend target, customer longevity, or dates of customer significance like birthday, anniversary etc.

The reward tokens get activated immediately for a duration set by the banks or customer can xchoose to activate it at a later date or for a specific transaction as per his/her wish.

The points which are accumulated via purchases can be used for exchange items at the NFT stores: rewards store will be established for users to exchange their NFTs - convert your points to coffee, bagel, shoes, laptops or whatever the customer might like.

## Technologies

This project leverages the following tools:

- Conda
- Solidity - v0.5.0
- Remix IDE
- OpenZeppelin
- Ganache
- MetaMask xtension
- SafeMath
- Git Bash

## Installation Guide

Note: You must install and have an operating local blockchain on your machine to test and deploy the smart contracts - such as Ganache and an operating MetaMask wallet.

## Usage
## Deploying Smart Contracts

Note: Please refer to folder Screenshots-Videos for screenshots and videos of completed test transactions.

The following code imports standard ERC-20 token contracts into our solidity files. Using constructor, we are then able to build upon the imported smart contracts to our desire for our token.

```solidity
// Set version of Solidity
pragma solidity ^0.5.0;

// Set imports from OpenZeppelin
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

// Establish contract name
contract RT_Token is ERC20, ERC20Detailed {
    address payable owner;

// Require that only contract owner is allowed to mint tokens
    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

// Fill in constructor information for RT token
    constructor(uint initial_supply) ERC20Detailed("RT_Token", "RT", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

// Define new function for owner to mint tokens to a specific recipient
    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
```


The following screenshots capture each contract's successful deployment once the main source code for each smart contract is complete.

![](https://github.com/Alexisg324/Rewards-R-Tokens/blob/main/Images/Screen%20Shot%202022-06-08%20at%201.07.29%20PM.png)
![](https://github.com/Alexisg324/Rewards-R-Tokens/blob/main/Images/Screen%20Shot%202022-06-08%20at%201.07.42%20PM.png)

Above screenshot shows the connection between the two minted accounts.  Now, there should be no problem with any transactions directly between store and account.  

---

## Testing Smart Contracts Using Ganache and Metamask

Once each smart contract is successfully compiled, the next step would be to run some test transactions. In our case, Ganache will serve as our local blockchain network and the injected Web3 will be MetaMask extension. 

![](https://github.com/Alexisg324/Rewards-R-Tokens/blob/main/Images/Screen%20Shot%202022-06-08%20at%201.41.02%20PM.png)
![](https://github.com/Alexisg324/Rewards-R-Tokens/blob/main/Images/Screen%20Shot%202022-06-08%20at%201.41.27%20PM.png)

The following video shows how to successfully deploy the smart contract and run test transactions.

[Initial Setup](https://drive.google.com/file/d/1IYYnArhZov05DsWCBvChrarL91VwDYF-/view?usp=sharing)

[Test Transactions](https://drive.google.com/file/d/11fS0aclShvnZ_BVJn79Bao1eTKfNSaU_/view?usp=sharing)

----

## Using The Rewards Store 
The following is a demonstration on how to use the Rewards Store for RT tokens.  
[RT Rewards Store](https://drive.google.com/file/d/1IxXQQjLqZ5PEFsvU-Zy6ZJo9LQRcSSuc/view?usp=sharing)


## Contributors
David Lee Ping [Linkedin](https://www.linkedin.com/in/david-lee-ping/)

Alexis Garcia [Linkedin](https://www.linkedin.com/in/alexis-rose-garcia/)

Ashok Kumar  [INSERT-LINKEDIN]

Dev Patel [LINKEDIN](https://www.linkedin.com/in/dev-patel-sanjose/)

Daniel English [INSERT-LINKEDIN]

Kyle Huber  [Linkedin](https://www.linkedin.com/in/huberkyle/)

---
Other Acknowledgements
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/davidlp94/18-Blockchain-With-Python.svg?style=for-the-badge
[contributors-url]: https://github.com/davidlp94/18-Blockchain-With-Python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/davidlp94/18-Blockchain-With-Python.svg?style=for-the-badge
[forks-url]: https://github.com/davidlp94/18-Blockchain-With-Python/network/members
[stars-shield]: https://img.shields.io/github/stars/davidlp94/18-Blockchain-With-Python.svg?style=for-the-badge
[stars-url]: https://github.com/davidlp94/18-Blockchain-With-Python/stargazers
[issues-shield]: https://img.shields.io/github/issues/davidlp94/18-Blockchain-With-Python/network/members?style=for-the-badge
[issues-url]: https://github.com/davidlp94/18-Blockchain-With-Python/issues
[license-url]: https://choosealicense.com/licenses/mit/#

---
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
