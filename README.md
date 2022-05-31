
<!-- Find and Replace All [repo_name] -->
<!-- Replace [product-screenshot] [product-url] -->
<!-- Other Badgets https://naereen.github.io/badges/ -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


![21-4-application-image](https://user-images.githubusercontent.com/96163075/168725892-da31d5f1-ecd0-44cf-ad2a-08e4dcc2e3ad.png)



# Rewards R' Tokens
Note: Please refer to smart contract files for complete source code.


---

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

Note: You must install and have an operating local blockchain on your machine to test and deploy the smart contracts - such as Ganache and an operating MetaMask wallet.

---
## Deploying Smart Contracts

Note: Please refer to folder Screenshots-Videos for screenshots and videos of completed test transactions.

The following code imports standard ERC-20 token contracts into our solidity files. Using constructor, we are then able to build upon the imported smart contracts to our desire for our token.

```solidity
pragma solidity ^0.5.0;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

// Create a constructor for the KaseiCoin contract and have the contract inherit the
// libraries that you imported from OpenZeppelin.

contract KaseiCoin is ERC20, ERC20Detailed, ERC20Mintable {

    constructor(string memory name, string memory symbol, uint initial_supply)
        ERC20Detailed(name, symbol, 18) public {
            // constructor can stay empty
        }

}
```

The crowdsale smart contract can also imported and built using OpenZeppelin's Crowdsale contracts available on thier website.

```solidity
pragma solidity ^0.5.0;

import "./KaseiCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";


// Have the KaseiCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract KaseiCoinCrowdsale is Crowdsale, MintedCrowdsale {
    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`,
    //`wallet` for fundraising, and `token`.
    constructor(
        uint rate,
        address payable wallet,
        KaseiCoin token
    )   
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }
}
```

The following screenshots capture each contract's successful deployment once the main source code for each smart contract is complete.

---

## Testing Smart Contracts Using Ganache and Metamask

Once each smart contract is successfully compiled, the next step would be to run some test transactions. In our case, Ganache will serve as our local blockchain network and the injected Web3 will be MetaMask extension. The following video shows how to successfully deploy each smart contract.



## Contributors
David Lee Ping [Linkedin](https://www.linkedin.com/in/david-lee-ping/)
Alexis
Ashok
Dev
Daniel

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
