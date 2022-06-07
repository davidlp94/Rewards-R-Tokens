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
